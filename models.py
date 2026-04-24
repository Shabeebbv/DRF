from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()

    def __str__(self):
        return self.name
    
class Profile(models.Model):
    bio=models.TextField()
    
class User(models.Model):
    name=models.CharField(max_length=100)
    profile=models.OneToOneField(Profile,on_delete=models.CASCADE)

