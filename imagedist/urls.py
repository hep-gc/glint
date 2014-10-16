'''
Created on May 15, 2014

@author: rd
'''
from django.conf.urls import patterns, include, url

from imagedist import jsonservices

urlpatterns = patterns('',
    #return current cache of all images on all sites
    url(r'^/imagedistribution/$', jsonservices.getImages,name='getImages'),
    url(r'/save', jsonservices.save,name='distribute Images'), 
    url(r'/managecredentials', jsonservices.credentials,name='manage credentials'), 
    url(r'/createsite', jsonservices.createsite,name='createsite'),  
    url(r'/deletesite', jsonservices.deletesite,name='deletesite'),   
    url(r'/listsites', jsonservices.listsites,name='listsites'),  
    url(r'/addcredential', jsonservices.addcredential,name='addcredential'),  
    url(r'/hascredential', jsonservices.hascredential,name='addcredential'), 
)
