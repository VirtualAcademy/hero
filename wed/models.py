from django.db import models
from django.utils.encoding import smart_unicode
#from tinymce.models import HTMLField

# Create your models here.
class Hero(models.Model):
	groom_nick=models.CharField(max_length=10,blank=False)
	bride_nick=models.CharField(max_length=10,blank=False)
	slogan=models.CharField(max_length=100,blank=False)
	wedin_date=models.DateField()
	email=models.EmailField(default='odieleowedding@gmail.com')
	phone=models.CharField(max_length=15,default='00237677757776')
	
	class Meta:
		verbose_name_plural = "Heroes"
		
	def __unicode__(self):
		return smart_unicode(u'%s & %s' % (self.bride_nick, self.groom_nick))

	
class Event(models.Model):
	subtitle=models.CharField(max_length=20,blank=False)
	intro=models.TextField(blank=False)
	startime=models.DateTimeField()
	endtime=models.DateTimeField()
	venue=models.CharField(max_length=200,blank=False)	
	pix=models.ImageField(upload_to='pix/',null=True,blank=True)
	
	def __unicode__(self):
		return smart_unicode(u'%s' % (self.subtitle))
		
class Direction(models.Model):
	event=models.ForeignKey(Event)
	means=models.CharField(max_length=200,blank=False)
	direction=models.TextField(blank=False)
	
	def __unicode__(self):
		return smart_unicode(u'%s' % (self.means))

class Facility(models.Model):
	#title=models.CharField(max_length=200,blank=False)
	event=models.ForeignKey(Event)
	item=models.CharField(max_length=200,blank=False)
	description=models.TextField(blank=True)
	
	class Meta:
		verbose_name_plural = "Facilities"
		
	def __unicode__(self):
		return smart_unicode(u'%s' % (self.item))
	
class Story(models.Model):
	title=models.CharField(max_length=200,blank=False)
	content=models.TextField(blank=False)#HTMLField()
	created=models.DateTimeField(auto_now_add=True,auto_now=False)
	updated=models.DateTimeField(auto_now_add=False,auto_now=True)
	
	class Meta:
		verbose_name_plural = "Stories"
		
	def __unicode__(self):
		return smart_unicode(u'%s' % (self.title))
	
class Giftregistry(models.Model):
	note=models.TextField()
	signature=models.CharField(max_length=200,blank=False)
	
	class Meta:
		verbose_name_plural = "Gift Registries"
		
	def __unicode__(self):
		return smart_unicode(u'Gift Registry')
	

class Gallery(models.Model):
	photo = models.ImageField(upload_to='gallery/', max_length=100)
	alt_text = models.CharField(max_length=200,default='pic')
	
	class Meta:
		verbose_name_plural = "Galleries"
		
	def __unicode__(self):
		return smart_unicode(u'%s' % (self.alt_text))
		
class Rsvp(models.Model):
	"""RSVP information"""
	
	full_name = models.CharField(max_length=50)
	email = models.EmailField(blank=True)
	guests = models.PositiveSmallIntegerField()
	attending = models.BooleanField()
	events= models.CharField(max_length=200)
	guestinfo= models.TextField()
	message= models.TextField()
	
	def __unicode__(self):
		return smart_unicode(u'%s' % (self.full_name))