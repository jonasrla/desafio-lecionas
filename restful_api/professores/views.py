from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from professores.models import Professor

class BookList(ListView):
    model = Professor

class BookView(DetailView):
    model = Professor

class BookCreate(CreateView):
    model = Professor
    fields = ['nome','email','nascimento']
    success_url = reverse_lazy('book_list')

class BookUpdate(UpdateView):
    model = Professor
    fields = ['nome','email','nascimento']
    success_url = reverse_lazy('book_list')

class BookDelete(DeleteView):
    model = Professor
    success_url = reverse_lazy('book_list')
