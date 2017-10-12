# -*- coding: utf-8 -*-
import  dmoz_spider
import  urllib2
test_a = dmoz_spider.DmozSpider
url = 'http://www.w3school.com.cn/example/xmle/books.xml'
pc_req = urllib2.Request(url)
#pc_useagent = userAgents.pcUserAgent.get('IE 9.0')
#pc_head =pc_useagent.split(':')[1]
#mobile_useagent = userAgents.mobileUserAgent.get('BlackBerry').split(':')[1]
#mobile_req = req.add_header("User-Agent",)
#pc_req.add_header("User-Agent",pc_head)
pc_html = urllib2.urlopen(pc_req)
title = pc_html.xpath('//div[@class="title"]/a/text()').extract()[0]
#str = pc_html.read()



# -*- coding: utf-8 -*-
import  dmoz_spider
import  urllib2
str='\u8fd8\u662f7\u6708\u521d\u53d1\u751f\u7684\u4e8b\u6545\uff0c\u5f88\u660e\u663e\u7684\u8ffd\u5c3e\uff0c\u4ea4\u8b66\u73b0\u573a\u51fa\u5177\u4e86\u8d23\u4efb\u8ba4\u5b9a\u4e66'
print  str.encode('utf-8')
