'''
Created on Mar 31, 2015

@author: ronaldjosephdesmarais
'''

import glintViewer as g_view

#list-sites
data = [u'{"name":"Mosue","url":"http://mouse01.heprc.uvic.ca:5000/v2.0","authport":"5000","version":"v2.0","type":"Openstack","pk":"1"}', u'{"name":"Rateroni","url":"http://rat01.heprc.uvic.ca:5000/v2.0","authport":"5000","version":"v2.0","type":"Openstack","pk":"2"}']

g_view.cli_view(data,"list-sites")