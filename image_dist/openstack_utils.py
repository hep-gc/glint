#!/usr/bin/env python

import subprocess, requests, json,re
import keystoneclient.v2_0.client as ksclient
import glanceclient
from pprint import pprint


def distribute_image(image, site, file_loc, password,image_type):
    """
    Takes image file and site RC file that the user specified and extracts
    the source RC file information to create an image on the site
    """
    k_ind = str(image).rfind('/')
    name=str(image)[k_ind+1:]
    
    OS_PASSWORD = password
    
    # extracts information from site RC file
    for line in open(str(file_loc),'r'):
        if line.startswith('export OS_AUTH_URL='):
            OS_AUTH_URL = line[19:].strip()
        if line.startswith('export OS_TENANT_ID='):
            OS_TENANT_ID = line[20:].strip()
        if line.startswith('export OS_TENANT_NAME='): # not used in glance command
            OS_TENANT_NAME = line[23:-2].strip()
        if line.startswith('export OS_USERNAME='):
            #OS_USERNAME = line[20:-2].strip()
            os_ind = str(line).rfind('=')
            OS_USERNAME = (line[os_ind+1:]).replace('"','')
            OS_USERNAME = OS_USERNAME.replace('\n','')
    pprint("Adding Image %s : %s : %s : %s "%(OS_AUTH_URL,OS_USERNAME,OS_PASSWORD,OS_TENANT_NAME));
    keystone = ksclient.Client(auth_url=OS_AUTH_URL,username=OS_USERNAME,password=OS_PASSWORD,tenant_name=OS_TENANT_NAME)       
    glance_ep = keystone.service_catalog.url_for(service_type='image',endpoint_type='publicURL')
    glance = glanceclient.Client('1',glance_ep,token=keystone.auth_token)
    #glance = glanceclient.Client()
    fimage = open(str(image))
    
    # uses glance image-create command to create the given name image on the site
    # currently assumes disk format is qcow2, container format is bare, and public
    pprint("UN:%s PW:%s T_ID:%s AUTH_URL:%s NAME:%s IMFILE:%s IMGTYPE:%s" %(OS_USERNAME,OS_PASSWORD,OS_TENANT_ID,OS_AUTH_URL,name,image,image_type) )
    #ret = subprocess.check_output(["glance", "-I", OS_USERNAME, "-K", OS_PASSWORD, "--os-tenant-id", OS_TENANT_ID, "--os-auth-url", OS_AUTH_URL, "image-create", "--name", name, "--disk-format=qcow2", "--container-format=bare", "--is-public=True", "--file=" + str(image)])
    #pprint(ret)
    result = glance.images.create(name=name,is_public="False",disk_format=image_type,container_format="bare",data=fimage)
    
    pprint(result)
    return result
    
def delete_image(image, site, file_loc, password,id):
    """
    Takes image file and site RC file that the user specified and extracts
    the source RC file information to create an image on the site
    """
    k_ind = str(image).rfind('/')
    name=str(image)[k_ind+1:]
    
    OS_PASSWORD = password
    
    # extracts information from site RC file
    for line in open(str(file_loc),'r'):
        if line.startswith('export OS_AUTH_URL='):
            OS_AUTH_URL = line[19:].strip()
        if line.startswith('export OS_TENANT_ID='):
            OS_TENANT_ID = line[20:].strip()
        if line.startswith('export OS_TENANT_NAME='): # not used in glance command
            OS_TENANT_NAME = line[23:-2].strip()
        if line.startswith('export OS_USERNAME='):
            #OS_USERNAME = line[20:-2].strip()
            os_ind = str(line).rfind('=')
            OS_USERNAME = (line[os_ind+1:]).replace('"','')
            OS_USERNAME = OS_USERNAME.replace('\n','')

    # uses glance image-create command to create the given name image on the site
    # currently assumes disk format is qcow2, container format is bare, and public
    pprint("UN:%s PW:%s T_ID:%s AUTH_URL:%s NAME:%s IMFILE:%s" %(OS_USERNAME,OS_PASSWORD,OS_TENANT_ID,OS_AUTH_URL,name,image) )
    #ret = subprocess.check_output(["glance", "-I", OS_USERNAME, "-K", OS_PASSWORD, "--os-tenant-id", OS_TENANT_ID, "--os_auth_url", OS_AUTH_URL, "image-delete", id])
    #pprint(ret)
    keystone = ksclient.Client(auth_url=OS_AUTH_URL,username=OS_USERNAME,password=OS_PASSWORD,tenant_name=OS_TENANT_NAME)       
    glance_ep = keystone.service_catalog.url_for(service_type='image',endpoint_type='publicURL')
    glance = glanceclient.Client('1',glance_ep,token=keystone.auth_token)
    
    #images is an iterator interface abstraction
    images = glance.images.list()
    #image = images.find()
    for index,image in enumerate(images):
        #pprint('Images:%s:%s' %(index,image))
        if image.id == id:
            pprint("found image id %s" % image.id)
            #glance.images.delete(id=image.id)
            image.delete()
            pprint("done delteiing")
    #pprint('Images:%s' %image)
    #pprint(images)

