from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def rootindex(request):
    return HttpResponse("server activated successfully")
