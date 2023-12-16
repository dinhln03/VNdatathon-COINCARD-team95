from selenium import webdriver
import pandas as pd
from dataprocess.process import DataProcess
from types import TracebackType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CrawlData(webdriver.Chrome):
    def __init__(self,teardown=True):
        super(CrawlData,self).__init__()
        self.teardown = teardown
        self.implicitly_wait(3)
        self.maximize_window()
        self.sellabe_products_value = []

    def __exit__(self, exc_type: type[BaseException] | None, exc: BaseException | None, traceback: TracebackType | None):
        if self.teardown:
            self.quit()

    def land_page(self,url:str):
        self.get(url)
    
    def filter_oft_products(self):
        xpath_expression = "//span[@class='pip-btn__label' and contains(text(), 'Add to bag')]"
        
        try:
            WebDriverWait(self, 7).until(
            EC.visibility_of_element_located(
            (By.XPATH,xpath_expression),
            )
            )
            self.sellabe_products_value.append(True)
        except:
            self.sellabe_products_value.append(False)

    def crawl_color(self,product_link:str,dataframe:pd.DataFrame,empty_value = True,start_point = 0):
        # if multiple color:
        color_values = []
        index_values = []
        if empty_value:
            dataframe["Color"] = None
        for (index,link) in enumerate(product_link[start_point:], start=start_point):
            index_values.append(index)
            self.land_page(link)
            try:
                try:
                    color_value = f""
                    xpath_expression = "//span[@class='pip-list-view-item__title pip-list-view-item__title--emphasised' and (contains(text(), 'Choose colour') or contains(text(), 'Choose cover') or contains(text(), 'Choose Table colour'))]/ancestor::button"
                    choose_color_button = self.find_element(By.XPATH,xpath_expression)
                    choose_color_button.click()
                    WebDriverWait(self, 3).until(
                    EC.visibility_of_element_located(
                    (By.CLASS_NAME, "pip-link-list__item-title"),
                    )
                    )
                    for i in self.find_elements(By.CLASS_NAME, "pip-link-list__item-title"):
                        color_value = color_value + str(i.text) +","
                    color_value = color_value[:-1]
                except:
                    description = self.find_element(By.CLASS_NAME, "pip-header-section__description-text").text
                    description = description.split(",")[1].strip().capitalize()
                    color_value = description
            except:
                color_value = ""
            print(color_value)
            color_values.append(color_value)
            if index%20==0:
                dataframe["Color"][index_values] = color_values
                dataframe.to_csv("last_16h.csv")
        dataframe["Color"] = color_value
        dataframe.to_csv("last_16h.csv")

    def crawl_image(self,product_link:str,dataframe:pd.DataFrame,empty_value = True,start_point = 0):
        # if multiple color:
        image_values = []
        index_values = []
        if empty_value:
            dataframe["Image_link"] = None
        for (index,link) in enumerate(product_link[start_point:], start=start_point):
            index_values.append(index)
            self.land_page(link)
            try:
                image_value = f""
                xpath_expression = "//button[@class='pip-media-grid__image-button']/span/img"
                img_button= self.find_elements(By.XPATH,xpath_expression)

                for button in img_button:
                    image_value = image_value + str(button.get_attribute("src"))+","
                image_value = image_value[:-1]
            except:
                image_value  = ""
            image_values.append(image_value)
            print(image_value)
            if index%20==0:
                dataframe["Image_link"][index_values] = image_values
                dataframe.to_csv("last_24h.csv")
                print(f"Have been processed {index}")
        dataframe["Image_link"] = image_values
        dataframe.to_csv("last_24h.csv")

        
        











