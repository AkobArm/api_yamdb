from .models import Category, Genre, Title, User
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


class CategorySerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Category
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ['name', 'slug']


class TitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Title
        fields = '__all__'
