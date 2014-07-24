"""Copyright (C) <2014>  <Saymon Pires da Silva>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA"""
# -*- coding: latin1 -
from BeautifulSoup import BeautifulSoup
import requests
#import urllib

#def unquote(value):
#    return unquote(value)
#make the search
def doSearch(query, type,lang = "pt-BR", domain="com",num=30):
	url = "http://www.google."+domain+"/search"
	#url = "http://www.google."+domain+
	#-inurl:htm -inurl:html intitle:"index of" "Last modified" mp3 
	#"?intitle:index?%s %s last modified -html -wallywashis"
	parameters = {'q':"%s -inurl:htm -inurl:html intitle:index  %s -wallywashis"%(type,query.encode('utf8')),'hl':lang,'num':num}
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
			.replace("%42","@")
			.replace("%20"," ")
			.replace("%255B","[")
			.replace("%255D","]")
			.replace("%5B","[")
			.replace("%5D","]")
			.replace("%257B","{")
			.replace("%257D","}")
			.replace("%7B","{")
			.replace("%7D","}")
			.replace("%252F","/")
			.replace("%f3","�")
			.replace("%2F","/"))
		#results.append(url.next['href'].encode('latin1')[7:].split('&')[0])
		#print url.next['href'].encode('latin1')[7:].split('&')[0].replace("%2520","%20")
		#print url.next['href'].encode('latin1')[7:]
		#This replace made change of 1º term for 2º term (1º"%3f", 2º "?"), used on redirection links 
	return results
		
#def unescape_this(url):
#    return url.replace(r"\\/", "/")