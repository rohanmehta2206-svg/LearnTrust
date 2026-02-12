from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # Home Page (Core App)
    path("", include("core.urls")),

    # Courses Page (Courses App)
    path("courses/", include("courses.urls")),

    # Accounts page(accounts app)
     path("accounts/", include("accounts.urls")),
]
