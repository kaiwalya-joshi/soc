from attr import fields
from .models import NEWS
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