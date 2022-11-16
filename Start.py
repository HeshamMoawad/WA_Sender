# -*- coding: utf-8 -*-
# Created by: PyQt5 UI code generator 5.15.4


import random,pandas,csv
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QMessageBox,QMainWindow,QApplication
from PyQt5.QtCore import QThread,pyqtSignal
from styles import Styles
from time import sleep
from requests import get,ConnectionError
from mainclass import Whatsapp,StockInfo
from datetime import datetime
import logging
#from DB_online import Database_connection,Dataframe

logging.basicConfig(level=logging.INFO,filename="Data\logger.log",filemode="a",format="%(asctime)s:%(levelname)s:%(message)s",datefmt='%Y-%m-%d %H:%M:%S')

dicta2 = {'Key': {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f', 16: 'g', 17: 'h', 18: 'i', 19: 'j', 20: 'k', 21: 'l', 22: 'm', 23: 'n', 24: 'o', 25: 'p', 26: 'q', 27: 'r', 28: 's', 29: 't', 30: 'u', 31: 'v', 32: 'w', 33: 'x', 34: 'y', 35: 'z', 36: 'A', 37: 'B', 38: 'C', 39: 'D', 40: 'E', 41: 'F', 42: 'G', 43: 'H', 44: 'I', 45: 'J', 46: 'K', 47: 'L', 48: 'M', 49: 'N', 50: 'O', 51: 'P', 52: 'Q', 53: 'R', 54: 'S', 55: 'T', 56: 'U',
57: 'V', 58: 'W', 59: 'X', 60: 'Y', 61: 'Z', 62: '!', 63: '$', 64: '%', 65: '&', 66: '*', 67: '+', 68: '-', 69: '/', 70: ':', 71: ';', 72: '<', 73: '=', 74: '>', 75: '?', 76: '@', 77: '[', 78: ']', 79: '^', 80: '_', 81: '`', 82: '{', 83: '|', 84: '}', 85:
'~'}, 'value': {0: '<Z', 1: '+h', 2: 'n*', 3: 'Ri', 4: 'ND', 5: 'UW', 6: '>W', 7: '=4', 8: '98', 9: 'N^', 10: '%E', 11: 'dY', 12: 'Zp', 13: 'ws', 14: 'u;', 15: 'kY', 16: 'z_', 17: 'dr', 18: 'JT', 19: 'NY', 20: 'h-', 21: 'hY', 22: 'ya', 23: 'A>', 24: '>>',
25: 'vF', 26: 'G<', 27: 'SI', 28: 'A_', 29: '5{', 30: 'Ou', 31: 'yc', 32: 'Ye', 33: 'fC', 34: '2n', 35: 'P[', 36: 'qE', 37: 'u@', 38: '7A', 39: '78', 40: '5@', 41: '+|', 42: 'pr', 43: 'pC', 44: '=I', 45: 'pp', 46: '^;', 47: 'iP', 48: '$+', 49: 'Ah', 50: '[}', 51: 'zu', 52: '_9', 53: 'AF', 54: 'UB', 55: 'SL', 56: 'h{', 57: '/D', 58: 'gS', 59: '<}', 60: ':W', 61: '`H', 62: 'A?', 63:
'Mb', 64: 'Ym', 65: 'ne', 66: 'GT', 67: '}4', 68: 'vc', 69: 'nH', 70: '92', 71: 'bW', 72: 'qb', 73: 'qq', 74: 'J&', 75: '=L', 76: '8-', 77: 'kI', 78: '?V', 79: '!+', 80: 'tv', 81: '$G', 82: '`T', 83: 'qe', 84: 'q~', 85: '8G'}}
dicta3 ={'Key': {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f', 16: 'g', 17: 'h', 18: 'i', 19: 'j', 20: 'k', 21: 'l', 22: 'm', 23: 'n', 24: 'o', 25: 'p', 26: 'q', 27: 'r', 28: 's', 29: 't', 30: 'u', 31: 'v', 32: 'w', 33: 'x', 34: 'y', 35: 'z', 36: 'A', 37: 'B', 38: 'C', 39: 'D', 40: 'E', 41: 'F', 42: 'G', 43: 'H', 44: 'I', 45: 'J', 46: 'K', 47: 'L', 48: 'M', 49: 'N', 50: 'O', 51: 'P', 52: 'Q', 53: 'R', 54: 'S', 55: 'T', 56: 'U',
57: 'V', 58: 'W', 59: 'X', 60: 'Y', 61: 'Z', 62: '!', 63: '$', 64: '%', 65: '&', 66: '*', 67: '+', 68: '-', 69: '/', 70: ':', 71: ';', 72: '<', 73: '=', 74: '>', 75: '?', 76: '@', 77: '[', 78: ']', 79: '^', 80: '_', 81: '`', 82: '{', 83: '|', 84: '}', 85:
'~'}, 'value': {0: 'Rq?', 1: 'rK4', 2: '?NJ', 3: 'iN}', 4: ':}C', 5: '7a1', 6: '`k<', 7: '5GG', 8: 'tB[', 9: '*+=', 10: 'V0l', 11: 'cTj', 12: 'h;D', 13: '_rU', 14: 'S}`', 15: 'y{t', 16: 'j3{', 17: 'go*', 18: 'l$I', 19: 'o&7', 20: 'z*v', 21: 'D&r', 22: 'K:3', 23: '2]M', 24: 'Mav', 25: '^^p', 26: 'QYO', 27: 'U~{', 28: 'V}M', 29: '-^{', 30: '*P&', 31: 'Adu', 32: 'cZa', 33: '<Hj', 34:
'e%g', 35: 'q|^', 36: 'o[Z', 37: 'MfK', 38: '/`C', 39: '6]K', 40: 'Ja1', 41: '[Hv', 42: 'bjk', 43: 'LE`', 44: 'FPl', 45: 'SOQ',
46: 'H=_', 47: '/7w', 48: 'Sl!', 49: '?ub', 50: 'tQ:', 51: '5~M', 52: '[pe', 53: 'hNM', 54: 'Rvg', 55: '75g', 56: 'w1/', 57: 'qD5', 58: 'HGW', 59: 'yut', 60: '3~`', 61: 'Emi', 62: '_QH', 63: 'ZJ[', 64: 'OlN', 65: 'J]x', 66: 'b%6', 67: 'nvb', 68: 'B`w', 69: '4d:', 70: '-T>', 71: 'a~G', 72: 'tBp', 73: 'x_E', 74: '0oB', 75: '<Kd', 76: 'rMj', 77: ';dt', 78: 'T=!', 79: '}Z?', 80: 'xD0', 81: 'L@+', 82: 'JFO', 83: 'ZLl', 84: 'n[=', 85: 'eR&'}}
######################

