import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow,QTableWidgetItem,QTableView,QCheckBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from spider import *
from urllib import request
import re
import sqlite3
import time

'''
特定网址爬虫程序v1.1

未实现程序复用，程序很卡

为实现多线程，不能实时更新
'''

class mwindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self,parent=None):
        super(mwindow, self).__init__(parent)
        self.setupUi(self)

        self.pushButton_4.setEnabled(False)
        self.model=QStandardItemModel(0,0)
        self.model.setHorizontalHeaderLabels(['更新内容','已保存内容'])
        self.tableView.setModel(self.model)

        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.thread_1 = Worker()
        self.thread_1.progressBarValue.connect(self.gg)
        self.checkBox.stateChanged.connect(self.checkin)

    def ps_bt4(self):
        '''
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
        '''
    
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
        num=len(articl)
        conn=sqlite3.connect('mrsoft.db')
        cursor=conn.cursor()
        sql='select title from Dragon5'
        cursor.execute(sql)
        result1=cursor.fetchall()
        num1=len(result1)
        self.model=QStandardItemModel(num,2)#数据写入表格
        for row in range(num1,num):
            item_checked = QStandardItem(articl[row][1])
            item_checked.setCheckState(Qt.Unchecked)
            item_checked.setCheckable(True)
            self.model.setItem(row,0, item_checked)
            i=QStandardItem('等待更新......')
            self.model.setItem(row,1,i)

        for row in range(num1):
            item_checked = QStandardItem(articl[row][1])
            item_checked.setCheckState(Qt.PartiallyChecked)
            item_checked.setCheckable(False)
            self.model.setItem(row,0, item_checked)
            i=QStandardItem(result1[row][0])
            self.model.setItem(row,1,i)

        cursor.close()
        conn.close()

        self.model.setHorizontalHeaderLabels(['更新内容','已保存内容'])
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.lineEdit_3.setText(str(len(articl)))
        self.lineEdit_2.setText(str(num-num1))
    
    def download(self):
        articl=self.data()
        num=len(articl)
        conn=sqlite3.connect('mrsoft.db')
        cursor=conn.cursor()
        sql='select title from Dragon5'
        cursor.execute(sql)
        result1=cursor.fetchall()
        num1=len(result1)
        if self.checkBox.isChecked():
            for row in range(num1,num):
                url=articl[row][0]
                title=articl[row][1]
                data=self.html(url)
                result=re.findall('id="BookText">(.*?)<div',data,re.S)
                one=result[0].replace('<br/><br/>','\n')
                two=one.replace('<br/><br />','\n')
                line=two.replace('<br/>　　<br/>','\n')
                a=row+1
                cursor.execute('insert into Dragon5 values(?,?,?)',(a,title,line))
                #cursor.execute('update into Dragon5 values(?,?,?)',(a,title,line))
                item_checked = QStandardItem(articl[row][1])
                item_checked.setCheckState(Qt.PartiallyChecked)
                item_checked.setCheckable(False)
                self.model.setItem(row,0, item_checked)
                i=QStandardItem(articl[row][1])
                self.model.setItem(row,1,i)
                self.checkBox.setCheckState(Qt.PartiallyChecked)
                self.checkBox.setCheckable(False)
        else:
            QMessageBox.information(self,'警告','你什么都没选呢！')
        cursor.close()
        conn.commit()
        conn.close()
    
    def checkin(self):
        articl=self.data()
        num=len(articl)
        conn=sqlite3.connect('mrsoft.db')
        cursor=conn.cursor()
        sql='select title from Dragon5'
        cursor.execute(sql)
        result1=cursor.fetchall()
        num1=len(result1)
        cb=self.checkBox.checkState()
        if cb==Qt.Checked:
            for row in range(num1,num):
                item_checked = QStandardItem(articl[row][1])
                item_checked.setCheckState(Qt.Checked)
                item_checked.setCheckable(True)
                self.model.setItem(row,0, item_checked)
        else:
            for row in range(num1,num):
                item_checked = QStandardItem(articl[row][1])
                item_checked.setCheckState(Qt.Unchecked)
                item_checked.setCheckable(True)
                self.model.setItem(row,0, item_checked)
        cursor.close()
        conn.close()

    def gg(self,data):
        self.model.setItem(data,2,QStandardItem('正在下载'))

class Worker(QThread):

    progressBarValue = pyqtSignal(int)  # 更新进度条

    def __init__(self):
        super(Worker, self).__init__()


    def run(self):
        for data in range(207):
            self.progressBarValue.emit(int(data))  # 发射信号
            time.sleep(0.1)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = mwindow()
    w.pushButton.clicked.connect(w.getlist)
    w.pushButton_4.clicked.connect(w.ps_bt4)
    w.pushButton_2.clicked.connect(w.download)
    w.show()
    sys.exit(app.exec_())