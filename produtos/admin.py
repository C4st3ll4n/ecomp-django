from django.contrib import admin

# Register your models here.
from produtos.models import Product, Order, Category

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
