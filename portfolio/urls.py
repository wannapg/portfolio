from django.urls import path

from . import views

urlpatterns = [
    path('',views.main,name='main'),
    path('courses/',views.courses,name='courses'),
    path('projects/',views.projects,name='projects'),
    path('dino/',views.dino,name='dino')
]