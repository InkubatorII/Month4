from random import choices
from django.db import models

'''
post.



'''

class Post(models.Model):
    title = models.CharField(max_length=70)
    content = models.TextField(null=True, blank=True)
    rate = models.IntegerField(default=0)

    def __str__(self):
        return self.title

