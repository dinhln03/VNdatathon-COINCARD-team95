from crawl.crawl_data import CrawlData
from dataprocess.process import DataProcess
import requests

data = DataProcess(dataframe_path="ikea_products_mentor_data.csv")
i=0

for (index,link) in enumerate(data.product_link):
    try:
        response = requests.get(link)
        if str(response.url) == "https://www.ikea.com/sa/en/cat/products-products/":
            data.delete_colunm(index=index)
            i+=1
            print(f"{i} products have been deleted")
    except:
        print("Surpass")

data.dataframe.to_csv("new_data.csv")


