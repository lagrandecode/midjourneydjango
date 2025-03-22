from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    story = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="images/")
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
