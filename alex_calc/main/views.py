from django.shortcuts import render
from .models import Page
# Create your views here.

def index(request):
    page = Page.objects.filter(alias='index-page').first()
    return render(request,'index.html', {"page": page})

from .library.calcproc import ThreeProcCalc

def report(request):
    data =     {
        "date_start": "01/01/2001",
        "date_end": "01/01/2002",
        "sum": 1000,
        "proc": 30,
        "payments": [
            {"date": "10/02/2001", "sum": 100},
            {"date": "25/02/2001", "sum": 150},
            {"date": "01/03/2001", "sum": 200},
            {"date": "01/04/2001", "sum": 300}
        ]
    }

    counter = ThreeProcCalc(data)
    data = counter.calc_debt()
    total = counter.count_total(data)
    return render(request,'report.html', {"data": data, "total": total})