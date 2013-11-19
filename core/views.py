#!/usr/bin/env python
# coding: utf-8
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.http import HttpResponse
from forms import SearchForm
from google import search
from util import doSearch
from urllib import unquote

#def  index(request):
#print "inicio"
#s = search(query="?intitle: index of?mkv game of thrones",tld="com.br",lang="pt-BR",stop=10)
#print "fim"
#r = ""
#for url in s:
#	print url
#	r = r + "<a hrfe="+url+">"+url+"<a><br>"
#a = {"a":1,"b":2}	
#context = RequestContext(request)
#return render_to_response("core/result.html",locals(),context)
#return HttpResponse(r)
#if request.method == 'GET':
#form = SearchForm(request.GET)
#else:
#	form = SearchForm()		
#context = RequestContext(request)
#return render_to_response("core/index.html",context)
from django.conf import settings
from django.utils import encoding
@csrf_exempt
def index(request):
	return render_to_response("core/construction.html")

@csrf_exempt
def find(request):	
	if request.method == 'POST':
		form = SearchForm(request.POST,auto_id=False)
		if form.is_valid():
			q = encoding.smart_str(request.POST['q'], encoding='ascii', errors='ignore')			
			if(request.POST['typeGroup']):
				type = request.POST['typeGroup']
				print("Q: %s , type: %s",q,request.POST['typeGroup'])
			else:
				type = ''
			
			results = doSearch(query=q,type=type)						
			#results = [1,2,3,4,5,6,7,8,9]
		return render_to_response("core/index.html",locals(),context_instance=RequestContext(request))
	elif request.method == 'GET':
		form = SearchForm(auto_id=False)
		context = RequestContext(request, {'form': form,'STATIC_URL' :settings.STATIC_URL})		
		return render_to_response("core/index.html",context)

def construction(request):
	return render_to_response("core/construction.html")		

