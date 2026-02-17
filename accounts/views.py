from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from student.models import Student
from teacher.models import Instructor


# ======================================================
# ✅ REGISTER VIEW (FIXED)
# ======================================================
def register(request):

    if request.method == "POST":

        role = request.POST.get("role")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # ✅ Duplicate Email Check
        if User.objects.filter(email=email).exists():
            return render(request, "accounts/register.html", {
                "error": "Email already registered! Please login instead."
            })

        # ✅ Create User (username=email)
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        # ===============================
        # ✅ STUDENT REGISTER
        # ===============================
        if role == "student":
            Student.objects.create(user=user)
            login(request, user)

            # ✅ FIXED Redirect with Namespace
            return redirect("student:student_dashboard")

        # ===============================
        # ✅ INSTRUCTOR REGISTER (Pending Approval)
        # ===============================
        elif role == "instructor":
            Instructor.objects.create(user=user, is_approved=False)

            return render(request, "accounts/login.html", {
                "success": "Instructor registered successfully! Wait for admin approval."
            })

        return render(request, "accounts/register.html", {
            "error": "Invalid role selected!"
        })

    return render(request, "accounts/register.html")


# ======================================================
# ✅ LOGIN VIEW (FULLY FIXED)
# ======================================================
def login_view(request):

    if request.method == "POST":

        role = request.POST.get("role")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # ==================================================
        # ✅ STEP 1: Find User by Email
        # ==================================================
        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            return render(request, "accounts/login.html", {
                "error": "Invalid email or password!"
            })

        # ==================================================
        # ✅ STEP 2: Authenticate Using Username
        # ==================================================
        user = authenticate(
            request,
            username=user_obj.username,
            password=password
        )

        if user is None:
            return render(request, "accounts/login.html", {
                "error": "Invalid email or password!"
            })

        # ✅ Login Session Start
        login(request, user)

        # ==================================================
        # ✅ ADMIN LOGIN (ONLY SUPERUSER)
        # ==================================================
        if role == "admin":
            if user.is_superuser:

                # ✅ FIXED Admin Redirect
                return redirect("adminpanel:admin_dashboard")

            return render(request, "accounts/login.html", {
                "error": "Only Admin (superuser) can login here!"
            })

        # ==================================================
        # ✅ STUDENT LOGIN
        # ==================================================
        if role == "student":

            if Student.objects.filter(user=user).exists():

                # ✅ FIXED Student Redirect
                return redirect("student:student_dashboard")

            return render(request, "accounts/login.html", {
                "error": "You are not registered as a Student!"
            })

        # ==================================================
        # ✅ INSTRUCTOR LOGIN
        # ==================================================
        if role == "instructor":

            try:
                instructor = Instructor.objects.get(user=user)

                # ❌ Block if Not Approved
                if not instructor.is_approved:
                    return render(request, "teacher/not_approval.html")

                # ✅ FIXED Teacher Redirect
                return redirect("teacher:teacher_dashboard")

            except Instructor.DoesNotExist:
                return render(request, "accounts/login.html", {
                    "error": "You are not registered as an Instructor!"
                })

        # ==================================================
        # ❌ Invalid Role
        # ==================================================
        return render(request, "accounts/login.html", {
            "error": "Invalid role selected!"
        })

    return render(request, "accounts/login.html")
