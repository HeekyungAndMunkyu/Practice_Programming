import urllib2

websiteOpen = urllib2.urlopen('http://www.comworld.co.kr/news/articleView.html?idxno=47908')

websiteContent = websiteOpen.read()

print websiteContent
