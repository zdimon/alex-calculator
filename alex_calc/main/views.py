from django.shortcuts import render
from .models import Page
from .forms import CreditForm

# Create your views here.

def index(request):
    form = CreditForm()
    page = Page.objects.filter(alias='index-page').first()


    return render(request,'index.html', {"page": page, "form": form})

from .library.calcproc import ThreeProcCalc

def report(request):
    if request.method == 'POST':
        print(request.POST.getlist('datep[]'))
        credit_start = request.POST.get('credit_start')
        credit_end = request.POST.get('credit_end')
        credit_sum = int(request.POST.get('credit_sum'))
        credit_proc = int(request.POST.get('credit_proc'))
        print('---',credit_start, credit_end, credit_sum)
        data =     {
            "date_start": credit_start,
            "date_end": credit_end,
            "sum": credit_sum,
            "proc": credit_proc,
            "payments": []
        }
        for index, pd in enumerate(request.POST.getlist('datep[]')):
            data['payments'].append({"date": pd, "sum":int(request.POST.getlist('sump[]')[index])})
    else:
        credit_proc = 3
        data =     {
            "date_start": "01/08/2001",
            "date_end": "09/01/2002",
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
    return render(request,'report.html', {"data": data, "total": total, "credit_proc": credit_proc})