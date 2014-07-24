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

