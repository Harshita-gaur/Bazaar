from django.urls import path
from .views import login_user,logout,signup,activate_email
urlpatterns=[
    path('login/',login_user,name='login'),
    path('logout/',logout,name='logout'),
    path('signup/',signup,name='signup'),
    path('activate/<email_token>/',activate_email,name='activate_email')
]