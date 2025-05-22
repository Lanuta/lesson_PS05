import scrapy
import csv

class SvetnewparsSpider(scrapy.Spider):
    name = "svetnewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        parsed_data = []
        svets = response.css('div.WdR1o')
        for svet in svets:

                name = svet.css('div.lsooF span::text').get(),
                price = svet.css('div.pY3d2 span::text').get(),
                url = svet.css('a::attr(href)').get()
                url = response.urljoin(url)

                parsed_data.append([name, price, url])

        with open("svet.csv", 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Название источника света', 'цена', 'Ссылка'])
            writer.writerows(parsed_data)