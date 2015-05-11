# -*- coding: utf-8 -*-

i = 0
numbers = []

while i < 6:
    print "At peak, i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Now, the number is ", numbers
    print "At the bottom, i is %d" % i


print "Numbers: "

for num in numbers:
    print num

# Use Function
def appendNum(num, step):
    '''
    num: int >= 1
    step: int

    returns: list = [0, 1, 2, ..., num - 1, num]
    '''
    i = 0
    numbers = []

    while i < num:
        print "At peak, i is %d" % i
        numbers.append(i)

        i = i + step
        print "Now, the number is ", numbers
        print "At the bottom, i is %d" % i

    return numbers

print ""
print "Use Function"
print ""
num = int(raw_input('num: '))
step = int(raw_input('step: '))
numbers = appendNum(num, step)

print "Numbers: "

for num in numbers:
    print num


# Use For & Range
print ""
print "Use For & Range"
print ""


num = int(raw_input('num: '))

numbers = []

for i in range(num):
    print "At peak, i is %d" % i
    numbers.append(i)
    i = i + 1
    print "Now, the number is ", numbers
    print "At the bottom, i is %d" % i



print "Numbers: "

for num in numbers:
    print num
