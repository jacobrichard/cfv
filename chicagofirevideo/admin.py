from chicagofirevideo.models import Video, Incident, Photo, AlarmLevel, MerchantInfo
from django.contrib import admin
from django.forms import ModelForm

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
    filter_horizontal = [
        'video','alarm_level' 
    ]

class MerchantInfoAdmin(admin.ModelAdmin):
	form = 'MerchantAdminForm'
	
class MerchantAdminForm(ModelForm):
	class Meta:
		model = MerchantInfo
	def validate_singleton(self):
		if len(MerchantInfo.objects.all()) > 0:
			"Only one item allowed for Merchant Info"
		else:
			return self
	
admin.site.register(Video,VideoAdmin)
admin.site.register(Incident,IncidentAdmin)
admin.site.register(Photo)
admin.site.register(AlarmLevel)
admin.site.register(MerchantInfo)
