import scrapy


class PopulationTest0Spider(scrapy.Spider):
    name = "population_test_0"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)"]

    def parse(self, response):
        rows = response.xpath("//tbody/tr")

        for row in rows:
            country_name = row.xpath('.//td/span/a/text()').get()
            country_popylation = row.xpath('.//td[2]/tr[2]/text()').get
            link = row.xpath
            yield response.follow(url=link if link else 'wiki/Pitcairn_Islands', callback=self.parse_country,
                                  meta={'country_name' : country_name,
                                        'country_popylation' : country_popylation})

    def parse_country(self, response):
        rows = response.xpath("//table[contains(@class,'infobox ib-country vcard')][1]/tbody")
        for row in rows:
            capital = row.xpath('.//td[contains(@class,"infobox-data")]/a/text()').get()
            religion = row.xpath('.//th[contains(text(), "Religion")]/following-sibling::td//text()').get()
            name = response.request.meta['country_name']
            membership_un = response.request.meta['membership_un']
            sovereignty_dispute_info = response.request.meta['sovereignty_dispute_info']
            country_status = response.request.meta['country_status']
            yield {
                'country': name,
                'capital': capital,
                'religion': religion if religion else "None",
                'membership_un': membership_un.strip(),
                'sovereignty_dispute_info': sovereignty_dispute_info.strip(),
                'country_status': country_status.strip(),
            }

