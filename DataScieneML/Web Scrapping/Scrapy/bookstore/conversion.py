import json
import pandas as pd
import numpy as np
import requests

img_urls=[]
img_titles=[]
img_prices=[]

with open("all_books.json","r") as f:
    data=json.load(f)
    for ele in data:
        img_urls.append(ele['img_url'])
        img_titles.append(ele['img_title'])
        img_prices.append(ele['img_price'])

re=list(zip(img_urls,img_titles,img_prices))

df=pd.DataFrame(re)
df.columns=['image_url','book_title','product_price']

print(df)

df.to_csv("books.csv",index=False)

# for i,url in enumerate(img_urls):
#     with open(f"book-{i}.jpg","wb") as f:
#         u="http://"+url
#         response=requests.get(u)
#         f.write(response.content)
