import urllib2
import json

request_string = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?fq=data+science&facet_field=\
day_of_week&begin_date=20120101&end_date=20120101&api-key=99d7b651ac8108a2a9ed799af4b3b467:1:71594713'

file = urllib2.urlopen(request_string).read()

decoded = json.loads(file)
print decoded
