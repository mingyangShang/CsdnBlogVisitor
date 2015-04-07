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

    # thread1 = urlthread.urlthread(1,"shang","shangmingyang");

    for i in range(blogsize):
        newurlthread  = urlthread.urlthread(i,"thread"+str(i),bloglist[i]);
        urlthreadlist.append(newurlthread);
        # urlthreadlist.append(urlthread.urlthread(id=i,name="thread"+str(i)),url=bloglist[i]); #add a urlthread to list

    for i in range(blogsize):
        urlthreadlist[i].start();#start urlthread

# visitCsdnBlog();


