from django.contrib import admin
from .models import Supplier
from .models import Restaurant
from .models import Order

# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Order)
admin.site.register(Supplier)