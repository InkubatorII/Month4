from random import choices
from django.db import models

'''
post.



'''
class Comment(models.Model):
    text = models.CharField(max_length=250)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

class Tag(models.Model):
    name = models.CharField(max_length=50)

class Post(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='static/images/')
    title = models.CharField(max_length=70)
    content = models.TextField(null=True, blank=True)
    rate = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag, related_name='posts')

    def __str__(self):
        return self.title


