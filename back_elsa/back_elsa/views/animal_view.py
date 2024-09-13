# from django.http import HttpResponse
# from django.http import JsonResponse
# from back_elsa.models import Animal
# # from rest_framework.decorators import permission_classes
# from django.views.decorators.csrf import csrf_exempt
# from django.views.decorators.http import require_http_methods
# # from rest_framework.permissions import IsAuthenticated
# import json
# from back_elsa.serializer import AnimalSerializer
# # @permission_classes([IsAuthenticated])
# @require_http_methods(["GET"])
# def animal_list(request):
#     animals = Animal.objects.all()
#     data = list(animals.values())  # Convierte el queryset a una lista de diccionarios
#     return JsonResponse(data, safe=False)  # Devuelve una respuesta JSON

# @require_http_methods(["GET"]) 
# def animal_list_by_id(request,id):
#     animal = Animal.objects.get(id=id)
#     serializer = AnimalSerializer(animal)
#     # data = list(animal.values())  # Convierte el queryset a una lista de diccionarios
#     return JsonResponse(serializer.data, safe=False)  # Devuelve una respuesta JSON

# @csrf_exempt
# @require_http_methods(['POST', 'OPTIONS'])
# def create_animal(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         serializer = AnimalSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()  # Guarda los datos si son válidos
#             return JsonResponse(serializer.data, status=201)  # Devuelve la respuesta con los datos guardados
#         else:
#             return JsonResponse(serializer.errors, status=400) 
#     elif request.method == 'OPTIONS':
#         return JsonResponse({'message': 'Person ID not found'}, status=200) 

# @csrf_exempt
# @require_http_methods(["PUT"])
# def update_animal(request, id):
#     try:
#         animal = Animal.objects.get(id=id)
#     except Animal.DoesNotExist:
#         return JsonResponse({'error': 'Animal not found'}, status=404)
#     data = json.loads(request.body)
#     serializer = AnimalSerializer(animal, data=data, partial=True)
#     if serializer.is_valid():
#         serializer.save()
#         return JsonResponse(serializer.data)
#     return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# @require_http_methods(["DELETE"])
# def delete_animal(request, id):
#     animal = Animal.objects.get(id=id)
    
#     animal.delete()
    
#     return JsonResponse({'message': 'Animal deleted successfully'}, status=204)
