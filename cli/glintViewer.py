import os, sys

import cli_factory_utils as fact_utils

def cli_view(json,cmd):
    print "View the Json %s with command %s"%(json,cmd)
    #get titles
    headers = fact_utils.get_titles(cmd)
    #print headers
    if "%s"%cmd in "get-images":
        col_sizes = fact_utils.get_image_max_column_sizes(json,headers)
    else:
        col_sizes = fact_utils.get_max_column_sizes(json,headers)
    print headers
    print col_sizes
    if "%s"%cmd in "get-images":
        prettyPrintGetImages(json,headers,col_sizes)
    else:
        prettyPrint(json,headers,col_sizes)

def prettyPrintGetImages(json,headers,colum_sizes):
    #print "implemnt htis"
    print line(colum_sizes)
    print header(headers,colum_sizes)
    print line(colum_sizes)
    for row in json['rows']:
        row_data=[row['image']]
        for col_site in json['sites']:
            found=False
            for image_site in row['sites']:
                if col_site['name'] == image_site['name']:
                    found=True
            if found:
                row_data.append("X")
            else:
                row_data.append("")
        printRow(row_data,colum_sizes)
    print line(colum_sizes)

def printRow(row_data,col_sizes):
    line = "|"
    for idx,col_size in enumerate(col_sizes):
        data_len = len(row_data[idx])
        line+=' '
        line+=row_data[idx]
        line+=' '*(col_size-data_len)
        line+=" |"
    print line
    
def prettyPrint(json, headers, colum_sizes):
    print_line = line(colum_sizes)
    print print_line
    print header(headers, colum_sizes)
    print print_line
    content = body(json, headers, colum_sizes)
    for content_line in content:
        print content_line
    print print_line

def line(colum_sizes):
    rtn_line = '+'
    for colum in colum_sizes:
        rtn_line += '-'*(colum+2)
        rtn_line += '+'
    return rtn_line


def header(headers, colum_sizes):
    rtn_header = '|'
    for header, colum in zip(headers, colum_sizes):
        rtn_header += ' ' + header['header']
        rtn_header += ' '*(colum-len(header['header'])+1)
        rtn_header += '|'
    return rtn_header


def body(json, headers, colum_sizes):
    rtn_lines = []
    for item in json:
        tmp_line = '|'
        for header, colum in zip(headers, colum_sizes):
            tmp_line += ' ' + str(item[header['key']])
            tmp_line += ' '*(colum-len(str(item[header['key']]))+1)
            tmp_line += '|'
        rtn_lines.append(tmp_line)
    return rtn_lines
