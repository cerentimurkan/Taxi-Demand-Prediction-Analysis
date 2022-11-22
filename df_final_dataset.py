import pandas as pd
import numpy as np
import seaborn as sns
import datetime as dt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

#2019(tüm aylar) - 2020(ilk iki ay) >> https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page

#İlk datasetinden toplam 9 milyon satır geliyor.
df=pd.read_csv(r"C:\Users\asd\PycharmProjects\pythonProject\Week 6\nyc_data_201901_202003.csv")
df.head()
df.shape

#Datasetinden yüzde 10 u nu almak için aşağıdaki işlemi yaptık.
df=df.sample(frac=0.1)
df.describe()
df.shape

#Taxi zone adlı verisetinde lat/long değerlerini almak için.
df_geo=pd.read_csv(r"C:\Users\asd\PycharmProjects\pythonProject\geo_coor.csv")

#Final veriseti olarak iki dataframe i birleştiriyoruz.
df_final=df.merge(df_geo,on="PULocationID",how="left")
df_final.head()

#Son olarak final seti csv ye alıyoruz.
df_final.to_csv(r"C:\Users\asd\PycharmProjects\pythonProject\Week 6\df_final_dataset.csv")




