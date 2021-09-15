from django.contrib import admin
from .models import *
from .models import smartphone,Genre,Customer,CustomerLike,CustomerAddress,order

admin.site.register(smartphone)
admin.site.register(Genre)
admin.site.register(Customer)
admin.site.register(CustomerAddress)
admin.site.register(CustomerLike)
admin.site.register(order)