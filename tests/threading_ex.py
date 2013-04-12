#!/usr/bin/python

import threading

class Example(threading.Thread):

    def run(self):
        ##print '%s from %s' % (self._Thread__args[0],
         #                     self._Thread__args[1])
        L.append(self._Thread__args[0])
        L.append(self._Thread__args[1])
        
L=[]
example = Example(args=["hello","yes",L])
example.start()
example.join()
print L[0] 
print L[1]
