import scrapy

class BooksSpider(scrapy.Spider):
    name="books"

    def start_requests(self):
        urls=["http://books.toscrape.com/catalogue/page-1.html"]

        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)


    def parse(self,response):
        #page=response.url.split("/")[-1]
        #id=page.split("-")[1][0]
        #filename=f"books-{id}.html"
        
        for c in response.css("article.product_pod"):
            img=c.css("img.thumbnail::attr(src)").get()
            title=c.css("h3 a::attr(title)").get()
            price=c.css("p.price_color::text").get()

            yield {
                'img_url':img,
                'img_title':title,
                'img_price':price
            }

        next_page=response.css("li.next a::attr(href)").get()

        if next_page is not None:
            next_page=response.urljoin(next_page)
            print(next_page)
            yield scrapy.Request(url=next_page,callback=self.parse)