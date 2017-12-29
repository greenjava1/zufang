import scrapy
from scrapy.http import Request
import itertools
from urllib import parse
import sys
sys.path.append("C:\\python_work\\zufang\\zufang\\")
from items import ZufangItem

class GanjiSpider(scrapy.Spider):
    name = "zufang"
    allowed_domains = ["esf.fang.com"]
    start_urls = ['http://esf.fang.com/house-a012/']
    #start_urls = ['http://esf.fang.com/house/g21/']
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
        #for test
        title_list = response.xpath("//*[@class=\"list rel\"]/dd/p[1]/a/@title").extract()
        money_list = response.xpath("//*[@class=\"list rel\"]/dd/div[3]/p[1]/span[1]/text()").extract()
        size_list = response.xpath("//*[@class=\"list rel\"]/dd/div[2]/p[1]/text()").extract()
        name_list = response.xpath("//*[@class=\"list rel\"]/dd/p[3]/a/span/text()").extract()
        floor_list = response.xpath('//*[@class="list rel"]/dd/p[2]/text()[2]').extract()
        url_list =  response.xpath('//*[@class="list rel"]/dd/p[1]/a/@href').extract()
        location_list =   response.xpath('//*[@class="list rel"]/dd/p[3]/span/@title').extract()


        print("=======================================================================================")
        #print (name_list)
        print (floor_list)

        resultfile = open("result", 'a')
        result=[]

        zset = itertools.zip_longest(title_list, money_list, size_list, name_list, floor_list, url_list,
                                       location_list,fillvalue=-1)
        print (zset)
        #for i,j,z,n,f,u,l in zip(title_list, money_list,size_list,name_list,floor_list,url_list,location_list):

        for i, j, z, n, f, u, l in zset:
            zf['title'] = i
            zf['money'] = j
            zf['size'] = z
            zf['name'] = n
            zf['floor'] = f.strip()
            zf['url'] =  urls.scheme +"://"+urls.hostname+u
            zf['location'] = l
            result = zf
            resultfile.write(str(result))
            #f.write("\n")
            #print(i,":",j)
            yield zf
        #for next_page in response.xpath('//*[@id="PageControl1_hlk_next"]'):
        #    yield response.follow(next_page, self.parse)
        resultfile.close()