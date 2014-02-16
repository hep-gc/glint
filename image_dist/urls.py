'''
Created on Jan 30, 2014

@author: rd
'''
from django.conf.urls import patterns, url


from image_dist.handlers import userviews
from image_dist.handlers import userapi

urlpatterns = patterns('',
    url(r'^$',userviews.index ,name='index'),
    #user views - html templates
    url(r'^/imagedistribution/$',userviews.user_dist_vms_table, name='user_dist_vms_table' ),
    url(r'^/userimages/$',userviews.user_images_table, name='user_dist_vms_table' ),
    url(r'^/usersites/$',userviews.user_sites_table, name='user_sites_table' ),
    #user api - json requests
    #url(r'^/distimage/(?P<img_name>[\w\ ]+)/(?P<site2_name>[\w\ ]+)/',userapi.add_image_to_site, name='image_dist' ),
    url(r'^/distimage/',userapi.add_image_to_site, name='image_dist' ),
    url(r'^/jsonrequestpost/',userapi.handle_request, name='json_request' ),
    #url(r'^/removeimage/(?P<img_name>[\w\ ]+)/(?P<site2_name>[\w\ ]+)/' ,userapi.remove_image_from_site, name='vm_remove' ),
    url(r'^/removeimage/' ,userapi.remove_image_from_site, name='vm_remove' ),
)
