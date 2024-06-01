from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register your models here.

@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(Company)
class Company(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(subCategory)
class Subcategory(admin.ModelAdmin):
    list_display = ['id','name','Category_id']

@admin.register(Review)
class Reviews(admin.ModelAdmin):
    list_display = ['id','review','rating','Created_at']

@admin.register(Cart)
class Carts(admin.ModelAdmin):
    list_display = ['id', 'user', 'created_at']

@admin.register(CartItem)
class CartItems(admin.ModelAdmin):
    list_display = ['id','cart','product','quantity','Totalprice']


class ImageAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:100px; max-height:100px"/>'.format(obj.image.url))
    
    def description_txt(self,obj):
        return obj.description[:120]+'.....'

    image_tag.short_description = 'Image'
    list_display = ['id', 'image_tag','name','company','Category','subCategory','description_txt','price']

admin.site.register(Product, ImageAdmin)
# @admin.register(Product)
# class Product(admin.ModelAdmin):
#     list_display = ['id','image','name','company','Category','subCategory','description','price']
