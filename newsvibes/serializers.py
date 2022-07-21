from attr import fields
from .models import NEWS, Person, User
from rest_framework import serializers

class Newsserializer(serializers.ModelSerializer):
    class Meta:
        model = NEWS
        fields = (
            'id',
            'title',
            'description',
            'Newsurl',
            'Imageurl',
            'publishedAt',
            "likes"
        )

class Personserializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = (
            'id',
            'user',
            'username',
            'password',
            'token',
            'is_verified'
        )


class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = (
            'id',
            'username',
            'email',
            'password',
            'is_authenticated'
        )