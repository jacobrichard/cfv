from django.db import models
from django.contrib import admin
from stdimage import StdImageField
from django.core.exceptions import ValidationError
from django.contrib.localflavor.us.us_states import STATE_CHOICES

# Create your models here.
# NEED TO CHANGE ImageField to StdImageField (auto thumbnailing, naming, etc)

class Video(models.Model):
    title = models.CharField(max_length=200)
    length = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    release_date = models.DateField()
    item_number = models.CharField(max_length=10,unique=True)
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
    alarm_level = models.ManyToManyField('AlarmLevel',related_name='alarm_levels')
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

class MerchantInfo(models.Model):
    business = models.CharField(max_length=200)	# This is the email associated with checkout i.e. orders@chicagofirevideo.com
    merchant_id = models.CharField(max_length=20) # This is the merchant id for checkout i.e. ToCheckoutId in the hidden fields
    ship_cost_first_item = models.DecimalField(max_digits=6,decimal_places=2) # Cost to ship first item
    ship_cost_additional_item = models.DecimalField(max_digits=6,decimal_places=2) # Each Addt'l Item
    thank_you_page = models.CharField(max_length=200) # URL of page to return to after checkout

    def __unicode__(self):
        return "Merchant Info"

#	def save(self, *args, **kwargs):
#		if len(MerchantInfo.objects.all()) > 0:
#			raise ValidationError("Only one entry allowed for Merchant Info")
#		else:
#			super(MerchantInfo, self).save(*args, **kwargs)
