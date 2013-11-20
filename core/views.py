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
		return render_to_response("core/index.html",locals(),context_instance=RequestContext(request))
	elif request.method == 'GET':
		form = SearchForm(auto_id=False)
		context = RequestContext(request, {'form': form,'STATIC_URL' :settings.STATIC_URL})		
		return render_to_response("core/index.html",context)

def construction(request):
	return render_to_response("core/construction.html")		

