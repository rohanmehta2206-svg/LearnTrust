from django.urls import path
from . import views

# ✅ Namespace Fix (VERY IMPORTANT)
app_name = "student"

urlpatterns = [

    # ✅ Student Dashboard
    path(
        "dashboard/",views.student_dashboard, name="student_dashboard"
    ),

    # ✅ Student Courses
    path(
        "my-courses/",views.student_courses,name="student_courses"
    ),

    # ✅ Profile Pages
    path(
        "profile/", views.student_profile,name="student_profile"
    ),

    path(
        "profile/edit/", views.student_edit_profile,name="student_edit_profile"
    ),

    # ✅ Certificates
    path(
        "certificates/",views.student_certificates,name="student_certificates"
    ),

    # ✅ Progress Tracking
    path(
        "progress/",views.student_progress, name="student_progress"
    ),

    # ✅ Quizzes
    path(
        "quizzes/",views.student_quizzes,name="student_quizzes"
    ),

    # ✅ Settings
    path(
        "settings/",views.student_settings,name="student_settings"
    ),

    # ✅ Change Password
    path(
        "change-password/",views.student_change_password,name="student_change_password"
    ),
]
