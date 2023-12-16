from crawl.crawl_data import CrawlData
from dataprocess.process import DataProcess
import requests

data = DataProcess(dataframe_path="last_16h.csv")
driver = CrawlData()

driver.crawl_image(data.product_link,data.dataframe,empty_value=True,start_point =0)

