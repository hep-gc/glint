'''
Created on Mar 26, 2015

@author: ronaldjosephdesmarais
'''
import glint_api as g_api
import logging,json

api = g_api.glint_api('g_log.log',logging.DEBUG,'glint_api_cfg.yaml')

####for the easy part repository management####################
print "Create Site"
opres = api.createSite('Rateroni', 'http://rat01.heprc.uvic.ca:5000/v2.0', 'Openstack')
print opres
print "----------"
print "Delete Site"
opres = api.deleteSite(opres['site_id'])
print opres
print "----------"
print "Create Site Again"
opres = api.createSite('Rateroni', 'http://rat01.heprc.uvic.ca:5000/v2.0', 'Openstack')
print opres
print "----------"
print "Add Credential to %s"%opres['site_id']
opres_cred = api.addCredential('HEP', 'un', 'pw',opres['site_id'])
print opres_cred
print "----------"
print "Delete Credential to %s"%opres['site_id']
opres_del_cred = api.deleteCredential(opres['site_id'])
print opres_del_cred
print "----------"
print "Delete Site"
opres = api.deleteSite(opres['site_id'])
print opres
print "----------"
print "Create Site Again Again"
opres = api.createSite('Rateroni 2', 'http://rat01.heprc.uvic.ca:5000/v2.0', 'Openstack')
print opres
print "----------"
print "Add Credential to %s"%opres['site_id']
opres_cred = api.addCredential('HEP', 'un', 'pw',opres['site_id'])
print opres_cred
print "----------"
print "Test HAS Credential ck_type is ONE  on site %s"%opres['site_id']
opres_has_cred = api.hasCredential(opres['site_id'],"ONE")
print opres_has_cred
print "----------"
print "Test HAS Credential ck_type is '' on site %s"%opres['site_id']
opres_has_cred = api.hasCredential(opres['site_id'],"")
print opres_has_cred
print "----------"
print "Test get Credential on site %s"%opres['site_id']
opres_get_cred = api.getCredential(opres['site_id'])
print opres_get_cred
print "----------"
print "Delete Credential to %s"%opres['site_id']
opres_del_cred = api.deleteCredential(opres['site_id'])
print opres_del_cred
print "----------"
print "Delete Site"
opres = api.deleteSite(opres['site_id'])
print opres
print "----------"

#now for the tough part Image Distribution
print "Get Images"
images = api.getImages()
print images
print "----------"
print "List Sites"
sites = api.listSites()
print sites
print "----------"
print "Image Copy"
img_copy = api.imageCopy("Cirros 2","TestSite",["Mosue"])
print img_copy
print "----------"





