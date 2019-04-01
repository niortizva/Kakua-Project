# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from kai.genKey import getKey

from django.contrib.auth.models import Group, User
from django.db import models
from django.contrib import admin
from django.utils.timezone import datetime

class Profile(models.Model):

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	key = models.CharField((u'User Key'), max_length=30, default=getKey)

	def __str__(self):
		return "{'User': %s, 'Key': %s }" %(self.user,self.key)

	class Meta:
		verbose_name = "User Profile"

class APIgroup(models.Model):
	name = models.CharField((u'API Group'),null=True,max_length=20)
	
	def __str__(self):
		return '%s' % self.name

	class Meta:
		verbose_name = "API Group"

class API(models.Model):
	name = models.CharField((u'API'),null=True,max_length=20)
	group = models.ForeignKey(APIgroup,on_delete=models.PROTECT)
	
	def __str__(self):
		return '%s' % self.name

	class Meta:
		verbose_name = "API"

class request(models.Model):
	user = models.ForeignKey(User, on_delete=models.PROTECT)
	userinfo = models.ForeignKey(Group, on_delete=models.PROTECT)
	api = models.ForeignKey(API, on_delete=models.PROTECT)
	date = models.DateField((u'Date'), null=True, default=datetime.now)
	time = models.TimeField((u"Time"), auto_now_add=True, null=True)
	success = models.BooleanField((u'Request State'), default=False)
	properties = models.CharField((u'Request Properties'), blank=True, max_length=500)


	def __str__(self):
		return "{'User': %s, 'Group': %s, 'API': %s, 'Date': %s, 'Time': %s, 'State': %s}" % (self.user, 
		self.userinfo, self.api, str(self.date), str(self.time), str(self.success))

	class Meta:
		verbose_name = "Request"
        
class adminAPIgroups(admin.ModelAdmin):
    list_display = ('name',)

class adminAPIs(admin.ModelAdmin):
    list_display = ('name','group')
    
class adminRequests(admin.ModelAdmin):
	list_display = ('user','userinfo','api','date','time','success','properties')

class adminProfile(admin.ModelAdmin):
	list_display = ('user','key')
admin.site.register
admin.site.register(APIgroup,adminAPIgroups)
admin.site.register(API,adminAPIs)
admin.site.register(request,adminRequests)
admin.site.register(Profile,adminProfile)