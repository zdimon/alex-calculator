from django.shortcuts import render
from .models import Person, Rota, Vzvod, Position2Person, Position

# Create your views here.

def index(r):
    persons = Person.objects.all()
    rotas = Rota.objects.all()
    return render(r,'index.html', {"rotas":rotas})

def rota_list(request,rota_id):
    rota = Rota.objects.get(pk=rota_id)
    vzvods = Vzvod.objects.filter(rota=rota_id)
    persons = Person.objects.filter(rota=rota)
    return render(request,'persons_list.html', {"rota":rota, 
    "persons": persons, "vzvods": vzvods})

def vzvod_list(request,rota_id, vzvod_id):
    rota = Rota.objects.get(pk=rota_id)
    vzvod = Vzvod.objects.get(pk=vzvod_id)
    persons = Person.objects.filter(rota=rota, vzvod=vzvod)
    return render(request,'persons_list.html', {"rota":rota, 
    "persons": persons, "vzvod": vzvod})

def person_detail(request,person_id):
    person = Person.objects.get(pk=person_id)
    moves = Position2Person.objects.filter(person=person)
    return render(request,'persons_detail.html', {"person": person, "moves": moves})

def change_position(request, person_id):
    person = Person.objects.get(pk=person_id)
    ptmp = Position.objects.all()
    positions = []
    for p in ptmp:
        if p != person.position:
            positions.append(p)
    return render(request,'change_position.html', {"person": person, "positions":positions})