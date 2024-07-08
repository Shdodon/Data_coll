import scrapy


class PopulationTest0Spider(scrapy.Spider):
    name = "population_test_0"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)"]

    def parse(self, response):
        countries = response.xpath("////tbody/tr")

        for country in countries:
            country_name = row.xpath('.')
