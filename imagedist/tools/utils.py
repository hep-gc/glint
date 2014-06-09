'''
Created on May 15, 2014

@author: rd
'''
import base64

def encode(string,key):
    msg = "%s %s"%(key,string)
    return base64.encodestring(msg)

def decode(string,key):
    msg = base64.decodestring(string)
    return msg.split()[1]
    