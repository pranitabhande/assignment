from asyncio.windows_events import NULL
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    author=models.CharField(max_length=14)
    upvote=models.IntegerField(default=0)
    downvote=models.IntegerField(default=0)
    timeStamp=models.DateTimeField(default=now)

    def __str__(self):
        return self.title

class Comment(models.Model):
    data=models.TextField()
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    time=models.DateTimeField(default=now)

    def __str__(self):
        return self.data