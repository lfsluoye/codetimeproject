from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm, ProductForm
from . import models
# Create your views here.
# def get_name(request):
# 	if request.method == 'POST':
# 		form = LoginForm(request.POST)
# 		if form.is_valid():
# 			return HttpResponse(content='1',mimetype='text/html',status=200,content_type='text/plain')
# 	else:
# 		form = LoginForm()
# 	return render(request, 'codetime/login.html',{'form': form})
def loginForm(request):
	if request.method == 'POST':
		login_form = LoginForm(request.POST)
		if login_form.is_valid():
			name = request.POST.get('name', 'NAME')
			password = request.POST.get('password', 'PASSWORD')

			person = models.Person.objects.get(pk=1)
			if name == person.name and password == person.password:
				return render(request, 'codetime/product.html')
			return render(request, 'codetime/login.html')
		else:
			print(login_form.errors.as_json())
			return render(request, 'codetime/login.html', {"person": login_form.cleaned_data})
	return render(request, 'codetime/login.html')		
def productForm(request):
	if request.method == 'POST':
		product_form = ProductForm(request.POST)
		if product_form.is_valid():
			product_form.save()
			return render(request, 'codetime/product.html')
		else:
			print(product_form.errors.as_json())
			return render(request, 'codetime/product.html', {"product": product_form.cleaned_data})
	return render(request, 'codetime/product.html')
def login(request):
	return render(request, 'codetime/login.html')

def login_action(request):
	name = request.POST.get('name', 'NAME')
	password = request.POST.get('password', 'PASSWORD')

	person = models.Person.objects.get(pk=1)
	if name == person.name and password == person.password:
		return render(request, 'codetime/product.html')
	return render(request, 'codetime/login.html')

def product(request):
	return render(request, 'codetime/product.html')
	