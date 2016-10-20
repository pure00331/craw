#coding:utf-8

class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, new_url):#判断是否加入未爬过的set
        if new_url is None:
            return
        elif new_url not in self.new_urls and new_url not in self.old_urls:
            self.new_urls.add(new_url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        else:
            for new_url in urls:
                self.add_new_url(new_url)

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        new_url = self.new_urls.pop()#获取并删除
        self.old_urls.add(new_url)
        return new_url

