from django.urls import path
from . import views

# ✅ Namespace
app_name = "adminpanel"

urlpatterns = [

    path("login/", views.admin_login, name="admin_login"),

    # ✅ Admin Dashboard
    path("dashboard/", views.admin_dashboard, name="admin_dashboard"),

    # ✅ Manage Instructor Approvals
    path("users/", views.admin_manage_users, name="admin_manage_users"),

    # ✅ Approve Instructor
    path(
        "approve/<int:instructor_id>/",
        views.approve_instructor,
        name="approve_instructor"
    ),

    # ✅ Reject Instructor
    path(
        "reject/<int:instructor_id>/",
        views.reject_instructor,
        name="reject_instructor"
    ),

    # ✅ Courses Page
    path("courses/", views.admin_courses, name="admin_courses"),

    # ✅ Reports Page
    path("reports/", views.admin_reports, name="admin_reports"),
]
