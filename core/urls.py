from django.urls import path
from . import views

# Namespace for this app
app_name = "core"

urlpatterns = [

    # ✅ Home Page
    path("", views.home, name="home"),

    # ✅ About Page
    path("about/", views.about, name="about"),

    # ✅ Contact Page
    path("contact/", views.contact, name="contact"),
]
