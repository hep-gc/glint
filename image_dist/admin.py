'''
Created on Jan 28, 2014

@author: rd
'''

from django.contrib import admin
from image_dist.models import user_messages,site_info,image_info,user_site_env_setup_script,deployed_images

class user_messages_admin(admin.ModelAdmin):
    list_display = ('user_name','msg_type','message','pub_date')
    list_filter = ('user_name','msg_type','message','pub_date')

class site_admin(admin.ModelAdmin):
    list_display = ('site_name','site_url','site_type','site_state')
    list_filter = ['site_type','site_state']
    
class image_admin(admin.ModelAdmin):
    list_display = ('image_user_id','image_name','image_type','image_src_location')
    list_filter = ['image_type','image_user_id','image_name']
    
class env_admin(admin.ModelAdmin):
    list_display= ('user','site','un','pw','user_site_script')

class deployed_admin(admin.ModelAdmin):
    list_display= ('user','image','site','site_script','imageid')
    list_filter = ['user','image','site','site_script','imageid']

admin.site.register(user_messages,user_messages_admin)
admin.site.register(site_info,site_admin)
admin.site.register(image_info,image_admin)
admin.site.register(user_site_env_setup_script,env_admin)
admin.site.register(deployed_images,deployed_admin)

