from chicagofirevideo.models import Video, Incident, Photo, AlarmLevel, MerchantInfo
from django.contrib import admin
from django import forms

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

class MerchantInfoAdminForm(forms.ModelForm):
    class Meta:
        model = MerchantInfo
    def clean(self):
        if len(MerchantInfo.objects.all()) > 0:
            raise forms.ValidationError("Only one entry is allowed for Merchant Info, please modify or delete the existing entry!")
        else:
            return self.cleaned_data

class MerchantInfoAdmin(admin.ModelAdmin):
    form = MerchantInfoAdminForm

	
admin.site.register(Video,VideoAdmin)
admin.site.register(Incident,IncidentAdmin)
admin.site.register(Photo)
admin.site.register(AlarmLevel)
admin.site.register(MerchantInfo,MerchantInfoAdmin)
