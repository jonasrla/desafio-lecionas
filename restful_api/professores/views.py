from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from professores.models import Professor

class ProfessorList(ListView):
    model = Professor

class ProfessorView(DetailView):
    model = Professor

class ProfessorCreate(CreateView):
    model = Professor
    fields = ['nome','email','nascimento']
    success_url = reverse_lazy('professor_list')

class ProfessorUpdate(UpdateView):
    model = Professor
    fields = ['nome','email','nascimento']
    success_url = reverse_lazy('professor_list')

class ProfessorDelete(DeleteView):
    model = Professor
    success_url = reverse_lazy('professor_list')
