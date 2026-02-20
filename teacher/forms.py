from django import forms
from .models import Category, Course


# ============================
# ✅ Category Form (Parent + Child Support)
# ============================
class CategoryForm(forms.ModelForm):

    parent = forms.ModelChoiceField(
        queryset=Category.objects.none(),
        required=False,
        empty_label="-- No Parent (Main Category) --",
        widget=forms.Select(attrs={
            "class": "form-control"
        })
    )

    class Meta:
        model = Category
        fields = ["name", "parent"]

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Category Name"
            }),
        }


# ============================
# ✅ Course Form (Moodle Style FIXED)
# ============================
class CourseForm(forms.ModelForm):

    # ✅ FIX: Visibility Dropdown Correct
    visibility = forms.ChoiceField(
        choices=[
            (True, "Visible ✅"),
            (False, "Hidden ❌")
        ],
        widget=forms.Select(attrs={
            "class": "form-control"
        })
    )

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

            "category": forms.Select(attrs={
                "class": "form-control"
            }),

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

            "start_date": forms.DateInput(attrs={
                "type": "date",
                "class": "form-control"
            }),

            "end_date": forms.DateInput(attrs={
                "type": "date",
                "class": "form-control"
            }),
        }
