"""portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from jobs import views

urlpatterns = [
    path('', views.job_list, name='job_list'),  # This is the home page route
    path('job_create/', views.job_create, name='job_create'),
    path('job_detail/<int:pk>/', views.job_detail, name='job_detail'),
    path('application_create/<int:pk>/', views.application_create, name='application_create'),
    path('accounts/', include('django.contrib.auth.urls')),  # Includes auth-related URLs
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('admin/', admin.site.urls),
]
