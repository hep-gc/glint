'''
Created on Mar 26, 2015

@author: ronaldjosephdesmarais
'''
import logging,yaml

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
        cfg_f = yaml.load( open("%s"%glint_cfg,'r') )
        self.glint_url=cfg_f['glint_url']
        self.auth_url=cfg_f['auth_url']
        self.un=cfg_f['keystone_un']
        self.pw=cfg_f['keystone_pw']
        self.tenant_id=cfg_f['keystone_tenant_id']
        self.log.debug("Configuring glint api with %s:%s:%s:%s:%s"%(self.glint_url,self.auth_url,self.un,self.pw,self.tenant_id))
        
        #use keystone client un and pw to get an auth token 
        keystone = ksclient.Client(auth_url=self.auth_url, username=self.un, password=self.pw, tenant_id=self.tenant_id)
        self.token = keystone.auth_ref['token']['id']
        self.log.debug("Received token %s"%self.token)
        

    
    
    
    
    
    
    