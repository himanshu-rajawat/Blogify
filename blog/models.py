from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from jsonfield import JSONField

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.JSONField(null=False)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    upwote_count = models.IntegerField(default=0)
    downwote_count = models.IntegerField(default=0)

class Following(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    following = models.IntegerField()
    following_date = models.DateTimeField(default=timezone.now)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'], name='unique_user_following_combination'
            )
        ]

class Readlater(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Post,on_delete = models.CASCADE)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'post'], name='unique_user_post_combination'
            )
        ]
