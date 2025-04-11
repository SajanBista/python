import scrapy

class EbookSpider(scrapy.Spider):
    name = "ebook"
    start_urls = ["https://books.toscrape.com/"]
    def parse(self, response):
        print("From Here")
        ebooks = response.css("article")
        #print(ebooks)

        #print(response.css("h3 a").get())
        #print(response.css("h3 a:: text").get())
        for ebook in ebooks:
            title = ebook.css("a::text").get()
            price = ebook.css("p.price_color::text").get()
            #print(title, price)
            #extracting data
            yield{"title": title,
                  "price": price}
        

