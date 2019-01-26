# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CourseraScrapeItem(scrapy.Item):
	# define the fields for your item here like:
	# info collected from search result page
	name = scrapy.Field()
	creator = scrapy.Field()
	courseType = scrapy.Field()
	level = scrapy.Field()
	hours = scrapy.Field()
	num_course = scrapy.Field()

	# info collected from individual course page
	# if it is a 'course' type, there is only one course
	#if it is a 'specialized' type, there are multiple courses
	courseName = scrapy.Field()
	courseInfo = scrapy.Field()
	skills = scrapy.Field()
	courseTopic = scrapy.Field()
	rating = scrapy.Field()

	num_rating = scrapy.Field()
	num_review = scrapy.Field()
	review_user = scrapy.Field()
	review_date = scrapy.Field()
	review_rating = scrapy.Field()
	review_text = scrapy.Field()
	
