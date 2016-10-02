import os,csv
from django.conf import settings

def csvparse():
	files = []
	for filename in os.listdir(settings.BASE_DIR+'/static/datastash'):
		csvfile = open(settings.BASE_DIR+'/static/datastash/'+filename, 'rU')
		reader = csv.reader(csvfile)
		data = []
		for row in reader:
			data.append(row)
		files.append(data)
	return files
