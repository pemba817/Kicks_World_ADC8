from django.urls import path,include
from .views import *

urlpatterns=[
    path('add-product',get_products)
]