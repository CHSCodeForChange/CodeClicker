from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Code


# Sending user object to the form, to verify which fields to display/remove (depending on group)
# def click(request):
#     if Code.objects.count() == 0:
#         code = Code.objects.create()
#         # You can do something here as this should be the first person
#     else:
#         code = Code.objects.first()
#     code.clicks = code.clicks + 1
#     code.save()

#     if (code.prize != 0 and code.clicks % code.prize == 0):
#         return prize(request)
#     return redirect('/')


def userView(request):
    if Code.objects.count() == 0:
        code = Code.objects.create()
        # You can do something here as this should be the first person
    else:
        code = Code.objects.first()
    return render(request, 'userView.html', {'code':code})

def displayView(request):
    if Code.objects.count() == 0:
        code = Code.objects.create()
        # You can do something here as this should be the first person
    else:
        code = Code.objects.first()
    return render(request, 'displayView.html', {'code':code})

def prize (request):
    code = Code.objects.first()
    return render(request, 'prize.html', {'code':code})
