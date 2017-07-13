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
    allowed_domains = ['funes.uniandes.edu.co']
    start_urls = ['http://funes.uniandes.edu.co/']

    rules = [Rule(LxmlLinkExtractor(allow=(), allow_domains = 'funes.uniandes.edu.co', process_value = formatLink), 'parse_items', follow =True)]
    
    def parse_items(self, response):
        item = HttpScrapperItem()
        item["url"] = response.url
        item["status"] = response.status
        return item

