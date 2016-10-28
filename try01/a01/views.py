# coding:utf-8
from django.shortcuts import render
import models
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'try01.settings')
import django
django.setup()
# Create your views here.
import html_downloader, html_parser, url_manager

class SpiderMain(object):
    global datas
    datas = []
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.UrlDownloader()
        self.html_parser = html_parser.UrlParser()

    def collect(self, new_data):
        if new_data is None:
            return
        else:
            datas.append(new_data)

    def craw(self, root_url):

        count = 1

        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:#处理异常
                new_url = self.urls.get_new_url()
                print 'craw %d %s' % (count, new_url)
                html_content = self.downloader.download(new_url)
                new_urls, new_text = self.html_parser.parse(new_url, html_content)
                self.urls.add_new_urls(new_urls)
                self.collect(new_text)
                if count == 5:
                    break
                count += 1

            except:
                print 'craw failed'
                count += 1

if True:
    root_url = 'http://baike.baidu.com/view/1634.htm'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)

    models.per.objects.create(url=datas['url'], title=datas['title'], summary=datas['summary'])
