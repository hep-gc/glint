'''
Created on Feb 3, 2014

@author: rd
'''

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from pprint import pprint

import json,threading
import image_dist.openstack_utils

from django.views.decorators.csrf import csrf_exempt
from image_dist.models import site_info

@login_required
@csrf_exempt
def handle_request(request):
    jsonMsg = request.POST['jsonMsg']
    #pprint(jsonMsg)
    json_req = json.loads(jsonMsg)
    ret_msg="done";
    if json_req['op'] == 'save':
        tasks=[]
        img_deployments = json_req['deployments']
        for key in img_deployments:
            sites = img_deployments[key]
            #pprint("key %s sites %s" %(key,sites))
            for site in sites:
                site_name=site['site_name']
                site_cfg = site['site_script']
                #pprint("img: %s site name:%s cfg:%s"%(key,site_name,site_cfg))
                
                img_src_line = request.user.image_info_set.get(image_name=key)
    
                #site_dest_line = request.user.site_info_set.get(site_name=site_name)
                site_dest_line = site_info.objects.get(site_name=site_name)
                
                cfg_file = request.user.user_site_env_setup_script_set.get(site=site_dest_line.pk,user_site_script=site_cfg)
                
                if request.user.deployed_images_set.filter(image=img_src_line,site=site_dest_line,site_script=cfg_file).count() == 0:
                    #create an add task
                    t = threading.Thread(target=add_image,args=[request,key,site_name,site_cfg] )
                    #add_image(request,key,site_name,site_cfg)
                    tasks.append(t)
                    pprint("now start thread")
                    #t.start()
                    pprint("successfully submitted image to site")
                    site['site_status']="deployed"
                #else:
                #    pprint("Entry already exists in db")
        
        deployed_sites = request.user.deployed_images_set.all()
        for t in tasks:
            t.start()
        for t in tasks:
            t.join()
        
        for site in deployed_sites:
            image_name = site.image.image_name
            site_name = site.site.site_name
            site_script_name = site.site_script.user_site_script
            #pprint("found a deployed table site %s llok for image name %s in %s" %(site_name,image_name,img_deployments) )
            
            if image_name in img_deployments:
                #pprint("name is deps");
                dep_sites = img_deployments[image_name]
                found = False
                for dep_site in dep_sites:
                    #pprint("found dep_site in sites for image_name %s"%image_name)
                    dep_site_name = dep_site['site_name']
                    dep_site_cfg = dep_site['site_script']
                    #pprint("looking for %s %s"%(dep_site_name,dep_site_cfg))
                    if site_name == dep_site_name and site_script_name==dep_site_cfg:
                        found = True
                        
                        #pprint("found %s , %s for image %s "%(site_name,site_script_name,image_name))
                
                if not found:
                    pprint("could not find %s %s for iamge %s so remove it "%(site_name,site_script_name,image_name))
                    #create a remove task
                    rem_image(request,image_name,site_name,site_script_name)
                    
        
        ret_msg=json.dumps(img_deployments)
                                                   
                    
            
    return HttpResponse("%s" %ret_msg )



def rem_image(request,img_name,site2_name,site2_script):
    img_src_line = request.user.image_info_set.get(image_name=img_name)
    pprint(img_src_line.image_src_location)
    #site_dest_line = request.user.site_info_set.get(site_name=site2_name)
    site_dest_line = site_info.objects.get(site_name=site2_name)
    pprint(site_dest_line.site_url)
    cfg_file = request.user.user_site_env_setup_script_set.get(site=site_dest_line.pk,user_site_script=site2_script)
    
    deployed_image_info = request.user.deployed_images_set.get(image=img_src_line,site_script=cfg_file)
    pprint(cfg_file)
    image_dist.openstack_utils.delete_image(img_src_line.image_src_location, site_dest_line.site_url, cfg_file.user_site_script,cfg_file.pw,deployed_image_info.imageid)
    
    request.user.deployed_images_set.filter(user=request.user.pk,image=img_src_line,site=site_dest_line,site_script=cfg_file).delete()
    

def add_image(request,img_name,site2_name,site2_script):
    img_src_line = request.user.image_info_set.get(image_name=img_name)
    pprint("%s %s"%(img_src_line.image_src_location,img_src_line.image_type))
    #site_dest_line = request.user.site_info_set.get(site_name=site2_name)
    site_dest_line = site_info.objects.get(site_name=site2_name)
    pprint(site_dest_line.site_url)
    cfg_file = request.user.user_site_env_setup_script_set.get(site=site_dest_line.pk,user_site_script=site2_script)
    
    pprint(cfg_file)
    image_info = image_dist.openstack_utils.distribute_image(img_src_line.image_src_location, site_dest_line.site_url, cfg_file.user_site_script,cfg_file.pw,img_src_line.image_type)
    
    request.user.deployed_images_set.create(user=request.user.pk,image=img_src_line,site=site_dest_line,site_script=cfg_file,imageid=image_info.id)
    
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
    #site_dest_line = request.user.site_info_set.get(site_name=site2_name)
    site_dest_line = site_info.objects.get(site_name=site2_name)
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
    #site_dest_line = request.user.site_info_set.get(site_name=site2_name)
    site_dest_line = site_info.objects.get(site_name=site2_name)
    pprint(site_dest_line.site_url)
    cfg_file = request.user.user_site_env_setup_script_set.get(site=site_dest_line.pk,user_site_script=site2_script)
    
    deployed_image_info = request.user.deployed_images_set.get(image=img_src_line,site_script=cfg_file)
    pprint(cfg_file)
    image_dist.openstack_utils.delete_image(img_src_line.image_src_location, site_dest_line.site_url, cfg_file.user_site_script,cfg_file.pw,deployed_image_info.imageid)
    
    res = request.user.deployed_images_set.filter(user=request.user.pk,image=img_src_line,site=site_dest_line,site_script=cfg_file).delete()
    #pprint(res)
    return HttpResponse("vm distributed  img:%s site:%s cfg:%s" %(img_src_line.image_src_location,site_dest_line.site_url,cfg_file.user_site_script) )
    #return HttpResponse("wha")

