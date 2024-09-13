from rest_framework import serializers
from back_elsa.models import Animal

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ['id', 'name', 'age', 'species','type_animal','status_code','created_at','user_created']