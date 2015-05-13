# -*- encoding: utf-8 -*-

from pattern.web import URL, download, Node, DOM, Element

url = URL('http://klue.kr/lecture.php?no=29086')
url.username = u'yhk00323'
url.password = u'qufskfk3'
html = url.download(unicode  = True)
#node = Node(html, type = NODE)
dom = DOM(html)
print dom.children

for i in dom:
	print i
