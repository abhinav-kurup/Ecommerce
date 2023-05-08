from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length= 100,blank=True)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Order(models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_ordered = models.DateField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.IntegerField(null=True)
    @property
    def status(self):
        return self.complete

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
            
    

    def __int__(self):
        return self.id

class ShippingAddress(models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    address = models.CharField(max_length= 200)
    city = models.CharField(max_length= 50)
    state = models.CharField(max_length= 50)
    zipcode = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.address

class Product(models.Model):
    name = models.CharField(max_length= 100)
    price = models.IntegerField()
    digital = models.BooleanField(default=False,null=True, blank=True)
    image = models.ImageField(upload_to="product_images",default="placeholder.png")

class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    date_added = models.DateField(auto_now_add=True)
    
    def __int__(self):
        return self.id
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
