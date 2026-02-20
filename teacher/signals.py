from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Instructor, Category


@receiver(post_save, sender=Instructor)
def create_default_categories(sender, instance, created, **kwargs):

    if created:
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

        for cat in default_categories:
            Category.objects.create(
                instructor=instance,
                name=cat,
                parent=None
            )

        print("✅ Default Categories Created Successfully!")
