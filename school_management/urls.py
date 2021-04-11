"""school_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.shortcuts import redirect
from django.urls import path, include
from school.views import *
from Class.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("schools/", SchoolList.as_view(), name="school-list"),
    path("schools/<int:pk>/", SchoolDetail.as_view(), name="school-detail"),
    path("schools/add/", SchoolCreate.as_view(), name="school-add"),
    path("schools/<int:pk>/delete/",
         SchoolDelete.as_view(),
         name="school-delete"),
    path("schools/<int:pk>/update/",
         SchoolUpdate.as_view(),
         name="school-update"),
    path("", include("Class.urls")),
    path("", include("student.urls")),
]
