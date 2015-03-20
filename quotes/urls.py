from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'quotes.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^quotes/admin/', include(admin.site.urls)),
	url(r'^quotes/', include('briggs.urls', namespace='briggs')),
)
