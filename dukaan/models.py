from django.db import models
import uuid
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class TimeStamp(models.Model):
    uid=models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    created_at=models.DateTimeField(auto_now=True)
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="category_created_by")
    # updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="category_updated_by")
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        abstract=True
   
class Category(TimeStamp):
    category=models.CharField(max_length=250)
    slug=models.SlugField(null=True,unique=True)
    desc=models.TextField()
    cat_image=models.ImageField(upload_to="categories")
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.category)
        super(Category,self).save(*args,**kwargs) 
    def __str__(self):
        return self.category

class ColorVariant(TimeStamp):
    color = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.color

class SizeVariant(TimeStamp):
    size = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    
    def __str__(self):
        return self.size
     
class Product(TimeStamp):
    title=models.CharField(max_length=50)
    price=models.FloatField(default=0)
    slug =models.SlugField(null=True,unique=True)
    category =models.ForeignKey(Category,on_delete=models.PROTECT,related_name="category_products")
    desc=models.TextField()
    color= models.ManyToManyField(ColorVariant , blank=True)
    size = models.ManyToManyField(SizeVariant , blank=True)
    # image=models.ImageField(upload_to='products')
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(Product,self).save(*args,**kwargs)
    def __str__(self):
        return self.title
        
class ProductImage(TimeStamp):
    product = models.ForeignKey(Product , on_delete=models.CASCADE , related_name="product_images")
    image =  models.ImageField(upload_to="products")