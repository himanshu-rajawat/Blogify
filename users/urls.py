from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview,name="apiOverview"),
    path('register/', views.register,name="user_registration"),
    path('userdetails/',views.userdetails,name="user_details"),
]