class Myhash:
    def __init__(self,num:int=2):
        if num == 3:
            self.dataframe = pandas.DataFrame().from_dict(data=dicta3)
            self.num = 3
        else:
            self.dataframe = pandas.DataFrame().from_dict(data=dicta2)
            self.num = 2
        global df
        df = self.dataframe


    def encoder(self,text:str):
        """
        No # in text
        """
        values = []
        for i in text:
            value = df["value"].iloc[df[df["Key"]==i].index].values[0]
            values.append(value)
        result = "".join(values)
        return result


    def decoder(self,text:str):
        keys = []
        try:
            for i in range(0,len(text),self.num):
                
                value = df["Key"].iloc[df[df["value"]==text[i:i+self.num]].index].values[0]
                keys.append(value)
        except Exception as e :
            print("Can't decode ")
            
        result = "".join(keys)    
        return result    
    
    def enlayers(self,text:str,num_of_layers:int):
        for i in range(num_of_layers):
            text = self.encoder(text)
        return text

    def delayers(self,text:str,num_of_layers:int):
        for i in range(num_of_layers):
            text = self.decoder(text)
        return text

    def creat_file_to_hash(self,output:str,value_per_key:int)->None:
        keys = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!$%&*+-/:;<=>?@[]^_`{|}~"
        value = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!$%&*+-/:;<=>?@[]^_`{|}~"
        with open(output,"w+") as file:
            col = ["Key","value"]
            w = csv.writer(file)
            w.writerow(col)
            for key in keys:
                values = ""
                for i in range(value_per_key):
                    values = values + str(value[random.randint(0,len(value)-1)])
                result = [f"{key}" , f"{values}"]
                w.writerow(result)
            file.close()


    
    


