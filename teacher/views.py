from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import CategoryForm, CourseForm
from .models import Instructor


# ======================================================
# ✅ Helper Function (Approved Instructor Check)
# ======================================================
def approved_instructor_required(request):
    """
    Returns Instructor if approved.
    Otherwise shows not approved page.
    """

    try:
        instructor = Instructor.objects.get(user=request.user)

        # ❌ Block if not approved
        if not instructor.is_approved:
            return None

        return instructor

    except Instructor.DoesNotExist:
        return None


# ======================================================
# ✅ TEACHER DASHBOARD
# ======================================================
@login_required
def teacher_dashboard(request):

    instructor = approved_instructor_required(request)

    if instructor is None:
        return render(request, "teacher/not_approved.html")

    return render(request, "teacher/dashboard.html")


# ======================================================
# ✅ MANAGE COURSES
# ======================================================
@login_required
def teacher_manage_courses(request):

    instructor = approved_instructor_required(request)

    if instructor is None:
        return render(request, "teacher/not_approved.html")

    return render(request, "teacher/manage_courses.html")


# ======================================================
# ✅ STUDENTS PAGE
# ======================================================
@login_required
def teacher_students(request):

    instructor = approved_instructor_required(request)

    if instructor is None:
        return render(request, "teacher/not_approved.html")

    return render(request, "teacher/students.html")


# ======================================================
# ✅ ASSIGNMENTS PAGE
# ======================================================
@login_required
def teacher_assignments(request):

    instructor = approved_instructor_required(request)

    if instructor is None:
        return render(request, "teacher/not_approved.html")

    return render(request, "teacher/assignments.html")


# ======================================================
# ✅ GRADEBOOK PAGE
# ======================================================
@login_required
def teacher_gradebook(request):

    instructor = approved_instructor_required(request)

    if instructor is None:
        return render(request, "teacher/not_approved.html")

    return render(request, "teacher/gradebook.html")


# ======================================================
# ✅ QUIZ QUESTION BANK
# ======================================================
@login_required
def quiz_question_bank(request):

    instructor = approved_instructor_required(request)

    if instructor is None:
        return render(request, "teacher/not_approved.html")

    return render(request, "teacher/quiz_question_bank.html")


# ======================================================
# ✅ CREATE CATEGORY
# ======================================================
@login_required
def create_category(request):

    instructor = approved_instructor_required(request)

    if instructor is None:
        return render(request, "teacher/not_approved.html")

    form = CategoryForm()

    if request.method == "POST":
        form = CategoryForm(request.POST)

        if form.is_valid():
            category = form.save(commit=False)
            category.instructor = instructor
            category.save()

            return redirect("teacher_manage_courses")

    return render(request, "teacher/create_category.html", {"form": form})


# ======================================================
# ✅ CREATE COURSE
# ======================================================
@login_required
def create_course(request):

    instructor = approved_instructor_required(request)

    if instructor is None:
        return render(request, "teacher/not_approved.html")

    form = CourseForm()

    if request.method == "POST":
        form = CourseForm(request.POST)

        if form.is_valid():
            course = form.save(commit=False)
            course.instructor = instructor
            course.save()

            return redirect("teacher_manage_courses")

    return render(request, "teacher/create_course.html", {"form": form})
