from django.urls import path
from .views import get_product,index
urlpatterns=[
    path('',index,name='index'),
    path('dukaan/<slug:slug>/',get_product.as_view(),name='get_product')
]