import os
import uuid

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


    class Meta:
        abstract = True


class Content(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(default='')

    class Meta:
        ordering = ['-created_at']


def image_upload_to(instance, filename):
    ext = filename.split('.')[-1]
    return os.path.join(instance.UPLOAD_PATH, filename)


class Image(BaseModel):
    UPLOAD_PATH = 'user-upload'

    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    image = models.FileField(upload_to=image_upload_to)
    order = models.SmallIntegerField() # image numbering
    downloads = models.IntegerField()
    point = models.SmallIntegerField()


    class Meta:
        unique_together = ['content', 'order']
        ordering = ['order']


class VideoFile(BaseModel):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)

    video = models.FileField(upload_to="user-upload/")

    def __str__(self):
        return self.caption


class FollowRelation(BaseModel):
    follower = models.OneToOneField(User, on_delete=models.CASCADE)
    followee = models.ManyToManyField(User, related_name='followee')
