from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^chicagofirevideo/', include('chicagofirevideo.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
     (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^admin/', include(admin.site.urls)),

     (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),

     (r'^$', 'chicagofirevideo.views.index'),
     (r'^index/$', 'chicagofirevideo.views.index'),
     (r'^videos/(?P<video_id>\d+)/$', 'chicagofirevideo.views.video_detail'),
     (r'^incident/(?P<incident_id>\d+)/$', 'chicagofirevideo.views.incident_detail'),
     (r'^item/(?P<item_number>.+)/$', 'chicagofirevideo.views.detail_by_item_number'),

     (r'^util/memcached/$', 'chicagofirevideo.views.memcached_stats')
)
