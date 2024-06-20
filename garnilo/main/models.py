from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User





class Rota(models.Model):
    name = models.CharField(max_length=20)
    class Meta:
        verbose_name = _('Рота')
        verbose_name_plural = _('Роти')
    def __str__(self) -> str:
        return self.name



class Vzvod(models.Model):
    name = models.CharField(max_length=20)
    rota = models.ForeignKey(Rota, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = _('Взвод')
        verbose_name_plural = _('Взводи')

class Position(models.Model):
    name = models.CharField(max_length=80)
    color = models.CharField(max_length=10)
    class Meta:
        verbose_name = _('Локація')
        verbose_name_plural = _('Локації')
    def __str__(self) -> str:
        return self.name

class Person(models.Model):
    surname = models.CharField(max_length=60)
    name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    rota = models.ForeignKey(Rota, on_delete=models.CASCADE)
    vzvod = models.ForeignKey(Vzvod, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, blank=True)
    class Meta:
        verbose_name = _('Курсант')
        verbose_name_plural = _('Курсанти')
    def __str__(self) -> str:
        return '%s %s %s' % (self.surname, self.name, self.last_name)

    def short_name(self) -> str:
        return '%s %s. %s.' % (self.surname, self.name[0], self.last_name[0])

class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    can_edit = models.BooleanField(default=False)
    name = models.CharField(max_length=60)
    phone = models.CharField(max_length=60)
    class Meta:
        verbose_name = _('Командир')
        verbose_name_plural = _('Командири')
    def __str__(self) -> str:
        return self.name


class Position2Person(models.Model):
    position = models.ForeignKey(Position, on_delete=models.DO_NOTHING)
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    file = models.ImageField(upload_to='docs')
    created_at = models.DateTimeField(auto_now_add=True)
    editor = models.ForeignKey(Instructor,on_delete=models.SET_NULL, null=True, blank=True)
    desc = models.TextField(null=True)
    class Meta:
        verbose_name = _('Пересування')
        verbose_name_plural = _('Пересування')
    def __str__(self) -> str:
        return self.position.name