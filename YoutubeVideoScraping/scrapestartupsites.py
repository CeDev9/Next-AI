import scrapy


class MassChallengeSpider(scrapy.Spider):
    name = 'startupsites'
    start_urls = [
        'https://masschallenge.org/startups',
    ]

    def parse(self, response):
        startup_page_links = response.css('.startup a::attr("href")')
        print(startup_page_links)
        yield from response.follow_all(startup_page_links, self.parse_startup)

        pagination_links = response.css('.page-item:last-child a::attr(href)')
        print("pagination_links",pagination_links)
        yield from response.follow_all(pagination_links, self.parse)

    def parse_startup(self, response):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        yield {
            'startupname': extract_with_css('.startup-detail .card-title::text'),
            'industry':  response.css('.startup-detail .industry-items p::text').getall(),
            'year': extract_with_css('.startup-detail .lead::text'),
            'description': extract_with_css('.startup-detail .startup-fullelevatorpitch::text'),
            'short-description': extract_with_css('.startup-detail .startup-tweetablepitch::text'),
            'links': response.css('.startup-detail .startup-links a::attr(href)').getall(),
            'youtubelink': extract_with_css('.ytp-title-link::attr(href)'),
            'youtubetitle': extract_with_css('.ytp-title-link::text'),
        }

from time import time

class YCSpider(scrapy.Spider):
    name = 'ycombinator'
    start_urls = [
        'https://masschallenge.org/startups',
    ]

    def parse(self, response):

        SCROLL_PAUSE_TIME = 20

        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        startup_page_links = response.css('.startup a::attr("href")')
        print(startup_page_links)
        yield from response.follow_all(startup_page_links, self.parse_startup)

        pagination_links = response.css('.page-item:last-child a::attr(href)')
        print("pagination_links",pagination_links)
        yield from response.follow_all(pagination_links, self.parse)

    def parse_startup(self, response):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        yield {
            'startupname': extract_with_css('.startup-detail .card-title::text'),
            'industry':  response.css('.startup-detail .industry-items p::text').getall(),
            'year': extract_with_css('.startup-detail .lead::text'),
            'description': extract_with_css('.startup-detail .startup-fullelevatorpitch::text'),
            'short-description': extract_with_css('.startup-detail .startup-tweetablepitch::text'),
            'links': response.css('.startup-detail .startup-links a::attr(href)').getall(),
            'youtubelink': extract_with_css('.ytp-title-link::attr(href)'),
            'youtubetitle': extract_with_css('.ytp-title-link::text'),
        }