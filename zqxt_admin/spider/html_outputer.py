#coding:utf-8
import os
class UrlOutputer(object):
    os.chdir('C:\\Users\\Administrator\\zqxt_admin\\spider\\templates')
    def __init__(self):
        self.datas = []

    def collect(self, new_data):
        if new_data is None:
            return
        else:
            self.datas.append(new_data)

    def output(self):
        fout = open('output.html', 'w')

        fout.write('{% extends "base.html" %}')
        fout.write('{% block title %}欢迎光临首页{% endblock %}')
        fout.write("{% block content %}")
        fout.write('<table class="table table-striped">')
        fout.write('<caption>linux百科</caption>')
        fout.write("<thead>")
        fout.write("<tr>")
        fout.write("<th>网址</th>")
        fout.write("<th>词条</th>")
        fout.write("<th>简介</th>")
        fout.write("</tr>")
        fout.write("</thead>")

        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['url'].encode('utf-8'))
            fout.write('<td>%s</td>' % data['title'].encode('utf-8'))
            fout.write('<td>%s</td>' % data['summary'].encode('utf-8'))
            fout.write('</tr>')

        fout.write('</table>')
        fout.write("{% endblock %}")

        fout.close()



