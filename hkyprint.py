# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

file = open(u'C:/Users/윤희경/Documents/Practice_Python/heekyungyoon.txt', 'r')
fileList = file.readlines()
#print u'\n'.join(fileList)

#print '\n'.join(fileList).encode('utf-8').decode('utf-8')

listA = ['a', 'b', 'c']
print '\n'.join(listA)

listH = ['윤', '희', '경']
print u'\n'.join(listH)
