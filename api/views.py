from django.shortcuts import render, HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from main.models import Code, User
from .serializers import UserSer


@api_view(['GET'])
def post_click(request):
    user = get_user(request)
    user.clicks = user.clicks + 1;
    user.save()

    clicks = Code.objects.all().first()
    clicks.clicks = clicks.clicks + 1;
    clicks.save()

    name = request.GET.get('name')
    if name is not None and name != '/' and user.name != name:
        user.name = name
        user.save()

    response = HttpResponse(user.clicks)
    response.set_cookie('user_id', user.id)
    print(user.id)
    return response


@api_view(['GET'])
def get_code_data(request):
    clicks = Code.objects.all().first()
    return HttpResponse(clicks.clicks)

@api_view(['GET'])
def get_user_data(request):
    user = get_user(request)
    response = HttpResponse(user.clicks)
    response.set_cookie('user_id', user.id)
    return response

@api_view(['GET'])
def get_leaderboard(request):
    user = User.objects.all().order_by('-clicks')[:5]

    serializer = UserSer(user, many=True)
    return Response(serializer.data)
    return request.META['REMOTE_ADDR']



def get_user(request):
    pk = request.COOKIES.get('user_id')
    if (pk is None):
        user = User()
        user.save()
    else:
        try: 
            user = User.objects.get(id=pk)
        except: 
            user = User()
            user.save()
    return user