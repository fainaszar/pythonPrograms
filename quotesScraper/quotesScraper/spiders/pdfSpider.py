# -*- coding: utf-8 -*-
import scrapy
import urlparse
from scrapy.http import Request
from quotesScraper.items import QuotesscraperItem

class PdfspiderSpider(scrapy.Spider):
    name = 'pdfSpider'
    allowed_domains = ['http://cs.uok.edu.in/']
    start_urls = ['http://cs.uok.edu.in/']
    parsePdf= False
    def parse(self, response):
        
        if not self.parsePdf:
            links = response.css("ul#lstAnnouncements.list.doughnut li a::attr('href')").extract()

            path = "http://" + response.url.split("/")[-3]
        
       
            base_url = "http://cs.uok.edu.in"
            file_urls = []


            for link in links:
                if link != "" and "/" in link:
                    path = urlparse.urljoin(base_url,link)
                    file_urls.append(path)


                

            yield QuotesscraperItem(file_urls=file_urls)

            


        


    