class Ui_MainWindow():#object
        def show(self):
                self.MainWindow.show()
        



        def setupUi(self):
                MainWindow = QMainWindow()
                self.MainWindow = MainWindow
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(540, 250)
                MainWindow.setMaximumWidth(540)
                MainWindow.setMaximumHeight(250)
                MainWindow.setStyleSheet(Styles.APP)
                MainWindow.setWindowIcon(QtGui.QIcon("Data\Icons\logo.png"))
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")



                self.tabs = QtWidgets.QTabWidget(self.centralwidget)
                self.tabs.setGeometry(QtCore.QRect(0, 0, 541, 251))
                self.tabs.setObjectName("tabs")
                # Tab 1 ---------
                self.tab_1 = QtWidgets.QWidget()
                self.tab_1.setObjectName("tab_1")
                
                self.progressBar = QtWidgets.QProgressBar(self.tab_1)
                self.progressBar.setGeometry(QtCore.QRect(20, 130, 501, 21))
                self.progressBar.setProperty("value", 0)
                self.progressBar.setObjectName("progressBar")
                self.statues_lbl = QtWidgets.QLabel(self.tab_1)
                self.statues_lbl.setGeometry(QtCore.QRect(0, 150, 531, 41))
                self.statues_lbl.setObjectName("statues_lbl")
                # Group Box of Login 
                self.groupBox_4 = QtWidgets.QGroupBox(self.tab_1)
                self.groupBox_4.setGeometry(QtCore.QRect(2, 0, 531, 81))
                self.groupBox_4.setObjectName("groupBox_4")
                self.label_7 = QtWidgets.QLabel(self.groupBox_4)
                self.label_7.setGeometry(QtCore.QRect(10, 20, 91, 21))
                self.label_7.setObjectName("label_7")
                self.label_8 = QtWidgets.QLabel(self.groupBox_4)
                self.label_8.setGeometry(QtCore.QRect(10, 50, 91, 21))
                self.label_8.setObjectName("label_8")
                self.user_input = QtWidgets.QLineEdit(self.groupBox_4)
                self.user_input.setGeometry(QtCore.QRect(110, 20, 131, 20))
                self.user_input.setObjectName("user_input")
                self.pwd_input = QtWidgets.QLineEdit(self.groupBox_4)
                self.pwd_input.setGeometry(QtCore.QRect(110, 50, 131, 20))
                self.pwd_input.setObjectName("pwd_input")
                self.pwd_input.setEchoMode(QtWidgets.QLineEdit.Password)
                self.label_9 = QtWidgets.QLabel(self.groupBox_4)
                self.label_9.setGeometry(QtCore.QRect(360, 10, 161, 21))
                self.label_9.setStyleSheet("color:rgb(32, 214, 0)")
                self.label_9.setObjectName("label_9")
                self.login_btn = QtWidgets.QPushButton(self.tab_1)
                self.login_btn.setGeometry(QtCore.QRect(250,20, 91, 51))
                self.user_login_labl = QtWidgets.QLabel(self.groupBox_4)
                self.user_login_labl.setGeometry(QtCore.QRect(360, 40, 161, 20))
                self.user_login_labl.setObjectName("user_login_labl")
                # Tab 1 ----
                self.start_btn = QtWidgets.QPushButton(self.tab_1)
                self.start_btn.setGeometry(QtCore.QRect(20, 90, 181, 31))
                self.start_btn.setObjectName("start_btn")
                #self.con_btn = QtWidgets.QPushButton(self.tab_1)
                #self.con_btn.setGeometry(QtCore.QRect(345, 90, 80, 31))
                #self.con_btn.setObjectName("con_btn")
                self.stop_btn = QtWidgets.QPushButton(self.tab_1)
                self.stop_btn.setGeometry(QtCore.QRect(365, 90, 131, 31))
                self.stop_btn.setObjectName("stop_btn")
                #self.stop_btn.setDisabled(True)
                self.check_btn = QtWidgets.QPushButton(self.tab_1)
                self.check_btn.setGeometry(QtCore.QRect(220, 90, 131, 31))
                self.check_btn.setObjectName("check_btn")
                self.version_lbl = QtWidgets.QLabel(self.tab_1)
                self.version_lbl.setGeometry(QtCore.QRect(260, 200, 141, 21))
                self.version_lbl.setObjectName("version_lbl")
                self.label_11 = QtWidgets.QLabel(self.tab_1)
                self.label_11.setGeometry(QtCore.QRect(10, 200, 241, 21))
                self.label_11.setObjectName("label_11")
                self.tabs.addTab(self.tab_1, "")
                self.tab_2 = QtWidgets.QWidget()
                self.tab_2.setObjectName("tab_2")
                self.scrollArea = QtWidgets.QScrollArea(self.tab_2)
                self.scrollArea.setGeometry(QtCore.QRect(0, 0, 531, 221))
                self.scrollArea.setWidgetResizable(True)
                self.scrollArea.setObjectName("scrollArea")
                self.scrollAreaWidgetContents = QtWidgets.QWidget()
                self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 529, 219))
                self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
                # Group Box of Paths 
                self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
                self.groupBox.setGeometry(QtCore.QRect(10, 10, 511, 80))
                self.groupBox.setObjectName("groupBox")
                self.label_4 = QtWidgets.QLabel(self.groupBox)
                self.label_4.setGeometry(QtCore.QRect(20, 20, 121, 16))
                self.label_4.setObjectName("label_4")
                self.phones_directory = QtWidgets.QLineEdit(self.groupBox)
                self.phones_directory.setGeometry(QtCore.QRect(150, 20, 311, 20))
                self.phones_directory.setObjectName("phones_directory")
                self.phone_tool_btn = QtWidgets.QToolButton(self.groupBox)
                self.phone_tool_btn.setGeometry(QtCore.QRect(470, 20, 31, 21))
                self.phone_tool_btn.setObjectName("phone_tool_btn")
                self.messages_directory = QtWidgets.QLineEdit(self.groupBox)
                self.messages_directory.setGeometry(QtCore.QRect(150, 50, 311, 20))
                self.messages_directory.setObjectName("messages_directory")
                self.message_tool_btn = QtWidgets.QToolButton(self.groupBox)
                self.message_tool_btn.setGeometry(QtCore.QRect(470, 50, 31, 21))
                self.message_tool_btn.setObjectName("message_tool_btn")
                self.label_5 = QtWidgets.QLabel(self.groupBox)
                self.label_5.setGeometry(QtCore.QRect(20, 50, 121, 16))
                self.label_5.setObjectName("label_5")
                
                # AI Message ------
                self.groupBox_5 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
                self.groupBox_5.setGeometry(QtCore.QRect(10, 160, 511, 51))
                self.groupBox_5.setFlat(False)
                self.groupBox_5.setCheckable(True)
                self.groupBox_5.setChecked(False)
                self.groupBox_5.setObjectName("groupBox_5")
                self.tasivalue = QtWidgets.QSpinBox(self.groupBox_5)
                self.tasivalue.setGeometry(QtCore.QRect(170, 20, 42, 22))
                self.tasivalue.setMinimum(10)
                self.tasivalue.setMaximum(10000)
                self.tasivalue.setProperty("value", 10)
                self.tasivalue.setObjectName("tasivalue")
                self.label_10 = QtWidgets.QLabel(self.groupBox_5)
                self.label_10.setGeometry(QtCore.QRect(10, 20, 151, 21))
                self.label_10.setObjectName("label_10")
                # Group Box of Time Option
                self.groupBox_3 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
                self.groupBox_3.setGeometry(QtCore.QRect(10, 100, 511, 51))
                self.groupBox_3.setObjectName("groupBox_3")
                self.label = QtWidgets.QLabel(self.groupBox_3)
                self.label.setGeometry(QtCore.QRect(10, 20, 131, 21))
                self.label.setObjectName("label")
                ###
                self.from_label = QtWidgets.QLabel(self.groupBox_3)  # start from index 
                self.from_label.setGeometry(QtCore.QRect(230, 20, 200, 21))
                self.from_label.setObjectName("from_label")
                self.from_label.setStyleSheet(Styles.LABEL)
                ###
                #self.to_label = QtWidgets.QLabel(self.groupBox_3)  # To
                #self.to_label.setGeometry(QtCore.QRect(375, 20, 21, 21))
                #self.to_label.setObjectName("to_label")
                #self.to_label.setStyleSheet(Styles.LABEL)
                ###
                #self.label_minus = QtWidgets.QLabel(self.groupBox_3)  # minus 
                #self.label_minus.setGeometry(QtCore.QRect(460, 20, 31, 21))
                #self.label_minus.setObjectName("label_minus")
                #self.label_minus.setStyleSheet(Styles.LABEL)
                ###
                self.time_sending_spin = QtWidgets.QSpinBox(self.groupBox_3)
                self.time_sending_spin.setGeometry(QtCore.QRect(140, 20, 42, 22))
                self.time_sending_spin.setMinimum(10)
                self.time_sending_spin.setMaximum(1000)
                self.time_sending_spin.setValue(65)
                self.time_sending_spin.setObjectName("time_sending_spin")
                self.time_sending_spin.setStyleSheet(Styles.SPINBOX)
                ##########
                self.index_start = QtWidgets.QSpinBox(self.groupBox_3)
                self.index_start.setGeometry(QtCore.QRect(420, 20, 41, 22))
                self.index_start.setMinimum(0)
                self.index_start.setMaximum(1000)
                self.index_start.setValue(0)
                self.index_start.setObjectName("index_start")
                self.index_start.setStyleSheet(Styles.SPINBOX)
                ##########
                #self.index_end = QtWidgets.QSpinBox(self.groupBox_3)
                #self.index_end.setGeometry(QtCore.QRect(400, 20, 42, 22))
                #self.index_end.setMinimum(0)
                #self.index_end.setMaximum(1000)
                #self.index_end.setValue(2)
                #self.index_end.setObjectName("index_end")
                #self.index_end.setStyleSheet(Styles.SPINBOX)
                self.scrollArea.setWidget(self.scrollAreaWidgetContents)
                self.tabs.addTab(self.tab_2, "")
                # Tab Hide ------------

                #self.tab = QtWidgets.QWidget()
                #self.tab.setObjectName("tab")
                #self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
                #self.groupBox_2.setGeometry(QtCore.QRect(2, 5, 531, 211))
                #self.groupBox_2.setCheckable(True)
                #self.groupBox_2.setObjectName("groupBox_2")
                #self.label_2 = QtWidgets.QLabel(self.groupBox_2)
                #self.label_2.setGeometry(QtCore.QRect(280, 20, 200, 100))
                #self.label_2.setObjectName("label_2")
                #self.tabs.addTab(self.tab, "")
                #self.label_3 = QtWidgets.QLabel(self.groupBox_2)
                #self.label_3.setGeometry(QtCore.QRect(20, 40, 141, 41))
                #self.label_3.setObjectName("label_3")
                #self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
                #self.pushButton.setGeometry(QtCore.QRect(20, 140, 141, 31))
                #self.pushButton.setObjectName("pushButton")
                #self.pushButton.setDisabled(True)
                # Tab 3 ------
                self.tab_3 = QtWidgets.QWidget()
                self.tab_3.setObjectName("tab_3")
                self.log_space = QtWidgets.QPlainTextEdit(self.tab_3)     #  Loging for Log Space
                self.log_space.setGeometry(QtCore.QRect(0, 0, 541, 231))
                self.log_space.setObjectName("log_space")
                self.log_space.setReadOnly(True)
                self.log_space.setStyleSheet("background-color:black; color:White;")
                self.tabs.addTab(self.tab_3, "")
                MainWindow.setCentralWidget(self.centralwidget)
                self.retranslateUi(MainWindow)
                self.tabs.setCurrentIndex(0)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)
                

        def retranslateUi(self, MainWindow):
                global _translate
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "WhatsApp Sender"))
                self.groupBox_4.setTitle(_translate("MainWindow", "Login"))
                self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">User Name</span></p></body></html>"))
                self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Password</span></p></body></html>"))
                self.version_lbl.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Version 2.0</span></p></body></html>"))
                self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Producer : Hesham Moawad</span></p></body></html>"))
                self.tabs.setTabText(self.tabs.indexOf(self.tab_1), _translate("MainWindow", "Run"))
                self.groupBox.setTitle(_translate("MainWindow", "Paths "))
                self.label_4.setText(_translate("MainWindow", "Numbers File Directory"))
                self.phone_tool_btn.setText(_translate("MainWindow", "..."))
                self.message_tool_btn.setText(_translate("MainWindow", "..."))
                self.label_5.setText(_translate("MainWindow", "Messages File Directory"))
                self.groupBox_5.setTitle(_translate("MainWindow", "AI Messaging"))
                self.label_10.setText(_translate("MainWindow", "Value that if Tasi Down from"))
                self.groupBox_3.setTitle(_translate("MainWindow", "Options"))
                self.label.setText(_translate("MainWindow", "Time to Send Messages "))
                #self.groupBox_2.setTitle(_translate("MainWindow", "Hide Option"))
                #self.label_2.setText(_translate("MainWindow", "QR Code Here"))
                #self.tabs.setTabText(self.tabs.indexOf(self.tab), _translate("MainWindow", "Hide"))
                self.tabs.setTabText(self.tabs.indexOf(self.tab_2), _translate("MainWindow", "Setting"))
                self.tabs.setTabText(self.tabs.indexOf(self.tab_3), _translate("MainWindow", "Logs"))
                #self.label_3.setText(_translate("MainWindow", "Scan QR code now and login "))
                self.start_btn.setDisabled(True)
                #self.log_space.setStyleSheet("background-color:black; color:green;")
                act.set(self.from_label,text="Count numbers that will sent to",stylesheet=Styles.LABEL)
                #act.set(self.to_label,text="To",stylesheet=Styles.LABEL)
                act.set(self.login_btn,text="Login",stylesheet=Styles.BUTTON)
                act.set(self.start_btn,text="Start",stylesheet=Styles.BUTTON)
                act.set(self.check_btn,text="Check Changes",stylesheet=Styles.BUTTON)
                act.set(self.stop_btn,text="Stop",stylesheet=Styles.BUTTON)
                self.tasivalue.setStyleSheet(Styles.SPINBOX)
                act.set(self.phones_directory,stylesheet=Styles.LINEDIT)
                act.set(self.messages_directory,stylesheet=Styles.LINEDIT)
                act.set(self.user_input,stylesheet=Styles.LINEDIT)
                act.set(self.pwd_input,stylesheet=Styles.LINEDIT)
                self.progressBar.setStyleSheet(Styles.PROGRESSBAR)
                self.check_btn.setDisabled(True)

                # Thread Part --------
                self.thread = Thread()
                self.thread.lock_start_btn.connect(self.start_btn.setDisabled)
                self.thread.statues.connect(act.set_statues)
                self.thread.log.connect(act.logs)
                self.start_btn.clicked.connect(self.thread.start)
                self.thread.message.connect(act.messagebox)
                self.thread.lock_check_btn.connect(ui.check_btn.setDisabled)
                self.thread.lock_check_btn.connect(act.setall_groups)
                self.thread2 = Thread2(self.thread)
                
                # End Thread Part --------
                self.check_btn.clicked.connect(act.check_changes)
                self.phone_tool_btn.clicked.connect(act.dialog_p)
                self.message_tool_btn.clicked.connect(act.dialog_m)
                self.login_btn.clicked.connect(act.login)
                self.stop_btn.clicked.connect(self.thread2.start)
                
                # Make Hints to all Objects
                act.set(self.start_btn,hint="لتشغيل البرنامج لكن يجب ضبط الاعدادات لفتح هذا الزر")               
                act.set(self.login_btn,hint="لوج و اخلص يا عم كدا كدا مكان الباص مش شغال اصلا ")
                act.set(self.progressBar,hint="النسبة المؤية لعدد الارقام التى تم المرور من خلالها")
                act.set(self.statues_lbl,hint="الرقم الذى يتم العمل عليه حاليا")
                act.set(self.phones_directory,hint="ادخال مسار ملف الارقام المراد العمل عليها")
                act.set(self.phone_tool_btn,hint="فتح الملفات لتحديد ملف الارقام المراد")
                act.set(self.messages_directory,hint="ادخال مسار ملف الرسائل المراد العمل عليها")
                act.set(self.message_tool_btn,hint="فتح الملفات لتحديد ملف الرسائل المراد")
                act.set(self.groupBox_3,hint="ضبط اعدادات الوقت")
                act.set(self.time_sending_spin,hint="عدد الثوانى المراد انتظارها بين كل رقم لارسال الرسالة")
                act.set(self.groupBox_5,hint="ذكاء اصتناعى بسيط لتحديد افضل الرسائل بالنسبة لوقت الجلسة و حالة السوق بشكل عام")
                act.set(self.tasivalue,hint="عدد النقاط التى اذا زاد هبوط السوق عنها يتم استخدام رسائل التعليق")
                act.set(self.log_space,hint="مش تبعك دى بتعتى انا و متلعبش فى اى حاجة تانى وخلاص")
                act.set(self.check_btn,hint="لتتاكد من صحة الاعدادات فى البرنامج و الغاء القفل فى زر البداية")
                act.set(self.label_11,hint="انا دا على فكرة ^_^")
                act.set(self.version_lbl,hint="اصدار البرنامج الحالى")
                act.set(self.stop_btn,hint="لتسجيل الخروج من الواتساب و ايقاف البرنامج و يمكنك تشغيله مرة اخرى بدون مشاكل")
                act.set(self.index_start,hint="فهرس الرقم المراد البدء منه فى شيت الاكسيل")
                act.set(self.from_label,hint="لتحديد العدد المراد الارسال له فقط")

                

                


