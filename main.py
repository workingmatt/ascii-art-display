import time,math
import csv

width,height = 170,63
inText = " ".join('The Geekery' for x in range(15))
output = []
bold,unbold = "\033[1m\033[33m","\033[0m\033[34m"
datasheet = []
frameoffset = 0

with open('data.csv','r') as data_file:
	data_reader = csv.reader(data_file)
	for row in data_reader: datasheet.append(row)
	ds_width,ds_height = len(datasheet[0]),len(datasheet)

while True:
	output = []
	for offset in range(height):
		output.append(list((''.join(list("".join(" " for a in range((offset + frameoffset) % 12)) + inText)[12:width]))))

	for rowi,row in enumerate(output):
		for vali,val in enumerate(row):
			if datasheet[math.floor(rowi/len(output)*ds_height)][math.floor(vali/len(row)*ds_width)] == '1':
	                	output[rowi][vali] = f"{bold}{output[rowi][vali]}{unbold}"
		print(''.join(row))

	frameoffset += 3
	frameoffset %= 12

	time.sleep(1)

