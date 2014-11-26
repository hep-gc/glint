'''
Created on Nov 25, 2014

@author: ronaldjosephdesmarais
'''

def print_line(cols):
    #for col in cols:
    print "+%s+%s+%s+%s+%s+%s+"%('-'*cols[0],'-'*cols[1],'-'*cols[2],'-'*cols[3],'-'*cols[4],'-'*cols[5])
    
def print_line_data(data,cols):
    #print titles
    print "| %s | %s | %s | %s | %s | %s |"%(data[0],data[1],data[2],data[3],data[4],data[5])
    
