#coding=utf-8
#!/usr/bin/python

__author__ = 'smy'
import  urllib2

def visitUrl(url):
    print 'visiting',url
    try:
        request = urllib2.Request(url)
        request.add_header(key="User-Agent",val="Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36")
        urllib2.urlopen(request)
    except urllib2.HTTPError,e:
        print "HttpError:",e.code
    except urllib2.URLError,e:
        print "UrlError:",e.message
    else:
        print "no error"
    finally:
        print "request completed"

# def visitCsdnBlog():
#     csdnurl = "http://blog.csdn.net/shangmingyang"
#     csdnblogurl = "http://blog.csdn.net/shangmingyang/article/details/44088753"
#     visitUrl(csdnblogurl)
#
# visitCsdnBlog();

