from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    UpdateView,
)
from school.models import *


class ClassList(ListView):
    model = Class
    template_name = "class-list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["schools"] = School.objects.all()
        return context


class ClassCreate(CreateView):
    model = Class
    template_name = "class-form.html"
    fields = ["name", "school_name", "room_no"]


class ClassUpdate(UpdateView):
    model = Class
    template_name = "class-update.html"
    fields = ["name", "school_name", "room_no"]


class ClassDelete(DeleteView):
    model = Class
    template_name = "confirm_delete.html"
