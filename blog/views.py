from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from .models import Post, Following, Readlater
# from.models import Post
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import PostSerializer, PostCreatetSerializer, AddReadLaterSerializer, FollowingSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from itertools import chain
from django.contrib.auth.models import User

# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def apiOverview(request):
    return Response("List of url Pattern")

# @api_view(['POST'])
# def createpost(request):
#     if request.method == 'POST':
#         data= request.data
#         print(request.user.id)
#         data["author"] = request.user.id
#         serializer = PostSerializer(data=data)
#         dic={}
#         if serializer.is_valid():
#             post = serializer.create(serializer.validated_data)
#             dic["response"]="Post uploaded"
#             dic["author"] = post.author
#             return Response({"response":"Post uploaded"})
#         else:
#             print("invalid format")
#             return Response(serializer.errors)
#         return Response({"response":"Post uploaded"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getfeed(request):
    if request.method == 'GET':
        blogs = Post.objects.none()
        blog = Post.objects.none()
        user_following = request.user.following_set.all()
        for user in user_following:
            id = user.following
            posts = User.objects.get(id =id).post_set.all()
            blogs = blogs|posts
        if blogs:
            serializer = PostSerializer(blogs,context={'request': request}, many=True)
            return Response(serializer.data)
        else:
            return Response({"res":"No post"},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def explore(request):
    if request.method == 'GET':
        try:
            posts = Post.objects.all()
            serializer = PostSerializer(posts, context={'request': request},many=True)
            return Response(serializer.data)
        except:
            return Response({"res":"No post"},status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createpost(request):
    if request.method == 'POST':
           data= request.data
           data["author"] = request.user.id
           serializer = PostCreatetSerializer(data=data)
           if serializer.is_valid():
               post = serializer.create(serializer.validated_data)
               return Response({"response":"Post uploaded"})
           else:
               return Response(serializer.errors)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updatelike(request):
    if request.method == 'POST':
        id = request.data["id"]
        post = Post.objects.get(id=id)
        post.upwote_count+=1
        post.save()
        val=post.upwote_count
        return Response({"upwote_count":val})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addreadlater(request):
    if request.method == 'POST':
        data = request.data
        data['user'] = request.user.id
        serializer = AddReadLaterSerializer(data=data)
        if serializer.is_valid():
            readlater = Readlater.objects.create(
            user=serializer.validated_data['user'],
            post = serializer.validated_data['post'])
            readlater.save()
            return Response({"response":"post added to read later section"})
        else:
            return Response({"response":"data format is incorrect"},status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getreadlater(request):
    if request.method == 'GET':
        try:
            blogs = Post.objects.none()
            objects = request.user.readlater_set.all()
            for object in objects:
                id = object.post.id
                post = Post.objects.filter(id=id)
                blogs = post|blogs
            serializer = PostSerializer(blogs,context={'request': request},many=True)
            return Response(serializer.data)
        except:
            return Response({"response":"No posts"},status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def unfollow(request,id):
    if request.method == 'DELETE':
        user = request.user.id
        following_obj = Following.objects.get(user=user, following = id )
        following_obj.delete()
        return Response({"resposne":"Unfollowed"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow(request):
    if request.method == 'POST':
        user = request.user.id
        data=request.data
        data['user'] = user
        serializer = FollowingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"response":"added as a follower"})
        else:
            return Response({"response":"Data Invalid"},status=status.HTTP_400_BAD_REQUEST)
