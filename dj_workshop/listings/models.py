from django.db import models

# Create your models here.
from realtors.models import Realtor


class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    zipcode = models.CharField(max_length=150)
    desc = models.CharField(max_length=150, verbose_name='Description')
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    garage = models.BooleanField()
    sqft = models.IntegerField()
    lot_size = models.DecimalField(decimal_places=2, max_digits=5)
    is_published = models.BooleanField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo4 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo5 = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    photo6 = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    list_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


