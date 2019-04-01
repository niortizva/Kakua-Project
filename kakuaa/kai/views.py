# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import base64

from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render

from kai.decorators import authentication

HTML = """
<div class="jumbotron text-center">
<h1>My First Kakuaa Project</h1>
<p>Welcome to Kakuaa Community !! This is a test template. </p> 
<button type="button" class="btn btn-primary" id="btn1"> Click </button>
</div>
""".replace("""\n""","")

@csrf_exempt
@authentication
def test(request):
    if request.method == "POST" or request.method == "GET":
        return HttpResponse(str(HTML))
