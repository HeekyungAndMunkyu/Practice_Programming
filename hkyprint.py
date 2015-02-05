# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

file = open(u'C:/Users/윤희경/Documents/Practice_Python/heekyungyoon.txt', 'r')

#print u'\n'.join(file.readlines())
print u' '.join(file.readlines())
