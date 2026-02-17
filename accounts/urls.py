from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# ✅ Namespace Fix (VERY IMPORTANT)
app_name = "accounts"

urlpatterns = [

    # ✅ Register Page
    path("register/", views.register, name="register"),

    # ✅ Login Page
    path("login/", views.login_view, name="login"),

    # ✅ Logout Page (FIXED)
    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout"
    ),
]
