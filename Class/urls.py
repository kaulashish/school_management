from django.urls import path
from Class.views import *

urlpatterns = [
    path("class/", ClassList.as_view(), name="class-list"),
    path(
        "class/edit/",
        ClassCreate.as_view(success_url="/class/"),
        name="class-create",
    ),
    path(
        "class/<int:pk>/update/",
        ClassUpdate.as_view(success_url="/class/"),
        name="class-update",
    ),
    path(
        "class/<int:pk>/delete/",
        ClassDelete.as_view(success_url="/class/"),
        name="class-delete",
    ),
]
