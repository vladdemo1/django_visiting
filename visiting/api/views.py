""" This module contains main views for this app """

from django.shortcuts import render
from django.http import JsonResponse


def api_overview(request):
    return JsonResponse("API BASE POINT", safe=False)
