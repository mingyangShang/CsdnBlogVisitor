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
            for i in range(len(self.urls)):
                visiting.visitUrl(self.urls[i])
            time.sleep(20)
        print "endThread"

# def testThread():
#     thread1 = urlthread(id=1,name="thread1",url="http://blog.csdn.net/shangmingyang/article/details/44088753")
#     thread2 = urlthread(id=2,name="thread2",url="http://blog.csdn.net/shangmingyang/article/details/44704787")
#     thread1.start()
#     thread2.start()

# testThread();