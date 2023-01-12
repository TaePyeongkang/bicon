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


    def attandence_check_page(self):
        self.stackedWidget.setCurrentIndex(6)
    def attandence_check(self):

        conn = pymysql.connect(host='10.10.21.119', port=3306, user='yh', password='00000000', db='beacon',
                               charset='utf8')
        cursor = conn.cursor()
        # # 데이터 추가하기
        cursor.execute(f"select * from attandence_check where 이름 = '{self.result[0][2]}'")
        # DB 저장
        conn.commit()
        # DB 닫기
        conn.close()
        self.check_attandence = cursor.fetchall()
        print(self.check_attandence)
        print('----------------------------------------------------------------------------------')
        Row = 0
        self.tableWidget_2.setRowCount(len(self.check_attandence))
        for f in self.check_attandence:
            # print(f,'해당날짜 db내용 전부 출력')
            self.tableWidget_2.setItem(Row, 0, QTableWidgetItem(f[10]))  # 이름
            self.tableWidget_2.setItem(Row, 1, QTableWidgetItem(f[4]))   # 결석
            self.tableWidget_2.setItem(Row, 2, QTableWidgetItem(f[0]))   # 출석시간
            self.tableWidget_2.setItem(Row, 3, QTableWidgetItem(f[1]))   # 퇴실시간
            self.tableWidget_2.setItem(Row, 4, QTableWidgetItem(f[2]))   # 외출시간
            self.tableWidget_2.setItem(Row, 5, QTableWidgetItem(f[3]))   # 복귀시간
            self.tableWidget_2.setItem(Row, 6, QTableWidgetItem(f[5]))   # 출석일
            self.tableWidget_2.setItem(Row, 7, QTableWidgetItem(f[6]))   # 지각
            self.tableWidget_2.setItem(Row, 8, QTableWidgetItem(f[7]))   # 조퇴
            self.tableWidget_2.setItem(Row, 9, QTableWidgetItem(f[8]))   # 외출
            self.tableWidget_2.setItem(Row, 10, QTableWidgetItem(f[9]))  # 결석
            Row += 1
            # print(Row,'로우값에 따른 추가 반영')

    def dm_inquire(self):               # 교수만 메시지 조회하는 매서드
        if self.logyn == True:
            if self.result[0][1] == 97 or self.result[0][1] == 98 or self.result[0][1] == 99:
                self.stackedWidget.setCurrentIndex(4)
                self.combo1 = self.comboBox_2.currentText()
                self.combo = self.comboBox.currentText()
                conn = pymysql.connect(host='10.10.21.119', port=3306, user='yh', password='00000000', db='beacon',
                                       charset='utf8')
                cursor = conn.cursor()
                # cursor.execute(f"SELECT * FROM beacon where 아이디 = %s", self.id)
                # print(self.id,'아이디 확인')
                # cursor.execute(f"SELECT * FROM dm where 교수 = '{self.combo}'")
                cursor.execute(f"SELECT * FROM dm where 이름 = '{self.combo1}' and 교수 = '{self.combo}'")
                self.check = cursor.fetchall()
                # print(self.combo1)
                # print(self.check,'내용 조회')
                Row = 0
                self.dm_table_2.setRowCount(len(self.check))
                for c in self.check:
                    # print(c,'해당날짜 db내용 전부 출력')
                    self.dm_table_2.setItem(Row, 0, QTableWidgetItem(c[1]))    # 이름
                    self.dm_table_2.setItem(Row, 1, QTableWidgetItem(c[2]))    # 내용
                    self.dm_table_2.setItem(Row, 2, QTableWidgetItem(c[3]))    # 시간
                    self.dm_table_2.setItem(Row, 3, QTableWidgetItem(c[4]))    # 날짜
                    Row += 1
                    # print(Row,'로우값에 따른 추가 반영 )
            else:
                QMessageBox.information(self, "열람", f"교수만 열람 가능합니다.")
    def dm_page(self):      # 학생이 로그인하면 그때 메세지 보낼수 있는 페이지로 이동 교수는 안됨
        # if self.result[0][1] <= 27:

        if self.result[0][1] <= 27:
            self.stackedWidget.setCurrentIndex(5)
        else:
            QMessageBox.information(self, "학생", f"학생만 열람 가능합니다.")
        # else:
        #     self.stackedWidget.setCurrentIndex(4)

    def sending_dm(self):       # 교수에게 메세지 보내는 매서드
        self.dm = self.dm_text.text()
        self.now = datetime.now()
        self.the_day = self.now.strftime('%Y-%m-%d')
        self.the_time = self.now.strftime('%H:%M')
        self.combo = self.comboBox.currentText()
        print(self.combo)
        # print(self.dm,'입력한값 확인')
        conn = pymysql.connect(host='10.10.21.119', port=3306, user='yh', password='00000000', db='beacon',
                               charset='utf8')
        cursor = conn.cursor()
        # cursor.execute(f"SELECT * FROM beacon where 아이디 = %s", self.id)
        # print(self.id,'아이디 확인')
        cursor.execute(
            f"INSERT INTO dm (번호,이름,내용,시간,날짜,교수) VALUES ('{(self.result[0][1])}','{(self.result[0][2])}','{self.dm}','{self.the_time}','{self.the_day}','{self.combo}')")
        cursor.execute(f"SELECT * FROM dm where 이름 = '{(self.result[0][2])}' and 교수 = '{(self.combo)}'")

        self.dm = cursor.fetchall()
        conn.commit()
        conn.close()
        # print(123)
        print(self.dm)
        # print(456)

        Row = 0
        self.dm_table.setRowCount(len(self.dm))
        for x in self.dm:
            # print(x, '해당날짜 db내용 전부 출력')
            self.dm_table.setItem(Row, 0, QTableWidgetItem(x[1]))  # 이름
            self.dm_table.setItem(Row, 1, QTableWidgetItem(x[2]))  # 내용
            self.dm_table.setItem(Row, 2, QTableWidgetItem(x[4]))  # 날짜
            self.dm_table.setItem(Row, 3, QTableWidgetItem(x[3]))  # 시간
            Row += 1
            # print(Row,'로우값에 따른 추가 반영 )
    def add_time(self):                     # 캘린더에 일정 추가하는 함수
        self.line = self.lineEdit.text()

        conn = pymysql.connect(host='10.10.21.119', port=3306, user='yh', password='00000000', db='beacon',
                                   charset='utf8')
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO calendar (구분,번호,이름,내용,날짜) VALUES ('{(self.result[0][0])}','{(self.result[0][1])}','{self.result[0][2]}','{self.line}','{self.date}')")
        cursor.execute(f"SELECT * FROM calendar where 날짜 = '{self.date}' and 이름 = '{self.result[0][2]}'")
        self.a = cursor.fetchall()
        conn.commit()
        conn.close()
        print(self.a,'날짜별로 저장된값 출력')
        # print(len(self.a),'저장된값 개수 파악')
        # print(self.a[0])
        # print(len(self.a[0]))
        Row = 0
        self.tableWidget.setRowCount(len(self.a))
        for i in self.a:
            print(i,'해당날짜 db내용 전부 출력')
            self.tableWidget.setItem(Row, 0, QTableWidgetItem(i[4]))    # 구분
            self.tableWidget.setItem(Row, 1, QTableWidgetItem(i[3]))    # 날짜
            self.tableWidget.setItem(Row, 2, QTableWidgetItem(i[1]))    # 이름
            self.tableWidget.setItem(Row, 3, QTableWidgetItem(i[2]))    # 내용
            Row += 1
            # print(Row,'로우값에 따른 추가 반영 )
        # self.tableWidget.clearContents()
    def calwrite(self):     # 날짜 yyyy-mm-dd로 나타내는 함수
        self.cal = self.calendarWidget.selectedDate()
        self.date = (str(self.cal.year()) + '-' + str(self.cal.month()) + '-' + str(self.cal.day()))

    def MoveLoginPage(self):                        # 로그인 페이지로 이동하는 함수
        self.stackedWidget.setCurrentIndex(0)

    def MainPage(self):                             # 메인페이지로 이동하는 함수
        self.stackedWidget.setCurrentIndex(1)

    def Enter_check(self):                                                                       # 입실 눌렀을때 함수
        if self.logyn == True:                                                                   # 로그인 여부가 참일떄
            if self.result[0][1] <= 27:
                # print('출석체크 학생만 들어가도록 체크')
                self.stackedWidget.setCurrentIndex(2)                                            # 입실 버튼누를수 있는 페이지로 이동
                self.enter_time.setText(f"{self.result[0][7]}")                                  # 입실 누르면 데이터에 저장된 시간 라벨에 표시
                self.stackedWidget_4.setCurrentIndex(0)
                # self.stackedWidget_5.setCurrentIndex(1)
                self.finish_time.setText(f"{self.result[0][8]}")                                 # 퇴실
                self.out_time.setText(f"{self.result[0][11]}")                                   # 외출
                self.stackedWidget_4.setCurrentIndex(0)
                self.back_time.setText(f"{self.result[0][12]}")                                  # 복귀
            else:
                # print('확인 작업')
                QMessageBox.information(self, "알림", f"출석체크는 학생만 할수있습니다.")
        else:                                                                                   # 로그인 여부가 거짓일때
            QMessageBox.information(self, "로그인", f"로그인 해야 출석체크 할수있습니다.")           # 메세지 나오게 함

    def Schedule_check(self):                                                         # 출석체크 함수
        if self.logyn == True:                                                        # 로그인 여부가 참일때 출석체크 페이지로 이동
            self.stackedWidget.setCurrentIndex(3)
        else:
            QMessageBox.information(self, "로그인", f"로그인 해야 열람 가능합니다.")       #

    def Login(self):                                                                                         # 로그인 할때

        self.id = self.idtext.text()                                                                         # 입력한 값이 id
        self.pw = self.pwtext.text()                                                                         # 입력한 값이 pw

        conn = pymysql.connect(host='10.10.21.119', port=3306, user='yh', password='00000000', db='beacon',
                               charset='utf8')                                                                # db 연결
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM beacon where 아이디 = %s",self.id)                                      # db에 있는 해당 아이디의 행의 값을 가져옴
        self.result = cursor.fetchall()
        conn.close()
        # print(self.result)

        if self.id == '' or self.pw == '':                                                                     # 아이디나 비밀번호가 공백일때  로그인 오류 표시
            QMessageBox.critical(self, "로그인 오류", "정보를 입력하세요")
            # return # 의미는 무엇인가

        elif self.result == ():                                                                                 # 일치하는 값이 없으면 ()로 나옴 그때 오류 표시
            QMessageBox.critical(self, "로그인 오류", "일치하는 정보가 없습니다")

        elif self.result[0][3] == self.id and self.result[0][4] == self.pw:                                     # 아이디와 비밀번호가 일치했을때  로그인 성공 메시지 표시함
            if self.result[0][1] <= 27:
                QMessageBox.information(self, "로그인 성공", f"{self.result[0][2]}님 로그인 성공하셨습니다")
                self.stackedWidget_3.setCurrentIndex(1)                                                         # 로그인 버튼이 로그아웃 버튼으로 변경
                self.stackedWidget.setCurrentIndex(1)                                                           # 로그인시 메인페이지로 이동
                self.logyn = True                                                                               # 로그인 여부가 참
            else:
                QMessageBox.information(self, "로그인 성공", f"{self.result[0][2]} 교수님 로그인 성공하셨습니다")
                self.stackedWidget_3.setCurrentIndex(1)                                                         # 로그인 버튼이 로그아웃 버튼으로 변경
                self.stackedWidget.setCurrentIndex(1)                                                           # 로그인시 메인페이지로 이동
                self.logyn = True                                                                               # 로그인 여부가 참

    def Logout(self):                                                                                # 로그아웃
        QMessageBox.information(self, "로그아웃 성공", f"{self.result[0][2]}님 로그아웃하셨습니다")
        self.stackedWidget_3.setCurrentIndex(0)                                                      # 로그아웃 버튼이 로그인으로 변경
        # self.stackedWidget_4.setCurrentIndex(1)
        self.logyn = False                                                                           # 로그인 여부 거짓

    def attend_check(self):                                                                                    # 입실 체크 하는 함수
        self.stackedWidget_5.setCurrentIndex(0)
        self
        self.now = datetime.now()
        # self.time = self.now.strftime('%Y-%m-%d %H:%M')
        self.time = self.now.strftime('%H:%M:%S')
        self.day = self.now.strftime('%Y-%m-%d')
        print(self.time)
        conn = pymysql.connect(host='10.10.21.119', port=3306, user='yh', password='00000000', db='beacon',
                               charset='utf8')
        cursor = conn.cursor()
        # # 데이터 추가하기
        # cursor.execute(f"update beacon set 입실시간 = '{self.time}', 출석여부 = '{'O'}' where 번호 = {self.result[0][1]}")
        cursor.execute(f"insert into attandence_check (출석시간,날짜,이름) values ('{(self.time)}','{(self.day)}','{self.result[0][2]}')")



        # DB 저장
        conn.commit()
        # DB 닫기
        conn.close()
        QMessageBox.information(self, "입실", f"{self.result[0][2]}님 입실하셨습니다")
        self.enter_time.setText(self.now.strftime('%Y-%m-%d %H:%M'))
        self.stackedWidget_4.setCurrentIndex(1)
