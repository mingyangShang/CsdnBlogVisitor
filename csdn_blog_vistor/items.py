# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class CsdnBlogItem(Item):
    # define the fields for your item here like:
    title = Field(); #title
    link = Field();  #url link
    vistorCount = Field(); #number of vistor
    commentCount = Field(); #number of comment

