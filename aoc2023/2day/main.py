import sys

file = sys.argv[1]

f = open(file, "r")
#only 12 red cubes, 13 green cubes, and 14 blue cubes
red_def = 12
green_def = 13
blue_def = 14
sum = 0
for line in f:
    arr = line.split(":")
    game_number = int(arr[0].split(" ")[1])
    games = arr[1].split(";")
    rgb = [0,0,0]
    for game in games:
        colors = game.split(",")
        for color in colors:
            if "red" in color:
                if int(color.split(" ")[1]) > rgb[0]:
                    rgb[0] = int(color.split(" ")[1])
            if "green" in color:
                if int(color.split(" ")[1]) > rgb[1]:
                    rgb[1] = int(color.split(" ")[1])
            if "blue" in color:
                if int(color.split(" ")[1]) > rgb[2]:
                    rgb[2] = int(color.split(" ")[1])
    sum+=rgb[0] * rgb[1] * rgb[2]
print(sum)