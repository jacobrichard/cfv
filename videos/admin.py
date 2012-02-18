from videos.models import Video
from videos.models import Incident
from videos.models import Photo
from django.contrib import admin

class AppearanceInline(admin.TabularInline):
	model = Incident.video.through

class IncidentInline(admin.TabularInline):
	model = Incident

class PhotoInline(admin.TabularInline):
	model = Photo	
	
class VideoAdmin(admin.ModelAdmin):
    inlines = [
        AppearanceInline
	]
	
class IncidentAdmin(admin.ModelAdmin):
    inlines = [
        PhotoInline,
	]
	
admin.site.register(Video,VideoAdmin)
admin.site.register(Incident,IncidentAdmin)
admin.site.register(Photo)
admin.site.register(AlarmLevel)
