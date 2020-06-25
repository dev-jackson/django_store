from django.db import models
from decimal import Decimal
# Create your models here.

class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    type_user = models.CharField(max_length=8,default='client')
    def __srt__(self):
        return self.first_name

class Product(models.Model):
    id_product = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'media/',default='media/none/no_product.png')
    description = models.CharField(max_length = 500)
    price = models.DecimalField(max_digits =500, decimal_places=2, default=Decimal('0.0'))

class User_Product(models.Model):
    id_user = models.ForeignKey(User,on_delete=models.CASCADE)
    id_product = models.ForeignKey(Product,on_delete=models.CASCADE)
