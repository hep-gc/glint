'''
Created on Mar 31, 2015

@author: ronaldjosephdesmarais
'''

titles = {
          "list-sites":[{"header":"Site Name","key":"name"},{"header":"Site URL","key":"url"},{"header":"Cloud Type","key":"type"}],
          }

def get_titles(cmd):
    #read in cfg file to get titles
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
    max=0
    for obj in json:
        print obj
        print "Found %s"%obj["name"]
        size = len(obj[key])
        if max < size:
            max = size
        
    return max
        
        