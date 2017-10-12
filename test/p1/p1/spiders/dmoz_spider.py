# -*- coding: utf-8 -*-

import scrapy
from p1.items import P1Item
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#from p1.items import P1Item
class DmozSpider(scrapy.Spider):
    name = "baidu"
    allowed_domains = ["baidu.com"]
    start_urls = ["http://www.8080.net"]

    def parse(self,response):
	    for sel in response.xpath('//head/meta[@charset="UTF-8"]/title'):
			item = P1Item()
			item['title'] = sel.xpath('text()').extract()
			title = sel.xpath('text()').extract()
			print  title
			#link = sel.xpath('a/@href').extract()
		    #desc = sel.xpath('text()').extract()
			yield item
			str = "".join(title)
			print(str)
			filename = response.url.split("/")[-2]
			with open(filename, 'w') as f:
				f.writelines(str)



