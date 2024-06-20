from django.shortcuts import render
from .models import Person, Rota, Vzvod, Position2Person, Position, Instructor
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from pathlib import Path
from garnilo.settings import BASE_DIR
from django.core.files import File
from django.conf import settings
import os

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
    if request.method == "POST":
        person = Person.objects.get(pk=request.POST.get('person_id'))
        position = Position.objects.get(pk=request.POST.get('position_id'))
        person.position = position
        if request.FILES["file"]:
            #save_path = os.path.join(settings.MEDIA_ROOT, 'uploads', request.FILES['file'])
            #path = '%s/%s' % (BASE_DIR,'docs/')
            p2p = Position2Person()
            p2p.person = person
            p2p.position = position
            random_instructor = Instructor.objects.order_by('?')[0]
            p2p.editor = random_instructor
            p2p.file.save(request.FILES['file'].name,File(request.FILES['file']))
            p2p.save()
            print('ddddddd')
        person.save()
        return redirect("person_detail", person_id=person.id)

    person = Person.objects.get(pk=person_id)
    ptmp = Position.objects.all()
    positions = []
    for p in ptmp:
        if p != person.position:
            positions.append(p)
    return render(request,'change_position.html', {"person": person, "positions":positions})