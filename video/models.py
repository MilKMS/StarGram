from django.db import models

# Create your models here.
class Video(models.Model):
    caption = models.CharField(max_length=100)
    video = models.FileField(upload_to="video/")
    def __str__(self):
        return self.caption

class FilesAdmin(models.Model):
    adminupload = models.FileField(upload_to='media/')
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
