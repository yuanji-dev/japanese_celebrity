# -*- coding: utf-8 -*-
import scrapy


class PasonicaSpider(scrapy.Spider):

    name = 'pasonica'
    allowed_domains = ['www.pasonica.com']
    download_delay = 1

    def start_requests(self):
        for year in range(2000, 1910, -10):
            for gender in ('女', '男'):
                url = 'https://www.pasonica.com/{}性芸能人-{}年代誕生/'.format(gender, year)
                yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for div in response.css('.thumb_sq2'):
            for link in div.css('a'):
                profile_url = link.attrib.get('href')
                yield response.follow(url=profile_url, callback=self.parse_celebrity)

    def parse_celebrity(self, response):
        name = response.css('h2::text').get()
        image = response.css('.j-blog-post--header + div img').attrib.get('src', '')
        intro = ''.join(response.css('.j-module.n.j-text p::text').getall())
        self.log('GET {}'.format(name))
        return dict(name=name, image=image, intro=intro)
