from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from web.models import CustomUser
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from rest_framework import serializers, viewsets,status
# Create your views here.
class TokenViewSet(viewsets.ViewSet):
    """
    API endpoint that allows users to obtain a token.
    """
    serializer_class = TokenObtainPairSerializer

    def create(self, request):
        print("called")
        print(request.data)
        
        serializer = self.serializer_class(data=request.data)
       
        serializer.is_valid(raise_exception=True)
        
        
        phone_number = serializer.validated_data.get('phone_number')
        
        print("this",serializer.validated_data)
        
        
        if phone_number is None:
            return Response({'error': 'Phone number is required'}, status=400)
        user = get_object_or_404(CustomUser, phone_number=phone_number)
        test = CustomUser.objects.get(username = user)
        print('test passed',test.id)
        print(user)
        print(phone_number)
        token = serializer.get_token(user)
        return Response({
            'access': str(token.access_token),
            'refresh': str(token),
            'user': str(user.id)
        })