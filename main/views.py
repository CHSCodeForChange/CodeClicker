from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Code


# Sending user object to the form, to verify which fields to display/remove (depending on group)
def click(request):
    code = Code.objects.first()
    code.clicks = code.clicks + 1
    code.save()
    print(code.clicks)
    return redirect('/')


def userView(request):
    code = Code.objects.first()
    return render(request, 'userView.html', {'code':code})

def displayView(request):
    code = Code.objects.all().first()
    return render(request, 'displayView.html', {'code':code})
