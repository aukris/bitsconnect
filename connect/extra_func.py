from .models import Event,ProblemVote
import datetime
from django.utils import timezone

def get_weekly_calendar(week=0):
	today = datetime.date.today()
	monday = today - datetime.timedelta(days=today.weekday()) + datetime.timedelta(weeks=week)
	monday = datetime.datetime.combine(monday,datetime.datetime.min.time())
	monday = timezone.make_aware(monday, timezone.get_current_timezone())
	next_monday = monday+datetime.timedelta(weeks=1)
	query_set= Event.objects.filter(time__lte=next_monday, time__gt=monday).order_by('time')
	context={'mon':[],'tue':[],'wed':[],'thu':[],'fri':[],'sat':[],'sun':[],'first_day':monday, 
	'last_day':monday+datetime.timedelta(days=6), 'week':week}
	for event in query_set:
		if event.time.weekday() == 0:
			context['mon'].append(event)
		elif event.time.weekday() == 1:
			context['tue'].append(event)
		elif event.time.weekday() == 2:
			context['wed'].append(event)
		elif event.time.weekday() == 3:
			context['thu'].append(event)
		elif event.time.weekday() == 4:
			context['fri'].append(event)
		elif event.time.weekday() == 5:
			context['sat'].append(event)
		elif event.time.weekday() == 6:
			context['sun'].append(event)

	return context

def get_fav_status(problems,user):
	query_set = ProblemVote.objects.filter(user=user,problem__in=problems)
	status_dict={}
	for x in query_set:
		status_dict[x.problem.id]=True
	return status_dict
	

