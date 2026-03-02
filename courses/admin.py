from django.contrib import admin
from .models import Course, Enrollment

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "level", "price", "is_active")
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Enrollment)