from django.db import models

# Create your models here.
class upload(models.Model):
    upload = models.FileField()

    def __str__(self):
        return self.uploadText

class results(models.Model):
    genome_size = models.CharField(max_length = 30)
    repeat = models.CharField(max_length = 30)
    tax_ID = models.CharField(max_length = 30)
    dist = models.CharField(max_length = 30)