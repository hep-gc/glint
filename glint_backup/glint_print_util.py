'''
Created on Nov 25, 2014

@author: ronaldjosephdesmarais
'''

def print_line(cols):
    #for col in cols:
    print "+%s+%s+%s+%s+%s+%s"%('-'*cols[0],'-'*cols[1],'-'*cols[2],'-'*cols[3],'-'*cols[4],'-'*cols[5])
    
def print_line_title(titles):
    print "|%s|%s|%s|%s|%s|%s|"%(titles[0],titles[1],titles[1],titles[2],titles[3],titles[4],titles[5])