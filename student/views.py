from school.models import Student
from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    UpdateView,
    DetailView,
)
from school.models import *

# Create your views here.
class StudentList(ListView):
    model = Student
    template_name = "student-list.html"


class StudentDetail(DetailView):
    model = Student
    template_name = "student-detail.html"
    context_object_name = "student"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["class_list"] = Class.objects.all()
        return context


class StudentCreate(CreateView):
    model = Student
    template_name = "student-create.html"
    success_url = "/students/"
    fields = ["name", "age", "marks", "school", "class_name", "roll_no"]


class StudentUpdate(UpdateView):
    model = Student
    template_name = "student-update.html"
    success_url = "/students/"
    fields = ["name", "age", "marks", "school", "class_name", "roll_no"]


class StudentDelete(DeleteView):
    model = Student
    template_name = "student-delete.html"
    success_url = "/students/"
