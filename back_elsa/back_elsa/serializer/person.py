from rest_framework import serializers
from back_elsa.models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'name', 'last_name','username','password','type_user', 'status','created_at','user_created']