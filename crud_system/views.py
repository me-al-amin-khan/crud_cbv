from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import School, Student



# Create your views here.

class IndexView(TemplateView):
    template_name = 'crud_system/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['inserted_data'] = 'This data is inserted from views'
        return context


class SchoolListView(ListView):
    context_object_name = 'school_list'
    model = School


class SchoolDetailView(DetailView):
    context_object_name = 'detail_con'
    model = School

    template_name = 'crud_system/school_detail.html'


class SchoolCreateView(CreateView):
    fields = ('school_name', 'school_type', 'principal_name', 'location')
    model = School

    success_url = reverse_lazy('crud_system:list')


class SchoolUpdateView(UpdateView):
    fields = ('school_name', 'school_type', 'principal_name', 'location')
    model = School


class SchoolDeleteView(DeleteView):
    model = School
    success_url = reverse_lazy('crud_system:list')
