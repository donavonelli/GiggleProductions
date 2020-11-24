from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('newsletter/', views.newsletter_signup, name='newsletter'),
    path('mobile/', views.mobile, name='mobile')
]