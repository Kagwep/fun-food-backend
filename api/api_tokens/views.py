from django.shortcuts import render

# Create your views here.
from django.forms.models import model_to_dict
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
        
        
        phone_number = request.data.get('phone_number')
        
        
        if phone_number is None:
            return Response({'error': 'Phone number is required'}, status=400)
        user = get_object_or_404(CustomUser, phone_number=phone_number)
        print(user)
        user_det = CustomUser.objects.get(full_names = user)
        print(user_det)
        print(phone_number)
        user_details = model_to_dict(user_det)
        token = serializer.get_token(user)
        return Response({
            'access': str(token.access_token),
            'refresh': str(token),
            'user': user_details,
        })
        
        