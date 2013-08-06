from django.conf.urls import patterns, include, url
from mathclass import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fizzbuzz.views.home', name='home'),
    # url(r'^fizzbuzz/', include('fizzbuzz.foo.urls')),
	url(r'^$', 'mathclass.views.index_view', name='home'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