####

    def attend_out(self):                                                                                      # 퇴실 체크하는 함수
        self.now = datetime.now()
        # self.time = self.now.strftime('%Y-%m-%d %H:%M')
        self.time = self.now.strftime('%H:%M:%S')
        self.day = self.now.strftime('%Y-%m-%d')
        conn = pymysql.connect(host='10.10.21.119', port=3306, user='yh', password='00000000', db='beacon',
                               charset='utf8')
        cursor = conn.cursor()
        # # 데이터 추가하기
        cursor.execute(f"update attandence_check set 퇴실시간 = '{self.time}' where 이름 = '{self.result[0][2]}' and 날짜 = '{self.day}'")
        # cursor.execute(
            # f"insert into attandence_check (출석시간,날짜,이름) values ('{(self.time)}','{(self.day)}','{self.result[0][2]}')")
        # DB 저장
        conn.commit()
        # DB 닫기
        conn.close()
        QMessageBox.information(self, "퇴실", f"{self.result[0][2]}님 퇴실하셨습니다")
        self.finish_time.setText(self.now.strftime('%Y-%m-%d %H:%M'))
        self.stackedWidget_4.setCurrentIndex(2)
        self.stackedWidget_5.setCurrentIndex(1)
    def outing(self):                                                                                           # 외출체크하는 함수
        self.now = datetime.now()
        # self.time = self.now.strftime('%Y-%m-%d %H:%M')
        self.time = self.now.strftime('%H:%M:%S')
        self.day = self.now.strftime('%Y-%m-%d')
        conn = pymysql.connect(host='10.10.21.119', port=3306, user='yh', password='00000000', db='beacon',
                               charset='utf8')
        cursor = conn.cursor()
        # # 데이터 추가하기
        # cursor.execute(f"update beacon set 외출시간 = '{self.time}', 외출여부 = '{'O'}' where 번호 = {self.result[0][1]}")
        cursor.execute(f"update attandence_check set 외출시간 = '{self.time}' where 이름 = '{self.result[0][2]}' and 날짜 = '{self.day}'")
        # DB 저장
        conn.commit()
        # DB 닫기
        conn.close()
        QMessageBox.information(self, "외출", f"{self.result[0][2]}님 외출하셨습니다")
        self.out_time.setText(self.now.strftime('%Y-%m-%d %H:%M'))
        self.stackedWidget_4.setCurrentIndex(3)
        self.stackedWidget_5.setCurrentIndex(1)


    def Back(self):                                                                                             # 복귀체크하는 함수
        self.now = datetime.now()
        # self.time = self.now.strftime('%Y-%m-%d %H:%M')
        self.time = self.now.strftime('%H:%M:%S')
        self.day = self.now.strftime('%Y-%m-%d')
        conn = pymysql.connect(host='10.10.21.119', port=3306, user='yh', password='00000000', db='beacon',
                               charset='utf8')
        cursor = conn.cursor()
        # # 데이터 추가하기
        # cursor.execute(f"update beacon set 복귀시간 = '{self.time}', 복귀여부 = '{'O'}' where 번호 = {self.result[0][1]}")
        cursor.execute(f"update attandence_check set 복귀시간 = '{self.time}' where 이름 = '{self.result[0][2]}' and 날짜 = '{self.day}'")
        # DB 저장
        conn.commit()
        # DB 닫기
        conn.close()
        QMessageBox.information(self, "복귀", f"{self.result[0][2]}님 복귀하셨습니다")
        self.back_time.setText(self.now.strftime('%Y-%m-%d %H:%M'))
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