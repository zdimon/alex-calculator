from django.core.management.base import BaseCommand, CommandError
from main.models import Person
from garnilo.settings import BASE_DIR


class Command(BaseCommand):
    help = "Loads"



    def handle(self, *args, **options):
        print("Load users")
        Person.objects.all().delete()
        file = str(BASE_DIR) + '/data/1.txt'
        fo = open(file,'r')
        for line in fo:
            print(line)
            arr = line.split(' ')
            print(arr[0])
            print(arr[1])
            print(arr[2])
            p = Person()
            p.surname = arr[0]
            p.name = arr[1]
            p.last_name = arr[2]
            p.save()