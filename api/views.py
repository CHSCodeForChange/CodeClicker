from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from main.models import Code, User
from .serializers import CodeSer, UserSer


@api_view(['GET'])
def post_click(request):
    name = request.GET.get('name')
    ip = get_client_ip(request)

    user = User.objects.filter(ip=ip).first()
    clicks = Code.objects.all().first()

    user.clicks = user.clicks + 1;
    user.save()

    clicks.clicks = clicks.clicks + 1;
    clicks.save()

    if name is not None and name != '/' and user.name != name:
        user.name = name
        user.save()

    return Response()


@api_view(['GET'])
def get_code_data(request):
    clicks = Code.objects.all().first()
    serializer = CodeSer(clicks)
    return Response(serializer.data, template_name="api.html")

@api_view(['GET'])
def get_user_data(request):
    ip = get_client_ip(request)
    user = User.objects.filter(ip=ip).first()
    
    if user is None:
        user = User(ip=ip)
        user.save()

    serializer = UserSer(user)
    return Response(serializer.data)

@api_view(['GET'])
def get_leaderboard(request):
    user = User.objects.all().order_by('-clicks')[:5]

    serializer = UserSer(user, many=True)
    return Response(serializer.data)

def get_client_ip(request):
    return request.META['HTTP_X_FORWARDED_FOR']  



