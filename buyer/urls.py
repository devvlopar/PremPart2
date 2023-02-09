from django.urls import path
from .views import * 

urlpatterns = [ 
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('create_row/', create_row, name="create_row"),
    path('delete_row/', delete_row, name="delete_row"),
    path('faqs/', faqs, name="faqs"),
    path('register/', register, name="register"),
    path('otp/', otp, name="otp"),





    
]