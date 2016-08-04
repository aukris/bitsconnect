from django.contrib import admin
from .models import *
from django.forms import ValidationError

class BookOrderAdmin(admin.ModelAdmin):
	list_display = ['book','nos','is_approved','is_delivered','approved_by']
	readonly_fields = ['approved_by','book','nos','address','phone', 'user']

	def save_model(self, request, obj, form, change):
		if not obj.is_approved and obj.is_delivered:
	 		 raise ValidationError('You cannot mark this order as delivered without approving it first')
	 	if obj.is_approved and not obj.approved_by:
	 		obj.approved_by = request.user
	 	obj.save()

admin.site.register(Service)
admin.site.register(Classified)
admin.site.register(Event)
admin.site.register(Bhavan)
admin.site.register(Problem)
admin.site.register(ProblemSolved)
admin.site.register(ProblemVote)
admin.site.register(Place)
admin.site.register(Travel)
admin.site.register(GlobalEvent)
admin.site.register(MissedCall)
admin.site.register(Book)
admin.site.register(BookOrder, BookOrderAdmin)
admin.site.register(PhoneNumberDB)
admin.site.register(BookRequest)
admin.site.register(UserFacebookData)