from rest_framework import serializers
from .models import Card

class CardSerializer(serializers.ModelSerializer):
    # id= serializers.IntegerField()
    class Meta:
        model = Card
        fields = ['title', 'image', 'video']
        # extra_kwargs = {'id': {'read_only': False}}