from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Advisor(models.Model):
    name=models.CharField(max_length=150,blank=True,null=True)
    profile_pic=models.ImageField(upload_to='media/advisor')

    def __str__(self) -> str:
        return self.name

class Booking(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    advisor=models.ForeignKey(Advisor,on_delete=models.CASCADE)
    time=models.DateTimeField(auto_now=False, auto_now_add=False)

