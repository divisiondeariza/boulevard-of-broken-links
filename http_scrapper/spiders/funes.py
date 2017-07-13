# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders.crawl import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from http_scrapper.items import HttpScrapperItem

def formatLink(link):
    if link[-1] == "/":
        return link[0:-1]
    return link

class FunesSpider(CrawlSpider):
    name = 'funes'
    domain = 'funes.uniandes.edu.co'
    allowed_domains = [domain]
    start_urls = ['http://' + domain + '/']

    rules = [Rule(LxmlLinkExtractor(allow=(), allow_domains = domain, process_value = formatLink), 'parse_items', follow =True)]
    
    def parse_items(self, response):
        item = HttpScrapperItem()
        item["url"] = response.url
        item["status"] = response.status
        return item

