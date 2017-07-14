# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders.crawl import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from http_scrapper.items import HttpScrapperItem
from scrapy.http.request import Request

def formatLink(link):
    if link[-1] == "/":
        return link[0:-1]
    return link

class FunesSpider(CrawlSpider):
    name = 'funes'
#     domain = 'funes.uniandes.edu.co'
#     allowed_domains = [domain]
#     start_urls = ['http://' + domain + '/']
    rules = [Rule(LxmlLinkExtractor(allow=(),  process_value = formatLink), 'parse_items', follow =True)]
    
    def start_requests(self):
        yield Request(url=self.user_input)
    
    def parse_items(self, response):
        item = HttpScrapperItem()
        item["url"] = response.url
        item["status"] = response.status
        return item

