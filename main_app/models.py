from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.

RATES = (
    ('G', 'General Audience'),
    ('P', 'Parental Guidance'),
    ('R', 'Restricted'),
    ('N', 'No one 17 and under admitted'))

STATUS = (
    ('N', "To watch"),
    ('F', "Watching"),
    ('H', "Half way!"),
    ('D', "Done!"),
)

class Streamer(models.Model):
    name = models.CharField(max_length=50)
    device = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('streamers_detail', kwargs={'pk': self.id})

class Anime(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    rate = models.CharField(
        max_length=1,
        choices=RATES,
        default=RATES[0][0])
    streamer = models.ManyToManyField(Streamer)

    def __str__(self):
        return f'{self.title} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'anime_id': self.id})
    
    def phas_for_today(self):
        return self.phasing_set.filter(date=date.today()).count() >= len(STATUS)
    
class Phasing(models.Model):
    date = models.DateField('Phasing Date')
    status = models.CharField(
        max_length=1,
        choices=STATUS,
        default=STATUS [0][0]
    )

    anime = models.ForeignKey(
        Anime,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.get_status_display()} on {self.date}"
  
class Meta:
    ordering = ['-date']

