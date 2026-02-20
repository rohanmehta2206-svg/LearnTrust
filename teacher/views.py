from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import CourseForm
from .models import Instructor, Course, Category


# ======================================================
# ✅ Approved Instructor Check
# ======================================================
def approved_instructor_required(request):
    try:
        instructor = Instructor.objects.get(user=request.user)

        if not instructor.is_approved:
            return None

        return instructor

    except Instructor.DoesNotExist:
        return None


# ======================================================
# ✅ DEFAULT CATEGORIES (Auto Create)
# ======================================================
default_categories = [
    "Programming Languages",
    "Web Development",
    "Mobile Development",
    "Game Development",
    "Data Science & AI",
    "IT & Software",
    "Cyber Security",
    "Cloud & DevOps",
    "UI/UX & Design",
    "Business & Freelancing",
    "Career Paths",
    "Tools & Technologies",
    "Other"
]


# ======================================================
# ✅ Auto Create Default Categories Only Once
# ======================================================
def create_default_categories(instructor):
    if Category.objects.filter(instructor=instructor).count() == 0:
        for name in default_categories:
            Category.objects.create(
                instructor=instructor,
                name=name,
                parent=None
            )


# ======================================================
# ✅ Teacher Dashboard
# ======================================================
@login_required
def teacher_dashboard(request):

    instructor = approved_instructor_required(request)
    if instructor is None:
        return render(request, "teacher/not_approved.html")

    return render(request, "teacher/dashboard.html")


# ======================================================
# ✅ Manage Courses Page
# ======================================================
@login_required
def teacher_manage_courses(request):

    instructor = approved_instructor_required(request)
    if instructor is None:
        return render(request, "teacher/not_approved.html")

    # ✅ Ensure default categories exist
    create_default_categories(instructor)

    categories = Category.objects.filter(
        instructor=instructor,
        parent=None
    )

    courses = Course.objects.filter(instructor=instructor)

    return render(request, "teacher/manage_courses.html", {
        "categories": categories,
        "courses": courses
    })


# ======================================================
# ✅ Teacher Students Page (Dummy View)
# ======================================================
@login_required
def teacher_students(request):

    instructor = approved_instructor_required(request)
    if instructor is None:
        return render(request, "teacher/not_approved.html")

    return render(request, "teacher/students.html")


# ======================================================
# ✅ Teacher Assignments Page (Dummy View)
# ======================================================
@login_required
def teacher_assignments(request):

    instructor = approved_instructor_required(request)
    if instructor is None:
        return render(request, "teacher/not_approved.html")

    return render(request, "teacher/assignments.html")


# ======================================================
# ✅ Teacher Gradebook Page (Dummy View)
# ======================================================
@login_required
def teacher_gradebook(request):

    instructor = approved_instructor_required(request)
    if instructor is None:
        return render(request, "teacher/not_approved.html")

    return render(request, "teacher/gradebook.html")


# ======================================================
# ✅ Quiz Question Bank Page (Dummy View)
# ======================================================
@login_required
def quiz_question_bank(request):

    instructor = approved_instructor_required(request)
    if instructor is None:
        return render(request, "teacher/not_approved.html")

    return render(request, "teacher/quiz_question_bank.html")


# ======================================================
# ✅ Course Detail Page
# ======================================================
@login_required
def course_detail(request, course_id):

    instructor = approved_instructor_required(request)
    if instructor is None:
        return render(request, "teacher/not_approved.html")

    course = get_object_or_404(
        Course,
        id=course_id,
        instructor=instructor
    )

    return render(request, "teacher/course_detail.html", {
        "course": course
    })


# ======================================================
# ✅ Delete Course
# ======================================================
@login_required
def delete_course(request, course_id):

    instructor = approved_instructor_required(request)
    if instructor is None:
        return render(request, "teacher/not_approved.html")

    course = get_object_or_404(Course, id=course_id, instructor=instructor)
    course.delete()

    return redirect("teacher:teacher_manage_courses")


# ======================================================
# ✅ Delete Category
# ======================================================
@login_required
def delete_category(request, category_id):

    instructor = approved_instructor_required(request)
    if instructor is None:
        return render(request, "teacher/not_approved.html")

    category = get_object_or_404(Category, id=category_id, instructor=instructor)
    category.delete()

    return redirect("teacher:teacher_manage_courses")


# ======================================================
# ✅ Create Course
# ======================================================
@login_required
def create_course(request):

    instructor = approved_instructor_required(request)
    if instructor is None:
        return render(request, "teacher/not_approved.html")

    # ✅ Ensure categories exist
    create_default_categories(instructor)

    form = CourseForm()

    form.fields["category"].queryset = Category.objects.filter(
        instructor=instructor
    )

    if request.method == "POST":
        form = CourseForm(request.POST)

        form.fields["category"].queryset = Category.objects.filter(
            instructor=instructor
        )

        if form.is_valid():
            course = form.save(commit=False)
            course.instructor = instructor
            course.save()

            return redirect("teacher:teacher_manage_courses")

    return render(request, "teacher/create_course.html", {
        "form": form
    })
