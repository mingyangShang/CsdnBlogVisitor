import csdn_blog_vistor.urlthread
from scrapy.spider import Spider
from scrapy.selector import Selector
from csdn_blog_vistor.items import CsdnBlogItem

__author__ = 'smy'

class CsdnBlogSpider(Spider):

    csdn_root_url = "http://blog.csdn.net"
    my_csdn_blog_url = "http://blog.csdn.net/shangmingyang"
    blogs = []

    name = "csdn_blog"
    allowed_domains = ["blog.csdn.net"]
    start_urls = [my_csdn_blog_url]

    # parse the response of csdnblog request
    def parse(self, response):
        print "finished";
        for sel in response.xpath('//div[@class="list_item article_item"]'):
            csdnblog = CsdnBlogItem();
            csdnblog['title'] = sel.xpath('div[@class="article_title"]/h1/span/a/text()').extract();
            csdnblog["link"] = sel.xpath('div[@class="article_title"]/h1/span/a/@href').extract();
            csdnblog["vistorCount"] = sel.xpath(
                'div[@class="article_manage"]/span[@class="link_view"]/text()').extract();
            csdnblog["commentCount"] = sel.xpath(
                'div[@class="article_manage"]/span[@class="link_comments"]/text()').extract();
            self.blogs.append(csdnblog)

        self.visit_csdn_blog()


    def visit_csdn_blog(self):
        urls = [];
        for i in range(len(self.blogs)):
            urls.append(self.csdn_root_url+self.blogs[i]["link"][0])
        csdn_blog_vistor.urlthread.urlthread(0,"csdn_blog_thread",urls).start()

