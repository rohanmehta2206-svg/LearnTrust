from django import forms
from .models import Category, Course


# ============================
# ✅ Category Form
# ============================
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Category Name"
            })
        }


# ============================
# ✅ Course Form (Updated Moodle Style)
# ============================
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course

        fields = [
            "category",
            "full_name",
            "short_name",
            "description",
            "visibility",
            "start_date",
            "end_date"
        ]

        widgets = {

            "full_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "e.g. Python for Beginners"
            }),

            "short_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "e.g. PY101 (Must be unique)"
            }),

            "description": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Enter Course Description",
                "rows": 4
            }),

            "visibility": forms.Select(attrs={
                "class": "form-control"
            }),

            "start_date": forms.DateInput(attrs={
                "type": "date",
                "class": "form-control"
            }),

            "end_date": forms.DateInput(attrs={
                "type": "date",
                "class": "form-control"
            }),
        }
