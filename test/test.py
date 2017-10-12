# encoding:UTF-8
#import requests
import urllib2
#import BeautifulSoup
import userAgents
import types
import logging
import savefile
#f = open('/home/chenzhen2181/git/test/1.txt', 'w')

url ="http://www.baidu.com"
pc_req = urllib2.Request(url)
pc_useagent = userAgents.pcUserAgent.get('IE 9.0')
pc_head =pc_useagent.split(':')[1]
#mobile_useagent = userAgents.mobileUserAgent.get('BlackBerry').split(':')[1]
#mobile_req = req.add_header("User-Agent",)
pc_req.add_header("User-Agent",pc_head)
pc_html = urllib2.urlopen(pc_req)

savefile.savefile('/home/chenzhen2181/git/test/3.html',pc_html,pc_useagent)



