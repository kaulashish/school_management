from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)
from .models import *

# Create your views here.


class SchoolList(ListView):
    # either specify model name or create a queryset that contains the model object
    # model = School
    template_name = "school-list.html"
    queryset = School.objects.all()


class SchoolDetail(DetailView):
    model = School
    template_name = "school-detail.html"
    # The context_object_name attribute on a generic view specifies the context variable to use
    # context_object_name = "schools"


class SchoolCreate(CreateView):
    model = School
    template_name = "school-form.html"
    fields = ["name", "address", "phone"]
    success_url = "/schools/"


class SchoolDelete(DeleteView):
    model = School
    template_name = "confirm_delete.html"
    success_url = "/schools/"


class SchoolUpdate(UpdateView):
    model = School
    fields = ["name", "address", "phone"]
    template_name = "school-update.html"
    success_url = "/schools/"
