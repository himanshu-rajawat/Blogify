from django.shortcuts import render
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserSerializer, UserDetailSerializer, UserProfileSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import parser_classes
from rest_framework.parsers import FormParser, MultiPartParser

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

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser,FormParser])
def profilepicupload(request):
    if request.method == 'POST':
        id = request.user.id
        profile = User.objects.get(id=id).profile
        if profile:
            profile.image = request.data['image']
            profile.save()
            return Response({"status":"uploaded"})
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def profilebioupload(request):
    if request.method == 'POST':
        id = request.user.id
        profile = User.objects.get(id=id).profile
        if profile:
            serializer = UserProfileSerializer(instance=profile,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status":"uploaded"})
            else:
                return Response({"status":"invalid format"},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
