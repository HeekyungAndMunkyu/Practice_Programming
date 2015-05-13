import urllib2, base64

username = 'yhk00323'
password = 'qufskfk3'
auth_encoded = base64.encodestring('%s:%s' % (username, password))[:-1]

req = urllib2.Request('http://klue.kr/lecture.php?no=29086')
req.add_header('Authorization', 'Basic %s' % auth_encoded)
try:
    response = urllib2.urlopen(req)
except urllib2.HTTPError, http_e:
    pass

print response.read()
