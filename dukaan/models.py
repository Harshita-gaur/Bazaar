from django.db import models
import uuid
# Create your models here.
class TimeStamp(models.Model):
    uid=models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    created_at=models.DateTimeField(auto_now=True)
    created_by=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)
    updated_by=models.DateTimeField(auto_now=True)
    class Meta:
        abstract=True
        
class Product(models.Model):
    Title=models.CharField(max_length=50)
    Price=models.FloatField(default=0)
    class Meta:
        abstract=True
        
class Category(models.Model):
    category=models.CharField(max_length=250)
    desc=models.TextField()