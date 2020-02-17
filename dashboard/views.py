from django.shortcuts import render

# Create your views here.
def Dashboard(request):
	return render(request, 'dashboard.html', {})

def Login(request):
	return render(request, 'login.html', {})

def Register(request):
	return render(request, 'register.html', {})