from django.db import models

# Create your models here.
#tabels:
class userlogin(models.Model):
    username=models.CharField(max_length=40)
    password=models.CharField(max_length=20)
    utype=models.CharField(max_length=20)

class CustRegistration(models.Model): #this all are we create tables( cmd: 1 makemigrations 2.migrate)
    custid = models.CharField(max_length=20)
    name=models.CharField(max_length=40)
    city=models.CharField(max_length=30)
    pincode=models.IntegerField()
    address=models.CharField(max_length=60)
    contectno=models.CharField(max_length=10)
    email=models.CharField(max_length=40)
    block_status=models.CharField(max_length=30)



class ShopReg(models.Model):
    shopid = models.CharField(max_length=20)
    shopname=models.CharField(max_length=50)
    city=models.CharField(max_length=30)
    address=models.CharField(max_length=60)
    contectper=models.CharField(max_length=40)
    contectno=models.CharField(max_length=10)
    email=models.CharField(max_length=40)
    status = models.CharField(max_length=40)
    block_status = models.CharField(max_length=40)



class Feedback(models.Model):
    orderno =models.CharField(max_length=20)
    productname =models.CharField(max_length=20)
    aboutproduct =models.CharField(max_length=100)
    aboutservice =models.CharField(max_length=100)
    ratings =models.CharField(max_length=20)
    shop_id = models.CharField(max_length=50)

class AddProduct(models.Model):
    pid =models.CharField(max_length=20)
    shopid =models.CharField(max_length=30)
    category =models.CharField(max_length=30)
    productname =models.CharField(max_length=30)
    qty =models.CharField(max_length=20)
    price =models.CharField(max_length=30)
    image = models.FileField(upload_to='documents/')#to upload document in forder
    shopname = models.CharField(max_length=50,null=True)

class OrderRequest(models.Model):
    shop_id=models.CharField(max_length=40)
    cust_id=models.CharField(max_length=50)
    pname=models.CharField(max_length=100)
    qty=models.IntegerField()
    unit_price=models.IntegerField()
    total=models.IntegerField()
    gst=models.IntegerField()
    cgst=models.IntegerField()
    sgst=models.IntegerField()
    grandtotal=models.IntegerField()
    order_date=models.DateField()
    order_status=models.CharField(max_length=30)
    payment_status = models.CharField(max_length=30)

class PaymentInfo(models.Model):
    shop_id=models.CharField(max_length=50)
    cust_id=models.CharField(max_length=50)
    order_no=models.IntegerField()
    total_amount=models.IntegerField()
    pay_date=models.CharField(max_length=30)



