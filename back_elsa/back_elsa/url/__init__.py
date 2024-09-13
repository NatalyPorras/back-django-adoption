from django.urls import path, include

urlpatterns = [
    path('api/', include('back_elsa.url.animal_url')),
    path('api/', include('back_elsa.url.status_url')),
    path('api/', include('back_elsa.url.person_url')),
    # Puedes incluir otras URLs aquí si es necesario
]