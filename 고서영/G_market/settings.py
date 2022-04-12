# -*- coding: utf-8 -*-

# Scrapy settings for G_market project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'G_market'

SPIDER_MODULES = ['G_market.spiders']

NEWSPIDER_MODULE = 'G_market.spiders'

ROBOTSTXT_OBEY = False

LOG_FILE = 'G_Market.log'

FEED_EXPORT_ENCODING="utf-8-sig"

FEED_EXPORT_FIELDS = ['Name','Price','Delivery_Charge','URL']