from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='timeline_photo/%y/%m/%d')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "text : " + self.text