from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib import messages

from .models import Product
from .forms import ProductForm

# Create your views here.
def index(req):
	if settings.DEBUG:
		template = 'product.html'
	else:
		template = 'product.html'

	products = Product.objects.all()

	resp = render(req, template,{"products":products})

	return resp

def addproduct(request):
	if request.method == 'POST':
	# create a form instance and populate it with data from the request:
		form = ProductForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			new_article = form.save()
			messages.success(request, 'Product Added Sucessfully.')
		else:
			messages.error(request, 'Product Added Unsucessfully')
		return HttpResponseRedirect('/addproduct')

	else:
		form = ProductForm()

	return render(request, 'form.html', {'form': form})

