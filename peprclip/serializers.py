
# article/serializers.py

from rest_framework import serializers
from peprclip import models

class Peprclip_function_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.peprclip_function
        fields = [
            'id',
            'function_name',
            'created',
            'updated'
        ]

class Peprclip_function_detail_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.peprclip_function
        fields = '__all__'
