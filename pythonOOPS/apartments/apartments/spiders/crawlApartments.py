# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
import time
from scrapy.http import HtmlResponse


class CrawlapartmentsSpider(scrapy.Spider):
    name = 'crawlApartments'
    allowed_domains = ['https://www.apartmentguide.com/apartments/Maryland/Laurel/Briarwood-Place-Apartment-Homes/48001/']
    start_urls = ['https://www.apartmentguide.com/apartments/Maryland/Laurel/Briarwood-Place-Apartment-Homes/48001//']

    def parse(self, response):


    	browser = webdriver.Chrome(executable_path="/home/faizan/Documents/python/pythonOOPS/chromedriver")
    	browser.get(response.url)

    	comments=[]
    	#print "Finding Buttons"
    	try:
    		while browser.find_element_by_css_selector('a._1i1ia') is not None:
    			button = browser.find_element_by_css_selector('a._1i1ia')
    	#		print("Button Found")
    			button.click()
    	#		print("Button Clicked")
    	except Exception:
    		pass

    	#print("No more buttons to search")



    	
    	# response.replace(body = str(browser.page_source.encode('utf-8')))

    	response = HtmlResponse(browser.current_url, body=browser.page_source, encoding='utf-8')


    	#using css


        # for comment in response.css("._140NQ p span::text").extract():

        # 	comments.append(comment)
        # 	print comment
        # 	time.sleep(0.4)


        #using Xpath

        for comment in response.xpath("//div[@class='_140NQ']/p/span/text()").extract():

        	print comment
        	time.sleep(2)



