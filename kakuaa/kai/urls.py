from django.conf.urls import url
from kai.views import test

urlpatterns = [
    url(r'test/$', test, name="test"),   
]
