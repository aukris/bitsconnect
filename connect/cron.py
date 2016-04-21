import datetime
from .models import *
from django.utils import timezone

def delete_old_travel():
    Travel.objects.filter(date__lt=timezone.now()).delete()

def delete_old_events():
	today = datetime.date.today()
	monday = today - datetime.timedelta(days=today.weekday())
	monday = datetime.datetime.combine(monday,datetime.datetime.min.time()) - datetime.timedelta(weeks=-1)
	monday = timezone.make_aware(monday, timezone.get_current_timezone())
	Event.objects.filter(time__lt=monday).delete()

def delete_old_problem():
	obj = ProblemSolved.objects.all()
	if obj.count() > 30:
		obj.filter(solved_on__lt=timezone.make_aware(datetime.datetime.now()-datetime.timedelta(weeks=2), timezone.get_current_timezone() ) ).delete()

def delete_old_ads():
	obj = Classified.objects.all()
	if obj.count() > 30:
		obj.filter(created__lt=timezone.make_aware(datetime.datetime.now()-datetime.timedelta(weeks=2),timezone.get_current_timezone() ) ).delete()

def delete_old_service():
	obj = Service.objects.all()
	if obj.count() > 30:
		obj.filter(created__lt=timezone.make_aware(datetime.datetime.now()-datetime.timedelta(weeks=2), timezone.get_current_timezone() ) ).delete()


def run():
    delete_old_travel()
    delete_old_events()
    delete_old_problem()
    delete_old_ads()
    delete_old_service()