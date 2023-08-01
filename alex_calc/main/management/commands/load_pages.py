from django.core.management.base import BaseCommand, CommandError
from main.models import Page


class Command(BaseCommand):
    
    def handle(self, *args, **options):
        print('Грузю сраницы')
        Page.objects.all().delete()
        p1 = Page()
        p1.alias = 'index-page'
        p1.title = 'Добро пожаловать!'
        p1.content = 'Этот сайт создан нами в помощь бедным юристам.'
        p1.save()

        