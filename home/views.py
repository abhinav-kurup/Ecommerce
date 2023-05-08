from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from .models import *
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout


def http(request):
     return HttpResponse("Successful")
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return render(request,'home/signup.html')
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return render(request,'home/signup.html')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()

                user_model = User.objects.get(username=username)
                new_costumer = Customer.objects.create(user=user_model, name= username )
                new_costumer.save()
                auth.login(request,user)

                return redirect("/")

        else:
            messages.info(request,'Password not matching')
            return render(request,'home/signup.html')

    else: 
        return render(request,'home/signup.html')
    
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            costumer = Customer.objects.filter(user=user)
            context = {'usern': costumer}
            return redirect("/",context)
        else:
             messages.info(request,'Bad Credentials')
             return redirect("signin")
    else: 
        return render(request,'home/signin.html')



def logout_view(request):
    logout(request)
    return redirect('/')

def home(request):
    products = Product.objects.all()
    user = request.user
    context = {'products':products,'user': user}
    return render(request,'home/store.html',context)

@csrf_exempt
@login_required(login_url="signin")
def add_cart(request):
    pid = request.POST["add"] 
    product = Product.objects.get(id=pid)
    user = request.user
    customer = Customer.objects.get(user=user)
    order , created = Order.objects.get_or_create(customer=customer,complete=False)
    orderitem ,created = OrderItem.objects.get_or_create(product=product,order=order)
    orderitem.quantity = 1
    orderitem.save()
    return redirect("/")

@login_required(login_url="signin")
def cart(request):
    user= request.user
    customer = Customer.objects.get(user=user)
    order = Order.objects.get(customer=customer)
    if order:
        if order.complete == False:
            orderitem = OrderItem.objects.filter(order=order)

            context = { 'items':orderitem,'order':order}
    else:
        context={}
    return render(request, 'home/cart.html', context)

def checkout(request):
    id = request.GET["ord"]
    print(id)
    order = Order.objects.get(id=id)
    context = {"order":order}
    return render(request, 'home/checkout.html', context)

def shipping(request):
     if request.method == 'POST': 
        addr = request.POST["address"]
        city = request.POST["city"]
        state = request.POST["state"]
        zip = request.POST["zipcode"]
    
     user= request.user
     customer = Customer.objects.get(user=user)
     order = Order.objects.get(customer=customer)
     ship , created = ShippingAddress.objects.get_or_create(customer=customer,order=order,address=addr,city=city,state=state,zipcode=zip)
     if created == False:
         
        ship.save()
     return JsonResponse("DONE",safe=False)
     
