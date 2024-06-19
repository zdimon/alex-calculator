from django.db import models




class Rota(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.name

class Vzvod(models.Model):
    name = models.CharField(max_length=20)
    rota = models.ForeignKey(Rota, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.name

class Person(models.Model):
    surname = models.CharField(max_length=60)
    name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    rota = models.ForeignKey(Rota, on_delete=models.CASCADE)
    vzvod = models.ForeignKey(Vzvod, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return '%s %s %s' % (self.surname, self.name, self.last_name)