import scrapy


class MirFactovSpider(scrapy.Spider):
    name = "mir_factov"
    main_url = 'http://mirfactov.com/page/'

    def start_requests(self):
        for i in range(0, 400):
            url = self.main_url + str(i)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        titles = response.css('div.contentbox').css('h2.style1').css('a::text').getall()
        titles = list(map(lambda x: x.strip('\n '), titles))

        for text in titles:
            yield {'title': text}
