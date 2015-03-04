# -*- coding: utf-8 -*-

def cheese_and_crackers(cheese_count, boxs_of_crackers):
	print "There are %d slices of cheese." % cheese_count
	print "There are %d boxes of crakcers." % boxs_of_crackers
	print "Enough to throw a party!"
	print "Brinkg a blanket with you. \n"


print "You can give numbers dirctly to the function."
cheese_and_crackers(20, 30)


print "Or you can use variables of a script."
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "You can even calculate numbers inside brackets."
cheese_and_crackers(10 + 20, 5 + 6)


print "Variables and numbers can be calculated together."
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

