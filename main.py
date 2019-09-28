import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow,QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
from spider import Ui_Form
from urllib import request
import re
import sqlite3


'''
小说爬虫v1.0版主程序（已废弃）
'''

class mwindow(QWidget, Ui_Form):
    def __init__(self):
        super(mwindow, self).__init__()
        self.setupUi(self)

    def ps_bt4(self):
        start=self.lineEdit_2.text()
        end=self.lineEdit_3.text()
        self.textBrowser.clear()
        articl=self.data()
        self.textBrowser.append('开始下载......')
        conn=sqlite3.connect('mrsoft.db')
        cursor=conn.cursor()
        a=int(start)-1
        while a<int(end):
            url=articl[a][0]
            title=articl[a][1]
            data=self.html(url)
            result=re.findall('id="BookText">(.*?)<div',data,re.S)
            one=result[0].replace('<br/><br/>','\n')
            two=one.replace('<br/><br />','\n')
            line=two.replace('<br/>　　<br/>','\n')
            a=a+1
            sql='update Dragon5 set content=? where id=?'
            cursor.execute(sql,(line,a))
            self.textBrowser.append(title+'......更新成功')
        cursor.close()
        conn.commit()
        conn.close()
        self.textBrowser.append('更新完成，请在数据库中查看')
    
    def data(self):
        url=self.lineEdit.text()
        header={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
        req=request.Request(url=url,headers=header)
        response=request.urlopen(req)
        data=response.read().decode('utf-8')
        articl=re.findall('<span>.*?"(.*?)">(.*?)<.*?</span>',data,re.S)
        return articl

    def html(self,url):
        header={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
        req=request.Request(url=url,headers=header)
        response=request.urlopen(req)
        data=response.read().decode('utf-8')
        return data

    def getlist(self):
        articl=self.data()
        x=0
        for i in articl:
            x=x+1
            txt='['+str(x)+']===='+i[1]
            self.textBrowser.append(txt)
        self.lineEdit_3.setText(str(len(articl)))
    
    def download(self):
        start=self.lineEdit_2.text()
        end=self.lineEdit_3.text()
        self.textBrowser.clear()
        articl=self.data()
        self.textBrowser.append('开始下载......')
        conn=sqlite3.connect('mrsoft.db')
        cursor=conn.cursor()
        a=int(start)-1
        while a<int(end):
            url=articl[a][0]
            title=articl[a][1]
            data=self.html(url)
            result=re.findall('id="BookText">(.*?)<div',data,re.S)
            one=result[0].replace('<br/><br/>','\n')
            two=one.replace('<br/><br />','\n')
            line=two.replace('<br/>　　<br/>','\n')
            a=a+1
            cursor.execute('insert into Dragon5 values(?,?,?)',(a,title,line))
            self.textBrowser.append(title+'......写入成功')
        cursor.close()
        conn.commit()
        conn.close()
        self.textBrowser.append('写入完成，请在数据库中查看')
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = mwindow()
    w.pushButton.clicked.connect(w.getlist)
    w.pushButton_4.clicked.connect(w.ps_bt4)
    w.pushButton_2.clicked.connect(w.download)
    w.show()
    sys.exit(app.exec_())