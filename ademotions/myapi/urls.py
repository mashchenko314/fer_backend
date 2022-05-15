from operator import methodcaller
from django.contrib import admin
from django.urls import path, include, re_path
from myapi.views import add_respondent
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import AdvertisementViewSet

router = DefaultRouter()
router.register(r'advertisements', AdvertisementViewSet, basename='advertisements')


urlpatterns = [
    path('respondent', add_respondent, name='respondent'),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    #path('auth/', include('djoser.urls.jwt')),
    #path('auth/', include('djoser.social.urls')),
]

urlpatterns += router.urls
