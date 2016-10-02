from django.shortcuts import render
from django.http import HttpResponse

import csvparse

# Create your views here.
def index(request):
	files =csvparse.csvparse()
	return HttpResponse(files)