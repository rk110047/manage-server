
from django.contrib import admin
from .models import Product,Brand,Categories,SubCategory,Content,ProductImages,ContentCategory,ProductTax



admin.site.register(Product)
admin.site.register(Categories)
admin.site.register(Content)
admin.site.register(ProductImages)
admin.site.register(ContentCategory)
admin.site.register(ProductTax)
