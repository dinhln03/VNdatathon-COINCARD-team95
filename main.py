from crawl.crawl_data import CrawlData
from dataprocess.process import DataProcess
import requests

data = DataProcess(dataframe_path="ikea_products_mentor_data.csv")

for (index,link) in enumerate(data.product_link):
    response = requests.get(link)
    if str(response.url) == "https://www.ikea.com/sa/en/cat/products-products/":
        data.delete_colunm(index=index)

data.dataframe.to_csv()


