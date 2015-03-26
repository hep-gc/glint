'''
Created on Mar 26, 2015

@author: ronaldjosephdesmarais
'''
import glint_api as g_api
import logging

api = g_api.glint_api('g_log.log',logging.DEBUG,'glint_api_cfg.yaml')

print "Get Images"
images = api.getImages()
print images
print "----------"
