from django.urls import path
from . import views

app_name = 'myprofile'

urlpatterns = [
    path('main/', views.main, name='main'),
    path('bloglist/', views.bloglist, name='bloglist'),
    path('myprofile/', views.myprofile, name='myprofile'),
]

