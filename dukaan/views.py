from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.response import Response

class ExampleView(APIView):
    @swagger_auto_schema(
        operation_description="Retrieve a greeting message",
        responses={200: openapi.Response('Success', schema=openapi.Schema(type=openapi.TYPE_STRING))}
    )
    def get(self, request):
        return Response({"message": "Hello, World!"})
