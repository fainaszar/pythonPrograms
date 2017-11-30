# -*- coding: utf-8 -*-
import scrapy


class RedditbotSpider(scrapy.Spider):
    name = 'redditbot'
    allowed_domains = ['https://www.reddit.com/r/gameofthrones/']
    start_urls = ['https://www.reddit.com/r/gameofthrones//']

    def parse(self, response):

    	
        
        titles = response.css('.title.may-blank::text').extract()
        votes = response.css('.score.unvoted::text').extract()
        times = response.css('time::attr(title)').extract()
        comments = response.css('.comments::text').extract()

        

        info  = zip(titles,votes,times,comments)
        print "Info: **************\n" , info

        scrapped_info={}


        
        for item in info:
            scrapped_info={'title' : item[0],'vote' : item[1],'created_at' : item[2],'comments' : item[3]}
            yield scrapped_info


       	   	


        