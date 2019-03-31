# -*- coding: utf-8 -*-
import re
from contextlib import closing

import scrapy
from scrapy import Spider, FormRequest, Request
import requests


class WallpaperSpider(Spider):
    name = 'wallpaper'
    start_urls = 'https://alpha.wallhaven.cc/search?q=4k&categories=000&purity=100&atleast=3840x2160&sorting=relevance&order=desc&page=2'
    def start_requests(self):
        for i in range(10):
            start_urls = 'https://alpha.wallhaven.cc/random?page=%d'% (i+1)

            yield FormRequest(start_urls,callback=self.get_image)

    def get_image(self,response):
        urls = response.xpath('//li/figure/a/@href').extract()
        print(len(urls))
        for url in urls:
            print(url)
        # url = 'https://alpha.wallhaven.cc/wallpaper/593940'
            yield Request(url,callback=self.download_url)
    def download_url(self,response):
        url = response.xpath('//img[@id="wallpaper"]/@src').extract()
        print(len(url))

        # yield FormRequest("https:"+url,callback=self.download)
        print(url[0])
        titlr = re.findall("-(\d+).",url[0])
        print(titlr[0])

        with closing(requests.get(url='https:'+url[0], stream=True, verify=False)) as r:
            with open(str('download/'+titlr[0])+'.jpg', 'ab+') as f:
                f.write(r.content)
                # for chunk in r.iter_content(chunk_size=2048):
                #     if chunk:
                #         f.write(chunk)
                #         f.flush()


