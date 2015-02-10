from django.shortcuts import render
from django.http import HttpResponse

from rango.models import Category

def index(request):

	category_list = Category.objects.order_by('-likes')[:5]
	context_dict = {'categories': category_list}
	# context_dict = {'boldmessage': 'I am bold font from the context'}
	return render(request, 'rango/index.html', context_dict)
	# return HttpResponse("Rango says: Hello world! <br/> <a href='/rango/about'>About</a>")


def about(request):
	context_dict = {'desc': 'This is the about page in bold from the context'}
	return render(request, 'rango/about.html', context_dict)
	# return HttpResponse("Rango says here is the about page <br/> <a href='/rango/'>Index</a>")