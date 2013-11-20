# -*- coding: latin1 -
from BeautifulSoup import BeautifulSoup
import requests

def doSearch(query, type,lang = "pt-BR", domain="com.br",num=30):
	url = "http://www.google."+domain+"/search"
	results = []	
	if type == 'music':
		parameters = {'q':"?intitle:index?%s %s last modified -html"%('.mp3',query.encode('utf8')),'hl':lang,'num':num}
		result1 = requests.get(url,params = parameters)		
		soup = BeautifulSoup(result1.content).findAll('h3',attrs = {'class':'r'})		
		print soup
		for url in soup:
			results.append(str(url.next['href'].encode('latin1')[7:].split('&')[0]).replace("%2520","%20"))	
		
		parameters = {'q':"?intitle:index?%s %s last modified -html"%('.wma',query.encode('utf8')),'hl':lang,'num':num}		
		result2 = requests.get(url,params = parameters)							
		soup = BeautifulSoup(result2.content).findAll('h3',attrs = {'class':'r'})		
		for url in soup:			
			results.append(str(url.next['href'].encode('latin1')[7:].split('&')[0]).replace("%2520","%20"))					
			print url
		#except Exception as e:
		#	print e		

		"""
		parameters = {'q':"?intitle:index?%s %s last modified -html"%('.ogg',query.encode('utf8')),'hl':lang,'num':num}
		result = requests.get(url,params = parameters)
		soup = BeautifulSoup(result.content).findAll('h3',attrs = {'class':'r'})		
		for url in soup:
			results.append(str(url.next['href'].encode('latin1')[7:].split('&')[0]).replace("%2520","%20"))	"""
	elif type == 'picture':
		parameters = {'q':"?intitle:index?%s %s last modified -html"%('.jpg',query.encode('utf8')),'hl':lang,'num':num}
		result = requests.get(url,params = parameters)
		soup = BeautifulSoup(result.content).findAll('h3',attrs = {'class':'r'})		
		for url in soup:
			results.append(str(url.next['href'].encode('latin1')[7:].split('&')[0]).replace("%2520","%20"))	
		parameters = {'q':"?intitle:index?%s %s last modified -html"%('.png',query.encode('utf8')),'hl':lang,'num':num}
		result = requests.get(url,params = parameters)
		soup = BeautifulSoup(result.content).findAll('h3',attrs = {'class':'r'})		
		for url in soup:
			results.append(str(url.next['href'].encode('latin1')[7:].split('&')[0]).replace("%2520","%20"))			
	elif type == 'file':
		parameters = {'q':"?intitle:index?%s %s last modified -html"%('.iso',query.encode('utf8')),'hl':lang,'num':num}
		result = requests.get(url,params = parameters)
		soup = BeautifulSoup(result.content).findAll('h3',attrs = {'class':'r'})		
		for url in soup:
			results.append(str(url.next['href'].encode('latin1')[7:].split('&')[0]).replace("%2520","%20"))	
		parameters = {'q':"?intitle:index?%s %s last modified -html"%('.rar',query.encode('utf8')),'hl':lang,'num':num}
		result = requests.get(url,params = parameters)
		soup = BeautifulSoup(result.content).findAll('h3',attrs = {'class':'r'})		
		for url in soup:
			results.append(str(url.next['href'].encode('latin1')[7:].split('&')[0]).replace("%2520","%20"))				
		parameters = {'q':"?intitle:index?%s %s last modified -html"%('.doc',query.encode('utf8')),'hl':lang,'num':num}
		result = requests.get(url,params = parameters)
		soup = BeautifulSoup(result.content).findAll('h3',attrs = {'class':'r'})		
		for url in soup:
			results.append(str(url.next['href'].encode('latin1')[7:].split('&')[0]).replace("%2520","%20"))	
		parameters = {'q':"?intitle:index?%s %s last modified -html"%('.pdf',query.encode('utf8')),'hl':lang,'num':num}
		result = requests.get(url,params = parameters)
		soup = BeautifulSoup(result.content).findAll('h3',attrs = {'class':'r'})		
		for url in soup:
			results.append(str(url.next['href'].encode('latin1')[7:].split('&')[0]).replace("%2520","%20"))	
		parameters = {'q':"?intitle:index?%s %s last modified -html"%('.apk',query.encode('utf8')),'hl':lang,'num':num}
		result = requests.get(url,params = parameters)
		soup = BeautifulSoup(result.content).findAll('h3',attrs = {'class':'r'})		
		for url in soup:
			results.append(str(url.next['href'].encode('latin1')[7:].split('&')[0]).replace("%2520","%20"))	
		parameters = {'q':"?intitle:index?%s %s last modified -html"%('.exe',query.encode('utf8')),'hl':lang,'num':num}
		result = requests.get(url,params = parameters)
		soup = BeautifulSoup(result.content).findAll('h3',attrs = {'class':'r'})		
		for url in soup:
			results.append(str(url.next['href'].encode('latin1')[7:].split('&')[0]).replace("%2520","%20"))
	elif type == 'video':		
		parameters = {'q':"?intitle:index?%s %s last modified -html"%('.avi',query.encode('utf8')),'hl':lang,'num':num}
		result = requests.get(url,params = parameters)
		soup = BeautifulSoup(result.content).findAll('h3',attrs = {'class':'r'})		
		for url in soup:
			results.append(str(url.next['href'].encode('latin1')[7:].split('&')[0]).replace("%2520","%20"))	
		parameters = {'q':"?intitle:index?%s %s last modified -html"%('.mp4',query.encode('utf8')),'hl':lang,'num':num}
		result = requests.get(url,params = parameters)
		soup = BeautifulSoup(result.content).findAll('h3',attrs = {'class':'r'})		
		for url in soup:
			results.append(str(url.next['href'].encode('latin1')[7:].split('&')[0]).replace("%2520","%20"))	
		parameters = {'q':"?intitle:index?%s %s last modified -html"%('.mkv',query.encode('utf8')),'hl':lang,'num':num}
		result = requests.get(url,params = parameters)
		soup = BeautifulSoup(result.content).findAll('h3',attrs = {'class':'r'})		
		for url in soup:
			results.append(str(url.next['href'].encode('latin1')[7:].split('&')[0]).replace("%2520","%20"))

		parameters = {'q':"?intitle:index?%s %s last modified -html"%('.mpeg',query.encode('utf8')),'hl':lang,'num':num}
		result = requests.get(url,params = parameters)
		soup = BeautifulSoup(result.content).findAll('h3',attrs = {'class':'r'})		
		for url in soup:
			results.append(str(url.next['href'].encode('latin1')[7:].split('&')[0]).replace("%2520","%20"))
	
	return results