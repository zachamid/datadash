from django.http import HttpResponse
from django.template import loader

import csvparse

# Create your views here.
def index(request):
	files =csvparse.csvparse()
	template = loader.get_template('csvparse/index.html')
	return HttpResponse(template.render({'files': files}, request))