'''
Created on 2011-04-07

@author: francis
'''

import xmlrpclib

class WKClient(object):
    
    def __init__(self):
        self.proxy = None
        
    def set_proxy(self, server, port):
        self.proxy = xmlrpclib.ServerProxy('http://' + str(server) + ":" + str(port))
        
    def run_command(self, cmd, args):
        func = getattr(self.proxy, cmd)
        func(args)

