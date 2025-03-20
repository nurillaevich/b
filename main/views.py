from unicodedata import category

from django.shortcuts import render, get_object_or_404, redirect
from .models import Teacher, AboutUs, Category, Course, News


def home_page(request):
    categories = Category.objects.all()
    courses = Course.objects.all()
    teachers = Teacher.objects.all()[:4]
    about = AboutUs.objects.all()
    new = News.objects.all()

    context = {'cate': categories,
               'cour': courses,
               'teach': teachers,
               'ab': about,
               'news': new}
    return render(request, 'index.html', context)


def about_page(request):
    about1= AboutUs.objects.all()
    teacher1 = Teacher.objects.all()
    context ={'about2': about1,
              'teacher2': teacher1}
    return render(request, 'about.html', context)

def course_page(request):
    cat = Category.objects.all()
    course = Course.objects.all()
    context = {
        'caty': cat,
        'courses': course
    }

    return render(request, 'courses.html', context)


def instructors_page(request):
    teacher = Teacher.objects.all()
    context = {
        'teachers': teacher
    }
    return render(request, 'instructor.html', context)


def news_page(request):
    newses = News.objects.all()
    context = {
        'news': newses
    }
    return render(request, 'blog.html', context)