from ast import Try
from email.mime import image
from pickle import TRUE
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver 
from django.db.models.signals import post_save

# Create your models here.


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

class Order(models.Model):
    #a single customer can have multiple orders
    customer = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    order_day = models.DateField(auto_now_add=True, null= True)
    complete=models.BooleanField(default=False,null=True,blank=False)
    transaction_id=models.CharField(max_length=100,null=True)  

    def __str__(self):
        if self.customer is not None:
            return str(self.customer)
        return "Unknown"

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    @property
    def shipping(self):
        shipping=False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping=True
            return shipping

class OrderItem (models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True)
    #order ynjm ykoun aando barsha orderitems
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
   

class ShippingAddress (models.Model):
    customer = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True, related_name='addresse')
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
    name=models.CharField(max_length=200,null=True)   
    address=models.CharField(max_length=200,null=True)   
    city=models.CharField(max_length=200,null=True)   
    state=models.CharField(max_length=200,null=True)   
    zipcode=models.CharField(max_length=200,null=True)   
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


class Post(models.Model):
    title=models.CharField(max_length=200,null=True)   
    description=models.CharField(max_length=800,null=True) 
    slug=models.SlugField(max_length=200,default="")   
    date_posted = models.DateTimeField(auto_now_add=True)
    image= models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.title
        
    @property
    def imageURL(self):
        try:
            url=self.image.url
        except: 
            url=''
        return url

class Comment(models.Model):
    post=models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    body=models.TextField(max_length=200)
    date_commented=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title,self.name)


@receiver(post_save, sender=User)
def create_user_customer(sender, instance, created, **kwargs):
	print('****', created)
	if instance.is_staff == False:
		Customer.objects.get_or_create(user = instance, name = instance.username, email = instance.email)

