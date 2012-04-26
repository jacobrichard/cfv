from django.db import models
from django.contrib import admin
from stdimage import StdImageField
from django.core.exceptions import ValidationError
from django.contrib.localflavor.us.us_states import STATE_CHOICES
from south.modelsinspector import add_introspection_rules

class Video(models.Model):
    title = models.CharField(max_length=200)    # Video Title
    length = models.CharField(max_length=200)   # Total Running Time
    price = models.DecimalField(max_digits=6,decimal_places=2)  # Price
    release_date = models.DateField()   # Release Date
    item_number = models.CharField(max_length=10,unique=True)   # Item Number
    narrative = models.TextField()  # Narrative of the video contents
    product_photo = StdImageField(upload_to='product_photos', blank=True, size=(640, 480), thumbnail_size=(150, 150))   # Product Photo
    detail_photo_1 = StdImageField(upload_to='detail_photos', blank=True, size=(640, 480), thumbnail_size=(150, 150))   # Photo 1 of incident
    detail_photo_2 = StdImageField(upload_to='detail_photos', blank=True, size=(640, 480), thumbnail_size=(150, 150))   # Photo 2 of incident
    video_clip = models.TextField(max_length=200, blank=True)

    def __unicode__(self):
        return self.title

	def __str__(self):
		return self.title

    def get_absolute_url(self):
        return '/video/%i' % self.id

    def get_item_url(self):
        return '/item/%s' % self.item_number

class Incident(models.Model):
    video = models.ManyToManyField(Video,related_name='incidents',blank=True,null=True)  # Videos it appears on
    date = models.DateField()   # Date of occurence
    address = models.CharField(max_length=200)  # Address of occurence
    city = models.CharField(max_length=200) # City of occurence
    state = models.CharField(max_length=2,choices=STATE_CHOICES)    # State of occurence
    alarm_level = models.ManyToManyField('AlarmLevel',related_name='alarm_levels',blank=True,null=True)  # Alarm Level
    department = models.CharField(max_length=200)   # Department(s)
    description = models.TextField()    # Description of incident
    keywords = models.ManyToManyField('Keyword',related_name='keywords',blank=True,null=True) # Relevant Keywords

    def __unicode__(self):
        return ' - '.join([str(self.date),self.address])

	def __str__(self):
		return ' - '.join([str(self.date),self.address])

    def get_absolute_url(self):
        return '/incident/%i' % self.id

class Photo(models.Model):
    incident = models.ForeignKey(Incident)  # Incident the photo appears in
    photo = StdImageField(upload_to='incident_photos', blank=True, size=(640, 480), thumbnail_size=(150, 150))  # Path to the photo

    def __unicode__(self):
        return ' - '.join([str(self.id),unicode(self.incident)])

	def __str__(self):
		return ' - '.join([str(self.id),unicode(self.incident)])

class AlarmLevel(models.Model):
    level_description = models.CharField(max_length=50) # Alarm Level Name 
    response_detail = models.TextField(blank=True)  # Alarm Response Detail

    def __unicode__(self):
        return self.level_description

	def __str__(self):
		return self.level_description

class MerchantInfo(models.Model):
    business = models.CharField(max_length=200)	# This is the email associated with checkout i.e. orders@chicagofirevideo.com
    merchant_id = models.CharField(max_length=20) # This is the merchant id for checkout i.e. ToCheckoutId in the hidden fields
    ship_cost_first_item = models.DecimalField(max_digits=6,decimal_places=2) # Cost to ship first item
    ship_cost_additional_item = models.DecimalField(max_digits=6,decimal_places=2) # Each Addt'l Item
    thank_you_page = models.CharField(max_length=200) # URL of page to return to after checkout

    def __unicode__(self):
        return "Merchant Info"
	
	def __str__(self):
		return "Merchant Info"

class Keyword(models.Model):
    keyword = models.CharField(max_length=50)

    def __unicode__(self):
        return self.keyword
	
	def __str__(self):
		return self.keyword
		
## South Introspection Rules for StdImageField
rules = [
    (
        (StdImageField,),
        [],
        {
            "size": ["size", {"default": None}],
            "thumbnail_size": ["thumbnail_size", {"default": None}],
            "upload_to": ["upload_to", {"default": None}],
        },
    )
]
add_introspection_rules(rules, ["^stdimage\.fields"])
