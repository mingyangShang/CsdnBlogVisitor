#coding=utf-8
from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.selector import Selector
import csdn_blog_vistor.urlthread
from csdn_blog_vistor.items import CsdnBlogItem

__author__ = 'smy'

class CsdnBlogSpider(Spider):

    csdn_root_url = "http://blog.csdn.net"
    my_csdn_blog_url = "http://blog.csdn.net/shangmingyang"
    blogs = []

    name = "csdn_blog"
    download_delay = 1
    allowed_domains = ["blog.csdn.net"]
    start_urls = [my_csdn_blog_url]

    # parse the response of csdnblog request
    def parse(self, response):
        print "finished";
        for sel in response.xpath('//div[@class="list_item article_item"]'):
            csdnblog = CsdnBlogItem();
            csdnblog['title'] = sel.xpath('div[@class="article_title"]/h1/span/a/text()').extract()
            csdnblog["link"] = sel.xpath('div[@class="article_title"]/h1/span/a/@href').extract()
            csdnblog["vistorCount"] = sel.xpath('div[@class="article_manage"]/span[@class="link_view"]/text()').extract()
            csdnblog["commentCount"] = sel.xpath('div[@class="article_manage"]/span[@class="link_comments"]/text()').extract()
            self.blogs.append(csdnblog)

        # find the next page and scrapy it
        next_page = None
        for sel in response.xpath('//div[@class="pagelist"]/a'):
            if(sel.xpath('text()').extract()[0] == u'下一页'):
                next_page = sel.xpath("@href")[0].extract()
                break

        # if have pagelist ,then imporve has the next page,visit it,else visit allurls
        if next_page :
            yield Request(self.wrapUrl(next_page),callback=self.parse)
        else:
            self.visit_csdn_blog()

    def visit_csdn_blog(self):
        urls = [];
        for i in range(len(self.blogs)):
            urls.append(self.csdn_root_url+self.blogs[i]["link"][0])
        csdn_blog_vistor.urlthread.urlthread(0,"csdn_blog_thread",urls).start()

    def wrapUrl(self,page):
        return self.csdn_root_url + page
