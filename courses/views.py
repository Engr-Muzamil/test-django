from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Course, Enrollment

def course_list(request):
    courses = Course.objects.filter(is_active=True)
    return render(request, "courses/course_list.html", {"courses": courses})

def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug, is_active=True)
    enrolled = False
    if request.user.is_authenticated:
        enrolled = Enrollment.objects.filter(user=request.user, course=course).exists()
    return render(request, "courses/course_detail.html", {"course": course, "enrolled": enrolled})

@login_required
def enroll(request, slug):
    course = get_object_or_404(Course, slug=slug, is_active=True)
    Enrollment.objects.get_or_create(user=request.user, course=course)
    messages.success(request, f"You are enrolled in {course.title}.")
    return redirect("course_detail", slug=slug)