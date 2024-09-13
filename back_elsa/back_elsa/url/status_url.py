from django.urls import path
from back_elsa.views import status_list, create_status  # Asegúrate de que el import sea correcto

urlpatterns = [
    path('status/', status_list, name='status_list'),
    path('status/create', create_status, name='create_status'),
]
