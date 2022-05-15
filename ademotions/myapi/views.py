import json
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST, require_GET
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponseNotFound, HttpResponse
from rest_framework.response import Response
from .models import Advertisement, Respondent
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import AdvertisementSerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.db.models import Count



class AdvertisementViewSet(viewsets.ModelViewSet):
    
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(user=self.request.user)
        query_set = queryset.annotate(Count('respondent'))
        return query_set

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        

@require_POST
def add_respondent(request):
    try:
        advertisement = Advertisement.objects.get(id=int(request.POST['advertisement_id']))
        new_respondent = Respondent.objects.create(
               name=request.POST['name'],
               record=request.POST['record'],
               advertisement=advertisement,
               )
        new_respondent.save()
    except KeyError:
        return JsonResponse({'message': 'Required parameter not entered.'})
    else:
        return JsonResponse({'message': 'New respondent successfully added.'})