import scrapy


class YCSpider(scrapy.Spider):
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