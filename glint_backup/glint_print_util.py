'''
Created on Nov 25, 2014

@author: ronaldjosephdesmarais
'''

def print_line(cols):
    #for col in cols:
    print "+%s+%s+%s+%s+%s+%s+"%('-'*cols[0],'-'*cols[1],'-'*cols[2],'-'*cols[3],'-'*cols[4],'-'*cols[5])
    
def print_line_data(data,cols):
    #print titles
    ln=[]
    for idx,d in enumerate(data):
        ln.append(  (cols[idx]-len(d)) /2 )
        if (  (cols[idx]-len(d)) % 2 ) == 0:
            ln.append(  (cols[idx]-len(d)) /2 )
        else:
            ln.append(  (cols[idx]-len(d)) /2 ) +1

    print "|%s%s%s|%s%s%s|%s%s%s|%s%s%s|%s%s%s|%s%s%s|"%(' '*ln[0],data[0],' '*ln[1],' '*ln[2],data[1],' '*ln[3],' '*ln[4],data[2],' '*ln[5],' '*ln[6],data[3],' '*ln[7],' '*ln[8],data[4],' '*ln[9],' '*ln[10],data[5],' '*ln[11])
    
