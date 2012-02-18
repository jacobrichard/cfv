from django.db import models
from django.contrib import admin

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=200)
    length = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    release_date = models.DateField()
    item_number = models.CharField(max_length=10)
    product_photo = models.ImageField(upload_to='product_photos')
    detail_photo_1 = models.ImageField(upload_to='detail_photos')
    detail_photo_2 = models.ImageField(upload_to='detail_photos')
	
    def __unicode__(self):
	    return self.title
	
class Incident(models.Model):
	video = models.ManyToManyField(Video,related_name='incidents')
	date = models.DateField()
	address = models.CharField(max_length=200)
	alarm_level = models.CharField(max_length=2)
	department = models.CharField(max_length=200)
	keywords = models.CharField(max_length=200)
	
	def __unicode__(self):
		return ' - '.join([str(self.date),self.address])

class Photo(models.Model):
	incident = models.ForeignKey(Incident)
	photo = models.ImageField(upload_to='incident_photos')
	
	def __unicode__(self):
		return ' - '.join([str(self.id),unicode(self.incident)])
