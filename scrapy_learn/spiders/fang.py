# -*- coding: utf-8 -*-
import scrapy

from scrapy_learn.items import FangItem

class FangSpider(scrapy.Spider):
    # 唯一标识（项目中可能会存在多个爬虫）
    name = 'fang'
    # 允许访问的域名
    allowed_domains = ['fang.5i5j.com']
    # 当前爬取的第一个url地址，可以用逗号拼接多个地址
    start_urls = ['https://fang.5i5j.com/bj/loupan/']

    # 爬取结束调用的方法
    def parse(self, response):
        print(response.status)
        hlist = response.css("li.houst_ctn")
        print("房屋信息：")
        for vo in hlist:
            item = FangItem()
            item['title'] = vo.css("span.house_name ::text").extract_first()
            item['address'] = vo.css("span.tag_icon_site left").extract_first()
            item['time'] = vo.re("(.*?)日开盘")

            item['price'] = vo.css("p.price").extract_first()

            # 将数据送到pipelines管道
            yield item
        # pass
