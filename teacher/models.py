from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# ==========================================================
# ✅ Instructor Model
# ==========================================================
class Instructor(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="instructor_profile"
    )

    created_at = models.DateTimeField(default=timezone.now)

    is_active = models.BooleanField(default=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Instructor: {self.user.username}"

    def approved_status(self):
        return "Approved" if self.is_approved else "Pending"


# ==========================================================
# ✅ Category Model (Parent + Child System)
# ==========================================================
class Category(models.Model):

    instructor = models.ForeignKey(
        Instructor,
        on_delete=models.CASCADE,
        related_name="categories"
    )

    name = models.CharField(max_length=200)

    # ✅ Parent Category Support
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="subcategories"
    )

    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["name"]

        # Prevent duplicate names per instructor
        unique_together = ("instructor", "name")

    def __str__(self):
        if self.parent:
            return f"{self.parent.name} → {self.name}"
        return self.name

    # Default Categories Auto Created
    @staticmethod
    def default_parent_categories():
        return [
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


# ==========================================================
# ✅ Course Model (Dummy Data Ready)
# ==========================================================
class Course(models.Model):

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
        unique=True
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
