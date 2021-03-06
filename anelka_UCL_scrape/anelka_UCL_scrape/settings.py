# Scrapy settings for anelka_UCL_scrape project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'anelka_UCL_scrape'

SPIDER_MODULES = ['anelka_UCL_scrape.spiders']
NEWSPIDER_MODULE = 'anelka_UCL_scrape.spiders'

ITEM_PIPELINES = [
    'anelka_UCL_scrape.files.FilesPipeline',
]
FILES_STORE = 'tactics'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'anelka_UCL_scrape (+http://www.yourdomain.com)'
