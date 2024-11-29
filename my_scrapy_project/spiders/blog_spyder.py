import scrapy

class BlogSpider(scrapy.Spider):
    # Name of the spider
    name = "blog"
    
    # Allowed domains to scrape
    allowed_domains = ["quotes.toscrape.com"]
    
    # Initial URL(s) to start scraping
    start_urls = ["http://quotes.toscrape.com/"]
    
    def parse(self, response):
        """
        The main parsing method. It extracts data from the response.
        """
        quotes = response.css("div.quote")
        
        for quote in quotes:
            yield {
                "text": quote.css("span.text::text").get(),
                
                "author": quote.css("span small.author::text").get(),
                
                "tags": quote.css("div.tags a.tag::text").getall(),
            }
        
        next_page = response.css("li.next a::attr(href)").get()
        
        if next_page:
            yield response.follow(next_page, callback=self.parse)



#Run command 

#---- Without Save
#scrapy crawl blog

#---- With Save
#scrapy crawl blog -o output.json