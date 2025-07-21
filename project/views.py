from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Signform
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from .models import Restaurant
from .models import Order
from django.contrib.auth.decorators import login_required

# Create your views here.



def sign_up(request):
         # if request.method=='POST':
               
               form=Signform(request.POST)
              
               if form.is_valid():
                    form.save()
                    return  redirect('signin')
               return render(request,'sign_up.html',{'form':form})  


def  log_in(request):

   form=AuthenticationForm(data=request.POST)

   if form.is_valid():
     login(request,user)
     return redirect('home')
   return render(request,'log_in.html',{'form':form})

def home(request):

    return render(request,'home.html')
@login_required(login_url="signin")
def rest(request):
     
       return render(request,'rest.html')

def rest1(request):
    if request.method=='POST':
      dish=Order()
      dish.food=request.POST['food']
      dish.drink=request.POST['drink']
      dish.sos1=request.POST['first']
      dish.sos2=request.POST['second']
      dish.desc=request.POST['description']
      dish.adet=request.POST['price']
      dish.phone=request.POST['numb']

      dish.address=request.POST['ad']

      dish.price=int(dish.adet)*250
      dish.user=request.user
     
      dish.restaurant=Restaurant.objects .get(restaurant_id=212)
      dish.save()
      return redirect('sadik')
    return render(request,'rest1.html')

def rest2(request):
    if request.method=='POST':
      dish=Order()
      dish.food=request.POST['food']
      dish.drink=request.POST['drink']
      dish.sos1=request.POST['first']
      dish.sos2=request.POST['second']
      dish.desc=request.POST['description']
      dish.adet=request.POST['price']
      dish.phone=request.POST['numb']

      dish.address=request.POST['ad']
      dish.price=int(dish.adet)*250
      dish.user=request.user
      dish.restaurant=Restaurant.objects .get(restaurant_id=213)
      dish.save()
      return redirect('sadik')
    return render(request,'rest2.html')


def rest3(request):
    if request.method=='POST':
      dish=Order()
      dish.food=request.POST['food']
      dish.drink=request.POST['drink']
      dish.sos1=request.POST['first']
      dish.sos2=request.POST['second']
      dish.desc=request.POST['description']
      dish.adet=request.POST['price']
      
      dish.phone=request.POST['numb']

      dish.address=request.POST['ad']
      dish.price=int(dish.adet)*250


      dish.user=request.user
      dish.restaurant=Restaurant.objects .get(restaurant_id=214)
      dish.save()
      return redirect('sadik')
    return render(request,'rest3.html')


def show(request):

     users = Restaurant.objects.get(restaurant_id=213)
     cars=users.user.all()
     return render(request,'show.html',{'cars':cars})


def user_restaurants(request):
    username=request.user
    user = User.objects.get(username=username)
    orders = Order.objects.filter(user=user).select_related('restaurant')
    return render(request, 'orders_rest.html', {'user': user, 'orders': orders})

def orders1(request):
    restaurant = Restaurant.objects.get(restaurant_id=212)
    orders = Order.objects.filter(user=request.user, restaurant=restaurant)
    return render(request, 'order.html', {'restaurant': restaurant, 'orders': orders})

def orders2(request):
    restaurant = Restaurant.objects.get(restaurant_id=213)
    orders = Order.objects.filter(user=request.user, restaurant=restaurant)
    return render(request, 'order.html', {'restaurant': restaurant, 'orders': orders})

def orders3(request):
    restaurant = Restaurant.objects.get(restaurant_id=214)
    orders = Order.objects.filter(user=request.user, restaurant=restaurant)
    return render(request, 'order.html', {'restaurant': restaurant, 'orders': orders})

def  log_out(request):
    
       logout(request)
       return redirect('signup')
def sadik(request):

    
     return render(request,'succes.html')
def status(request):

    
     return render(request,'status.html')


