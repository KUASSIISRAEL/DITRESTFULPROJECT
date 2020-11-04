from django.db import models
from django.urls import reverse

# Create your models here.

class Gerant(models.Model):
    SEXES_LIST = (("M", "MASCULIN"), ("F", "FEMININ"))

    name    = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email   = models.CharField(max_length=255)
    phone   = models.CharField(max_length=255)
    sexe    = models.CharField(max_length=2, choices=SEXES_LIST)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

class Magasin(models.Model):
    gerant  = models.OneToOneField(Gerant, on_delete=models.CASCADE)
    name    = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

class Article(models.Model):
    magasin = models.ForeignKey(Magasin, on_delete=models.CASCADE)
    name    = models.CharField(max_length=255)
    stock   = models.IntegerField(default=0)
    image   = models.ImageField(upload_to='articles', blank=True, default='')
    describe= models.TextField(verbose_name="desciption")
    price   = models.DecimalField(max_digits=10, decimal_places=3)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

class Customer(models.Model):
    SEXES_LIST = (("M", "MASCULIN"), ("F", "FEMININ"))

    name    = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email   = models.CharField(max_length=255)
    phone   = models.CharField(max_length=255)
    sexe    = models.CharField(max_length=2, choices=SEXES_LIST)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    STATUS = (("P", "PENDING"), ("C", "COMPLETED"), ("R", "REJECT"))
    
    article = models.OneToOneField(Article, on_delete=models.CASCADE)
    customer= models.OneToOneField(Customer, on_delete=models.CASCADE)
    amount  = models.DecimalField(max_digits=10, decimal_places=3)
    status  = models.CharField(max_length=2, choices=STATUS)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

class Invoice(models.Model):

    order   = models.OneToOneField(Order, on_delete=models.CASCADE)
    receipt = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
