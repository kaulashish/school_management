from django.urls import path
from student.views import *

urlpatterns = [
    path("students/", StudentList.as_view(), name="student-list"),
    path("students/<int:pk>", StudentDetail.as_view(), name="student-detail"),
    path("students/add", StudentCreate.as_view(), name="student-create"),
    path("students/<int:pk>/edit", StudentUpdate.as_view(), name="student-update"),
    path("students/<int:pk>/delete", StudentDelete.as_view(), name="student-del"),
]