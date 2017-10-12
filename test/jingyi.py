# encoding:UTF-8
#import requests
import urllib2
#import BeautifulSoup
import userAgents
import types
import logging
import savefile
import re
url ="http://www.jycinema.com/html/default/index.html"
pc_req = urllib2.Request(url)
pc_useagent = userAgents.pcUserAgent.get('IE 9.0')
pc_head =pc_useagent.split(':')[1]
#mobile_useagent = userAgents.mobileUserAgent.get('BlackBerry').split(':')[1]
#mobile_req = req.add_header("User-Agent",)
pc_req.add_header("User-Agent",pc_head)
pc_html = urllib2.urlopen(pc_req)
str = pc_html.read()
moivelist =re.findall(r'film-title',str)

#savefile('/home/chenzhen2181/git/test/3.html',pc_html,pc_useagent)



