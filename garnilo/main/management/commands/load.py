from django.core.management.base import BaseCommand, CommandError
from main.models import Person, Rota, Vzvod, Position, Position2Person
from garnilo.settings import BASE_DIR
from main.models import Instructor
from django.contrib.auth.models import User

def create_position():
    d = ['+', 'Хв', 'Шп', 'СЗЧ', 'Н', 'Від', 'Зв', 'Відр']
    cl = ['text-success', 'text-warning', 'text-danger','text-info','text-primary','text-primary','text-primary','text-primary']
    for idx, i in enumerate(d):
        p = Position()
        p.name = i
        p.color = cl[idx]
        p.save()

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

def create_instructor():
    inst = ['Комбатов','Начштабов','Деловодов','Ротников']
    for idx, item in enumerate(inst):
        passwd = 'admin%s' % idx
        adm = User()
        adm.username = passwd
        adm.set_password(passwd)
        adm.is_active = True
        adm.is_staff = True
        adm.is_superuser = True
        adm.save()
        inst = Instructor()
        inst.user = adm
        inst.name = item
        inst.save()

class Command(BaseCommand):
    help = "Loads"





    def handle(self, *args, **options):
        print("Load users")
        Position2Person.objects.all().delete()
        Position.objects.all().delete()
        Person.objects.all().delete()
        User.objects.all().delete()
        Rota.objects.all().delete()
        Vzvod.objects.all().delete()
        Instructor.objects.all().delete()
        
        #
        create_r_v()
        create_instructor()
        create_position()
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
                    p.phone = '0508762834'
                    p.phone2 = 'батько 0508745834'
                    p.addres = 'Хмельницька обл. село Мухосранське буд. 789'
                    p.dr = '23.06.82'
                    p.rota = rota
                    p.vzvod = vzvod
                    random_position = Position.objects.order_by('?')[0]
                    random_instructor = Instructor.objects.order_by('?')[0]
                    p.position = random_position
                    p.save()
                    p2p = Position2Person()
                    p2p.person = p
                    p2p.position = random_position
                    p2p.editor = random_instructor
                    p2p.save()
                    
                fo.close()