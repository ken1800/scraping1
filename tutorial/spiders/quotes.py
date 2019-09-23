import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        url ='https://www.goodreads.com/quotes'
        
        yield scrapy.Request(url=url , callback=self.parse)

    def parse(self, response):
        for quote in response.selector.xpath("//div[@class ='quote']"):
            yield{
                'text': quote.xpath(".//div[@class='quoteText']/text()[1]").extract_first(),
                'author':quote.xpath(".//div[@class='quoteText']/child::span").extract_first(),
                'tags':quote.xpath(".//div[@class='greyText smallText left']/a/text()").extract_first(),
            }