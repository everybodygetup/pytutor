import scrapy


class LocalSpider(scrapy.Spider):
    name = 'local'
    allowed_domains = ['']
    start_urls = ['http://localhost:5000/users']

    def parse(self, response):
        for user in response.css('.major ul li'):
            yield {
                'id': user.css('b::text').get(),
                'name': user.css('li::text').re(r'([a-zA-Zа-яА-ЯёЁ0-9\ ]+) \(([a-z@\-\.]+)\)')[0].strip() if user.css('li::text').re(r'(\w+) \(([a-z@\-\.]+)\)') else None,
                'email': user.css('li::text').re(r'\(([a-z@\-\.]+)\)')[0],
            }
