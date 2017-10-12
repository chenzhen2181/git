# encoding:UTF-8

import scrapy
#from p1.items import P1Item
class DmozSpider(scrapy.Spider):
    name = "baidu"
    allowed_domains = ["baidu.com"]
    start_urls = "http://www.cnblogs.com/xieshengsen/p/6727064.html"

    def parse(self, response):

	    for sel in response.xpath('//div[@class="postBody"]//pre'):
		    title = sel.xpath('text()').extract()
		    #link = sel.xpath('a/@href').extract()
		    #desc = sel.xpath('text()').extract()
		    print  title, type(title)
		    filename = response.url.split("/")[-2]
		    with open(filename, 'w') as f:
			    for i in title:
			        f.write(i)


