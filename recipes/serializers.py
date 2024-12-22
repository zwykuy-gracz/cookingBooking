# from django.contrib.auth.models import User, Tag, Dish
from .models import User, Tag, Dish
from rest_framework import serializers


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ["username", "email"]


# class TagSerializer(serializers.HyperlinkedModelSerializer):
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            "id",
            "name",
        ]


class DishSerializer(serializers.ModelSerializer):
    # food_tags = TagSerializer(many=True)
    food_tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Dish
        fields = [
            "id",
            "title",
            "ingredients",
            "recipe",
            "comments",
            "link",
            "food_tags",
        ]
