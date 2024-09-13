from rest_framework import serializers
from back_elsa.models import Status

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'name', 'code', 'created_at','user_created']