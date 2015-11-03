#coding=utf-8
#!/usr/bin/python
__author__ = 'smy'

import threading
import time
import visiting

class urlthread(threading.Thread):
    def __init__(self,id,name,urls):
        threading.Thread.__init__(self);
        self.id = id
        self.name = name
        self.urls = urls

    def run(self):
        print "startThread"
        while(True):
            map(visiting.visitUrl,self.urls)
            time.sleep(5)
        print "endThread"
