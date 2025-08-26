import json
import random
import string
import os
from django.core import serializers
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST, require_GET
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponseNotFound, HttpResponse
from rest_framework.response import Response
from .models import Advertisement, Respondent, Result
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from .serializers import AdvertisementSerializer, RespondentSerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes, action
from django.db.models import Count
from django.core.files import File
from pathlib import Path
from .fer import emotion_recognition, top, shade



class AdvertisementViewSet(viewsets.ModelViewSet):
    
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(user=self.request.user).order_by('upload_date')
        query_set = query_set.annotate(total_respondents=Count('respondent'))
        return query_set

    def perform_create(self, serializer):
        print(serializer)
        letters_and_digits = string.ascii_letters + string.digits
        rand_string =''.join(random.sample(letters_and_digits, 10))
        serializer.save(user=self.request.user, url=rand_string)


class RespondentViewSet(viewsets.ModelViewSet):
    
    queryset = Respondent.objects.all()
    serializer_class = RespondentSerializer
    
    
@permission_classes([IsAuthenticated])
@require_GET
def analyze(request, ad_id):
    respondents_queryset = Respondent.objects.all().filter(advertisement=ad_id)
    print(respondents_queryset)
    for respondent in respondents_queryset:
        print(respondent.record.url)
        result = emotion_recognition(respondent.record.url)
        print(result)
        path = Path('../ademotions/data.csv')
        f = open(path, mode='rb')
        csvfile = File(f, name=path.name)
        new_result = Result.objects.create(
               top_emotion=result['Преобладающая эмоция'],
               shade=result['Эмоциональный оттенок'],
               engagement=result['Вовлеченность'],
               respondent=respondent,
               angry=result['Злость'],
               disgust=result['Отвращение'],
               fear=result['Страх'],
               happy=result['Счастье'],
               sad=result['Грусть'],
               surprise=result['Удивление'],
               neutral=result['Нейтральность'],
               csv=csvfile
        )
        new_result.save()
        os.remove('../ademotions/data.csv')
    Advertisement.objects.filter(pk=ad_id).update(is_analyzed=True)
    return JsonResponse({'message': 'ok'})


@permission_classes([IsAuthenticated])
@require_GET
def result(request, ad_id):
    data = {
        'respondents':[],
        'emotions': []
    }
    engagement = 0
    angry = 0
    disgust = 0
    fear = 0
    happy = 0
    sad = 0
    surprise = 0
    neutral = 0
    respondents_queryset = Respondent.objects.all().filter(advertisement=ad_id)
    print(respondents_queryset)
    for respondent in respondents_queryset:
        result = get_object_or_404(Result, respondent=respondent.id)
        angry += result.angry
        disgust += result.disgust
        fear += result.fear
        happy += result.happy
        sad += result.sad
        surprise += result.surprise
        neutral += result.neutral
        engagement += result.engagement
        data['respondents'].append({'file': result.csv.url, 'name': respondent.name, 'top_emotion': result.top_emotion})
    data['top_emotion'] = top(angry, disgust, fear, happy, sad, surprise, neutral)  
    data['shade'] = shade(angry, disgust, fear, happy, sad, surprise, neutral)
    data['engagement'] = round(engagement/len(data['respondents']))
    emotions = [angry, disgust, fear, happy, sad, surprise, neutral]
    data['emotions'] = emotions
    ad = get_object_or_404(Advertisement, pk=ad_id)
    data['title'] = ad.title
    data['brand'] = ad.brand
    data['description'] = ad.description
    return JsonResponse(data)


@require_GET
def watch(request, ad_url):
    print(ad_url)
    advertisement = get_object_or_404(Advertisement, url=ad_url)
    if (advertisement.is_available):
        return JsonResponse({'video': advertisement.video.url, 'screensaver': advertisement.screensaver.url, 'id': advertisement.id})
    return HttpResponseNotFound()
