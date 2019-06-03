from django.db import models

# Create your models here.
class upload(models.Model):
    upload = models.FileField()
    uploadText = models.TextField()

    def __str__(self):
        return self.uploadText
