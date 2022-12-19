import os
import sys

with open(os.path.join(sys.path[0], "input.txt"), 'r') as file:
    caloriessum = 0
    calorieslist = []
    for line in file:
        if len(line.strip())>0:
            caloriessum = caloriessum + int(line.strip())
        else:
            calorieslist.append(caloriessum)
            caloriessum = 0
    calorieslist.sort(reverse=True)
    print("The most calories an elf is carrying: " + str(calorieslist[0]))
    caloriessumtopthree = sum(calorieslist[0:3])
    print("The total calories carried by the top 3 elves: " + str(caloriessumtopthree))