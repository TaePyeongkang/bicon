import pymysql
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QComboBox
from datetime import datetime

form_class = uic.loadUiType('beacon.ui')[0]


class Login(QWidget, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(1)
        self.logyn = False
        self.stackedWidget_3.setCurrentIndex(0)
        self.login.clicked.connect(self.MoveLoginPage)
        self.home1.clicked.connect(self.MainPage)
        self.home3.clicked.connect(self.MainPage)
        self.home4.clicked.connect(self.MainPage)
        self.home4_3.clicked.connect(self.MainPage)
        self.home4_2.clicked.connect(self.MainPage)
        self.home4_4.clicked.connect(self.MainPage)
        self.home3_3.clicked.connect(self.MainPage)
        self.home3_4.clicked.connect(self.MainPage)
        self.attend.clicked.connect(self.Enter_check)
        self.schedule.clicked.connect(self.Schedule_check)
        self.logbtn.clicked.connect(self.Login)
        self.logout.clicked.connect(self.Logout)
        self.enter_btn_2.clicked.connect(self.attend_check)
        self.out.clicked.connect(self.attend_out)
        self.enter_btn.clicked.connect(self.outing)
        self.enter_btn_7.clicked.connect(self.Back)
        self.calendarWidget.clicked.connect(self.calwrite)
        self.plus.clicked.connect(self.add_time)
        self.message.clicked.connect(self.dm_page)
        self.message_2.clicked.connect(self.dm_inquire)
        self.dm_send.clicked.connect(self.sending_dm)
        self.dm_text.returnPressed.connect(self.sending_dm)
        self.inquire.clicked.connect(self.dm_inquire)
        self.attend_2.clicked.connect(self.attandence_check_page)
        self.pushButton.clicked.connect(self.attandence_check)
        self.pushButton_3.clicked.connect(self.attandence_count)
        self.pushButton_4.clicked.connect(self.payout)

    def attandence_count(self):
        conn = pymysql.connect(host='10.10.21.119', port=3306, user='yh', password='00000000', db='beacon',
                               charset='utf8')
        cursor = conn.cursor()
        # # ????????? ????????????
        cursor.execute(f"select * from beacon where ????????? = '{self.result[0][3]}'")
        # DB ??????
        conn.commit()
        # DB ??????
        self.result = cursor.fetchall()
        conn.close()
        print(self.result,'123123112123')
        # print(self.chulcheck[0][11])

        # ????????????[8],????????????[9],?????????[11],??????[12],??????[13],,??????[14],??????[15],????????????[16],????????????[17]
        # ??????
        if self.result[0][7] == None or self.result[0][8] == None:
            print('????????????')
            conn = pymysql.connect(host='10.10.21.119', port=3306, user='yh', password='00000000', db='beacon',
                                   charset='utf8')
            cursor = conn.cursor()
            # # ????????? ????????????
            cursor.execute(
                f"UPDATE beacon SET ?????? = '{self.result[0][15] + 1}' WHERE ?????? = '{self.result[0][1]}'")
            cursor.execute(
                f"insert into attadence (??????,??????,??????) values ('O','{self.result[0][18]}','{self.result[0][2]}')")
            # DB ??????
            conn.commit()
            # DB ??????
            conn.close()

            conn = pymysql.connect(host='10.10.21.119', port=3306, user='yh', password='00000000', db='beacon',
                                   charset='utf8')
            cursor = conn.cursor()

            # # ????????? ????????????
            cursor.execute(f"UPDATE beacon SET ???????????? = NULL ,???????????? = NULL,???????????? = NULL, ???????????? = NULL ?????? = NULL WHERE ?????? = '{self.result[0][1]}'")
            # DB ??????
            conn.commit()
            # DB ??????
            conn.close()

            # ??????
        elif self.result[0][7] < '09:20:59' and self.result[0][8] > '17:20:59' and self.result[0][16] == None and self.result[0][17] == None:

            print('?????? ??????')

            conn = pymysql.connect(host='10.10.21.119', port=3306, user='yh', password='00000000', db='beacon',
                                   charset='utf8')
            cursor = conn.cursor()
            # # ????????? ????????????
            cursor.execute(f"UPDATE beacon SET ????????? = '{self.result[0][11] + 1}' WHERE ?????? = '{self.result[0][1]}'")
            # print('123123')
            cursor.execute(f"insert into attadence (??????,??????,??????) values ('O','{self.result[0][18]}','{self.result[0][2]}')")
            # DB ??????
            conn.commit()
            # DB ??????

            conn.close()

            conn = pymysql.connect(host='10.10.21.119', port=3306, user='yh', password='00000000', db='beacon',
                                   charset='utf8')
            cursor = conn.cursor()

            # # ????????? ????????????
            cursor.execute(f"UPDATE beacon SET ???????????? = NULL ,???????????? = NULL, ?????? = NULL, ???????????? = NULL, ???????????? = NULL WHERE ?????? = '{self.result[0][1]}'")
            # DB ??????
            conn.commit()
            # DB ??????
            conn.close()



            # ??????
        elif self.result[0][7] > '09:20:59' and self.result[0][8] > '17:20:59':
            # print('123123')
            time_5 = datetime.strptime(self.result[0][8], "%H:%M:%S")
            time_6 = datetime.strptime('09:20:59', "%H:%M:%S")
            time_interval3 = time_5 - time_6
            print(time_interval3.seconds, '?????? ????????? ?????? ??????')
            conn = pymysql.connect(host='10.10.21.119', port=3306, user='yh', password='00000000', db='beacon',
                                   charset='utf8')
            cursor = conn.cursor()
            # # ????????? ????????????
            cursor.execute(f"UPDATE beacon SET ????????? = '{self.result[0][11] + 1}', ?????? = '{self.result[0][12] + 1}' WHERE ?????? = '{self.result[0][1]}'")
            cursor.execute(
                f"insert into attadence (??????,??????,??????,?????????) values ('O','{self.result[0][18]}','{self.result[0][2]}','{time_interval3}')")
            # DB ??????
            conn.commit()
            # DB ??????
            conn.close()

            # # ????????? ????????????
            cursor.execute(f"UPDATE beacon SET ???????????? = NULL ,???????????? = NULL, ?????? = NULL, ???????????? = NULL, ???????????? = NULL WHERE ?????? = '{self.result[0][1]}'")
            # DB ??????
            conn.commit()
            # DB ??????
            conn.close()

        # ??????
        elif self.result[0][7] < '09:20:59' and self.result[0][8] > '17:20:59' and self.result[0][16] != None and self.result[0][17] != None:
            print('123123')
            time_1 = datetime.strptime(self.result[0][16], "%H:%M:%S")
            time_2 = datetime.strptime(self.result[0][17], "%H:%M:%S")
            #
            time_interval1 = time_2 - time_1
            print(time_interval1.seconds, '?????? ????????? ?????? ??????')
            # print(777777777777777777777777)
            conn = pymysql.connect(host='10.10.21.119', port=3306, user='yh', password='00000000', db='beacon',
                                   charset='utf8')
            cursor = conn.cursor()
            # # ????????? ????????????
            cursor.execute(
                f"UPDATE beacon SET ????????? = '{self.result[0][11] + 1}', ?????? = '{self.result[0][14] + 1}' WHERE ?????? = '{self.result[0][1]}'")
            cursor.execute(
                f"insert into attadence (??????,??????,??????,?????????) values ('O','{self.result[0][18]}','{self.result[0][2]}','{time_interval1}')")
            # cursor.execute(f"select * from attadence where ?????? = '{self.result[0][2]}'")
            # DB ??????
            # self.chchchc = cursor.fetchall()
            conn.commit()
            # DB ??????
            conn.close()
            # print(self.chchchc, '????????????')
            # print(self.chchchc[0][7], '????????????')
            # print(self.chchchc[0][7][0],'????????????')

            conn = pymysql.connect(host='10.10.21.119', port=3306, user='yh', password='00000000', db='beacon',
                                   charset='utf8')
            cursor = conn.cursor()

            # # ????????? ????????????
            cursor.execute(f"UPDATE beacon SET ???????????? = NULL ,???????????? = NULL, ?????? = NULL, ???????????? = NULL, ???????????? = NULL WHERE ?????? = '{self.result[0][1]}'")
            # DB ??????
            conn.commit()
            # DB ??????
            conn.close()

            # ??????
        elif self.result[0][7] < '09:20:59' and self.result[0][8] < '17:20:59':
            time_3 = datetime.strptime(self.result[0][8], "%H:%M:%S")
            time_4 = datetime.strptime('17:20:59', "%H:%M:%S")
            #
            time_interval2 = time_4 - time_3
            print(time_interval2.seconds, '?????? ????????? ?????? ??????')
            # print(777777777777777777777777)
            conn = pymysql.connect(host='10.10.21.119', port=3306, user='yh', password='00000000', db='beacon',
                                   charset='utf8')
            cursor = conn.cursor()
            # # ????????? ????????????
            cursor.execute(
                f"UPDATE beacon SET ????????? = '{self.result[0][11] + 1}', ?????? = '{self.result[0][13] + 1}' WHERE ?????? = '{self.result[0][1]}'")
            cursor.execute(
                f"insert into attadence (??????,??????,??????,?????????) values ('O','{self.result[0][18]}','{self.result[0][2]}','{time_interval2}')")

            conn.commit()
            # # DB ??????
            conn.close()

            conn = pymysql.connect(host='10.10.21.119', port=3306, user='yh', password='00000000', db='beacon',
                                   charset='utf8')
            cursor = conn.cursor()

            # # ????????? ????????????
            cursor.execute(f"UPDATE beacon SET ???????????? = NULL ,???????????? = NULL, ?????? = NULL WHERE ?????? = '{self.result[0][1]}'")
            # DB ??????
            conn.commit()
            # DB ??????
            conn.close()



    def payout(self):
        self.stackedWidget.setCurrentIndex(8)
        conn = pymysql.connect(host='10.10.21.119', port=3306, user='yh', password='00000000', db='beacon',
                               charset='utf8')
        cursor = conn.cursor()
        # # ????????? ????????????
        cursor.execute(f"select * from beacon where ?????? = '{self.result[0][2]}'")
        # DB ??????
        conn.commit()
        self.alllll = cursor.fetchall()
        conn.close()
        conn = pymysql.connect(host='10.10.21.119', port=3306, user='yh', password='00000000', db='beacon',
                               charset='utf8')
        cursor = conn.cursor()
        # # ????????? ????????????
        cursor.execute(f"select * from attadence WHERE ?????? = '{self.result[0][2]}'")
        # DB ??????
        conn.commit()
        # DB ??????
        self.money = cursor.fetchall()
        conn.close()
        # print(self.money)
        # print(self.money[0][7])
        # print(self.money[0][7][0],'?????????')

        asx = int(self.money[0][7][0])
        # if asx != 0:
        # print(type(asx))
        asx += 1
        # print(f"'{self.result[0][2]}'??? ???????????????{(self.result[0][11]*12000)-(asx*1250)}????????????")
        self.label_23.setText(f"{self.result[0][2]}??? ???????????????{(self.result[0][11]*10000)-(self.result[0][12]*asx*1250)-(self.result[0][13]*asx*1250)-(self.result[0][14]*asx*1250)}????????????")

    def attandence_check_page(self):
        # ?????? ????????????
        self.stackedWidget.setCurrentIndex(6)
        if self.result[0][1] <= 27:
            # print(self.result[0][1])
            # ????????????[8],????????????[9],?????????[11],??????[12],??????[13],,??????[14],??????[15],????????????[16],????????????[17]
            self.stackedWidget.setCurrentIndex(7)
            self.enter_time_3.setText(str(self.result[0][11]))  # ?????????
            self.finish_time_3.setText(str(self.result[0][12]))  # ??????
            self.out_time_3.setText(str(self.result[0][13]))  # ??????
            self.back_time_3.setText(str(self.result[0][14]))  # ??????
            self.back_time_4.setText(str(self.result[0][15]))  # ??????

    def attandence_check(self):

        if self.result[0][1] > 27:
            conn = pymysql.connect(host='10.10.21.119', port=3306, user='yh', password='00000000', db='beacon',
                                   charset='utf8')
            cursor = conn.cursor()
            # # ????????? ????????????
            cursor.execute(f"select * from beacon where ?????? ='??????'")
            # DB ??????
            conn.commit()
            # DB ??????
            conn.close()
            self.professor_attandence_check = cursor.fetchall()
            # print(self.professor_attandence_check)
            # print(len(self.professor_attandence_check))
            # print('????????? ?????? ????????? ???????????? ??????')
            Row = 0
            self.tableWidget_2.setRowCount(len(self.professor_attandence_check))
            for bb in self.professor_attandence_check:
                # print(bb, '???????????? ?????? db?????? ?????? ??????')
                # print(bb[11])
                # ????????????[8],????????????[9],?????????[11],??????[12],??????[13],,??????[14],??????[15],????????????[16],????????????[17]
                self.tableWidget_2.setItem(Row, 0, QTableWidgetItem(bb[2]))  # ??????
                self.tableWidget_2.setItem(Row, 2, QTableWidgetItem(str(bb[12])))  # ??????
                self.tableWidget_2.setItem(Row, 1, QTableWidgetItem(str(bb[11])))  # ?????????
                self.tableWidget_2.setItem(Row, 3, QTableWidgetItem(str(bb[13])))  # ??????
                self.tableWidget_2.setItem(Row, 4, QTableWidgetItem(str(bb[14])))  # ??????
                self.tableWidget_2.setItem(Row, 5, QTableWidgetItem(str(bb[15])))  # ??????
                Row += 1
                # print(Row, '???????????? ?????? ?????? ??????')

    def dm_inquire(self):  # ????????? ????????? ???????????? ?????????
        if self.logyn == True:
            if self.result[0][1] == 97 or self.result[0][1] == 98 or self.result[0][1] == 99:

                self.stackedWidget.setCurrentIndex(4)
                self.combo1 = self.comboBox_2.currentText()
                self.combo = self.comboBox.currentText()
                conn = pymysql.connect(host='10.10.21.119', port=3306, user='yh', password='00000000', db='beacon',
                                       charset='utf8')
                cursor = conn.cursor()
                # cursor.execute(f"SELECT * FROM beacon where ????????? = %s", self.id)
                # print(self.id,'????????? ??????')
                # cursor.execute(f"SELECT * FROM dm where ?????? = '{self.combo}'")
                cursor.execute(f"SELECT * FROM dm where ?????? = '{self.combo1}' and ?????? = '{self.combo}'")
                self.check = cursor.fetchall()
                # print(self.combo1)
                # print(self.check,'?????? ??????')
                Row = 0
                self.dm_table_2.setRowCount(len(self.check))
                for c in self.check:
                    # print(c,'???????????? db?????? ?????? ??????')
                    self.dm_table_2.setItem(Row, 0, QTableWidgetItem(c[1]))  # ??????
                    self.dm_table_2.setItem(Row, 1, QTableWidgetItem(c[2]))  # ??????
                    self.dm_table_2.setItem(Row, 2, QTableWidgetItem(c[3]))  # ??????
                    self.dm_table_2.setItem(Row, 3, QTableWidgetItem(c[4]))  # ??????
                    Row += 1
                    # print(Row,'???????????? ?????? ?????? ?????? )
        else:
            QMessageBox.information(self, "??????", f"????????? ?????? ???????????????.")

    def dm_page(self):  # ????????? ??????????????? ?????? ????????? ????????? ?????? ???????????? ?????? ????????? ??????
        # if self.result[0][1] <= 27:

        if self.result[0][1] <= 27:
            self.stackedWidget.setCurrentIndex(5)
        else:
            QMessageBox.information(self, "??????", f"????????? ?????? ???????????????.")
        # else:
        #     self.stackedWidget.setCurrentIndex(4)

    def sending_dm(self):  # ???????????? ????????? ????????? ?????????
        self.dm = self.dm_text.text()
        self.now = datetime.now()
        self.the_day = self.now.strftime('%Y-%m-%d')
        self.the_time = self.now.strftime('%H:%M')
        self.combo = self.comboBox.currentText()
        # print(self.combo)
        # print(self.dm,'???????????? ??????')
        conn = pymysql.connect(host='10.10.21.119', port=3306, user='yh', password='00000000', db='beacon',
                               charset='utf8')
        cursor = conn.cursor()
        # cursor.execute(f"SELECT * FROM beacon where ????????? = %s", self.id)
        # print(self.id,'????????? ??????')
        cursor.execute(
            f"INSERT INTO dm (??????,??????,??????,??????,??????,??????) VALUES ('{(self.result[0][1])}','{(self.result[0][2])}','{self.dm}','{self.the_time}','{self.the_day}','{self.combo}')")

        cursor.execute(f"SELECT * FROM dm where ?????? = '{(self.result[0][2])}' and ?????? = '{(self.combo)}'")

        self.dm = cursor.fetchall()
        conn.commit()
        conn.close()
        # print(123)
        print(self.dm)
        # print(456)

        Row = 0
        self.dm_table.setRowCount(len(self.dm))
        for x in self.dm:
            # print(x, '???????????? db?????? ?????? ??????')
            self.dm_table.setItem(Row, 0, QTableWidgetItem(x[1]))  # ??????
            self.dm_table.setItem(Row, 1, QTableWidgetItem(x[2]))  # ??????
            self.dm_table.setItem(Row, 2, QTableWidgetItem(x[4]))  # ??????
            self.dm_table.setItem(Row, 3, QTableWidgetItem(x[3]))  # ??????
            Row += 1
            # print(Row,'???????????? ?????? ?????? ?????? )

    def add_time(self):  # ???????????? ?????? ???????????? ??????
        self.line = self.lineEdit.text()

        conn = pymysql.connect(host='10.10.21.119', port=3306, user='yh', password='00000000', db='beacon',
                               charset='utf8')
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO calendar (??????,??????,??????,??????,??????) VALUES ('{(self.result[0][0])}','{(self.result[0][1])}','{self.result[0][2]}','{self.line}','{self.date}')")
        cursor.execute(f"SELECT * FROM calendar where ?????? = '{self.date}' and ?????? = '{self.result[0][2]}'")
        self.a = cursor.fetchall()
        conn.commit()
        conn.close()
        # print(self.a,'???????????? ???????????? ??????')
        # print(len(self.a),'???????????? ?????? ??????')
        # print(self.a[0])
        # print(len(self.a[0]))
        Row = 0
        self.tableWidget.setRowCount(len(self.a))
        for i in self.a:
            # print(i,'???????????? db?????? ?????? ??????')
            self.tableWidget.setItem(Row, 0, QTableWidgetItem(i[4]))  # ??????
            self.tableWidget.setItem(Row, 1, QTableWidgetItem(i[3]))  # ??????
            self.tableWidget.setItem(Row, 2, QTableWidgetItem(i[1]))  # ??????
            self.tableWidget.setItem(Row, 3, QTableWidgetItem(i[2]))  # ??????
            Row += 1
            # print(Row,'???????????? ?????? ?????? ?????? )
        # self.tableWidget.clearContents()

    def calwrite(self):  # ?????? yyyy-mm-dd??? ???????????? ??????
        self.cal = self.calendarWidget.selectedDate()
        self.date = (str(self.cal.year()) + '-' + str(self.cal.month()) + '-' + str(self.cal.day()))

    def MoveLoginPage(self):  # ????????? ???????????? ???????????? ??????
        self.stackedWidget.setCurrentIndex(0)

    def MainPage(self):  # ?????????????????? ???????????? ??????
        self.stackedWidget.setCurrentIndex(1)

    def Enter_check(self):  # ?????? ???????????? ??????
        if self.logyn == True:  # ????????? ????????? ?????????
            if self.result[0][1] <= 27:
                conn = pymysql.connect(host='10.10.21.119', port=3306, user='yh', password='00000000', db='beacon',
                                       charset='utf8')  # db ??????
                cursor = conn.cursor()

                cursor.execute(f"SELECT * FROM beacon where ????????? = '{self.result[0][3]}'")
                self.check_a = cursor.fetchall()
                print(self.check_a)
                # print('???????????? ????????? ??????????????? ??????')
                self.stackedWidget.setCurrentIndex(2)  # ?????? ??????????????? ?????? ???????????? ??????
                self.enter_time.setText(str(f"{self.check_a[0][7]}"))  # ?????? ????????? ???????????? ????????? ?????? ????????? ??????
                # print(self.enter_time)
                self.stackedWidget_4.setCurrentIndex(0)
                # self.stackedWidget_5.setCurrentIndex(1)
                self.finish_time.setText(f"{self.check_a[0][8]}")  # ??????
                self.out_time.setText(f"{self.check_a[0][16]}")  # ??????
                self.stackedWidget_4.setCurrentIndex(0)
                self.back_time.setText(f"{self.check_a[0][17]}")  # ??????
                # if self.result[0][7] == '':
                #     self.stackedWidget_4.setCurrentIndex(0)                                      # ?????? ????????? ?????? ????????? ???????????? ????????????
                # else:
                #     self.stackedWidget_4.setCurrentIndex(1)
                # if self.result[0][8] == '':
                #     self.stackedWidget_4.setCurrentIndex(1)
                # else:
                #     self.stackedWidget_4.setCurrentIndex(2)
            else:
                # print('?????? ??????')
                QMessageBox.information(self, "??????", f"??????????????? ????????? ??????????????????.")
        else:  # ????????? ????????? ????????????
            QMessageBox.information(self, "?????????", f"????????? ?????? ???????????? ??????????????????.")  # ????????? ????????? ???

    def Schedule_check(self):  # ???????????? ??????
        if self.logyn == True:  # ????????? ????????? ????????? ???????????? ???????????? ??????
            self.stackedWidget.setCurrentIndex(3)
        else:
            QMessageBox.information(self, "?????????", f"????????? ?????? ?????? ???????????????.")  #

    def Login(self):  # ????????? ??????

        self.id = self.idtext.text()  # ????????? ?????? id
        self.pw = self.pwtext.text()  # ????????? ?????? pw
        conn = pymysql.connect(host='10.10.21.119', port=3306, user='yh', password='00000000', db='beacon',
                               charset='utf8')  # db ??????
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM beacon where ????????? = %s", self.id)  # db??? ?????? ?????? ???????????? ?????? ?????? ?????????
        self.result = cursor.fetchall()
        conn.close()
        # print(self.result)

        if self.id == '' or self.pw == '':  # ???????????? ??????????????? ????????????  ????????? ?????? ??????
            QMessageBox.critical(self, "????????? ??????", "????????? ???????????????")
            # return # ????????? ????????????

        elif self.result == ():  # ???????????? ?????? ????????? ()??? ?????? ?????? ?????? ??????
            QMessageBox.critical(self, "????????? ??????", "???????????? ????????? ????????????")

        elif self.result[0][3] == self.id and self.result[0][4] == self.pw:  # ???????????? ??????????????? ???????????????  ????????? ?????? ????????? ?????????
            if self.result[0][1] <= 27:
                QMessageBox.information(self, "????????? ??????", f"{self.result[0][2]}??? ????????? ?????????????????????")
                # print(self.result[0][2])
                self.stackedWidget_3.setCurrentIndex(1)  # ????????? ????????? ???????????? ???????????? ??????
                self.stackedWidget.setCurrentIndex(1)  # ???????????? ?????????????????? ??????
                self.logyn = True  # ????????? ????????? ???
            else:
                QMessageBox.information(self, "????????? ??????", f"{self.result[0][2]} ????????? ????????? ?????????????????????")
                self.stackedWidget_3.setCurrentIndex(1)  # ????????? ????????? ???????????? ???????????? ??????
                self.stackedWidget.setCurrentIndex(1)  # ???????????? ?????????????????? ??????
                self.logyn = True  # ????????? ????????? ???

    def Logout(self):  # ????????????
        QMessageBox.information(self, "???????????? ??????", f"{self.result[0][2]}??? ???????????????????????????")
        self.stackedWidget_3.setCurrentIndex(0)  # ???????????? ????????? ??????????????? ??????
        # self.stackedWidget_4.setCurrentIndex(1)
        self.logyn = False  # ????????? ?????? ??????

    def attend_check(self):  # ?????? ?????? ?????? ??????
        self.stackedWidget_5.setCurrentIndex(0)
        self.now = datetime.now()
        # self.time = self.now.strftime('%Y-%m-%d %H:%M')
        self.time = self.now.strftime('%H:%M:%S')
        self.day = self.now.strftime('%Y-%m-%d')
        # print(self.time)
        conn = pymysql.connect(host='10.10.21.119', port=3306, user='yh', password='00000000', db='beacon',
                               charset='utf8')
        cursor = conn.cursor()
        # # ????????? ????????????
        # cursor.execute(f"update beacon set ???????????? = '{self.time}', ???????????? = '{'O'}' where ?????? = {self.result[0][1]}")
        cursor.execute(
            f"update beacon set ???????????? = '{(self.time)}',?????? = '{(self.day)}' where ????????? = '{self.result[0][3]}'")
        cursor.execute(
            f"select * from attandence_check ")

        # DB ??????
        conn.commit()
        # DB ??????
        conn.close()
        self.time_check = cursor.fetchall()
        # print(self.time_check)
        # print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
        QMessageBox.information(self, "??????", f"{self.result[0][2]}??? ?????????????????????")
        self.enter_time.setText(self.now.strftime('%H:%M:%S'))
        self.stackedWidget_4.setCurrentIndex(1)

        ####

    def attend_out(self):  # ?????? ???????????? ??????
        self.now = datetime.now()
        # self.time = self.now.strftime('%Y-%m-%d %H:%M')
        self.time = self.now.strftime('%H:%M:%S')
        self.day = self.now.strftime('%Y-%m-%d')
        conn = pymysql.connect(host='10.10.21.119', port=3306, user='yh', password='00000000', db='beacon',
                               charset='utf8')
        cursor = conn.cursor()
        # # ????????? ????????????
        cursor.execute(
            f"update beacon set ???????????? = '{(self.time)}',?????? = '{(self.day)}' where ????????? = '{self.result[0][3]}'")
        # cursor.execute(
        # f"insert into attandence_check (????????????,??????,??????) values ('{(self.time)}','{(self.day)}','{self.result[0][2]}')")
        # DB ??????
        conn.commit()
        # DB ??????
        conn.close()
        QMessageBox.information(self, "??????", f"{self.result[0][2]}??? ?????????????????????")
        self.finish_time.setText(self.now.strftime('%H:%M:%S'))
        self.stackedWidget_4.setCurrentIndex(2)
        self.stackedWidget_5.setCurrentIndex(1)

    def outing(self):  # ?????????????????? ??????
        self.now = datetime.now()
        # self.time = self.now.strftime('%Y-%m-%d %H:%M')
        self.time = self.now.strftime('%H:%M:%S')
        self.day = self.now.strftime('%Y-%m-%d')
        conn = pymysql.connect(host='10.10.21.119', port=3306, user='yh', password='00000000', db='beacon',
                               charset='utf8')
        cursor = conn.cursor()
        # # ????????? ????????????
        # cursor.execute(f"update beacon set ???????????? = '{self.time}', ???????????? = '{'O'}' where ?????? = {self.result[0][1]}")
        cursor.execute(
            f"update beacon set ???????????? = '{(self.time)}',?????? = '{(self.day)}' where ????????? = '{self.result[0][3]}'")
        # DB ??????
        conn.commit()
        # DB ??????
        conn.close()
        QMessageBox.information(self, "??????", f"{self.result[0][2]}??? ?????????????????????")
        self.out_time.setText(self.now.strftime('%H:%M:%S'))
        self.stackedWidget_4.setCurrentIndex(3)
        self.stackedWidget_5.setCurrentIndex(1)

    def Back(self):  # ?????????????????? ??????
        self.now = datetime.now()
        # self.time = self.now.strftime('%Y-%m-%d %H:%M')
        self.time = self.now.strftime('%H:%M:%S')
        self.day = self.now.strftime('%Y-%m-%d')
        conn = pymysql.connect(host='10.10.21.119', port=3306, user='yh', password='00000000', db='beacon',
                               charset='utf8')
        cursor = conn.cursor()
        # # ????????? ????????????
        # cursor.execute(f"update beacon set ???????????? = '{self.time}', ???????????? = '{'O'}' where ?????? = {self.result[0][1]}")
        cursor.execute(
            f"update beacon set ???????????? = '{(self.time)}',?????? = '{(self.day)}' where ????????? = '{self.result[0][3]}'")
        # DB ??????
        conn.commit()
        # DB ??????
        conn.close()
        QMessageBox.information(self, "??????", f"{self.result[0][2]}??? ?????????????????????")
        self.back_time.setText(self.now.strftime('%H:%M:%S'))
        self.stackedWidget_4.setCurrentIndex(1)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = QtWidgets.QStackedWidget()

    mainWindow = Login()

    widget.addWidget(mainWindow)

    widget.setFixedHeight(800)
    widget.setFixedWidth(1200)
    widget.show()
    app.exec_()
