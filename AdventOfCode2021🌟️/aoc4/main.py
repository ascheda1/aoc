import numpy as np
import os

def print_arr(arr):
	for i in arr:
		for j in i:
			arr=[]
			for k in j:
				arr.append(k)
			print(arr)

def win(arr, x, y):
	iswin = 1
	for i in range(5):
		if arr[x][i] == False:
			iswin = 0
			break

	if iswin == 1:
		return iswin

	iswin = 2
	for i in range(5):
		if arr[i][y] == False:
			iswin = 0
			break

	return iswin

def sumwin(arr, bool):
	sum = 0
	for i in range(5):
		for j in range(5):
			if bool[i][j] ==False:
				sum+=int(arr[i][j])
	return sum

data=list(open('in.txt','r').read().split('\n'))

drawn_n = data[0].split(',')

players=[]
used=[]

for i in range(2,len(data), 6):
	player=[]
	use=[]
	for j in range(5):
		player.append(data[i+j].split())
		use.append([False, False, False, False, False])
	players.append(player)
	used.append(use)

winning = 0
won=[]
index = -1
won=[False for i in range(len(players))]
for number in drawn_n:
	for i in range(len(players)):
		if won[i]:
			continue
		for x in range(len(players[i])):
			for y in range(len(players[i][x])):
				if players[i][x][y] == number:
					used[i][x][y] = True
					val = win(used[i], x, y)
					if val > 0:
						winning+=1
						won[i] = True
						if index != -1:
							print(int(number) * sumwin(players[index],used[index]))
							os.abort()
						#print(int(number) * sumwin(players[i],used[i]))
						#os.abort()
					if winning == len(players) - 1:
						for d in range(len(won)):
							if not won[d]:
								index = d
								break
