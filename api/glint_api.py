'''
Created on Mar 26, 2015

@author: ronaldjosephdesmarais
'''
import logging,yaml,json,requests
import keystoneclient.v2_0.client as ksclient

class glint_api(object):
    def __init__(self,log_name,log_lvl,glint_cfg):
        #setup logging for glint api
        self.log = logging.getLogger('glint_api')
        fh = logging.FileHandler(log_name)
        self.log.setLevel(log_lvl)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        self.log.addHandler(fh)
        
        #setup configuration to talk to glint
        cfg_f = yaml.load( open("api/%s"%glint_cfg,'r') )
        self.glint_url=cfg_f['glint_url']
        self.auth_url=cfg_f['auth_url']
        self.un=cfg_f['keystone_un']
        self.pw=cfg_f['keystone_pw']
        self.tenant_id=cfg_f['keystone_tenant_id']
        self.tenant_name=cfg_f['keystone_tenant_name']
        self.log.debug("Configuring glint api with %s:%s:%s:%s:%s"%(self.glint_url,self.auth_url,self.un,self.pw,self.tenant_id))
        
        #use keystone client un and pw to get an auth token 
        keystone = ksclient.Client(auth_url=self.auth_url, username=self.un, password=self.pw, tenant_id=self.tenant_id)
        self.token = keystone.auth_ref['token']['id']
        self.log.debug("Received token %s"%self.token)
        
    def getImages(self):
        self.log.debug("getImages  from %s"%( "%s/imagedistribution/"%self.glint_url))
        data_json = requests.post("%s/imagedistribution/"%self.glint_url,data={"USER_ID":self.un,"USER_TOKEN":"%s"%self.token,"USER_TENANT":self.tenant_name},cookies=None).text  
        data_obj = json.loads(data_json)
        return data_obj

    def imageCopy(self,image_name,src_site,dest_sites):
        self.log.debug("copy image %s from %s to %s"%(image_name,src_site,dest_sites))
        print "copy image %s from %s to %s"%(image_name,src_site,dest_sites)
        
        #getImages from glint and start copy process
        json_images=self.getImages()
        #find row object with image_name in it
        if len(dest_sites) == 0:
            print "Please Submit list of destination sites to copy image to"
            return {"Result":"Error, no destinatoin sites"}
        for dest_site in dest_sites:
            if dest_site == src_site:
                    return {"Result":"Dest site cannot be a source site"}
                
        for row in json_images['rows']:
            #print row
            if row['image'] == image_name:
                print "found image to copy now make sure src site exists"
                for site in row['sites']:
                    if site['name'] ==  src_site:
                        print "found source site to copy image from, now check for valid destination sites"
                        for dest_site in dest_sites:
                            fnd_site=False
                            
                            for avail_site in json_images['sites']:
                                print "Compare %s to dest %s"%(avail_site['name'],dest_site)    
                                if avail_site['name'] == dest_site:
                                    fnd_site=True
                                    
                            if not fnd_site:
                                print "Sorry destination site %s is not available please remove "%(avail_site)
                                return {"Result":"Destination site not found %s"%(avail_site)}
                            
                            print "All checks passed, prepare copy json"
                            json_save_obj={"op":"add_img","disk_format":row['disk_format'],"container_format":row['container_format'],"image_name":row['image'],"image_dest":dest_site,"img_src":[{"site_name":site['name'],"site_tenent":site['tenent']}]}
                            print json_save_obj
                            #data_json = requests.post("%s/save/"%self.glint_url,data={"jsonMsg":json.dumps(json_save_obj),"USER_ID":self.un,"USER_TOKEN":"%s"%self.token,"USER_TENANT":self.tenant_name},cookies=None).text  
                            #data_obj = json.loads(data_json)
                            #return data_obj
                            return {}
                            
                
            
        
        
    def save(self,jsonMsg, USER_TOKEN, USER_TENANT):
        return jsonMsg, USER_TOKEN, USER_TENANT

    def credentials(self,USER_TOKEN, USER_TENANT, USER_ID):
        return USER_TOKEN, USER_TENANT, USER_ID

    def listSites(self):
        self.log.debug("getImages  from %s"%( "%s/listsites/"%self.glint_url))
        data_json = requests.post("%s/listsites/"%self.glint_url,data={"USER_ID":self.un,"USER_TOKEN":"%s"%self.token,"USER_TENANT":self.tenant_name},cookies=None).text  
        data_obj = json.loads(data_json)
        return data_obj

    def deleteSite(self, SITE_ID):
        self.log.debug("delete site %s"%(SITE_ID))
        data_json = requests.post("%s/deletesite/"%self.glint_url,data={"SITE_ID":SITE_ID,"USER_ID":self.un,"USER_TOKEN":"%s"%self.token,"USER_TENANT":self.tenant_name},cookies=None).text  
        self.log.debug(data_json)
        data_obj = json.loads(data_json)
        return data_obj

    def createSite(self,name,url,formatt):
        self.log.debug("create site %s :: %s :: %s"%(name,url,formatt))
        site_data={'url':url,'name':name,'disk_format':formatt}
        data_json = requests.post("%s/createsite/"%self.glint_url,data={"SITEDATA":json.dumps(site_data),"USER_ID":self.un,"USER_TOKEN":"%s"%self.token,"USER_TENANT":self.tenant_name},cookies=None).text  
        self.log.debug(data_json)
        data_obj = json.loads(data_json)
        return data_obj

    def deleteCredential(self, site_id):
        self.log.debug("delete credential ")
        data_json = requests.post("%s/deletecredential/"%self.glint_url,data={"SITE_ID":site_id,"USER_ID":self.un,"USER_TOKEN":"%s"%self.token,"USER_TENANT":self.tenant_name},cookies=None).text  
        self.log.debug(data_json)
        data_obj = json.loads(data_json)
        return data_obj

    def getCredential(self,site_id):
        self.log.debug("get credential ")
        data_json = requests.post("%s/getcredential/"%self.glint_url,data={"SITE_ID":site_id,"USER_ID":self.un,"USER_TOKEN":"%s"%self.token,"USER_TENANT":self.tenant_name},cookies=None).text  
        self.log.debug(data_json)
        data_obj = json.loads(data_json)
        return data_obj

    def hasCredential(self, site_id, ck_type):
        #ck_type is "ONE" or "" 
        self.log.debug("has credential ")
        data_json = requests.post("%s/hascredential/"%self.glint_url,data={"SITE_ID":site_id,"CK_TYPE":ck_type,"USER_ID":self.un,"USER_TOKEN":"%s"%self.token,"USER_TENANT":self.tenant_name},cookies=None).text  
        self.log.debug(data_json)
        data_obj = json.loads(data_json)
        return data_obj

    def addCredential(self, remote_tenant,remote_un,remote_pw,remote_site_id):
        self.log.debug("add credential ")
        data_json = requests.post("%s/addcredential/"%self.glint_url,data={"CREDDATA":json.dumps({"tenent":remote_tenant,"username":remote_un,"password":remote_pw,"site_id":remote_site_id}),"USER_ID":self.un,"USER_TOKEN":"%s"%self.token,"USER_TENANT":self.tenant_name},cookies=None).text  
        self.log.debug(data_json)
        data_obj = json.loads(data_json)
        return data_obj
    
    
    
    
    
    
    