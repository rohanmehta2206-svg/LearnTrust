from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# ==========================================================
# ✅ Instructor Model (With Admin Approval System)
# ==========================================================
class Instructor(models.Model):
    """
    Instructor Profile Table

    Approval System:
    - Instructor registers → Pending Approval
    - Admin approves → Instructor can login
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="instructor_profile"
    )

    created_at = models.DateTimeField(default=timezone.now)

    # Active Account
    is_active = models.BooleanField(default=True)

    # ✅ Admin Approval Required
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Instructor: {self.user.email}"

    # ✅ Helper Function
    def approved_status(self):
        if self.is_approved:
            return "Approved"
        return "Pending"


# ==========================================================
# ✅ Category Model
# ==========================================================
class Category(models.Model):
    """
    Category Table

    Instructor can create categories like:
    - Programming
    - AI
    - Web Development
    """

    instructor = models.ForeignKey(
        Instructor,
        on_delete=models.CASCADE,
        related_name="categories"
    )

    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ("instructor", "name")
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.instructor.user.email})"


# ==========================================================
# ✅ Course Model (Moodle Style)
# ==========================================================
class Course(models.Model):
    """
    Course Table

    Each Instructor can create Moodle-like courses
    under categories.
    """

    instructor = models.ForeignKey(
        Instructor,
        on_delete=models.CASCADE,
        related_name="courses"
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="courses"
    )

    full_name = models.CharField(max_length=200)

    short_name = models.CharField(
        max_length=50,
        unique=True,
        null=True,
        blank=True
    )

    description = models.TextField(blank=True)

    visibility = models.BooleanField(default=True)

    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.full_name
