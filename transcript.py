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
'''
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

'''
major = []
for line in original_transcript_list:
	if '전공' in line and '지도'not in line and '교양'not in line and 'HO' not in line and '외국'not in line:
		major.append(line)
total = 0.0
count = 0.0
for line in major:
	if 'A+' in line:
		total += 4.5
		count += 1.0
	elif 'A' in line:
		total += 4.0
		count += 1.0
	elif 'B+' in line:
		total += 3.5
		count += 1.0
	elif 'B' in line:
		total += 3.0
		count += 1.0
	else:
		print line
average = total/count
print '%d / %d = %3d' % (total, count, total/count)	
for line in major:
	print line
