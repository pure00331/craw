#coding:utf-8
import models
class UrlOutputer(object):

    def collect(self, new_data):
        if new_data is None:
            return
        else:
            datas = []
            datas.append(new_data)

