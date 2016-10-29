#coding:utf-8
import re
import urlparse
from bs4 import BeautifulSoup
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'try.settings')
import django
django.setup()
class UrlParser(object):
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        #/view/123.htm
        links = soup.find_all('a', href=re.compile(r'/view/\d+\.htm'))
        for link in links:
            new_url = link['href']#此处不太理解
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_text(self, page_url, soup):
        res_data = {}

        #url
        res_data['url'] = page_url

        #<dd class="lemmaWgt-lemmaTitle-title"> <h1>linux</h1>
        title = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1')
        res_data['title'] = title.get_text()

        #<div class="lemma-summary" label-module="lemmaSummary">
        text = soup.find('div', class_="lemma-summary")
        res_data['summary'] = text.get_text()

        return res_data

    def parse(self, page_url, html_content):
        if page_url is None or html_content is None:
            return None
        else:
            soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
            new_urls = self._get_new_urls(page_url, soup)
            new_text = self._get_new_text(page_url, soup)
            return new_urls, new_text

