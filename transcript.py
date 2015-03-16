# -*- coding: utf-8 -*-
#import pandas as pd

original_transcript = file('transcript.txt','r')  # file

original_transcript_list = original_transcript.readlines() # list

aplus = []
a = []
bplus = []
b = []
other = []

for line in original_transcript_list:
	if 'A+' in line:
		aplus.append(line)
	elif 'A' in line:
		a.append(line)
	elif 'B+' in line:
		bplus.append(line)
	elif 'B' in line:
		b.append(line)
	else:
		other.append(line)	
print 'A+'
print
for record in aplus:
	print record
	print

print 'A'
print
for record in a:
	print record
	print 

 
