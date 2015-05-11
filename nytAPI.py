import urllib2
import json

request_string = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?q=Seoul&fq=news_desk:("Travel")&facet_field=\
source&begin_date=20140301&end_date=20150317&api-key=99d7b651ac8108a2a9ed799af4b3b467:1:71594713'

file = urllib2.urlopen(request_string).read()

decoded = json.loads(file)

for i in range(len(decoded['response']['docs'])):
	print
	print decoded['response']['docs'][i]['abstract']

for i in range(len(decoded['response']['facets']['source']['terms'])):
	print
	print decoded['response']['facets']['source']['terms'][i]['count'], '  ',  decoded['response']['facets']['source']['terms'][i]['term']
