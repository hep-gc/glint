# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from pprint import pprint

def index(request):
    return HttpResponse("hello vm dist")

@login_required()
def user_dist_vms_table(request):
    #site_set = request.user.site_info_set.all(); 
    site_set = request.user.user_site_env_setup_script_set.all()
    site_image_array={};
    
    #c = {}
    #c.update(csrf(request))
    tenet_set = request.user.user_site_env_setup_script_set.all()
    image_set = request.user.image_info_set.all()
    for image in image_set:
        site_image_array[image.image_name]=[]
        sites = request.user.deployed_images_set.filter(image=image.pk)
        #site_image_array[image.image_name]=sites
        for site in sites:
            #if image.image_name in site_image_array.keys(): 
            site_info={}
            site_info["site_name"]=site.site.site_name   
            site_info["site_script"]=site.site_script
            site_image_array[image.image_name].append(site_info)
            #else:
            #    site_image_array[image.image_name]=[site.site.site_name]
        
    pprint(site_image_array)
    
    return render(request, 'image_dist/imagemanagement.html',{'tenet_set':tenet_set,'site_set':site_set,'site_image_array':site_image_array.items(),'user_id': request.user.username})
    
@login_required()
def user_images_table(request):
    #get user images
    image_set = request.user.image_info_set.all(); 
    return render(request, 'image_dist/images_table.html',{'image_data': image_set,'user_id': request.user.username}) 

@login_required()
def user_sites_table(request):
    site_set = request.user.site_info_set.all(); 
    return render(request, 'image_dist/sites_table.html',{'site_data': site_set,'user_id': request.user.username}) 

@login_required()
def user_credential_table(request):
    return HttpResponse("Generate page with  " )