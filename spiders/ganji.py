import scrapy
from scrapy.http import Request
from urllib import parse
import sys
sys.path.append("C:\\python_work\\zufang\\zufang\\")
from items import ZufangItem

class GanjiSpider(scrapy.Spider):
    name = "zufang"
    allowed_domains = ["esf.fang.com"]
    start_urls = ['http://esf.fang.com/house-a012-b01182/i31/']
    #start_urls = ['http://esf.fang.com/house-a012-b01182/i31/']
    print ("just for test")
    def parse(self, response):
        filename = response.url.split("/")[-2]
        print("=======================================================================================")
        print (response)
        urls = parse.urlparse(response.url)

        print(urls)


        print ('protocol:', urls.scheme)
        print ('hostname:', urls.hostname)
        print ('port:', urls.port)
        print ('path:', urls.path)
        print("=======================================================================================")
        print(filename)
        zf = ZufangItem()
        title_list = response.xpath("//*[@class=\"list rel\"]/dd/p[1]/a/@title").extract()
        money_list = response.xpath("//*[@class=\"list rel\"]/dd/div[3]/p[1]/span[1]/text()").extract()
        size_list = response.xpath("//*[@class=\"list rel\"]/dd/div[2]/p[1]/text()").extract()
        name_list = response.xpath("//*[@class=\"list rel\"]/dd/p[3]/a/span/text()").extract()
        floor_list = response.xpath("//*[@class=\"list rel\"]/dd/p[2]/text()").extract()
        url_list =  response.xpath('//*[@class="list rel"]/dd/p[1]/a/@href').extract() 
        print("=======================================================================================")
        #print (name_list)
        #print (floor_list)
        print (url_list)
        resultfile = open("result", 'a')
        result=[]
        for i,j,z,n,f,u in zip(title_list, money_list,size_list,name_list,floor_list,url_list):
            zf['title'] = i.strip()
            zf['money'] = j.strip()
            zf['size'] = z.strip()
            zf['name'] = n.strip()
            zf['floor'] = f.strip()
            zf['url'] =  urls.scheme +"://"+urls.hostname+"/"+u
            result = zf
            resultfile.write(str(result))
            #f.write("\n")
            #print(i,":",j)
            yield zf
        for next_page in response.xpath('//*[@id="PageControl1_hlk_next"]'):
            yield response.follow(next_page, self.parse)
        resultfile.close()