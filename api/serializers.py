from rest_framework import serializers
from main.models import Code, User


class UserSer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk',
                    'name',
                    'clicks',
                )


class CodeSer(serializers.ModelSerializer):
    class Meta:
        model = Code
        fields = ('clicks', 
                    'prize', 
                )