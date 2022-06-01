from django.db import models
from accounts.models import CustomUser
# from card.models import Card

class Board(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


# owner = models.ForeignKey(CustomUser, related_name='boards', on_delete=models.CASCADE)
