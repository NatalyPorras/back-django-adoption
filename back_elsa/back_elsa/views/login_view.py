# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.views import APIView
# from django.contrib.auth import authenticate
# from django.contrib.auth.models import User
# from rest_framework.permissions import AllowAny
# from django.contrib.auth.hashers import check_password
# from rest_framework import serializers
# from back_elsa.models import Person
# class TokenObtainPairSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField()

# class TokenObtainPairView(APIView):
#     def post(self, request, *args, **kwargs):
#         # Obtén los datos del cuerpo de la solicitud
#         username = request.data.get('username')
#         password = request.data.get('password')

#         try:
#             # Intenta obtener el usuario de la tabla Persona
#             persona = Person.objects.get(username=username)
#             print(persona.password)
#             print(password)
#             # Verifica la contraseña (suponiendo que esté hasheada)
#             if persona.password == password:
#                 # Genera el token JWT
#                 refresh = RefreshToken.for_user(persona)
#                 return Response({
#                     'refresh': str(refresh),
#                     'access': str(refresh.access_token),
#                     'user_type': persona.type_user
#                 })
#             else:
#                 return Response({'error': 'Contraseña incorrecta'}, status=status.HTTP_401_UNAUTHORIZED)
        
#         except Person.DoesNotExist:
#             return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