class Actions(QtCore.QObject):
        def __init__(self) -> None:
                super().__init__()

        @staticmethod
        def messagebox(text,type=QMessageBox.Information)->None: # that mean this Function not working outside Class
            messagebox = QMessageBox()
            messagebox.setIcon(type)
            messagebox.setText(f"\t{text}\t")
            messagebox.setWindowTitle(" Warning ")
            messagebox.exec_()

        @staticmethod  # that mean this Function not working with calling a var of class
        def set(func,text=None,stylesheet=None,hint=None,clear =None,icon=None,progressvalue:int=None,plantext:str=None)->None:
                        """ text: the argument that change the text of object 
                        hint:the qrgument that change tooltip text (بيغير النص اللى بيظهر لما بتقف بالماوس شوية على العنصر) """
                        if text !=None :
                                func.setText(_translate("MainWindow", text))
                        if stylesheet!=None:
                                func.setStyleSheet(str(stylesheet))
                        if hint!=None:
                                func.setToolTip(hint)
                        if clear == True:
                                func.clear()
                        if icon!=None:
                                func.setIcon(icon)
                        if progressvalue != None :
                                func.setValue(progressvalue)
                        if plantext!=None:
                                func.appendPlainText(plantext)
                                


        def check_changes(self)->list:
                phone_path = ui.phones_directory.text()
                message_path = ui.messages_directory.text()
                time_sending_spin = ui.time_sending_spin.value()
                if ".xlsx" not in phone_path or ".xlsx" not in message_path:
                        self.messagebox("There is no Path please Check settings and try again")
                        ui.start_btn.setDisabled(True)
                else:
                        ui.start_btn.setDisabled(False)
                
                if ui.groupBox_5.isChecked():
                        ai = True
                        tasi_val = int(ui.tasivalue.text())
                        return [phone_path,message_path,time_sending_spin,tasi_val]

                return [phone_path,message_path,time_sending_spin]



        def dialog_m(self):
                file_filter = 'Data File (*.xlsx *.csv *.dat);; Excel File (*.xlsx *.xls)'
                dir = QtWidgets.QFileDialog.getOpenFileName(
                caption='Select a data file',
                filter=file_filter)
                try:
                        t = str(dir[0])#.split("/")[-1]
                        self.set(ui.messages_directory,text=f"{t}")
                except TypeError :
                        pass


        def dialog_p(self):

                file_filter = 'Data File (*.xlsx *.csv *.dat);; Excel File (*.xlsx *.xls)'
                dir = QtWidgets.QFileDialog.getOpenFileName(
                caption='Select a data file',
                filter=file_filter)
                try:
                        t = str(dir[0])#.split("/")[-1]
                        self.set(ui.phones_directory,text=f"{t}")
                except TypeError :
                        pass
        

        def login(self):
                self.user = ui.user_input.text()
                if self.user == "":
                        self.messagebox(" Please enter your username !")
                else:
                        ui.user_input.clear()
                        ui.pwd_input.clear()
                        ui.check_btn.setDisabled(False)
                        self.set(ui.user_login_labl,text=f"Welcome {self.user}",stylesheet=Styles.LABEL)
                        self.setall_groups(False)
                        ui.groupBox_4.setDisabled(True)
                        ui.login_btn.setDisabled(True)
                        self.set(ui.label_9,text="Login Succefully ^_^",stylesheet=Styles.LABEL+"color:lightgreen;")
                        
        def setall_groups(self,val:bool):
                ui.groupBox.setDisabled(val)
                ui.groupBox_3.setDisabled(val)
                ui.groupBox_5.setDisabled(val)

        
        def set_statues(self,phone,phone_index,len_phones):
                if "966" in phone:
                        act.set(ui.statues_lbl,text=f"\t\t\t  +{phone} in Progress . . .   ",stylesheet=Styles.LABEL+"font-weight: 900")
                        act.set(ui.progressBar,progressvalue=float(round((phone_index+1)/len_phones,3)*100))#,stylesheet=Styles.PROGRESSBAR
                else:
                        act.set(ui.statues_lbl,text=phone,stylesheet=Styles.LABEL+"font-weight: 800")
                        act.set(ui.progressBar,progressvalue=0)#,stylesheet=Styles.PROGRESSBAR


        def logs(self,text:str):
                time = datetime.now()
                plaintext = f"{time.date()} {time.hour}-{time.minute} : {text}"#
                act.set(ui.log_space,plantext=plaintext)
                if "xlsx" not in text:
                        logging.info(text)
               

        def contniue(self):
                pass
      
        def name(self)->str:
                return  self.user

       
