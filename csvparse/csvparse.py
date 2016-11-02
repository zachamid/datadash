import os,csv,sys, operator
from django.conf import settings
from django import template

class CSVFile:

	def __init__(self, file_name, data, header=False):
		self.filename = file_name
		self.data = data
		self.type = [[0]*3]*len(data[0])
		self.validation_check()

	def validation_check(self):
		for j in range(len(self.data[0])):
			column = self.data[:][j]
			for i in range(len(column)):
				data_type = classify(column[i])
				self.type[j][data_type] += 1


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

def classify(s):
	try:
		int(s)
		return 0
	except:
		try:
			float(s)
			return 1
		except:
			return 2

@register.filter
def get_type(value):
    return type(value)
