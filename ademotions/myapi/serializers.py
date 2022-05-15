from myapi.models import Advertisement
from django.contrib.auth.models import User
from rest_framework import serializers
import datetime
import os


class AdvertisementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advertisement
        fields = ['id', 'title', 'brand',  'description', 'url', 'upload_date',  'is_available', 'video', 'screensaver',]
   
