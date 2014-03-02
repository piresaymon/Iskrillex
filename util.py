# -*- coding: latin1 -
from BeautifulSoup import BeautifulSoup
import requests
#import urllib

#def unquote(value):
#    return unquote(value)
#make the search
def doSearch(query, type,lang = "pt-BR", domain="com.br",num=30):
	url = "http://www.google."+domain+"/search"
	#url = "http://www.google."+domain+
	parameters = {'q':"?intitle:index?%s %s last modified -html"%(type,query.encode('utf8')),'hl':lang,'num':num}
	#parameters = {'q':query,'hl':lang}
	print parameters["q"]
	result = requests.get(url,params = parameters)
	soup = BeautifulSoup(result.content).findAll('h3',attrs = {'class':'r'})
	results = []
	for url in soup:
		results.append(str(url.next['href'].encode('latin1')[7:].split('&')[0])
			.replace("%2520","%20")
			.replace("%3F","?")
			.replace("%24","$")
			.replace("%26","&")
			.replace("%2B","+")
			.replace("%2c",",")
			.replace("%3A",":")
			.replace("%3B",";")
			.replace("%3D","=")
			.replace("%42","@"))
		#results.append(url.next['href'].encode('latin1')[7:].split('&')[0])
		#print url.next['href'].encode('latin1')[7:].split('&')[0].replace("%2520","%20")
		#print url.next['href'].encode('latin1')[7:]
	return results

#def unescape_this(url):
#    return url.replace(r"\\/", "/")