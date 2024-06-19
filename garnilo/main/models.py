from django.db import models

class Person(models.Model):
    surname = models.CharField(max_length=60)
    name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)

    def __str__(self) -> str:
        return '%s %s %s' % (self.surname, self.name, self.last_name)
