from videos.models import Video, Incident, Photo, AlarmLevel
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
    filter_horizontal = [ Incident.alarm_level ]
	
admin.site.register(Video,VideoAdmin)
admin.site.register(Incident,IncidentAdmin)
admin.site.register(Photo)
admin.site.register(AlarmLevel)
