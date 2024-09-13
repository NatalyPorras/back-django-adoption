import uuid
from django.db import models
#  Creamos la tabla
class Animal(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    species=models.CharField(max_length=100)
    type_animal=models.CharField(max_length=5)
    status_code=models.CharField(max_length=2,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user_created = models.TextField(null=True)
    
    def __str__(self):
        return self.name