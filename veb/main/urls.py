from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('teacher', views.teacher, name='teacher'),
    path('create', views.create, name='create'),
    path('sub', views.sub, name='sub'),
]
