# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import base64
import json

from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render

from kai.decorators import authentication

HTML = """
<div class="jumbotron text-center" style="background-color: gray">
<h1>My First Kakuaa Project</h1>
<p>Welcome to Kakuaa Community !! This is a test template. </p> 
<button type="button" class="btn btn-primary" id="btn1"> Click </button>
</div>
""".replace("""\n""","")

@require_http_methods(["GET","POST"])
@csrf_exempt
@authentication
def test(request):
        #if request.read():
        view = {
                "body": HTML
        }
        return HttpResponse(json.dumps(view), content_type="application/json")