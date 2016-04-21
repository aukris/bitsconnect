from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.simple_tag
def navactive(request, urls):
    if request.path in ( reverse(url) for url in urls.split() ):
        return "active"
    return ""

@register.inclusion_tag('connect/fav.html', takes_context=True)
def fav_status(context, problem_id):
	return {'fav': context['status_dict'].get(problem_id,False), 'id':problem_id}