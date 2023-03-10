from django.db import models
#from django.contrib.auth import get_user_model

# Create your models here.
class Profile(models.Model):
    nom = models.CharField( primary_key=True ,max_length=50)
    password = models.CharField(max_length=50)

#class Amis(models.Model):
 #   nom_ami = models.CharField(max_length=30)
 #   user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    