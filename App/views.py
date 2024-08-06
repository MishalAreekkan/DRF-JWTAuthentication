from django.shortcuts import render
from . serializers import PersonSerializer
from . models import Person
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class PersonData(viewsets.ViewSet):
    queryset = Person.objects.all()
    serializer_class  = PersonSerializer()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    