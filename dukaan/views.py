from django.shortcuts import render
from .models import Product
# Create your views here.
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


def index(request):
    context={'products':Product.objects.all()}
    return render(request,'index.html',context)

class get_product(APIView):
    @swagger_auto_schema(
        operation_description="Retrieve a product",
        responses={200: openapi.Response('Success', schema=openapi.Schema(type=openapi.TYPE_STRING))}
    )
    def get(self,request,slug):
        try:
            product=Product.objects.filter(slug=slug)
            return render(request,'product.html',context={'product':product})
        except Exception as e:
            print(str(e))
