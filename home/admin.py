from django.contrib import admin
from django.contrib.admin import register
from .models import *


@register(Background)
class BackgroundAdmin(admin.ModelAdmin):
    list_display=["id","image"]
@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=["category_name"]
    list_display_links=['category_name']

@register(Product)
class ProductAdmin(admin.ModelAdmin):
     list_display=["id","name","description","category_name","image"]
     list_display_links=['name']


@register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display=["id","name","image"]
    list_display_links=['name']


@register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display=["id","title","description","publish_date","image"]
    list_display_links=['title']


@register(CustomerMessage)
class ContactAdmin(admin.ModelAdmin):
    list_display=["id","name","lastname","gender","email","subject","comment","send_date"]
    list_display_links=['name']


@register(Founder)
class FounderAdmin(admin.ModelAdmin):
    list_display=["id","name","position","bio","image"]
    list_display_links=['name']
