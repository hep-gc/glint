'''
Created on Mar 31, 2015

@author: ronaldjosephdesmarais
'''

titles = {
          "list-sites":[{"header":"Site Name","key":"name"},{"header":"Site URL","key":"url"},{"header":"Cloud Type","key":"type"}],
          "delete-site":[{"header":"Result of Operation","key":"Result"}],
          "delete-credential":[{"header":"Result of Operation","key":"Result"}],
          "add-credential":[{"header":"Result of Operation","key":"Result"}],
          "has-credential":[{"header":"Result of Operation","key":"result"}],
          "create-site":[{"header":"Result of Operation","key":"Result"},{"header":"site id","key":"site_id"}],
          "get-credential":[{"header":"Credential id","key":"cred_id"},{"header":"Tenant Name","key":"tenant"}],
          "image-copy":[{"header":"Image Operation Thread id","key":"thread_id"}],
          "image-delete":[{"header":"Image Operation Thread id","key":"thread_id"}],
          "get-image":[{"header":"","key":"image"}]
          }


def get_titles(cmd):
    return titles[cmd]

def get_image_max_column_sizes(json,header):
    #site_num = len(json['sites'])
    for site in json['sites']:
        header_obj = {"header":site['name']}
        header.append(header_obj)
    #print header
    cols_max=[0]*len(header)
    
    for row in json['rows']:
        if len(row['image']) > cols_max[0]:
            cols_max[0] = len(row['image'])
            
    for idx,head in enumerate(header):
        if len(head['header']) > cols_max[idx]:
            cols_max[idx]=len(head['header'])
    return cols_max
        
def get_max_column_sizes(json,header):
    sizes = [0]*len(header)
    for idx,head in enumerate(header):
        key = head['key']
        max_size = _handle_json_object_array(json,key)
        #if sizes[idx]<max_size:
        if len(head['header']) > max_size:
            max_size = len(head['header'])
        sizes[idx]=max_size
    return sizes        
   
def _handle_json_object_array(json,key): 
    _max_size=0
    for obj in json:
        size = len("%s"%obj[key])
        if _max_size < size:
            _max_size = size
        
    return _max_size
        
        