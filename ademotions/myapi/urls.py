from operator import methodcaller
from django.contrib import admin
from django.urls import path, include, re_path
from myapi.views import analyze, watch, result
from rest_framework.routers import DefaultRouter

from .views import AdvertisementViewSet, RespondentViewSet

router = DefaultRouter()
router.register(r'advertisements', AdvertisementViewSet, basename='advertisements')
router.register(r'respondents', RespondentViewSet, basename='respondents')

urlpatterns = [
    path('watch/<str:ad_url>', watch, name='watch'),
    path('analyze/<int:ad_id>', analyze, name='analyze'),
    path('result/<int:ad_id>', result, name='result'),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    #path('auth/', include('djoser.urls.jwt')),
    #path('auth/', include('djoser.social.urls')),
]

urlpatterns += router.urls
