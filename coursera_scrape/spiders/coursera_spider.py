from scrapy import Spider, Request
from coursera_scrape.items import CourseraScrapeItem
from selenium import webdriver
import time
import re

class CourseraSpider(Spider):
	name = 'coursera_spider'
	allowed_urls = ['https://www.coursera.org/']
	start_urls = ['https://www.coursera.org/browse/data-science?facets=skillNameMultiTag%2CjobTitleMultiTag%2CdifficultyLevelTag%2Clanguages%3AEnglish%2CentityTypeTag%2CpartnerMultiTag%2CcategoryMultiTag%3Adata-science%2CsubcategoryMultiTag&sortField=']
	
	def __init__(self):
		self.driver = webdriver.Chrome()

	def parse(self, response):
		items = []
		self.driver.get(response.url)

		result_names = self.driver.find_elements_by_xpath('//div[@class = "offering-wrapper"]//a')
		print(len(result_names))
		print('=' * 50)
		result_urls_ext = self.driver.find_elements_by_xpath('//div[@class = "offering-wrapper"]//a')
		print(len(result_urls_ext))
		print('=' * 50)

		try:
			for result_name in result_names:
				names_list = result_name.get_attribute('aria-label')
				print(names_list)
				print('*' * 50)

			for result_url in result_urls_ext:
				url_list = result_url.get_attribute('href')
				print(url_list)
				print('#' * 100)

		except Exception as e:
			print(e)
			self.driver.close()