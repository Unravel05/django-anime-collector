from django.db import models
from django.urls import reverse

# Create your models here.

class Anime(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    # rate = models.IntergerChoices("PG", "G", "R", "NC-17")
    # Pregunta:
    # TypeError: Anime() got unexpected keyword arguments: 'rate'
    # >>> a = Anime(title="Naruto Shippuden", genre="Action, Adventure, Fantasy", description="A series that follows the adventures of a young ninja in training and his friends.", rate=[0])
    # Traceback (most recent call last):
    #   File "<console>", line 1, in <module>
    #   File "/Users/nataliaparra05/.local/share/virtualenvs/django-anime-collector-JmYlC9ZS/lib/python3.12/site-packages/django/db/models/base.py", line 567, in __init__
    #     raise TypeError(
    # TypeError: Anime() got unexpected keyword arguments: 'rate'
    # >>> 

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'anime_id': self.id})
    # Pregunta