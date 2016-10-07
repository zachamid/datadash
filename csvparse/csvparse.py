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
		for i in range(len(self.data[0])):
			field = self.data[:][i]
			types = [0]*len(field)

			for j in range(len(field)):
				print >>sys.stderr,type(field[j])
				if type(field[j]) is str:
					self.valid[i]+=1
				else:
					self.valid[i]-=1

				self.data[i][j] = str(self.data[i][j]) + '(' + str(type(self.data[i][j])) + ')'

			if self.valid[i] > 0:
				self.type[i] = 'Numeric'
			else:
				self.type[i] = 'Alpha'

		for i in range(len(self.data[0])):
			self.valid[i] = self.valid[i]/len(self.data[0])

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

@register.filter
def get_type(value):
    return type(value)
