data=list(open('in.txt','r').read().split('\n'))
depth=horiz=aim=0
for i in range(len(data)):
    direction,num=data[i].split(' ')
    num=int(num)
    if direction=="forward":
        horiz+=num
        depth+=aim*num
    elif direction=="down": aim+=num
    else: aim-=num
print(depth*horiz)

