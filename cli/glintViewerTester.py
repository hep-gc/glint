'''
Created on Mar 31, 2015

@author: ronaldjosephdesmarais
'''

import glintViewer as g_view

#list-sites
data = [{u'name': u'Mosue', u'url': u'http://mouse01.heprc.uvic.ca:5000/v2.0', u'authport': u'5000', u'version': u'v2.0', u'pk': u'1', u'type': u'Openstack'}, {u'name': u'Rateroni', u'url': u'http://rat01.heprc.uvic.ca:5000/v2.0', u'authport': u'5000', u'version': u'v2.0', u'pk': u'2', u'type': u'Openstack'}]
g_view.cli_view(data,"list-sites")

#delete-credential
data = [{u'Result': u'Success removing Credential'}]
g_view.cli_view(data,"delete-credential")

#delete-site
data = [{u'Result': u'Successful Delete'}]
g_view.cli_view(data,"delete-site")

#create-site
data = [{u'site_id': 2, u'Result': u'Success'}]
g_view.cli_view(data,"create-site")

#add-credential
data = [{u'Result': u'Sites: add Credential'}]
g_view.cli_view(data,"add-credential")

#has-credential
data = [{u'result': True, u'error': False}]
g_view.cli_view(data,"has-credential")

#get-credential
data = [{u'tenant': u'HEP', u'cred_id': u'rd'}]
g_view.cli_view(data,"get-credential")

#image-copy
data = [{u'thread_id': 5}]
g_view.cli_view(data,"image-copy")

#image-delete
data = [{u'thread_id': 5}]
g_view.cli_view(data,"image-delete")

#get-image
data = {u'rows': [{u'container_format': u'bare', u'image': u'tinyvm', u'disk_format': u'qcow2', u'sites': [{u'is_public': u'False', u'tenant': u'glinttenant', u'is_owner': u'True', u'name': u'TestSite'}]}, {u'container_format': u'bare', u'image': u'CentOS 7 x86_64 QCOW', u'disk_format': u'qcow2', u'sites': [{u'is_public': u'False', u'tenant': u'glinttenant', u'is_owner': u'True', u'name': u'TestSite'}]}, {u'container_format': u'bare', u'image': u'Cirros 2', u'disk_format': u'qcow2', u'sites': [{u'is_public': u'False', u'tenant': u'glinttenant', u'is_owner': u'True', u'name': u'TestSite'}]}, {u'container_format': u'bare', u'image': u'cirros-0.3.3-x86_64', u'disk_format': u'qcow2', u'sites': [{u'is_public': u'True', u'tenant': u'glinttenant', u'is_owner': u'False', u'name': u'TestSite'}]}, {u'container_format': u'bare', u'image': u'Ubuntu 12.04 Precise', u'disk_format': u'qcow2', u'sites': [{u'is_public': u'True', u'tenant': u'testing', u'is_owner': u'True', u'name': u'Mosue'}]}, {u'container_format': u'bare', u'image': u'mjmc-htc-test-node', u'disk_format': u'qcow2', u'sites': [{u'is_public': u'False', u'tenant': u'testing', u'is_owner': u'True', u'name': u'Mosue'}]}, {u'container_format': u'bare', u'image': u'Ubuntu-14_04-Trusty', u'disk_format': u'qcow2', u'sites': [{u'is_public': u'False', u'tenant': u'testing', u'is_owner': u'True', u'name': u'Mosue'}]}, {u'container_format': u'bare', u'image': u'mjmc-htc/cs-base', u'disk_format': u'qcow2', u'sites': [{u'is_public': u'False', u'tenant': u'testing', u'is_owner': u'True', u'name': u'Mosue'}]}, {u'container_format': u'bare', u'image': u'Fedora-21', u'disk_format': u'qcow2', u'sites': [{u'is_public': u'False', u'tenant': u'testing', u'is_owner': u'True', u'name': u'Mosue'}]}, {u'container_format': u'bare', u'image': u'fedora-image', u'disk_format': u'qcow2', u'sites': [{u'is_public': u'False', u'tenant': u'testing', u'is_owner': u'True', u'name': u'Mosue'}]}, {u'container_format': u'bare', u'image': u'CentOS 7', u'disk_format': u'qcow2', u'sites': [{u'is_public': u'False', u'tenant': u'testing', u'is_owner': u'True', u'name': u'Mosue'}]}, {u'container_format': u'bare', u'image': u'shoal-demo-test', u'disk_format': u'qcow2', u'sites': [{u'is_public': u'False', u'tenant': u'testing', u'is_owner': u'True', u'name': u'Mosue'}]}, {u'container_format': u'bare', u'image': u'mjmc-test-3', u'disk_format': u'qcow2', u'sites': [{u'is_public': u'False', u'tenant': u'testing', u'is_owner': u'True', u'name': u'Mosue'}]}, {u'container_format': u'bare', u'image': u'mjmc-two', u'disk_format': u'qcow2', u'sites': [{u'is_public': u'False', u'tenant': u'testing', u'is_owner': u'True', u'name': u'Mosue'}]}, {u'container_format': u'bare', u'image': u'ucernvm-prod.1.18-13', u'disk_format': u'raw', u'sites': [{u'is_public': u'True', u'tenant': u'testing', u'is_owner': u'False', u'name': u'Mosue'}]}, {u'container_format': u'bare', u'image': u'centos6-bare', u'disk_format': u'qcow2', u'sites': [{u'is_public': u'True', u'tenant': u'testing', u'is_owner': u'False', u'name': u'Mosue'}]}, {u'container_format': u'bare', u'image': u'ubuntu-ec2-sps-x', u'disk_format': u'qcow2', u'sites': [{u'is_public': u'True', u'tenant': u'testing', u'is_owner': u'False', u'name': u'Mosue'}]}, {u'container_format': u'bare', u'image': u'ucernvm-prod.1.18-10', u'disk_format': u'raw', u'sites': [{u'is_public': u'True', u'tenant': u'testing', u'is_owner': u'False', u'name': u'Mosue'}, {u'is_public': u'False', u'tenant': u'testing', u'is_owner': u'True', u'name': u'Mosue'}]}, {u'container_format': u'bare', u'image': u'cernvm-mouse.fix03', u'disk_format': u'qcow2', u'sites': [{u'is_public': u'True', u'tenant': u'testing', u'is_owner': u'False', u'name': u'Mosue'}]}, {u'container_format': u'bare', u'image': u'fedora', u'disk_format': u'qcow2', u'sites': [{u'is_public': u'True', u'tenant': u'testing', u'is_owner': u'False', u'name': u'Mosue'}]}], u'sites': [{u'tenant': u'glinttenant', u'name': u'TestSite'}, {u'tenant': u'testing', u'name': u'Mosue'}]}
g_view.cli_view(data,"get-images")

