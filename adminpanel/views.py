import json
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import HeaderLink, AdvantageItem


def getHeaderLinks(request):
    header_links = HeaderLink.objects.all()[:6]
    header_links = [{"text": q.text, "endpoint": q.endpoint} for q in header_links]
    return HttpResponse(json.dumps(header_links), content_type="application/json")

def getAdvantages(request):
    advantages = AdvantageItem.objects.all()[:4]
    advantages= [{
        "first_text": q.first_text,
        "main_text": q.main_text,
        "second_text": q.second_text,
        "position": q.position
    } for q in advantages]

    return HttpResponse(json.dumps(advantages), content_type="application/json")