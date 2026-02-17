from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    # ✅ Django Admin Panel
    path("admin/", admin.site.urls),

    # ✅ Core App (Home, About, Contact)
    path("", include(("core.urls", "core"), namespace="core")),

    # ✅ Courses App
    path("courses/", include(("courses.urls", "courses"), namespace="courses")),

    # ✅ Accounts App
    path("accounts/", include(("accounts.urls", "accounts"), namespace="accounts")),

    # ✅ Student App
    path("student/", include(("student.urls", "student"), namespace="student")),

    # ✅ Teacher App
    path("teacher/", include(("teacher.urls", "teacher"), namespace="teacher")),

    # ✅ Custom Admin Panel App
    path("adminpanel/", include(("adminpanel.urls", "adminpanel"), namespace="adminpanel")),
]
