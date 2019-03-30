# -*- coding: utf-8 -*-
import scrapy


class WallpaperSpider(scrapy.Spider):
    name = 'wallpaper'
    allowed_domains = ['wallpaper.com']
    start_urls = ['http://wallpaper.com/']

    def parse(self, response):
        pass
