from django.shortcuts import render
from django.http import JsonResponse


def Home(request):
    return JsonResponse('Hello world', safe=False)


def Room(request):
    return JsonResponse('Room', safe=False)