class Thread2(QThread):
        
        def run(self):
                
                ui.thread.kill()
                ui.check_btn.setDisabled(False)
                act.setall_groups(False)

class Thread(QThread):
        lock_start_btn = pyqtSignal(bool)
        statues = pyqtSignal(str,int,int)
        log = pyqtSignal(str)
        lock_check_btn = pyqtSignal(bool)
        message = pyqtSignal(str)
        #whats = Whatsapp()

        def msg_ai(self,setting)->str:
                stock = StockInfo()
                s = stock.tasi_statues()
                if len(setting)>3:
                        if s[0]=="down":
                                if int(s[1].split(".")[0]) >= setting[3]:
                                        return "tasi down"
                                else:
                                        return stock.time_sission()
                        else:    
                                return stock.time_sission()
                else:
                        return "messages"

        def run(self):
                try:
                        self.log.emit(" App Started Now ")
                        self.lock_start_btn.emit(True)
                        self.lock_check_btn.emit(True)
                        self.statues.emit("\t\t\t\tApp Start ^_^ " ,0,0)
                        self.setting = act.check_changes()
                        path1= str(self.setting[0]).split("/")[-1]
                        path2= str(self.setting[1]).split("/")[-1]
                        self.log.emit(f"Username : {act.name()}    {path1} is phone path * {path2} is message path ")
                        self.whats.start_browser(self.setting)
                        phone_numbers = self.whats.convert_list(self.whats.contact_file,"Number")
                        self.log.emit(f" Length of numbers is {len(phone_numbers)}")
                        value = ui.index_start.value()
                        type = self.msg_ai(self.setting)
                        messages = self.whats.convert_list(self.whats.msg_file,type)
                        self.log.emit(f" Message Type is : {type}")
                        if 0 < value < len(phone_numbers):
                                phone_numbers = phone_numbers[0:value]
                        if len(messages)<1:
                                self.message.emit(" Please add More Messages to sheet and press start again ")
                                self.lock_start_btn.emit(False)
                        else:
                                index = 0
                                sent = 0
                                while index <= len(phone_numbers)-1:
                                        phone = str(phone_numbers[index])
                                        index += 1
                                        self.log.emit(f" +{phone} in Progress... index {index} sent {sent}")
                                        QThread.msleep(100)
                                        """
                                                # Database connection Online
                                                con = Database_connection()
                                                df= Dataframe(con.connect()) # DB_name info to make connection
                                                df.set_col_name()# col_name
                                                if df.is_double(phone):
                                                        # code -----
                                                else:
                                                        self.log.emit(f" +{phone} Is Double Skipped ")
                                        """
                                        self.statues.emit(phone,index,len(phone_numbers))
                                        if self.whats.check_number(f"+{phone}"):
                                                if self.whats.search(phone) == False:
                                                        try:
                                                                self.whats.send_msg_to_phone(f"+{phone}",self.whats.random_msg(messages))
                                                                self.log.emit(f" Message was sent for +{phone}")
                                                                sent += 1
                                                        except:
                                                                self.whats.driver.get("https://web.whatsapp.com/")
                                                                QThread.sleep(3)
                                                                self.log.emit(" Message not sent for there are an error in phone number")
                                                else:
                                                        self.whats.search_.clear()
                                                        self.log.emit(f" already exist Skipped")
                                        else:
                                                self.log.emit(f" +{phone} Dosen't match and Skipped")
                                
                                self.log.emit(" Progress Finished Good Luck ")
                        
                        self.whats.exit()
                        QThread.sleep(3)
                        self.lock_start_btn.emit(False)
                        self.lock_check_btn.emit(False)
                        self.statues.emit(f"\t\t\t\tFinished ^_^   ",0,1)
                        self.message.emit("\t\t\t\t Finished ")
                except Exception as e :
                        self.log.emit(f"{e}")
                        self.lock_check_btn.emit(False)
                        self.lock_start_btn.emit(False)
                        self.statues.emit("\t\t\t\t Stoped ",0,0)
                        self.message.emit("Stoped")
                        
                        
        def kill(self):
                try:
                        self.whats.exit()
                except Exception as e :
                        self.log.emit(f"{e}")
                        self.whats.driver.quit()
                self.statues.emit("\t\t\t\t Stoped ",0,0)
                self.message.emit("Stoped")
                self.quit()
                self.terminate()
                self.wait()
                
        








