# -*- coding: utf-8 -*-
import scrapy
import sys
from doubanmoive.items import DoubanmoiveItem
reload(sys)
sys.setdefaultencoding('utf-8')
class DbbookSpider(scrapy.Spider):
    name = "dbbook"
    #allowed_domains = ["https://www.douban.com/doulist/1264675/"]
    start_urls = (
        'https://www.douban.com/doulist/1264675/',
    )

    def parse(self, response):
        #print response.body
        selector = scrapy.Selector(response)
        book = selector.xpath('//div[@class="doulist-collect"]')
        items = DoubanmoiveItem()
        for each in book:
            title = each.xpath('//div[@class="title"]/a/text()').extract()
            rate = each.xpath('//div[@class="rating"]/span[@class="rating_nums"]/text()').extract()
            author = each.xpath('//div[@class="abstract"]/text()').extract()
            title = ','.join(title)
            rate = ','.join(rate)
            author = ','.join(author)
            title = title.replace(' ', '').replace('\n', '')
            rate = rate.replace(' ', '').replace('\n', '')
            author = author.replace(' ', '').replace('\n', '')
            items['title'] = title
            items['rate'] = rate
            items['author'] = author
            #print  title,rate,author
            yield items
        nextpage = selector.xpath('//span[@class="next"]/link/@href').extract()
        print nextpage
        if nextpage:
            next = nextpage[0]
            print next
            yield scrapy.http.Request(next,callback=self.parse)

