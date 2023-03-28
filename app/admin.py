from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

@admin.register(Usecases)
class UsecaseModelAdmin(admin.ModelAdmin):
	list_display = ['category']



admin.site.unregister(Group)


@admin.register(Company)
class CompanyModelAdmin(admin.ModelAdmin):
	list_display = ['name']


@admin.register(ProductCategory)
class ProductCategoryModelAdmin(admin.ModelAdmin):
	list_display = ['company','product_type']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
	list_display = ['category','title']

@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
	list_display = ['name','email','created_at']