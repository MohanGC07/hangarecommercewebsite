from django.db import models

# Create your models here.

class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=500, default="" ,blank=True, null=True)
    sub_category=models.CharField(max_length=500 , default="", blank=True, null=True)
    price=models.IntegerField(default=0)
    description=models.CharField(max_length=50000, blank=True, null=True)
    publish_date=models.DateField()
    image=models.ImageField(upload_to="shop/images",default="" )

def __str__(self):
    return self.product_name

class Contact(models.Model):
    msgid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=500, default="")
    phone=models.CharField(max_length=500 , default="")
    desc=models.CharField(max_length=50000 , default="")
    

def __str__(self):
    return self.name


class Orders(models.Model):
    order_id= models.AutoField(primary_key=True)
    items_json= models.CharField(max_length=5000)
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=111)
    address=models.CharField(max_length=111)
    city=models.CharField(max_length=111)
    phone = models.CharField(max_length=20)
    state=models.CharField(max_length=111)
    zip_code=models.CharField(max_length=111)

class OrderUpdate(models.Model):
    update_id= models.AutoField(primary_key=True)
    order_id= models.IntegerField(default="")
    update_desc= models.CharField(max_length=5000)
    timestamp= models.DateField(auto_now_add= True)

def __str__(self):
    return self.update_desc[0:7] + "..."



