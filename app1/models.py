from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    phone_number=models.IntegerField(blank=True)