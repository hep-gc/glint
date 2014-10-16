#!/usr/bin/python

import sys,subprocess
#user and group id
id=171

def execute_command(cmd_args):
    process = subprocess.Popen(cmd_args,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out,err = process.communicate()
    if err:
        print "warning: %s"%err
    return out,err

def create_group():
    print "Creating Group %s"%id
    [out,err] = execute_command(['groupadd','-g','%s'%id,'glint'])

def add_user():
    print "Adding User %s"%id
    [out,err] = execute_command(['adduser','-s','/sbin/nologin','-b','/var/lib','-g','%s'%id,'-u','%s'%id,'-c','OpenStack Glint Daemons','glint'])

def remove_user():
    print "Removing User %s"%id
    [out,err] = execute_command(['userdel','glint'])
    [out,err] = execute_command(['rm','-rf','/var/lib/glint'])
    [out,err] = execute_command(['rm','-rf','/var/mail/glint'])

def show_usage():
    print "USAGE"
    print "CREATE_USER: python system_create_user.py create-glint-user"
    print "REMOVE_USER: python system_create_user.py remove-glint-user"

if len(sys.argv) == 2:
    if sys.argv[1] == "create-glint-user":
        create_group()
        add_user()
    elif sys.argv[1] == "remove-glint-user":
        remove_user()
        #remove_group()
    else:
        show_usage()
else:
    show_usage()
