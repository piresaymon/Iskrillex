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
from django.conf.urls.defaults import patterns, include, url
from core.views  import index,find,construction
from core.views  import construction
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.utils.functional import curry
from django.views.defaults import *

handler500 = curry(server_error, template_name='500.html')
#import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
#	(r'^',find),
	(r'^$',find),
	#(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
#	(r'^',index),
    # Examples:
    # url(r'^$', 'iskrillex.views.home', name='home'),
    # url(r'^iskrillex/', include('iskrillex.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
