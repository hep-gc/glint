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
        self.parser.add_argument("-cfgfile",nargs=1)
        self.parser.add_argument("-version",nargs=1)
        self.parser.add_argument("-tenant",nargs=1)
        self.parser.add_argument("-image_name",nargs='*')
        self.parser.add_argument("-list_images",nargs=0)
        
        
    def init_backup_arg_parser(self):
        self.parser.add_argument("-cfgfile",nargs=1)    

    