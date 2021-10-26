"""
from django.http import HttpResponse


def home(request):
	return HttpResponse('<h1>Hello Acme</h1>')

"""
from django.shortcuts import render

def home(request):
	return render(request, 'home.html')


def about(request):
	return render(request, 'pages/about.html')


def contact(request):
	return render(request, 'pages/contact.html')


def handler404(request):
	return render(request, 'errors/404.html', {}, status=404 )