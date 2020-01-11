from django.db import models


class Product(models.Model):
    product_pic=models.ImageField()
    product_name=models.TextField()
    product_price=models.IntegerField()
    product_model=models.TextField()
    product_category=models.TextField()
    product_gender=models.TextField()
    product_details=models.TextField()