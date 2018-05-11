from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
	num =  random.randint(0,100000,)
	var = 'this is simples string'
	return render(request, 'base.html', {'html_var':var,'num':num})