import os,csv
from django.conf import settings

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
				types[j] = type(field[j])
			for j in range(len(field)):
				if types[j] == 'str':
					self.valid[j]+=1
				else:
					self.valid[j]-=1
			if self.valid[j] < 0:
				self.type[j] = 'Numeric'
			else:
				self.type[j] = 'Alpha'
		for i in range(len(self.data[0])):
			self.valid[i] = abs(self.valid[i])/len(self.data[0])

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
