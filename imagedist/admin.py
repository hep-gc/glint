'''
Created on May 15, 2014

@author: rd
'''
from django.contrib import admin
from imagedist.models import site,credential,image,user

class user_admin(admin.ModelAdmin):
    list_display = ('username','tenant','token','lastlogin')
    list_filter = ['username','tenant','token','lastlogin']
    
class site_admin(admin.ModelAdmin):
    list_display = ('name','url','authport','version','type')
    list_filter = ['name','url','authport','version','type']

class credential_admin(admin.ModelAdmin):
    list_display = ('user','site','un','pw','tenant')
    list_filter = ['user','site','un','pw','tenant']

class image_admin(admin.ModelAdmin):
    list_display = ('name','hash','type','location','tenant')
    list_filter = ['name','hash','type','location','tenant']
    

admin.site.register(user,user_admin)
admin.site.register(site,site_admin)
admin.site.register(credential,credential_admin)
admin.site.register(image,image_admin)
