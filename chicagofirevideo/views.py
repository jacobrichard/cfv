from django.http import HttpResponse
from chicagofirevideo.models import Video, Incident
from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404

def video_detail(request, video_id):
    try:
        v = Video.objects.get(pk=video_id)
        i = Incident.objects.filter(video=video_id)
    except Video.DoesNotExist:
        raise Http404
    return render_to_response('chicagofirevideo/video_detail.html', {'video': v, 'incidents': i})

def incident_detail(request, incident_id):
	try:
		i = Incident.objects.get(pk=incident_id)
		v = i.video.all()
		p = i.photo_set.all()
		a = i.alarm_level.all()
	except Incident.DoesNotExist:
		raise Http404
	return render_to_response('chicagofirevideo/incident_detail.html',{'incident': i, 'videos': v, 'photos': p, 'alarm_levels': a})

def detail_by_item_number(request, item_number):
    try:
        v = Video.objects.get(item_number=item_number)
        i = Incident.objects.filter(video=v.id)
    except Video.DoesNotExist:
        raise Http404
    return render_to_response('chicagofirevideo/video_detail.html', {'video': v, 'incidents': i})
