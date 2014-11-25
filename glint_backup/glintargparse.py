'''
Created on Nov 20, 2014

@author: ronaldjosephdesmarais
'''
import argparse

class GlintArgumentParser:
    parser=None
 
    def __init__(self):
        print "Init GlintArgumentParser"
        self.parser = argparse.ArgumentParser(description='Glint\'s Backup Argument Parser')
   
    def init_restore_arg_parser(self):
        self.parser.add_argument("-c","--cfgfile",nargs=1,help="Required Configuration File for restore or uses default")
        self.parser.add_argument("-v","--version",nargs=1,help="This Parameter is required or tool will fail")
        self.parser.add_argument("-t","--tenant",nargs=1,help="Specify a tenant directory you wish to restore, rather than all tenants of a versioning")
        self.parser.add_argument("-i","--image-name",nargs='*',help="Used with the --tenant option if you wish to restore a single image from a tenant")
        self.parser.add_argument("-l","--list-images",action='store_true',help="Used with --tenant to list images in a tenant at the specifed --version")
        
        
    def init_backup_arg_parser(self):
        self.parser.add_argument("-cfgfile",nargs=1)    

    