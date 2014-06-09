'''
Created on May 15, 2014

@author: rd
'''
from django.contrib import admin
from imagedist.models import site,credential,image,user

class user_admin(admin.ModelAdmin):
    list_display = ('username','tenent','token','lastlogin')
    list_filter = ['username','tenent','token','lastlogin']
    
class site_admin(admin.ModelAdmin):
    list_display = ('name','url','type')
    list_filter = ['name','url','type']

class credential_admin(admin.ModelAdmin):
    list_display = ('user','site','un','pw','tenent')
    list_filter = ['user','site','un','pw','tenent']

class image_admin(admin.ModelAdmin):
    list_display = ('name','hash','type','location','tenent')
    list_filter = ['name','hash','type','location','tenent']
    

admin.site.register(user,user_admin)
admin.site.register(site,site_admin)
admin.site.register(credential,credential_admin)
admin.site.register(image,image_admin)
