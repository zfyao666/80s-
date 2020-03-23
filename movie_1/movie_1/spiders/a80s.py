# -*- coding: utf-8 -*-
import scrapy
from movie_1.items import Movie1Item
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from movie_1.items import Movie1Item


class A80sSpider(CrawlSpider):
    name = '80s'
    allowed_domains = ['www.80s.tw']

    def start_requests(self):
        for page in range(1, self.settings.get('MAX_PAGE')+1):
            url = 'https://www.80s.tw/movie/list/-----p/{page}'.format(page=page)
            yield scrapy.Request(url=url, )

    rules = (
        Rule(LxmlLinkExtractor(
            allow='/movie/\d+',
            restrict_css='#block3 > div.clearfix.noborder.block1 > ul.me1.clearfix > li > a'
        ), callback='parse_detail'),
    )

    def parse_detail(self, response):
        item = Movie1Item()
        item['href'] = response.css(
            '#myform > ul > li.clearfix.dlurlelement.backcolor1 > span.dlname.nm > span > a::attr(href)'
        ).extract_first()
        item['title'] = response.css(
            '#minfo > div.info > h1::text'
        ).extract_first()
        yield item
