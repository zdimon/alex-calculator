from django.db import models

class Page(models.Model):
    title = models.TextField()
    content = models.TextField()
    alias = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title