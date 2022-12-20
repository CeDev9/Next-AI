from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['POST'])
def getFactor(request):
    urlfile = request.data['urlfile']
    list_result = {
        "vocal":{ "positive":0.01,"negative":0.01,"positive":0.01,"positive":0.01 },
        "verbal":{ "positive":0.01,"negative":0.01,"warmth":0.01,"ability":0.01 },
        "Factor":0.01,
        "UrlFile":urlfile
    }
    return Response(list_result)
