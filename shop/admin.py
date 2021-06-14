from django.contrib import admin

# Register your models here.
from .models import Product, contct

admin.site.register(Product)
admin.site.register(contct)
