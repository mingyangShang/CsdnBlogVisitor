#coding=utf-8
#!/usr/bin/python

__author__ = 'smy'
import urlthread;
import visiting;

def visitCsdnBlog():
    bloglist = ["http://blog.csdn.net/shangmingyang/article/details/44088753",
                "http://blog.csdn.net/shangmingyang/article/details/44704787"];
    blogsize = len(bloglist); #the length of blogs

    urlthreadlist = [];

    for i in range(blogsize):
        newurlthread  = urlthread.urlthread(i,"thread"+str(i),bloglist[i]);
        urlthreadlist.append(newurlthread);

    for i in range(blogsize):
        urlthreadlist[i].start();#start urlthread

# visitCsdnBlog();


