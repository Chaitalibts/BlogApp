from distutils.command.upload import upload
from email.mime import image
from email.policy import default
from unicodedata import category
from xml.parsers.expat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):

    title = models.CharField(max_length=150)
    desc = models.TextField()
    category = models.CharField(max_length=100,default="")
    image = models.ImageField(upload_to="blogImage",default="")

    def __str__(self):
        return self.category
