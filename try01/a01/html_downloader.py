#coding:utf_8
import urllib2
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'try01.settings')
import django
django.setup()
class UrlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        else:
            responce = urllib2.urlopen(url)
            if responce.getcode() != 200:
                return None
            else:
               return responce.read()