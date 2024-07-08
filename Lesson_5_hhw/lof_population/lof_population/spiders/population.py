import scrapy


class PopulationSpider(scrapy.Spider):
    name = "population"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)"]

    def parse(self, response):
        for country in response.css('table.wikitable.sortable tbody tr'):
            name = country.css('td:nth-child(1) b a::text').get()
            if name:
                yield {
                    "name": name
                }


