#coding:utf_8
import urllib2

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