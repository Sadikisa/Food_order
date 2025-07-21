from django.urls import path
from . import views

urlpatterns = [
     path('',views.sign_up,name='signup'),
     path('signin',views.log_in,name='signin'),
     path('home',views.home,name='home'),
     path('rest',views.rest,name='rest'),
     path('show',views.show,name='show'),
     path('rest1',views.rest1,name='rest1'),
     path('rest2',views.rest2,name='rest2'),
     path('rest3',views.rest3,name='rest3'),
     path('order',views.user_restaurants,name='order'),
     path('orders1',views.orders1,name='orders1'),
     path('orders2',views.orders2,name='orders2'),
     path('orders3',views.orders3,name='orders3'),
     path('out',views.log_out,name='out'),
     path('sad',views.sadik,name='sadik'),
     path('status',views.status,name='status')


]