'''
Created on 2011-04-07

@author: francis
'''

import time
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import SocketServer

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Threaded mix-in
class MultithreadXMLRPCServer(SocketServer.ThreadingMixIn,SimpleXMLRPCServer): pass

def avg(values):
    return sum(values, 0.0) / len(values)

    
def calibrate(target):
    m = 1000000
    samples = []
    for i in range(10):
        t1 = time.time()
        count(m)
        t2 = time.time()
        delay = t2 - t1
        x = int(float(m * target) / (delay))
        samples.append(x)
    
    return int(avg(samples)) 

def count(max):
    ite = 0
    while(True):
        ite += 1
        if (ite >= max):
            break
        
class WKServerInterface(object):
    def __init__(self):
        self.calibration_delay = 2
        self.calibration = calibrate(self.calibration_delay)

    def sleep(self, args):
        print "sleep " + str(args)
        t = args.get("time", None)
        if (t is None):
            return False
        time.sleep(float(t))

    def hog(self, args):
        print "self.calibrate=%s" % (self.calibration)
        print "hog " + str(args)
        t = args.get("time", None)
        if (t is None):
            return False
        c = int(float(t * self.calibration) / self.calibration_delay) 
        count(c)
    
class WKServer(object):
    def __init__(self):
        self.server = None
    def start(self, server, port):
        # Create server
        self.server = MultithreadXMLRPCServer((str(server), int(port)),
                                    requestHandler=RequestHandler)
        self.server.register_introspection_functions()
        self.server.register_instance(WKServerInterface())
        self.server.allow_none = True
        print "server started"
        self.server.serve_forever()