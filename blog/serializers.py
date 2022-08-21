from rest_framework import serializers
from .models import Post, Readlater, Following
from users.serializers import UserDetailSerializer

class PostSerializer(serializers.ModelSerializer):
    author = UserDetailSerializer()
    following = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = '__all__'
        depth = 1
    def get_following(self,obj):
        user =  self.context['request'].user
        author = obj.author
        qs = Following.objects.filter(user=user.id).filter(following = author.id)
        if len(qs) == 0:
            return(False)
        else:
            return(True)
    def validate(self,post):
        if post["title"] and post["content"]:
            return post
        else:
            raise serializers.ValidationError("Title and content are reuired fields")
    def create(self,validated_data):
        post = Post.objects.create(
        title = validated_data["title"],
        content= validated_data["content"],
        upwote_count=validated_data["upwote_count"],
        author=self.request.user
        )
        post.save()
        return post

class PostCreatetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
    def validate(self,post):
        if post["title"] and post["content"]:
            return post
        else:
            raise serializers.ValidationError("Title and content are reuired fields")
    def create(self,validated_data):
        post = Post.objects.create(
        title = validated_data["title"],
        content= validated_data["content"],
        author= validated_data["author"]
        )
        post.save()
        return post

class AddReadLaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Readlater
        fields = '__all__'

class FollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Following
        fields = '__all__'
