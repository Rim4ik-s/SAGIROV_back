import json
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render

# Create your views here.
from .models import HeaderLink, AdvantageItem
from rest_framework import viewsets

from .serializer import HeaderLinkSerializer, AdvantageItemSerializer
from .models import HeaderLink, AdvantageItem

class HeaderLinkViewSet(viewsets.ModelViewSet):
    queryset = HeaderLink.objects.all()
    serializer_class = HeaderLinkSerializer

class AdvantageItemViewSet(viewsets.ModelViewSet):
    queryset = AdvantageItem.objects.all()
    serializer_class = AdvantageItemSerializer