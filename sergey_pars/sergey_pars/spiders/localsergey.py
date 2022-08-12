import email
import scrapy


class LocalsergeySpider(scrapy.Spider):
    name = 'localsergey'
    allowed_domains = ['localhost:5000']
    start_urls = ['http://localhost:5000/users']

    def parse(self, response):
        for user in response.css('ol li'):
            yield {
                "user": user.css('li::text').get(),
                "id": int(user.css('li::text').get()[:1]),
                "name": str(user.css('li::text').get())
            }
