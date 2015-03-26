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
        self.log.debug("getImages ")
        #create web call and wait for return
        data_json = requests.post("%slistsites/"%self.glint_url,data={"USER_ID":self.un,"USER_TOKEN":"%s"%self.token,"USER_TENANT":self.tenant_name},cookies=None).text
        data_obj = json.loads(data_json)
        self.log.debug("Get Images returned %s"%data_obj)
        return data_obj

    def save(self,jsonMsg, USER_TOKEN, USER_TENANT):
        return jsonMsg, USER_TOKEN, USER_TENANT

    def credentials(self,USER_TOKEN, USER_TENANT, USER_ID):
        return USER_TOKEN, USER_TENANT, USER_ID

    def listSites(self,USER_TOKEN, USER_TENANT):
        return USER_TOKEN, USER_TENANT

    def deleteSite(self,USER_TOKEN, USER_TENANT, USER_ID, SITE_ID):
        return USER_TOKEN, USER_TENANT, USER_ID, SITE_ID

    def createSite(self,USER_TOKEN, USER_TENANT, USER_ID, SITEDATA):
        return USER_TOKEN, USER_TENANT, USER_ID, SITEDATA

    def deleteCredential(self,USER_TOKEN, USER_TENANT, USER_ID, SITE_ID):
        return USER_TOKEN, USER_TENANT, USER_ID, SITE_ID

    def getCredential(self,USER_TOKEN, USER_TENANT, USER_ID, SITE_ID):
        return USER_TOKEN, USER_TENANT, USER_ID, SITE_ID

    def hasCredential(self,USER_TOKEN, USER_TENANT, USER_ID, SITE_ID, CK_TYPE):
        return USER_TOKEN, USER_TENANT, USER_ID, SITE_ID, CK_TYPE

    def addCredential(self,USER_TOKEN, USER_TENANT, CREDDATA):
        return USER_TOKEN, USER_TENANT, CREDDATA
    
    
    
    
    
    
    