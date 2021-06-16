from django.contrib import admin

# Register your models here.
from .models import Product, contact, fc

admin.site.register(Product)
admin.site.register(contact)
admin.site.register(fc)
