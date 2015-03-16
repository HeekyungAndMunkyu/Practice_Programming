import urllib2
import json


request_string = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?q=new+york+times&page=2&sort=oldest&api-key=####'


response = urllib2.urlopen(request_string)
#content = response.read()

#decoded = json.loads(content)
#date_of_first_article = decoded['results'][0]['date']

#print date_of_first_article


