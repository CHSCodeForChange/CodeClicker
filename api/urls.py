from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^click/', views.post_click),
    url(r'^click_data/', views.get_code_data),
    url(r'^user_data/', views.get_user_data),
    url(r'^leaderboard/', views.get_leaderboard),
]
