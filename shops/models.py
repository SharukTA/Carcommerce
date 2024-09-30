from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class Shopowner(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='shopowner_profile')
    shopname=models.CharField(max_length=200,null=True)
    ownername=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=10)
    address=models.TextField()
    license_certificate=models.FileField(upload_to='licenses/',null=True)
    is_approved=models.BooleanField(default=False)
    rejected=models.BooleanField(default=False)

class Product(models.Model):
    PRODUCT_TYPE_CHOICES=[
        ('EV','EV'),
        ('diesel','Diesel'),
        ('petrol','Petrol')
    ]
    GEAR_TRANSMISSION_CHOICES=[
        ('automatic','Automatic'),
        ('manual','Manual')
    ]
    product_company=models.CharField(max_length=200,null=True)
    product_name=models.CharField(max_length=200,null=True)
    product_type=models.CharField(max_length=50,choices=PRODUCT_TYPE_CHOICES,null=True)
    gear_transmission=models.CharField(max_length=50,choices=GEAR_TRANSMISSION_CHOICES,null=True)
    model_no=models.CharField(max_length=10,null=True)
    quantity=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(7)],null=True)
    photo=models.FileField(upload_to='photos/',null=True)
    shop_owner=models.ForeignKey(User,on_delete=models.CASCADE)