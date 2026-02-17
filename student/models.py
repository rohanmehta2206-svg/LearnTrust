from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Student(models.Model):
    """
    Student Profile Table

    This table stores extra student information.
    Login credentials are stored safely inside Django's auth_user table.
    """

    # ✅ Link Student with Django User (One Student = One User Account)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="student_profile"
    )

    # Extra fields (future LMS use)
    created_at = models.DateTimeField(default=timezone.now)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Student: {self.user.email}"
