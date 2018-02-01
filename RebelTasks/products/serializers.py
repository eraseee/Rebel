from rest_framework import serializers
from products.models import Product, Company, Country, CountryProducts




class CountrySerializer(serializers.ModelSerializer):
	class Meta:
		model = Country
		fields = ('name', 'continent')



class CompanySerializer(serializers.ModelSerializer):
	country = CountrySerializer()
	
	class Meta:
		model = Company
		fields = ('name', 'country')
	

class ProductSerializer(serializers.Serializer):
	company = CompanySerializer()
	
	class Meta:
		model = Product
		fields = ('name', 'details', 'company')



class CountryProductsSerializer(serializers.Serializer):
	product = ProductSerializer()
	country = CountrySerializer()
	
	class Meta:
		model = CountryProducts
		fields = ('stock', 'price', 'product', 'country')
	

class CountriesWithProductsSerializer(serializers.Serializer):
	country = CountrySerializer()

	class Meta:
		model = CountryProducts
		fields = ('country')