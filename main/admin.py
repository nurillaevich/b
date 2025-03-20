from django.contrib import admin
from .models import AboutUs, News, Course, Category, Teacher


@admin.register(AboutUs)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'title']
    list_display_links = ['id', 'category']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name']
    list_display_links = ['id', 'full_name']
