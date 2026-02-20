from django.urls import path
from . import views

app_name = "teacher"

urlpatterns = [

    # ===============================
    # Dashboard
    # ===============================
    path("dashboard/", views.teacher_dashboard, name="teacher_dashboard"),

    # ===============================
    # Main Teacher Pages
    # ===============================
    path("courses/", views.teacher_manage_courses, name="teacher_manage_courses"),
    path("students/", views.teacher_students, name="teacher_students"),
    path("assignments/", views.teacher_assignments, name="teacher_assignments"),
    path("gradebook/", views.teacher_gradebook, name="teacher_gradebook"),

    # ===============================
    # Quiz Bank
    # ===============================
    path("quiz-bank/", views.quiz_question_bank, name="quiz_question_bank"),

    # ===============================
    # Category Delete Only (No Create)
    # ===============================
    path(
        "category/<int:category_id>/delete/",
        views.delete_category,
        name="delete_category"
    ),

    # ===============================
    # Course Management
    # ===============================
    path("course/create/", views.create_course, name="create_course"),

    path(
        "course/<int:course_id>/",
        views.course_detail,
        name="course_detail"
    ),

    path(
        "course/<int:course_id>/delete/",
        views.delete_course,
        name="delete_course"
    ),
]
