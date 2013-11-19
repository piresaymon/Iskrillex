from django.conf.urls.defaults import patterns, include, url
from core.views  import index,find,construction
from core.views  import construction
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
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
    # url(r'^$', 'iskrillexdj.views.home', name='home'),
    # url(r'^iskrillexdj/', include('iskrillexdj.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
