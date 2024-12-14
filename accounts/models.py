from django.db import models
from django.contrib.auth.models import User
from dukaan.models import TimeStamp
# Create your models here.
class Profile(TimeStamp):
    user= models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    is_email_verified=models.BooleanField(default=False)
    profile_image=models.ImageField(upload_to='profiles')
    email_token=models.CharField(max_length=100,null=True,blank=True)