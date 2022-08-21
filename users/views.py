from django.shortcuts import render
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserSerializer, UserDetailSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

@api_view(['GET'])
@permission_classes([AllowAny])
def apiOverview(request):
    return Response({
    'User Registration': 'register/'
    })

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            user = serializer.create(serializer.validated_data)
            data['response']="success"
            data['email'] = user.email
        else:
            data = serializer.errors
        return Response(data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def userdetails(request):
    if request.method == 'GET':
        id = request.user.id
        user = User.objects.get(id=id)
        if user:
            serializer = UserDetailSerializer(user,many=False)
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
