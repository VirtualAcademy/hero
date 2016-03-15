from django.contrib import admin

# Register your models here.
from .models import Hero, Event, Direction, Facility, Story, Giftregistry, Gallery

class HeroAdmin(admin.ModelAdmin):
	class Meta:
		model=Hero

class EventAdmin(admin.ModelAdmin):
	class Meta:
		model=Event
		
class DirectionAdmin(admin.ModelAdmin):
	class Meta:
		model=Direction
		
class FacilityAdmin(admin.ModelAdmin):
	class Meta:
		model=Facility
		
class StoryAdmin(admin.ModelAdmin):
	class Meta:
		model=Story
		
class GiftregistryAdmin(admin.ModelAdmin):
	plural = 'Giftregistries'
	class Meta:
		model=Giftregistry
		plural = 'Giftregistries'
		
class GalleryAdmin(admin.ModelAdmin):
	class Meta:
		model=Gallery
				
admin.site.register(Hero,HeroAdmin)
admin.site.register(Event,EventAdmin)
admin.site.register(Direction,DirectionAdmin)
admin.site.register(Facility,FacilityAdmin)
admin.site.register(Story,StoryAdmin)
admin.site.register(Giftregistry,GiftregistryAdmin)
admin.site.register(Gallery,GalleryAdmin)

