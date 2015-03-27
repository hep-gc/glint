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
print "List Sites"
sites = api.listSites()
print sites
print "----------"
print "Create Site"
opres = api.createSite('Rateroni', 'http://rat01.heprc.uvic.ca:5000/v2.0', 'Openstack')
print opres
print "----------"
print "Delete Site"
opres = api.deleteSite('Rateroni', 'http://rat01.heprc.uvic.ca:5000/v2.0', 'Openstack')
print opres
print "----------"

