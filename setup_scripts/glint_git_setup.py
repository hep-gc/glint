#!/usr/bin/python

glint_lib_directory='/var/lib/glint'
horizon_git_repo='https://github.com/rd37/horizon'
glint_git_repo='https://github.com/hep-gc/glint.git'

import sys,subprocess
def proceed(msg):
    print msg
    input = raw_input()
    if input == '' or input == 'y' or input == 'Y':
       return True
    return False

def execute_command(cmd_args):
    process = subprocess.Popen(cmd_args,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out,err = process.communicate()
    if err:
        print "warning: %s"%err
    return out,err

def check_dependencies():
    print "dependency check: check if git and user glint exist"
    [out,err] = execute_command(['which','git'])
    if "no git" in out:
        print "Error, unable to find git tool, please install and attempt glint install again"
        return False
    [out,err] = execute_command(['grep','glint','/etc/passwd'])
    if out == '':
        print "Warning, unable to find system user glint"
        if proceed('Do you wish to setup glint as a User? [Y,n]'):
            print "Ok lets setup glint user "
            [out,err] = execute_command(['python','glint_system_create_user.py','create-glint-user'])
            if err:
                print "Unable to create glint user"
                return False
            #print "out: %s"%out
            return True
        else:    
            return False

    return True 

def download_horizon():
    print "download horizon using git clone"
    [out,err] = execute_command(['git','clone','%s'%horizon_git_repo,'%s/horizon'%glint_lib_directory])
    if err:
        print "Unable to git clone glint-horizon "
        return False
    print "git clone glint-horizon result %s"%out
    return True

def download_glint():
    print "download glint using git clone"
    [out,err] = execute_command(['git','clone','%s'%glint_git_repo,'%s/glint'%glint_lib_directory])
    if err:
        print "Unable to git clone glint"
        return False
    print "git clone glint result %s"%out
    return True


def install_horizon():
    print "install glint-horizon"

def install_glint():
    print "install glint"

########### Uninstalling glint and and glint-horizon
def remove_glint():
    print "Try Removing Glint Git Repository"
    [out,err] = execute_command(['rm','-rf','/var/lib/glint/glint'])

def remove_glint_horizon():
    print "Try Removing Glint-Horizon Git Repository"
    [out,err] = execute_command(['rm','-rf','/var/lib/glint/horizon'])
    
########### Main Func
def show_usage():
    print "Usage"
    print "INSTALL: python glint_git_setup.py install"
    print "UNINSTALL (glint and glint-horizon): python glint_git_setup.py uninstall"
    print "UNINSTALL (glint): python glint_git_setup.py uninstall glint"
    print "UNINSTALL (glint-horizon): python glint_git_setup.py uninstall glint-horizon"

if len(sys.argv) == 2 or len(sys.argv) == 3:
    if sys.argv[1] == 'install':
        if check_dependencies():
            print "Git and User Glint are OK ... moving along"
            download_horizon()
            download_glint()
            #install_horizon()
            #install_glint()
        else:
            print "Check your Setup, system requirements are the git tool and user glint to exist"
    elif sys.argv[1] == 'uninstall':
        if len(sys.argv) == 3:
            if sys.argv[2] == 'glint':
                remove_glint() 
            elif sys.argv[2] == 'glint-horizon':
                remove_glint_horizon()
            else:
                show_usage()
        else:
            remove_glint()
            remove_glint_horizon()  
    else:
        show_usage()
else:
    show_usage()
