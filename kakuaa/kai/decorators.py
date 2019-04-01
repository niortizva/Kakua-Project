from __future__ import unicode_literals
import base64

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render

"""
Don't forget to add Key authentication for each user
"""

def authentication(func):
    def wrap(request, *args, **kwargs):
        if request.method == "POST" and "HTTP_AUTHORIZATION" in request.META:
            auth = request.META['HTTP_AUTHORIZATION'].split()
            if len(auth) == 2 and auth[0].lower() == "basic":
                username, password = base64.b64decode(auth[1]).split(':')
                user = authenticate(request,username=username, password=password)
                if user is not None and user.is_active:
                    return func(request, *args, **kwargs)
                else:
                    return HttpResponse("[ERROR] User Authentication Failed")
            else:
                return HttpResponse("[ERROR] Invalid Request Header")
        else:
            return HttpResponse("[ERROR] Invalid Request Method or Missing HTTP authorization header")

    return wrap