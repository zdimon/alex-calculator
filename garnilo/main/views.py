from django.shortcuts import render
from .models import Person

# Create your views here.

def index(r):
    persons = Person.objects.all()
    return render(r,'layout.html', {"persons":persons})
