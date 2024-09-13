from django.urls import path
from back_elsa.views import animal_list, create_animal, update_animal,animal_list_by_id,delete_animal  # Asegúrate de que el import sea correcto

urlpatterns = [
    path('animals/', animal_list, name='animal_list'),
    path('animals/<uuid:id>', animal_list_by_id, name='animal_list_by_id'),
    path('animals/create', create_animal, name='create_animal'),
    path('animals/<uuid:id>/update', update_animal, name='update_animal'),
    path('animals/<uuid:id>/delete', delete_animal, name='delete_animal'),
]
