from django.shortcuts import HttpResponse


def index(request):
    """Index for the polls application"""
    return HttpResponse("Hello, world. You're in at the polls index.")
