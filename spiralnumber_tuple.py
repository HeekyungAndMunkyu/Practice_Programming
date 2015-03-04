num = 0
numDict = {}

def tupGenRowFixed(rowPosition, colPosition):
    global num
    global numDict


    for i in range(0, colPosition+1):
        print num
        numDict[(rowPosition, i)] = num
        num += 1


rowListFixed = range(0, 3)
colListMoving = range(0, 3)


tupGenRowFixed(3, 3)

print numDict
print len(numDict)
