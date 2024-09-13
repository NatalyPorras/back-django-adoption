from django.urls import path
from back_elsa.views import person_list, update_person,person_list_by_id,delete_person,create_person  # Asegúrate de que el import sea correcto

urlpatterns = [
    path('persons/', person_list, name='person_list'),
    # path('persons/', person_user_list, name='person_user_list'),
    path('persons/<uuid:id>', person_list_by_id, name='person_list_by_id'),
    path('persons/create', create_person, name='create_person'),
    path('persons/<uuid:id>/update', update_person, name='update_person'),
    path('persons/<uuid:id>/delete', delete_person, name='delete_person'),
]
