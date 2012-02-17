from django.http import HttpResponse
from videos.models import Video, Incident
from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404

def video_detail(request, video_id):
    try:
        v = Video.objects.get(pk=video_id)
        i = Incident.objects.filter(video=video_id)
    except Video.DoesNotExist:
        raise Http404
    return render_to_response('videos/video_detail.html', {'video': v, 'incidents': i})

def incident_detail(request, incident_id):
	try:
		i = Incident.objects.get(pk=incident_id)
		v = i.video.all()
	except Incident.DoesNotExist:
		raise Http404
	return render_to_response('videos/incident_detail.html',{'incident': i, 'videos': v})
