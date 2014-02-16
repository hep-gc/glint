'''
Created on Jan 28, 2014

@author: rd
'''
from pprint import pprint

def file_uploader(instance,filename):
    url = "tmp/%s/%s" % (instance.image_user_id,filename)
    return url

def file_uploader_script(instance,filename):
    url = "tmp/%s/%s" % (instance.user,filename)
    return url