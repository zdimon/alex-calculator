from django.db import models

class Page(models.Model):
    title = models.TextField()
    content = models.TextField()
    alias = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title
    
class Credit(models.Model):
    start_date = models.CharField(max_length=15)
    end_date = models.CharField(max_length=15)
    sum = models.IntegerField()
    
class Payment(models.Model):
    date = models.CharField(max_length=15)
    sum = models.IntegerField()
    credit = models.ForeignKey(Credit, on_delete=models.CASCADE)