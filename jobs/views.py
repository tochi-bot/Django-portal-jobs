from django.shortcuts import render
from django.http import HttpResponse

def my_jobs(request):
    return HttpResponse("Hello, jobs!")


