from django.contrib import admin
from django import forms

from .models import CountryProducts
from .models import Country, Company, Product

class ProductInfo(admin.TabularInline):
	model = CountryProducts
	#exclude = ['country']

	
	
class CountryProductsAdmin(admin.ModelAdmin):
	inlines = [
		ProductInfo,
	]

admin.site.register(CountryProducts)
admin.site.register(Country)
admin.site.register(Company)
admin.site.register(Product, CountryProductsAdmin)