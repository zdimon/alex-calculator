from django.shortcuts import render
from .models import Page
# Create your views here.

def index(request):
    page = Page.objects.filter(alias='index-page').first()
    return render(request,'index.html', {"page": page})