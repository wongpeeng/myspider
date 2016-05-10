from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import Request, FormRequest
from rda.items import Rda

class RdaSpider(CrawlSpider)"
    name="rda_management"
    allowed_domains=["crm.rdamicro.com/RDAWebApp"]
    start_urls=()
    heads={"Uer-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36"}

