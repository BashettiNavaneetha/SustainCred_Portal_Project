from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    location=models.CharField(max_length=80)
    country=models.CharField(max_length=80)
    resume=models.FileField(upload_to='resumes/', null=True,blank=True)

    def __str__(self):
        return self.user.username