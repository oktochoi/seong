from django.db import models

# Create your models here.
class Content(models.Model):
    img_path = models.CharField(max_length=255)
    site = models.CharField(max_length=255)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description