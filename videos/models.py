from django.db import models
from django.contrib import admin
from stdimage import StdImageField
from django.contrib.localflavor.us.us_states import STATE_CHOICES

# Create your models here.
# NEED TO CHANGE ImageField to StdImageField (auto thumbnailing, naming, etc)

class Video(models.Model):
    title = models.CharField(max_length=200)
    length = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    release_date = models.DateField()
    item_number = models.CharField(max_length=10)
    narrative = models.TextField()
    product_photo = StdImageField(upload_to='product_photos', blank=True, size=(640, 480), thumbnail_size=(150, 150))
    detail_photo_1 = StdImageField(upload_to='detail_photos', blank=True, size=(640, 480), thumbnail_size=(150, 150))
    detail_photo_2 = StdImageField(upload_to='detail_photos', blank=True, size=(640, 480), thumbnail_size=(150, 150))
	
    def __unicode__(self):
	    return self.title
	
class Incident(models.Model):
	video = models.ManyToManyField(Video,related_name='incidents')
	date = models.DateField()
	address = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	state = models.CharField(max_length=2,choices=STATE_CHOICES)
	alarm_level = models.ManyToManyField('AlarmLevel',related_name='alarm_levels',filter_horizontal=True)
	department = models.CharField(max_length=200)
	description = models.TextField()
	keywords = models.CharField(max_length=200)
	
	
	def __unicode__(self):
		return ' - '.join([str(self.date),self.address])

class Photo(models.Model):
	incident = models.ForeignKey(Incident)
	photo = StdImageField(upload_to='incident_photos', blank=True, size=(640, 480), thumbnail_size=(150, 150))
	
	def __unicode__(self):
		return ' - '.join([str(self.id),unicode(self.incident)])
		
class AlarmLevel(models.Model):
	level_description = models.CharField(max_length=50)
	response_detail = models.TextField(blank=True)
   
	def __unicode__(self):
   		return self.level_description
