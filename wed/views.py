from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Hero, Event, Direction, Facility, Story, Giftregistry, Gallery, Rsvp

# Create your views here.
def	home(request):
	if request.method == 'POST':
		name=request.POST.get('name')
		message=request.POST.get('message')
		email=request.POST.get('email')
		guest=request.POST.get('guess')
		guest_info=request.POST.get('guestinfo')
		event=request.POST.get('event')
		csrf_token=request.POST.get('csrfmiddlewaretoken')
		# n=Rsvp(full_name = name,
		# 	email = email,
		# 	guests = guest,
		# 	attending = True,
		# 	events= event,
		# 	guestinfo= guestinfo,
		# 	message= message)
		# n.save()
		return HttpResponse("Well Received, Thank You.")
	else:
		events=Event.objects.all()
		directions=Direction.objects.all()
		facilities=Facility.objects.order_by('event')
		stories=Story.objects.all()
		registry=Giftregistry.objects.all()
		gallery=Gallery.objects.all().order_by('photo')
		for info in Hero.objects.all():
			context = {'bride':info.bride_nick,
					'groom':info.groom_nick,
					'wed_date':info.wedin_date,
					'email':info.email,
					'phonenumber':info.phone,
					'events':events,
					'directions':directions,
					'facilities':facilities,
					'stories':stories,
					'registry':registry,
					'gallery':gallery}
		return render(request,'index.html',context)