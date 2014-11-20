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
   
    def init_backup_arg_parser(self):
        self.parser.add_argument("-version")
        #self.parser.add_argument("-install",nargs=1,choices=['all','glint','horizon'])
        #self.parser.add_argument("-uninstall",nargs=1,choices=['all','glint','horizon'])
        #self.parser.add_argument("-glint_url")
        #self.parser.add_argument("-glint_hor_url")
        #self.parser.add_argument("-glint_inst_type")
        #self.parser.add_argument("-hor_inst_type")
        #self.parser.add_argument("-glint_server",nargs=1,choices=['django','paste'])
        #self.parser.add_argument("-glint_horizon_server",nargs=1,choices=['django','apache'])
        #self.parser.add_argument("-glint_user_id")

    