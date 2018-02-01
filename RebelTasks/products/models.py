from django.db import models

class Country(models.Model):
	name = models.CharField(max_length=100)
	continent = models.CharField(max_length=100)
	def __str__(self):
		return self.name
	

	#ManyToOne relation with country, as a country can have multiple companies, but a company can only exist in one country.
	#This could potentially be a ManyToMany relation, depending on whether a companies main office is the only one that counts
	#or if all sub offices counts aswell.
class Company(models.Model):
	name = models.CharField(max_length=100)
	country = models.ForeignKey(Country, on_delete=models.CASCADE)
	def __str__(self):
		return self.name
	

	#ManytoOne relationship with company as a company can produce many different products.
class Product(models.Model):
	name = models.CharField(max_length=100)
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	details = models.CharField(max_length=255)
	def __str__(self):
		return self.name
	
	
	# Moved prices to countryproducts, since both where linked through countryId and productId
	# OneToOne relation with product, as there can only be one product with that specific Id, even if it exists in multiple countries.
	# OneToOne relation with country, since each country that potentially sell this product, will have a different stock and potentially different price.
#product = models.OneToOneField(Product, on_delete=models.CASCADE) Does not work, since a product can exist multiple times, but with different countries
	#country = models.OneToOneField(Country, on_delete=models.CASCADE) Same reason as the product.
class CountryProducts(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	country = models.ForeignKey(Country, on_delete=models.CASCADE)
	stock = models.IntegerField()
	price = models.IntegerField()
	def __str__(self):
		return self.product.name
		#return '%s in stock, %s as the price' % (self.stock, self.price)

