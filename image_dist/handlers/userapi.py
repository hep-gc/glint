'''
Created on Feb 3, 2014

@author: rd
'''

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from pprint import pprint

import json
import image_dist.openstack_utils

from django.views.decorators.csrf import csrf_exempt


@login_required
@csrf_exempt
def handle_request(request):
    jsonMsg = request.POST['jsonMsg']
    pprint(jsonMsg)
    json_req = json.loads(jsonMsg)
    if json_req['op'] == 'save':
        img_deployments = json_req['deployments']
        for key in img_deployments:
            sites = img_deployments[key]
            #pprint("key %s sites %s" %(key,sites))
            for site in sites:
                site_name=site['site_name']
                site_cfg = site['site_script']
                pprint("img: %s site name:%s cfg:%s"%(key,site_name,site_cfg))
                #check site for image upload if necesary
                #check update models
            
    return HttpResponse("Got Json Message %s" %jsonMsg)
    
@login_required
@csrf_exempt
def add_image_to_site(request):
    img_name = request.POST['img_name']
    
    # this is json
    site2_name_json = request.POST['site_name']
    #pprint(site2_name_json)
    #site2_name_json=site2_name_json.replace("'","")
    #pprint(site2_name_json)
    json_data = json.loads(site2_name_json)
    
    site2_name = json_data['site']
    site2_script = json_data['script']
    pprint("in:%s sn:%s" %(img_name,site2_name))
    img_src_line = request.user.image_info_set.get(image_name=img_name)
    pprint(img_src_line.image_src_location)
    site_dest_line = request.user.site_info_set.get(site_name=site2_name)
    pprint(site_dest_line.site_url)
    cfg_file = request.user.user_site_env_setup_script_set.get(site=site_dest_line.pk,user_site_script=site2_script)
    
    pprint(cfg_file)
    image_info = image_dist.openstack_utils.distribute_image(img_src_line.image_src_location, site_dest_line.site_url, cfg_file.user_site_script,cfg_file.pw)
    
    request.user.deployed_images_set.create(user=request.user.pk,image=img_src_line,site=site_dest_line,site_script=cfg_file,imageid=image_info.id)
    return HttpResponse("vm distributed  img:%s site:%s cfg:%s id:%s" %(img_src_line.image_src_location,site_dest_line.site_url,cfg_file.user_site_script,image_info.id) )


@login_required
@csrf_exempt
def remove_image_from_site(request):
    img_name = request.POST['img_name']
    
    # this is json
    site2_name_json = request.POST['site_name']
    #pprint(site2_name_json)
    #site2_name_json=site2_name_json.replace("'","")
    #pprint(site2_name_json)
    json_data = json.loads(site2_name_json)
    
    site2_name = json_data['site_name']
    site2_script = json_data['site_script']
    pprint("in:%s sn:%s" %(img_name,site2_name))
    img_src_line = request.user.image_info_set.get(image_name=img_name)
    pprint(img_src_line.image_src_location)
    site_dest_line = request.user.site_info_set.get(site_name=site2_name)
    pprint(site_dest_line.site_url)
    cfg_file = request.user.user_site_env_setup_script_set.get(site=site_dest_line.pk,user_site_script=site2_script)
    
    deployed_image_info = request.user.deployed_images_set.get(image=img_src_line,site_script=cfg_file)
    pprint(cfg_file)
    image_dist.openstack_utils.delete_image(img_src_line.image_src_location, site_dest_line.site_url, cfg_file.user_site_script,cfg_file.pw,deployed_image_info.imageid)
    
    res = request.user.deployed_images_set.filter(user=request.user.pk,image=img_src_line,site=site_dest_line,site_script=cfg_file).delete()
    #pprint(res)
    return HttpResponse("vm distributed  img:%s site:%s cfg:%s" %(img_src_line.image_src_location,site_dest_line.site_url,cfg_file.user_site_script) )
    #return HttpResponse("wha")

