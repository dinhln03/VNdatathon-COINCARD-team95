import pandas as pd
import requests

class DataProcess():
    def __init__(self,dataframe_path):
        self.dataframe = pd.read_csv(dataframe_path)
        self.product_link = self.dataframe["link"]

    def delete_colunm(self, index):
        self.dataframe.drop(index=index,inplace=True)

    def delete_dead_link(self):
        i=0
        for (index,link) in enumerate(self.product_link):
            try:
                response = requests.get(link)
                if str(response.url) == "https://www.ikea.com/sa/en/cat/products-products/":
                    self.delete_colunm(index=index)
                    i+=1
                    print(f"{i} products have been deleted")
            except:
                print("Surpass")

        self.dataframe.to_csv("new_data_1.csv")
        #Assign new variabe 
        self.dataframe = pd.read_csv("new_data_1.csv")
        self.product_link = self.dataframe["link"]
    
    def concat_and_filter(self, datalink_1:str, datalink_2:str):
        dataframe_1 = pd.read_csv(datalink_1)
        dataframe_2 = pd.read_csv(datalink_2)
        frames = [dataframe_1,dataframe_2]
        new_dataframe = pd.concat(frames)
        new_dataframe=new_dataframe.drop_duplicates(subset=['item_id'], keep='last')
        new_dataframe.to_csv("last_10h.csv")




