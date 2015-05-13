import urllib2

#theurl = 'http://klue.kr/lecture.php?no=29086'
#username = 'yhk00323'
#password = 'qufskfk3'
# a great password

#different website
#theurl = 'https://mail.naver.com/?n=1430102483400&v=f'
#username = 'yhk00323'
#password = 'Rnadmfgidgo'
# a great password

#booking.com
#theurl = 'https://secure.booking.com/reviewtimeline.ko.html?sid=0b0b95ba488e027cbdd2fa91c8d4dd5b;dcid=2;'
#username = 'yhk00323@naver.com'
#password = 'qufskfk3'


#facebook
#theurl = 'https://www.facebook.com/heekyung.yoon.7'
#username = 'yhk00323@hanmail.net'
#password = 'qufskfk3'


#twitter
theurl = 'https://twitter.com/following'
username = 'yhk00323@naver.com'
password = 'qufskfk3'


passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
# this creates a password manager
passman.add_password(None, theurl, username, password)
# because we have put None at the start it will always
# use this username/password combination for  urls
# for which `theurl` is a super-url

authhandler = urllib2.HTTPBasicAuthHandler(passman)
# create the AuthHandler

opener = urllib2.build_opener(authhandler)

urllib2.install_opener(opener)
# All calls to urllib2.urlopen will now use our handler
# Make sure not to include the protocol in with the URL, or
# HTTPPasswordMgrWithDefaultRealm will be very confused.
# You must (of course) use it when fetching the page though.

pagehandle = urllib2.urlopen(theurl)
# authentication is now handled automatically for us

print pagehandle.read()
