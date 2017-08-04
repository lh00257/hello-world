# -*- coding: utf-8 -*-
#VIEWS TELL DJANGO WHAT TO DISPLAY TO THE USER. WE USE URLconf TO SAY WHERE ON A WEBSITE TO DISPLAY IT.

from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse # Imports HttpResponse so we can return a response object to the user

def index(request):
    return HttpResponse("Hello, world!")  #Hardcode our text to the response object
