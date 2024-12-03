import smtplib
from itertools import product

from django.shortcuts import render
from customer.models import CustRegistration

from customer.models import userlogin

from customer.models import Feedback

from customer.models import AddProduct

from customer.models import OrderRequest

from customer.models import PaymentInfo

from customer.models import ShopReg

from customer.models import userlogin


# Create your views here.
def insertindex(request):
    return render(request,"index.html")
def insertlogin(request):
    return render(request,"login.html")

def insertCustRegistration(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")
        s6 = request.POST.get("t6")
        s7 = request.POST.get("t7")
        s8 = request.POST.get("t8")
        CustRegistration.objects.create(custid=s1, name=s2, city=s3, pincode=s4, address=s5, contectno=s6, email=s7, block_status=s8)
        userlogin.objects.create(username=s7,password=s6,utype='customer')
        return render(request,"CustRegistration.html")

    return render(request,"CustRegistration.html")

def insertfeedback(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")
        s6 = request.POST.get("t6")
        Feedback.objects.create(orderno=s1, productname=s2, aboutproduct=s3, aboutservice=s4, ratings=s5, shop_id=s6)
        return render(request,"Feedback.html")
    return render(request,"Feedback.html")

def insertAddProduct(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")
        s6 = request.POST.get("t6")
        s7 = request.POST.get("t7")
        s8 = request.POST.get("t8")
        s9 = request.POST.get("t9")
        AddProduct.objects.create(pid=s1, shopid=s2, category=s3, productname=s4, qty=s5, price=s6, image=s7, shopname=s8)
        return render(request,"AddProduct.html")

    return render(request,"AddProduct.html")

def insertOrderRequest(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")
        s6 = request.POST.get("t6")
        s7 = request.POST.get("t7")
        s8 = request.POST.get("t8")
        s9 = request.POST.get("t9")
        s10 = request.POST.get("t10")
        s11 = request.POST.get("t11")
        s12 = request.POST.get("t12")
        s13 = request.POST.get("t13")
        OrderRequest.objects.create(shop_id=s1, cust_id=s2, pname=s3, qty=s4, unit_price=s5, total=s6, gst=s7,
                                  cgst=s8, sgst=s9, grandtotal=s10, order_date=s11, order_status=s12, payment_status=s13 )
        return render(request, "OrderReq.html")

    return render(request,"OrderReq.html")

def insertPaymentInfo(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")
        PaymentInfo.objects.create(shop_id=s1, cust_id=s2, order_no=s3, total_amount=s4, pay_date=s5)
        return render(request,"Payment.html")

    return render(request,"Payment.html")



def showproduct(request):
    userdict=AddProduct.objects.all()
    return render(request,"viewproduct.html",{'userdict':userdict})

def showCustRegistration(request):
    userdict=CustRegistration.objects.all()
    return render(request,"viewCustRegistration.html",{'userdict':userdict})

def showShopReg(request):
    userdict=ShopReg.objects.all()
    return render(request,"viewShopReg.html",{'userdict':userdict})

def showFeedback(request):
    userdict=Feedback.objects.all()
    return render(request,"viewFeedback.html",{'userdict':userdict})

def showOrderRequest(request):
    userdict=OrderRequest.objects.all()
    return render(request,"viewOrderRequest.html",{'userdict':userdict})

def showPaymentInfo(request):
    userdict=OrderRequest.objects.all()
    return render(request,"viewPaymentInfo.html",{'userdict':userdict})

def logcheck(request):
    if request.method == "POST":
        s1 = request.POST.get("t1")
        request.session['username'] = s1
        s2 = request.POST.get("t2")
        ucheck = userlogin.objects.filter(username=s1).count()
        if ucheck >= 1:
            udata = userlogin.objects.get(username=s1)
            upass = udata.password
            utype = udata.utype
            if upass == s2:
                if utype == "owner":
                    return render(request, 'owner_home.html')
                if utype == "customer":
                    return render(request, 'customer_home.html')
            else:
                return render(request, 'login.html', {'msg': 'invalid password'})
        else:
            return render(request, 'login.html', {'msg': 'invalid username'})
    return render(request,"login.html")


def changepassword(request):
    if request.method == "POST":
        uname = request.session['username']
        currentpass = request.POST.get('t1', '')
        newpass = request.POST.get('t2', '')
        confirmpass = request.POST.get('t3', '')

        ucheck = userlogin.objects.filter(username=uname).values()
        for a in ucheck:
            u = a['username']
            p = a['password']
            if u == uname and currentpass == p:
                if newpass == confirmpass:
                    userlogin.objects.filter(username=uname).update(password=newpass)
                    return render(request, 'login.html', {'msg': 'Password has been changed successfully'})
                else:
                    return render(request, 'changepassword.html', context={'msg': 'Both the Username and password'})
            else:
                return render(request, 'changepassword.html', context={'msg': 'Invalid Username'})
    return render(request, 'changepassword.html')

def custreg_del(request,pk):
    rid=CustRegistration.objects.get(id=pk)
    rid.delete()
    userdict=CustRegistration.objects.all()
    return render(request,'viewCustRegistration.html',{'userdict':userdict})

def shopcustreg_del(request,pk):
    rid=ShopReg.objects.get(id=pk)
    rid.delete()
    userdict=ShopReg.objects.all()
    return render(request,'viewShopReg.html',{'userdict':userdict})

def Feedbackreg_del(request,pk):
    rid=Feedback.objects.get(id=pk)
    rid.delete()
    userdict=Feedback.objects.all()
    return render(request,'viewFeedback.html',{'userdict':userdict})

def productreg_del(request,pk):
    rid=AddProduct.objects.get(id=pk)
    rid.delete()
    userdict=AddProduct.objects.all()
    return render(request,'viewproduct.html',{'userdict':userdict})

def OrderRequestreg_del(request,pk):
    rid=OrderRequest.objects.get(id=pk)
    rid.delete()
    userdict=OrderRequest.objects.all()
    return render(request,'viewOrderRequest.html',{'userdict':userdict})

def sendpass(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        udata = userlogin.objects.get(username=s1)
        upass = udata.password
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login('mohankrh573@gmail.com', 'zvpg hkvo vyxn ovhf')
        mail.sendmail('mohankrh573@gmail.com', s1, upass)
        mail.close()
        return render(request, "login.html")
    return render(request, "forgotpassword.html")


def logout(request):
    return render(request,"index.html")
