from django.http import HttpResponse
from chicagofirevideo.models import Video, Incident
from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import login_required
import memcache

@cache_page(60 * 15)
def video_detail(request, video_id):
    try:
        video = Video.objects.get(pk=video_id)
        incidents = Incident.objects.filter(video=video_id)
    except Video.DoesNotExist:
        raise Http404
    return render_to_response('chicagofirevideo/video_detail.html', {'video': video, 'incidents': incidents})

@cache_page(60 * 15)
def incident_detail(request, incident_id):
    try:
        incident = Incident.objects.get(pk=incident_id)
        videos = incident.video.all()
        photos = incident.photo_set.all()
        alarm_levels = incident.alarm_level.all()
    except Incident.DoesNotExist:
        raise Http404
    return render_to_response('chicagofirevideo/incident_detail.html',{'incident': incident, 'videos': videos, 'photos': photos, 'alarm_levels': alarm_levels})

@cache_page(60 * 15)
def incident_gallery(request, incident_id):
    try:
        incident = Incident.objects.get(pk=incident_id)
        videos = incident.video.all()
        photos = incident.photo_set.all()
        alarm_levels = incident.alarm_level.all()
    except Incident.DoesNotExist:
        raise Http404
    return render_to_response('chicagofirevideo/incident_gallery.html',{'incident': incident, 'videos': videos, 'photos': photos, 'alarm_levels': alarm_levels})

@cache_page(60 * 15)
def detail_by_item_number(request, item_number):
    try:
        video = Video.objects.get(item_number=item_number)
        incidents = Incident.objects.filter(video=video.id)
    except Video.DoesNotExist:
        raise Http404
    return render_to_response('chicagofirevideo/video_detail.html', {'video': video, 'incidents': incidents})

def index(request):
    return render_to_response('chicagofirevideo/index.html')

def memcached_stats (request):
    try:
        mc = memcache.Client(['127.0.0.1:11211'], debug=0)
    	response = mc.get_stats()[0][1]
    except:
        raise Http404
    return render_to_response('tools/memcached.html', {'stats': response})

def nginx_stats (request):
    return render_to_response('tools/nginx.html')
