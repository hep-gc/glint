#!/usr/bin/env python
# Copyright (c) 2013 Hewlett-Packard Development Company, L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# THIS FILE IS MANAGED BY THE GLOBAL REQUIREMENTS REPO - DO NOT EDIT
import os,re
import subprocess

#ensure environment variables are set
def environment_check():
    tenant_id = os.getenv("OS_TENANT_ID")
    tenant_name = os.getenv("OS_TENANT_NAME")
    os_auth_url = os.getenv("OS_AUTH_URL")
    os_username = os.getenv("OS_USERNAME")
    os_password = os.getenv("OS_PASSWORD")
    
    if (tenant_id == None or tenant_name == None or os_auth_url == None or os_username == None or os_password == None):

        print "Missing Parameter Please check that tenantid, tenantname , authurl , username and password are set in the environment variables"
        return False
    return True

# use keystone to register glint as a service
def setup_glint_service():
    print "setting up table service entry and endpoint entry into openstack db usng the keystone service"
    #check if service already registered
    process = subprocess.Popen(['keystone','service-list'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)      
    out,err = process.communicate()
    if "glint" in out:
        print "glint has been registered"
        return
    else:
        print "glint has not been registered, so register it."
        print "Create Service Glint"
        process = subprocess.Popen(['keystone','service-create','--name=glint','--type=image_mgt','--description="Image Distribution Service"'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        out,err = process.communicate()
        rexp_processor = re.compile('\|\s+id\s+\|\s+[a-z0-9]{32}\s+\|')
        rexp_res = rexp_processor.search(out)
        rexp_processor = re.compile('[a-z0-9]{32}')
        glint_service_id = rexp_processor.search(rexp_res.group()).group()
        print "Service id %s"%glint_service_id
        print "Create Glint Endpoint"
        process = subprocess.Popen(['keystone','endpoint-create','--region=openstack','--service-id=%s'%glint_service_id,'--publicurl=http://rat01.heprc.uvic.ca:8081/image_dist/','--internalurl=http://127.0.0.1:8081/','--adminurl=http://rat01.heprc.uvic.ca:8081/admin'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        out,err = process.communicate()
        return

env_ck = environment_check()

if env_ck:
    setup_glint_service()
else:
    print "Unable to setup glint service for use by openstack becuase the environment variables need to be set by the administrator, please source the admins .rc file which you can get from the openstack horizon interface Access and Security section"


