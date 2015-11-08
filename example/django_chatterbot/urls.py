from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers

from django_chatterbot.api import ChatterBotView


router = routers.DefaultRouter()

urlpatterns = [
    url(
        r'^$',
        ChatterBotView.as_view(),
        name="chatterbot",
    ),
]
