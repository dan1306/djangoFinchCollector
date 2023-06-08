from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Finch

# Create your views here.
from django.http import HttpResponse

from django.views.generic.edit import CreateView, UpdateView, DeleteView

class FinchCreate(CreateView):
  model = Finch
  fields = ['name', 'breed', 'description', 'age']
  success_url = '/finch/'

class FinchUpdate(UpdateView):
  model = Finch
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['breed', 'description', 'age']

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finch/'

# Define the home view
def home(request):
  return HttpResponse('<h1>Supposed to be a collector</h1>')

def about(request):
  return render(request, 'about.html')

def finch_index(request):
  finch = Finch.objects.all()
  return render(request, 'finch/index.html', { 'finch': finch })

def finch_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  return render(request, 'finch/detail.html', { 'finch': finch })