from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

from teacher.models import Instructor


# ======================================================
# ✅ Only Superuser Allowed (Admin Only)
# ======================================================
def admin_only(user):
    return user.is_superuser


# ======================================================
# ✅ ADMIN DASHBOARD
# ======================================================
@login_required
@user_passes_test(admin_only)
def admin_dashboard(request):
    return render(request, "adminpanel/admin_dashboard.html")


# ======================================================
# ✅ MANAGE USERS PAGE
# ======================================================
@login_required
@user_passes_test(admin_only)
def admin_manage_users(request):

    pending_instructors = Instructor.objects.filter(is_approved=False)
    approved_instructors = Instructor.objects.filter(is_approved=True)

    return render(request, "adminpanel/manage_users.html", {
        "pending_instructors": pending_instructors,
        "approved_instructors": approved_instructors,
    })


# ======================================================
# ✅ APPROVE INSTRUCTOR
# ======================================================
@login_required
@user_passes_test(admin_only)
def approve_instructor(request, instructor_id):

    instructor = get_object_or_404(Instructor, id=instructor_id)

    if instructor.is_approved:
        messages.info(request, "⚠ Instructor already approved.")
        return redirect("adminpanel:admin_manage_users")

    # ✅ Approve Instructor
    instructor.is_approved = True
    instructor.save()

    # ✅ Ensure Instructor is NOT staff
    instructor.user.is_staff = False
    instructor.user.save()

    messages.success(
        request,
        f"✅ Instructor {instructor.user.email} approved successfully!"
    )

    # ✅ FIXED REDIRECT
    return redirect("adminpanel:admin_manage_users")


# ======================================================
# ❌ REJECT INSTRUCTOR
# ======================================================
@login_required
@user_passes_test(admin_only)
def reject_instructor(request, instructor_id):

    instructor = get_object_or_404(Instructor, id=instructor_id)

    instructor.user.delete()

    messages.error(request, "❌ Instructor rejected and removed.")

    # ✅ FIXED REDIRECT
    return redirect("adminpanel:admin_manage_users")


# ======================================================
# ✅ COURSES PAGE
# ======================================================
@login_required
@user_passes_test(admin_only)
def admin_courses(request):
    return render(request, "adminpanel/admin_courses.html")


# ======================================================
# ✅ REPORTS PAGE
# ======================================================
@login_required
@user_passes_test(admin_only)
def admin_reports(request):
    return render(request, "adminpanel/admin_reports.html")