if __name__ == "__main__":
        import sys
        app = QApplication(sys.argv)
        app_icon = QtGui.QIcon()
        app_icon.addFile('Data\Icons\logo.png', QtCore.QSize(16,16))
        app_icon.addFile('Data\Icons\logo.png', QtCore.QSize(24,24))
        app_icon.addFile('Data\Icons\logo.png', QtCore.QSize(32,32))
        app_icon.addFile('Data\Icons\logo.png', QtCore.QSize(48,48))
        app_icon.addFile('Data\Icons\logo.png', QtCore.QSize(256,256))
        app.setWindowIcon(app_icon)
        ui = Ui_MainWindow()
        global act 
        act = Actions()
        ui.setupUi()
        try:
                get('http://google.com')
                con = True
        except ConnectionError as e:
                con = False
                act.messagebox(" Please check Connection and try again ")
        if con==True:
                ui.show() 
                sys.exit(app.exec_())
        else:
                pass


        #ui.show() 
        #sys.exit(app.exec_())

        






"""
                
class QTextEditLogger(logging.Handler):
    def __init__(self, parent):
        super().__init__()
        self.widget = QtWidgets.QPlainTextEdit(parent)
        self.widget.setReadOnly(True)

    def emit(self, record):
        msg = self.format(record)
        self.widget.appendPlainText(msg)



try:
                        
                        self.whats = Whatsapp(act.check_changes())
                        phone_numbers, messages = self.whats.convert()
                        phone_index = 0
                        while phone_index <= len(phone_numbers)-1 and self._running == True:
                                phone_index +=1
                                phone = str(phone_numbers[phone_index])
                                logging.info(f"{phone} in Progress ...")
                                #
                                )
                                print(int(phone_index+1/len(phone_numbers))*100)
                                if self.whats.check_number(f"+{phone}"):
                                        try:
                                                self.whats.search_.clear()
                                        except Exception as e :
                                                logging.info(e)
                                        if self.whats.search(self.whats.phone_s(f"+{phone}")) == False and self._running==True:
                                                self.whats.send_msg_to_phone(f"+{phone}",self.whats.random_msg(messages))
                                                logging.info(f" Message was sent for +{phone}")
                                else:
                                        logging.info(f"+{phone} Dosen't match and Skipped")
                except Exception as e :
                        logging.info("\n e \n")

class WhatsappTask():

      
        def __init__(self):
                
                #self.thread = threading.Thread(target = self.run, args =(),daemon=True)
                self._running = True
                
        def terminate(self):

                self._running = False
        

        def run(self):
                try:
                        ui.start_btn.setDisabled(True)
                        self.whats = Whatsapp(act.check_changes())
                        phone_numbers, messages = self.whats.convert()
                        phone_index = 0
                        while phone_index <= len(phone_numbers)-1 and self._running == True:
                                phone_index +=1
                                phone = str(phone_numbers[phone_index])
                                logging.info(f"{phone} in Progress ...")
                                act.set(ui.statues_lbl,text=f"             +{phone} in Progress . . . ",stylesheet=Styles.LABEL[0])#
                                ui.progressBar.setProperty("value",(int(phone_index)/len(phone_numbers)*100))
                                print(int(phone_index+1/len(phone_numbers))*100)
                                if self.whats.check_number(f"+{phone}"):
                                        try:
                                                self.whats.search_.clear()
                                        except Exception as e :
                                                logging.info(e)
                                        if self.whats.search(self.whats.phone_s(f"+{phone}")) == False and self._running==True:
                                                self.whats.send_msg_to_phone(f"+{phone}",self.whats.random_msg(messages))
                                                logging.info(f" Message was sent for +{phone}")
                                else:
                                        logging.info(f"+{phone} Dosen't match and Skipped")
                except Exception as e :
                        logging.info("\n e \n")
                        

                        

class Tasks(QtCore.QObject):
    def __init__(self):
        super(Tasks, self).__init__()
        self.pool = QtCore.QThreadPool.globalInstance()
        self.pool.setMaxThreadCount(8)

    def start(self):
        worker = Worker()
        self.pool.start(worker)

        #self.pool.waitForDone()




from PyQt5 import QtCore

class Worker(QtCore.QRunnable):
    def __init__(self):
        ui.start_btn.setDisabled(True)
        super().__init__()
    
    def send(self,phone,messages):
        if self.whats.check_number(f"+{phone}"):
                if self.whats.search(self.whats.phone_s(f"+{phone}")) == False:
                        self.whats.send_msg_to_phone(f"+{phone}",self.whats.random_msg(messages))
                        logging.info(f" Message was sent for +{phone}")
                else:
                        self.whats.search_.clear()
        else:
                        logging.info(f"+{phone} Dosen't match and Skipped")

    def sets(self,phone,phone_index,phone_numbers):
        logging.info(f"{phone} in Progress ...")
        act.set(ui.statues_lbl,text=f"               +{phone} in Progress . . . ",stylesheet=Styles.LABEL[0])#
        ui.progressBar.setProperty("value",float(round((phone_index+1)/phone_numbers,3)*100))
        

    def run(self):
        self.whats = Whatsapp(act.check_changes())
        phone_numbers, messages = self.whats.convert()
        phone_index = 0
        while phone_index <= len(phone_numbers)-1 :
                phone_index +=1
                phone = str(phone_numbers[phone_index])
                th = threading.Thread(target=self.send,args=(phone,messages),daemon=True)
                th2 = threading.Thread(target=self.sets,args=(phone,phone_index,len(phone_numbers)),daemon=True)
                th2.start()
                th.start()
                th2.join()
                th.join()
                        
"""
        