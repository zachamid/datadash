import os,csv,sys
from django.conf import settings
from django import template

class CSVFile:

	def __init__(self, file_name, data, header=False):
		self.filename = file_name
		self.data = data
		self.valid = [0]*len(data[0])
		self.type = [0]*len(data[0])
		self.validation_check()

	def validation_check(self):
		for i in range(len(self.data)):
			for j in range(len(self.data[i])):
				if is_number(self.data[i][j]):
					self.valid[j] += 1
				else:
					self.valid[j] -= 1
#				self.valid[j] /= len(self.data[])

def csvparse():
	files = []
	for filename in os.listdir(settings.BASE_DIR+'/static/datastash'):
		csvfile = open(settings.BASE_DIR+'/static/datastash/'+filename, 'rU')
		reader = csv.reader(csvfile)
		data = []
		for row in reader:
			data.append(row)
		file_obj = CSVFile(filename, data)
		files.append(file_obj)
	return files

register = template.Library()

def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		return False

@register.filter
def get_type(value):
    return type(value)
