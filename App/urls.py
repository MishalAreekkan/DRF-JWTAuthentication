from django.urls import path,include
from . views import PersonData
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView,
    TokenVerifyView
)

route = DefaultRouter()
route.register(r'person',PersonData,basename='person')
urlpatterns = [
    path('',include(route.urls)),
    path('gettoken/',TokenObtainPairView.as_view(),name='gettoken'),
    path(' /',TokenRefreshView.as_view(),name='tokenrefresh'),
    path('tokenverify',TokenVerifyView.as_view(),name='tokenverify')
]
