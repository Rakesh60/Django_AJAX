from django.db import models

# Create your models here.

class Blog(models.Model):
    title=models.CharField(max_length=128)
    likes=models.IntegerField(default=0)
    def __str__(self):
        return self.title
