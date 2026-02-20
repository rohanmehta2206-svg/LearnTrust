from django.contrib import admin
from .models import Course, Category, Instructor

admin.site.register(Instructor)
admin.site.register(Category)
admin.site.register(Course)
