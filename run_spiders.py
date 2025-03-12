from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from NewsScraping.spiders.aljazeera import aljazeeraSpider
from NewsScraping.spiders.arabnews import arabnewsSpider
from NewsScraping.spiders.breitbart import BreitbartSpider
from NewsScraping.spiders.foxspider import FoxSpider
from NewsScraping.spiders.guardian import guardianSpider
from NewsScraping.spiders.mee import meeSpider
from NewsScraping.spiders.time import TimeSpider


def run_spiders():
    # Initialize CrawlerProcess with your project's settings
    process = CrawlerProcess(get_project_settings())

    # Add spiders to the process
    process.crawl(aljazeeraSpider)  # Replace with your actual spider class
    process.crawl(arabnewsSpider)  # Replace with your actual spider class
    process.crawl(BreitbartSpider)  # Replace with your actual spider class
    process.crawl(FoxSpider)  # Replace with your actual spider class
    process.crawl(guardianSpider)  # Replace with your actual spider class
    process.crawl(meeSpider)  # Replace with your actual spider class
    process.crawl(TimeSpider)  # Replace with your actual spider class
    
    # Start the crawling process
    process.start()  # This will run all spiders sequentially

if __name__ == "__main__":
    run_spiders()
