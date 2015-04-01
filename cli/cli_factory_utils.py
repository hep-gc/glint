'''
Created on Mar 31, 2015

@author: ronaldjosephdesmarais
'''

titles = {
          "list-sites":[{"header":"Site Name","key":"name"},{"header":"Site URL","key":"url"},{"header":"Cloud Type","key":"type"}],
          "basic-result":[{"header":"Result of Operation","key":"Result"}],
          "basic-result-creds":[{"header":"Result of Operation","key":"result"}],
          "create-site-result":[{"header":"Result of Operation","key":"Result"},{"header":"site id","key":"site_id"}],
          "get-credential":[{"header":"Credential id","key":"cred_id"},{"header":"Tenant Name","key":"tenant"}],
          "image-operation":[{"header":"Image Operation Thread id","key":"thread_id"}],
          }

def get_titles(cmd):
    return titles[cmd]

def get_max_column_sizes(json,header):
    sizes = [0]*len(header)
    for idx,head in enumerate(header):
        key = head['key']
        max_size = _handle_json_object_array(json,key)
        #if sizes[idx]<max_size:
        sizes[idx]=max_size
    return sizes        
   
def _handle_json_object_array(json,key): 
    _max_size=0
    for obj in json:
        size = len("%s"%obj[key])
        if _max_size < size:
            _max_size = size
        
    return _max_size
        
        