import os, sys
import cli_factory_utils as fact_utils
def cli_view(json,cmd):
    print "View the Json %s with command %s"%(json,cmd)
    #get titles
    headers = fact_utils.get_titles(cmd)
    print headers
    col_sizes = fact_utils.get_max_column_sizes(json,headers)
    print col_sizes
    

def prettyPrint(json, headers, colum_sizes):
    print "Pretty Print this"


