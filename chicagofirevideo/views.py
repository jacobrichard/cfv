from django.http import HttpResponse
from chicagofirevideo.models import Video, Incident
from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404

def video_detail(request, video_id):
    try:
        video = Video.objects.get(pk=video_id)
        incidents = Incident.objects.filter(video=video_id)
    except Video.DoesNotExist:
        raise Http404
    return render_to_response('chicagofirevideo/video_detail.html', {'video': video, 'incidents': incidents})

def incident_detail(request, incident_id):
    try:
        incident = Incident.objects.get(pk=incident_id)
        videos = i.video.all()
        photos = i.photo_set.all()
        alarm_levels = i.alarm_level.all()
    except Incident.DoesNotExist:
        raise Http404
    return render_to_response('chicagofirevideo/incident_detail.html',{'incident': incident, 'videos': videos, 'photos': photos, 'alarm_levels': alarm_levels})

def detail_by_item_number(request, item_number):
    try:
        video = Video.objects.get(item_number=item_number)
        incidents = Incident.objects.filter(video=v.id)
    except Video.DoesNotExist:
        raise Http404
    return render_to_response('chicagofirevideo/video_detail.html', {'video': video, 'incidents': incidents})
