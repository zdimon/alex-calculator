from django.core.management.base import BaseCommand, CommandError
from main.models import Person, Rota, Vzvod
from garnilo.settings import BASE_DIR

def create_r_v():
    for i in range(1,6):
        r = Rota()
        r.name = i
        r.save()
        for n in range(1,6):
            v = Vzvod()
            v.rota = r
            v.name = n
            v.save()

class Command(BaseCommand):
    help = "Loads"





    def handle(self, *args, **options):
        print("Load users")
        Person.objects.all().delete()
        Rota.objects.all().delete()
        Vzvod.objects.all().delete()
        create_r_v()
        file = str(BASE_DIR) + '/data/1.txt'
        
        for rota in Rota.objects.all():
            for vzvod in Vzvod.objects.all():
                fo = open(file,'r')
                for line in fo:
                    arr = line.split(' ')
                    print(arr[0])
                    print(arr[1])
                    print(arr[2])
                    p = Person()
                    p.surname = arr[0]
                    p.name = arr[1]
                    p.last_name = arr[2]
                    p.rota = rota
                    p.vzvod = vzvod
                    p.save()
                fo.close()