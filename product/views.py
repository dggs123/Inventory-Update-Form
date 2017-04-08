from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Product
from .forms import ProductForm, UserForm

# Create your views here.
def index(request):
	p = Product.objects.all()
	if request.method == 'POST':
	# create a form instance and populate it with data from the request:
		if request.user.is_authenticated():
			form = ProductForm(request.POST, request.FILES)
			# print request.FILES['photo']
			if form.is_valid():
				new_game = form.save()
				messages.success(request, 'Game Added Sucessfully')
			else:
				print form.errors
				messages.error(request, 'Game Added Unsucessfully')
		else:
			user1 = UserForm(request.POST)
			user = authenticate(username = user1.data['username'], password = user1.data['password'] )
			if user is not None:
				login(request,user)
				messages.success(request, 'Login Sucessfully')
			else:
				messages.error(request, 'Login Unsucessfully')
		return HttpResponseRedirect('/')

	else:
		if request.user.is_authenticated():
			form = ProductForm()
		else:
			form = UserForm()

	return render(request, 'grid.html', {'form': form, "puzzles":p})

def play(request, id=None):
	puzzle = get_object_or_404(Product, id=id)
	return render(request, 'puzzle.html', {"puzzle":puzzle})


