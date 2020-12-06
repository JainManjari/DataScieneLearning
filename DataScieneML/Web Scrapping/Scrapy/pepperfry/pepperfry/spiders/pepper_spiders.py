import scrapy
import json
import os
import requests

class PepperFry(scrapy.Spider):
    name="pepper_fry"

    def start_requests(self):

        base_url="https://www.pepperfry.com/site_product/search?q="

        items=["Arm Chair","Bean Bags","Bench","Book Cases","Chest Drawers","Coffee Tables","Dining Set",
                "Garden Seating","King Beds","Queen Beds","2 Seater Sofa"]

        parent_dir="Products/"

        if not os.path.exists(parent_dir):
            path=os.path.join(parent_dir)
            os.mkdir(parent_dir)

        for item in items:
            path=os.path.join(parent_dir,item)
            if not os.path.exists(path):
                os.mkdir(path)
            l=item.split(" ")
            key="+".join(l)
            url=base_url+key
            yield scrapy.Request(url=url,callback=self.parse,dont_filter=True)

    
    def parse(self,response):
        prod_page=response.css("div.srchrslt-crd-10x11")
        parent_dir="Products/"
        if len(prod_page)>0:
            os.chdir("C:\\Users\\manja\\Python\\DataScieneML\\Web Scrapping\\Scrapy\\pepperfry\\Products")
            item=response.url.split("/")[-1].split("=")[-1].split("+")
            item=" ".join(item)
            path=os.path.join(item)
            os.chdir(path)
            first_20=response.css("div.srchrslt-crd-10x11")[:20]
            for i,prod in enumerate(first_20):
                url=prod.css("a::attr(href)").get()
                yield scrapy.Request(url=url,callback=self.parse)
                #print(os.getcwd())
        
        else:
            title=response.css("h1::text").get()
            new_dir=title.split(" ")[:3]
            new_dir="".join(e for e in new_dir if e.isalnum())
            item=response.url.split("&")[-1].split("=")[-1].split("%20")
            item=" ".join(e for e in item)
            os.chdir(f"C:\\Users\\manja\\Python\\DataScieneML\\Web Scrapping\\Scrapy\\pepperfry\\Products\\{item}")
            #print(os.getcwd())
            path=os.path.join(new_dir)
            if not os.path.exists(path):
                os.mkdir(path)
            os.chdir(path)
            #print("path: =>",os.getcwd())
            price=response.css("span.v-offer-price-amt::text").get()
            labels=response.css("span.v-prod-comp-dtls-listitem-label::text").getall()
            values=response.css("span.v-prod-comp-dtls-listitem-value::text").getall()
            small_di={}
            for i in range(len(labels)):
                small_di[labels[i]]=values[i]
            desc=response.css("div.v-more-info-tab-cont-para-wrap")[0]
            desc2=desc.css("p::text").getall()
            desc2=" ".join(e for e in desc2)
            big_di={
                "Title":title,
                "Price":price,
                "Details":small_di,
                "Description":desc2
            }
            with open("metadata.json","w") as f:
                json.dump(big_di,f)

            imgs=response.css("img.vipImage__thumb-each-pic::attr(data-src)").getall()[:5]

            for i,img in enumerate(imgs):
                with open(f"img_{i+1}.jpg","wb") as f:
                    response=requests.get(img)
                    f.write(response.content)
            
        


       