from django.contrib import admin
from .models import *

admin.site.register(FoodType)
admin.site.register(FoodItem)
admin.site.register(Cart)
admin.site.register(UserOrder)
