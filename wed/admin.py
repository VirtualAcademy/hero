from django.contrib import admin

# Register your models here.
from .models import Hero, Event, Direction, Facility, Story, Giftregistry, Gallery, Gift, Giver

class HeroAdmin(admin.ModelAdmin):
	list_display=['__unicode__','email','phone']
	class Meta:
		model=Hero

class EventAdmin(admin.ModelAdmin):
	list_display=['__unicode__','venue','startime','endtime']
	class Meta:
		model=Event
		
class DirectionAdmin(admin.ModelAdmin):
	list_display=['__unicode__','means','direction','event']
	class Meta:
		model=Direction
		
class FacilityAdmin(admin.ModelAdmin):
	list_display=['__unicode__','description','event']
	class Meta:
		model=Facility
		
class StoryAdmin(admin.ModelAdmin):
	list_display=['__unicode__','title', 'content','created','updated']
	class Meta:
		model=Story
		
class GiftregistryAdmin(admin.ModelAdmin):
	plural = 'Giftregistries'
	list_display=['__unicode__','note']
	class Meta:
		model=Giftregistry
		plural = 'Giftregistries'
		
class GalleryAdmin(admin.ModelAdmin):
	list_display=['__unicode__','photo']
	search_fields = ('photo',)
	class Meta:
		model=Gallery	
		
class GiftAdmin(admin.ModelAdmin):
	class Meta:
		model=Gift

class GiverAdmin(admin.ModelAdmin):
	class Meta:
		model=Giver

				
admin.site.register(Hero,HeroAdmin)
admin.site.register(Event,EventAdmin)
admin.site.register(Direction,DirectionAdmin)
admin.site.register(Facility,FacilityAdmin)
admin.site.register(Story,StoryAdmin)
admin.site.register(Giftregistry,GiftregistryAdmin)
admin.site.register(Gallery,GalleryAdmin)
admin.site.register(Gift,GiftAdmin)
admin.site.register(Giver,GiverAdmin)


