from django.urls import path
from .views import home_page, about_page, course_page, instructors_page, news_page
from contact.views import get_in_touch

urlpatterns = [
    path('', home_page, name='home'),
    path('about/', about_page, name='about'),
    path('courses/', course_page, name='course'),
    path('instructors/', instructors_page, name='instructors'),
    path('contact/', get_in_touch, name='contact'),
    path('news/', news_page, name='news')
]