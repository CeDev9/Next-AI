import scrapy
import scrapy
from scrapy_selenium import SeleniumRequest
import json


class YcombinatorSpider(scrapy.Spider):
    name = 'ycombinator'
    allowed_domains = ['ycombinator.com']
    start_urls = ['http://ycombinator.com/']

    def parse(self, response):
        """parse data from urls"""
        print(response.css('a'))
        script = 'var last_height = 0;var current_height = document.body.scrollHeight; while(current_height>last_height){last_height=current_height;window.scrollTo(0, document.body.scrollHeight);await new Promise(r => setTimeout(r, 2000));current_height=document.body.scrollHeight;}'

        yield SeleniumRequest(url='http://ycombinator.com/companies', callback=self.parse_all, script=script)
    
    def parse_all(self, response):
        startup_page_links = response.css(
            'a.no-hovercard::attr(href)')
        print(startup_page_links)
        script = 'var last_height = 0;var current_height = document.body.scrollHeight; while(current_height>last_height){last_height=current_height;window.scrollTo(0, document.body.scrollHeight);await new Promise(r => setTimeout(r, 2000));current_height=document.body.scrollHeight;}'

        for link in startup_page_links:
            linktext = 'http://ycombinator.com/' + link.get().strip()
            yield SeleniumRequest(url=linktext, callback=self.parse_startup,  script=script)

    def parse_startup(self, response):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()
        print('IN FUNCTION')
        print(response.url)
        yield {
            'title': response.css('h1.headline__text::text').get().strip(),
            'byline': (" ".join([s.strip() for s in response.css('div.byline ::text').getall()])).strip(),
            'link': response.url,
            'content': [s.strip() for s in response.css('div.article__content-container p::text').getall()],
        }
