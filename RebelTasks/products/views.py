from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from products.models import Country, Product, Company, CountryProducts
from products.serializers import ProductSerializer, CountrySerializer, CountriesWithProductsSerializer


# Create your views here.
def index(request):
	return HttpResponse("Hello, World. This is the Product Index")

def product_list(request):
	if request.method == 'GET':
		products = Product.objects.all()
		serializer = ProductSerializer(products, many=True)
		return JsonResponse(serializer.data, safe=False)

def product_details(request, pk):
	try:
		product = Product.objects.get(pk=pk)
	except product.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = ProductSerializer(product)
		return JsonResponse(serializer.data, safe=False)


def products_by_company(request, pk):
	try:
		products = Product.objects.filter(company=pk)
	except products.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = ProductSerializer(products, many=True)
		return JsonResponse(serializer.data, safe=False)


def product_countries(request, pk):
	try:
		countries = CountryProducts.objects.filter(product=pk)
	except countries.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = CountriesWithProductsSerializer(countries, many=True)
		return JsonResponse(serializer.data, safe=False)