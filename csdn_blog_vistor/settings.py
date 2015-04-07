# Scrapy settings for csdn_blog_vistor project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'csdn_blog_vistor'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['csdn_blog_vistor.spiders']
NEWSPIDER_MODULE = 'csdn_blog_vistor.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

