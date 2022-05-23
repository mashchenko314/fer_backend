from email.policy import default
from myapi.models import Advertisement, Respondent
from django.contrib.auth.models import User
from rest_framework import serializers
import datetime
import os


class AdvertisementSerializer(serializers.ModelSerializer):
    total_respondents = serializers.IntegerField(read_only=True, default=0)

    class Meta:
        model = Advertisement
        fields = ['id', 'title', 'brand',  'description', 'url', 'upload_date',  'is_available', 'is_analyzed', 'video', 'screensaver', 'total_respondents',]


class RespondentSerializer(serializers.ModelSerializer):
    advertisement = serializers.PrimaryKeyRelatedField(read_only=False, queryset=Advertisement.objects.all())

    class Meta:
        model = Respondent
        fields = ['id', 'name', 'view_date', 'record',  'advertisement']
