from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm
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
			login_form.save()
			return HttpResponse("登录成功")
		else:
			print(login_form.errors.as_json())
			return render(request, 'codetime/login.html')
	return render(request, 'codetime/login.html')		

def login(request):
	return render(request, 'codetime/login.html')

def login_action(request):
	name = request.POST.get('name', 'NAME')
	password = request.POST.get('password', 'PASSWORD')

	person = models.Person.objects.get(pk=1)
	if name == person.name and password == person.password:
		return render(request, 'codetime/product.html')
	return render(request, 'codetime/login.html')
def postProduct(request):
	kehu = request.POST.get('kehu', 'KEHU')
	

def product(request):
	return render(request, 'codetime/product.html')
	