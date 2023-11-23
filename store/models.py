from ast import Try
from email.mime import image
from pickle import TRUE
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver 
from django.db.models.signals import post_save

class Customer(models.Model):
    #yaani user aando one customer o customer aando one user
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True,blank=True, related_name = "customer")
    name=models.CharField(max_length=200,null=True)    
    email=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=200,null=True)   
    price=models.DecimalField(max_digits=7,decimal_places=2) 
    slug=models.SlugField(max_length=200,default="")
    category=models.CharField(max_length=200,null=True) 
    digital=models.BooleanField(default=False,null=True,blank=True)
    image= models.ImageField(null=True,blank=True)
    stock = models.IntegerField(null=True, blank=True)
    stock_limit = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url=self.image.url
        except: 
            url=''
        return url
