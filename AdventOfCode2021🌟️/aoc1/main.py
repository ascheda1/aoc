data = list(map(int, open('in.txt', 'r').read().split('\n')))
last = 0
counter = 0;
for i in range(len(data)-2):
    sum = 0
    for j in range(i, i+3):
        sum+=data[j]
    if i != 0 and sum - last > 0:
        counter+=1
    last = sum
        

print(counter)

