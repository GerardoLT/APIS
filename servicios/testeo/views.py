from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from logica import test
# Create your views here.
def index(request):
    return JsonResponse(
        {
            "test":"1",
            "angulo":"2",
            "adas":"3",
            "asd":test.f()
        }
    )
