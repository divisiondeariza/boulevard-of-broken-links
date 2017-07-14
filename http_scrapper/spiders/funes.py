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
    allowed_domains = []
    handle_httpstatus_all = True
    rules = [Rule(LxmlLinkExtractor(allow=(),  process_value = formatLink), 'parse_items', follow =True)]
    
    def __init__(self, *args, **kwargs):
        super(FunesSpider, self).__init__(*args, **kwargs)
        self.allowed_domains.append(self.domain)

    def start_requests(self):
        yield Request(url= 'http://' + self.domain + '/')
    
    def parse_items(self, response):
        item = HttpScrapperItem()
        item["url"] = response.url
        item["status"] = response.status
        return item

