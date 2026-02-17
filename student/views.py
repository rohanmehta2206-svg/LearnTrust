from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash


# ================= STUDENT DASHBOARD =================
@login_required
def student_dashboard(request):
    return render(request, "student/dashboard.html")


# ================= STUDENT COURSES =================
@login_required
def student_courses(request):
    return render(request, "student/my_courses.html")


# ================= STUDENT PROFILE =================
@login_required
def student_profile(request):
    return render(request, "student/profile.html")


# ================= STUDENT CERTIFICATES =================
@login_required
def student_certificates(request):
    return render(request, "student/certificates.html")


# ================= STUDENT PROGRESS =================
@login_required
def student_progress(request):
    return render(request, "student/student_progress.html")


# ================= STUDENT QUIZZES =================
@login_required
def student_quizzes(request):
    return render(request, "student/student_quizzes.html")


# ================= EDIT PROFILE =================
@login_required
def student_edit_profile(request):
    return render(request, "student/student_edit_profile.html")


# ================= STUDENT SETTINGS =================
@login_required
def student_settings(request):
    return render(request, "student/student_settings.html")


# ================= CHANGE PASSWORD =================
@login_required
def student_change_password(request):

    if request.method == "POST":

        old_pass = request.POST.get("old_password")
        new_pass = request.POST.get("new_password")
        confirm_pass = request.POST.get("confirm_password")

        # Check new password match
        if new_pass != confirm_pass:
            messages.error(request, "Passwords do not match!")
            return redirect("student_change_password")

        user = request.user

        # Check old password
        if not user.check_password(old_pass):
            messages.error(request, "Old password is incorrect!")
            return redirect("student_change_password")

        # Save new password
        user.set_password(new_pass)
        user.save()

        # Keep session active after password change
        update_session_auth_hash(request, user)

        messages.success(request, "Password updated successfully!")
        return redirect("student_settings")

    return render(request, "student/student_change_password.html")
