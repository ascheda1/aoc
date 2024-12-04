import numpy as np

data=list(open('in.txt','r').read().split('\n'))
arr=[]
arr=[1 for i in range(len(data))]

for i in range(len(data[0])):
	counter_alive = 0	
	number_of_ones = 0
	
	for j in range(len(data)):
		if arr[j] == 0:
			continue
		counter_alive+=1
		if data[j][i] == '1':
			number_of_ones+=1
	
	remove_item = 1
	if number_of_ones < counter_alive/2:
		remove_item = 0

	countertostop = 0
	index = 0
	for j in range(len(data)):
		if arr[j] != 0 and int(data[j][i]) == remove_item:
			arr[j] = 0
			continue
		if arr[j] == 1:
			countertostop+=1
			index = j

	if countertostop == 1:
		print(data[index])
		print(int(data[index], 2))
		break

