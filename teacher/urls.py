from django.urls import path
from . import views

# ✅ Namespace (VERY IMPORTANT)
app_name = "teacher"

urlpatterns = [

    # ✅ Teacher Dashboard
    path("dashboard/", views.teacher_dashboard, name="teacher_dashboard"),

    # ✅ Teacher Pages
    path("courses/", views.teacher_manage_courses, name="teacher_manage_courses"),
    path("students/", views.teacher_students, name="teacher_students"),
    path("assignments/", views.teacher_assignments, name="teacher_assignments"),
    path("gradebook/", views.teacher_gradebook, name="teacher_gradebook"),

    # ✅ Quiz Question Bank
    path("quiz-bank/", views.quiz_question_bank, name="quiz_question_bank"),

    # ✅ Category & Course Creation
    path("category/create/", views.create_category, name="create_category"),
    path("course/create/", views.create_course, name="create_course"),
]
