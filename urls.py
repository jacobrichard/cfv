from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     (r'^admin_tools/', include('admin_tools.urls')),
     (r'^admin/doc/', include('django.contrib.admindocs.urls')),
     (r'^admin/', include(admin.site.urls)),

     (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),

     (r'^$', 'chicagofirevideo.views.index'),
     (r'^index/$', 'chicagofirevideo.views.index'),
     (r'^videos/(?P<video_id>\d+)/$', 'chicagofirevideo.views.video_detail'),
     (r'^incident/(?P<incident_id>\d+)/$', 'chicagofirevideo.views.incident_gallery'),
     (r'^gallery/(?P<incident_id>\d+)/$', 'chicagofirevideo.views.incident_gallery'),
     (r'^item/(?P<item_number>.+)/$', 'chicagofirevideo.views.detail_by_item_number'),

     (r'^util/memcached/$', 'chicagofirevideo.views.memcached_stats'),
     (r'^util/nginx/$', 'chicagofirevideo.views.nginx_stats'),
)
