from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

from .models import Code


# Sending user object to the form, to verify which fields to display/remove (depending on group)
def click(request):
	if Code.objects.count() == 0:
		code = Code.objects.create()
		# You can do something here as this should be the first person
	else:
		code = Code.objects.first()
	code.clicks = code.clicks + 1
	code.save()
	print(code.clicks)
	# return redirect('/')


def userView(request):
	if Code.objects.count() == 0:
		code = Code.objects.create()
		# You can do something here as this should be the first person
	else:
		code = Code.objects.first()
	return render(request, 'userView.html', {'code': code})


def displayView(request):
  if Code.objects.count() == 0:
		code = Code.objects.create()
		# You can do something here as this should be the first person
	else:
		code = Code.objects.first()

	return render(request, 'displayView.html', {'code': code})
