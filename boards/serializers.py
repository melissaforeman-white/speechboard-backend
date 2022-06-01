from rest_framework import serializers
from .models import Board
from card.models import Card
from card.serializers import CardSerializer
# from drf_writable_nested.serializers import WritableNestedModelSerializer



class BoardSerializer(serializers.ModelSerializer):
    cards = CardSerializer(many=True)
    class Meta:
        model = Board
        fields = ['id','title', 'cards']

    def create(self, validated_data):
        print('the validated data is ', validated_data)
        cards_data = validated_data.pop('cards')
        print('the cards data in create is ', cards_data)
        board = Board.objects.create(**validated_data)
        print('the board in create is ', board)
        for card_data in cards_data:
            Card.objects.create(board=board, **card_data)
        return board

    # def update(self, instance, validated_data):
    #     # print('validated data ', validated_data)
    #     # cards= validated_data.pop('cards', [])
    #     # print('cards_data', cards)
    #     # board = super().update(instance, validated_data)
    #     # print('instance', instance)

    #     # for card_data in cards:
    #     #     # get the card object from the database
    #     #     Card.objects.update(board=board, **card_data)
    #     cards = validated_data.pop('cards')
    #     print('cards ', cards)
    #     item = instance.cards
    #     print('item', item)
    #     for k,v in cards:
    #         print('k', k)
    #         setattr(item, k, v)
    #     item.save()
    def update(self, instance, validated_data):
            cards_data = validated_data.pop('cards')
            # board = Board.objects.update(**validated_data)
            # for card_data in cards_data:
            #     Card.objects.update(board=board, **card_data)
            # return board
            cards = (instance.cards).all()
            print('cards', cards)
            cards = list(cards)
            print('cards list ', cards)
            instance.id = validated_data.get('id', instance.id)
            print(instance.id)
            instance.title = validated_data.get('title', instance.title)
            print(instance.title)
            instance.save()
            print('cards length is ',len(cards))

            for card_data in cards_data:
                card = cards.pop(0)
                card.id = card_data.get('id', card.id)
                print(card.id)
                card.title = card_data.get('title', card.title)
                print(card.title)
                card.image = card_data.get('image', card.image)
                print(card.image)
                card.video = card_data.get('video', card.video)
                print(card.video)
                card.save()
            return instance