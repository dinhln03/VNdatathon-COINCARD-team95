import pandas as pd

class DataProcess():
    def __init__(self,dataframe_path):
        self.dataframe = pd.read_csv(dataframe_path)
        self.product_link = self.dataframe["link"]

    def delete_colunm(self, index):
        self.dataframe.drop(index=index,inplace=True)
