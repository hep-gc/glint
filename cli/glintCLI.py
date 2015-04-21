#from api.glint_api import glint_api
import argparse
import logging
import os
import sys,json
import glintViewer as gl_view
#import warnings
#print "path %s"%os.path.dirname(os.path.realpath(__file__))
#print "cwd %s"%os.getcwd()

sys.path.insert(1,'%s'%os.getcwd())
from api.glint_api import glint_api

def env(*vars, **kwargs):
    """ Try to find the first environnental variable in vars,
        if successful return it.
        Otherwise return the default defined in kwargs.

    """
    for v in vars:
        value = os.environ.get(v)
        if value:
            return value
    return kwargs.get('default', '')


class glintCommands(object):

    def __init__(self, parser_class=argparse.ArgumentParser):
        self.parser_class = parser_class
        self.api = glint_api('api.log', 'DEBUG', 'glint_api_cfg.yaml')
        self.copy_delete = self.parser_class(add_help=False)
        self.site_id = self.parser_class(add_help=False)
        self.create_site = self.parser_class(add_help=False)
        self.has_credential = self.parser_class(add_help=False)
        self.add_credential = self.parser_class(add_help=False)

    # create parser for arguments to be inherited by the subcommand subparsers
    def copy_delete_parser(self):

        # used by image copy and image delete
        self.copy_delete.add_argument('--image-name',
                             help='Message used for authentication with the '
                                  'OpenStack Identity service. ')

        self.copy_delete.add_argument('--image-source-site',
                             help='Message used for authentication with the '
                                  'OpenStack Identity service. ')

    def site_id_parser(self):

        # used by delete-site, delete-credential, get-credential, and has-credential
        self.site_id.add_argument('--site-id',
                             default=env('SITE_ID'),
                             help='Site ID used for authentication with the '
                                  'OpenStack Identity service. '
                                  'Defaults to env[SITE_ID].')
    
    def create_site_parser(self):
        # used by create-site
        self.create_site.add_argument('--name',
                             help='Site data used for authentication with the '
                                  'OpenStack Identity service. ')

        self.create_site.add_argument('--url',
                             help='Site data used for authentication with the '
                                  'OpenStack Identity service. ')

        self.create_site.add_argument('--format',
                             help='Site data used for authentication with the '
                                  'OpenStack Identity service. ')

    def has_credential_parser(self):
        # used by has-credential
        self.has_credential.add_argument('--ck-type',
                             default=env('CK_TYPE'),
                             help='CK type used for authentication with the '
                                  'OpenStack Identity service. '
                                  'Defaults to env[CK_TYPE].')

    def add_credential_parser(self):
        # used-by add-credential
        self.add_credential.add_argument('--remote-tenant',
                             help='Credential data used for authentication with the '
                                  'OpenStack Identity service. ')

        self.add_credential.add_argument('--remote-username',
                             help='Credential data used for authentication with the '
                                  'OpenStack Identity service. ')

        self.add_credential.add_argument('--remote-password',
                             help='Credential data used for authentication with the '
                                  'OpenStack Identity service. ')

        self.add_credential.add_argument('--remote-site-id',
                             help='Credential data used for authentication with the '
                                  'OpenStack Identity service. ')
         
    
    # default funtions for subcommand parsers to make calls to the glint API

    def getImages(self, args):
        data = self.api.getImages()
        gl_view.cli_view(data,"get-images")

    def imageCopy(self, args):
        data = self.api.imageCopy(args.image_name,args.image_source_site,[args.image_destination_site])
        gl_view.cli_view([data],"image-copy")

    def imageDelete(self, args):
        data = self.api.imageDelete(args.image_name,args.image_source_site,args.image_source_tenant)
        gl_view.cli_view([data],"image-delete")

    def listSites(self, args):
        data = self.api.listSites()
        list_data = []
        for site in data:
            json_obj = json.loads(site)
            list_data.append(json_obj)
        #print list_data
        gl_view.cli_view(list_data,"list-sites")

    def deleteSite(self, args):
        if args.site_id == '':
            print ''
            print 'Command "glint delete-site" requires either varibale SITE_ID or argument --site-id'
            print ''
        else:
            data = self.api.deleteSite(args.site_id)
            gl_view.cli_view([data],"delete-site")

    def createSite(self, args):
        data = self.api.createSite(args.name,args.url,args.format)
        gl_view.cli_view([data],"create-site")

    def deleteCredential(self, args):
        if args.site_id == '':
            print ''
            print 'Command "glint delete-credential" requires either varibale SITE_ID or argument --site-id'
            print ''
        else:
            data = self.api.deleteCredential(args.site_id)
            gl_view.cli_view([data],"delete-credential")

    def getCredential(self, args):
        if args.site_id == '':
            print ''
            print 'Command "glint get-credential" requires either varibale SITE_ID or argument --site-id'
            print ''
        else:
            data = self.api.getCredential(args.site_id)
            gl_view.cli_view([data],"get-credential")

    def hasCredential(self, args):
        if (args.site_id  == '') and (args.ck_type == ''):
            print ''
            print 'Command "glint has-credential" requires either varibales SITE_ID and CK_TYPE or arguments --site-id and --ck-type'
            print ''
        elif args.site_id == '':
            print ''
            print 'Command "glint has-credential" requires either varibale SITE_ID or agument --site-id'
            print ''
        elif args.ck_type == '':
            print ''
            print 'Command "glint has-credential" requires either varibale CK_TYPE or a    gument --ck-type'
            print ''
        else:
            data = self.api.hasCredential( args.site_id, args.ck_type)
            gl_view.cli_view([data],"has-credential")

    def addCredential(self, args):
        #return self.api.addCredential(args.remote_tenant,args.remote_username,args.remote_password,args.remote_site_id)
        data = self.api.addCredential(args.remote_tenant,args.remote_username,args.remote_password,args.remote_site_id)
        gl_view.cli_view([data],"add-credential")



    def get_sub_command_parser(self):
        # create a new parser
        parser = self.parser_class(
                prog='glint',
                parents=[self.copy_delete, self.site_id,
                        self.create_site, self.has_credential,
                        self.add_credential],
                epilog='Type "glint COMMAND --help" '
                        'for help on a specific command.'
        )
                
        
        # create a subparser instance for the new parser
        subparser = parser.add_subparsers()
        

        # subparsers to handle subcommands and inherit argument parsing

        # get-images
        parser_getImages = subparser.add_parser('get-images',
                                                help='Display all user images')
        parser_getImages.set_defaults(func=self.getImages)

        
        # image-copy
        parser_image_copy = subparser.add_parser('image-copy',
                                           parents=[self.copy_delete],
                                           help='Copy user image to specified\
                                                 site')
        parser_image_copy.add_argument('--image-destination-site',
                                           help='Message used for authentication with the '
                                                'OpenStack Identity service. ')
        parser_image_copy.set_defaults(func=self.imageCopy)


        # image-delete
        parser_image_delete = subparser.add_parser('image-delete',
                                                 parents=[self.copy_delete],
                                                 help='Delete specified user\
                                                       image')
        parser_image_delete.add_argument('--image-source-tenant',
                                                 help='Message used for authentication with the '
                                                 'OpenStack Identity service. ')

        parser_image_delete.set_defaults(func=self.imageDelete)



        # list-sites 
        parser_listSites = subparser.add_parser('list-sites',
                                                 help='List all user sites')
        parser_listSites.set_defaults(func=self.listSites)


        # delete-site
        parser_deleteSite = subparser.add_parser('delete-site',
                                                 parents=[self.site_id],
                                                 help='Delete specified user\
                                                       site')
        parser_deleteSite.set_defaults(func=self.deleteSite)


        # create-site
        parser_createSite = subparser.add_parser('create-site',
                                                 parents=[self.create_site],
                                                 help='Create new user site')
        parser_createSite.set_defaults(func=self.createSite)


        # delete-credential 
        parser_deleteCredential = subparser.add_parser('delete-credential',
                                                 parents=[self.site_id],
                                                 help='Delete specified user\
                                                       credential')
        parser_deleteCredential.set_defaults(func=self.deleteCredential)


        # get-credential 
        parser_getCredential = subparser.add_parser('get-credential',
                                                 parents=[self.site_id],
                                                 help='Display user\
                                                       credential for\
                                                       specified site')
        parser_getCredential.set_defaults(func=self.getCredential)


        # has-credential
        parser_hasCredential = subparser.add_parser('has-credential',
                                                 parents=[self.site_id, self.has_credential],
                                                 help='has credential help')
        parser_hasCredential.set_defaults(func=self.hasCredential)


        # add-credential
        parser_addCredential = subparser.add_parser('add-credential',
                                                 parents=[self.add_credential],
                                                 help='add credential help')
        parser_addCredential.set_defaults(func=self.addCredential)

        return parser
    
    def get_parsers(self):
        self.copy_delete_parser()
        self.site_id_parser()
        self.create_site_parser()
        self.has_credential_parser()
        self.add_credential_parser()

    def main(self, argv):
        # initialize the parser to be inherited
        self.get_parsers()

        # setup subcommand parser and check for arguments
        subcommand_parser = self.get_sub_command_parser()
        if not argv:
            subcommand_parser.print_help()
        else:
            # parse the args and call the handler function 
            command_args = subcommand_parser.parse_args(argv)
            print command_args.func(command_args)
            

def main():
    glintCommands().main(sys.argv[1:])

if __name__=="__main__":
    sys.exit(main())
