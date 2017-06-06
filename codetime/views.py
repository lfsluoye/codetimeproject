from django.shortcuts import render
from django.http import HttpResponse

from . import models
# Create your views here.
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