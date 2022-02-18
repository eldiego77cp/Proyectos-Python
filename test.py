from turtle import Turtle, RawTurtle, TurtleScreenBase, TurtleScreen, TurtleGraphicsError

#n = int(input())
#list1 = []
#    
#for x in range(n):
#    list1.append(x)
#
#print(list1)
#        
#if n >= 1 and n <= 20:
#    for number in list1:
#        sqr = number ^ 2
#        print(sqr)

#n = int(input())
#string1 = ''
#if n >= 1 and n <= 150:
#    for x in range(1, n+1):
#        string1 += str(x)
#    print(string1)

#for i in range(1, int(input()) + 1): 
#    print(i, sep='', end='')

x = int(input())
y = int(input())
z = int(input())
n = int(input())
arrayItem = []
arrayList = []

for x1 in range(0, x+1):
    for y1 in range(0, y+1):
        for z1 in range(0, z+1):
            arrayItem.append([x1, y1, z1])
            if sum(arrayItem[0]) != n:
                arrayList.append([x1, y1, z1])
            arrayItem = []

print(arrayList)

