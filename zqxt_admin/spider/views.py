# coding:utf-8

from django.shortcuts import render
import url_manager, html_downloader, html_outputer, html_parser, os
from django.http import HttpResponse

# Create your views here.
class SpiderMain(object):

    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.UrlDownloader()
        self.html_parser = html_parser.UrlParser()
        self.html_outputer =html_outputer.UrlOutputer()

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
                self.html_outputer.collect(new_text)

                if count == 10:
                    break
                count += 1

            except:
                print 'craw failed'

        self.html_outputer.output()



if True:#运行时启动
    root_url = 'http://baike.baidu.com/view/1634.htm'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)

def home(request):
    return render(request, 'output.html')