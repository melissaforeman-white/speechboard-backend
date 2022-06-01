from django.db import models
from boards.models import Board

# Create your models here.
class Card(models.Model):
    title = models.CharField(max_length=255)
    image = models.URLField(max_length=1000, null=True, blank=True)
    video = models.URLField(max_length=1000, null=True, blank=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name="cards")


    def __str__(self):
        return f'{self.title}: {self.image if self.image else self.video}'
