import pymysql
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from datetime import datetime

form_class = uic.loadUiType('beacon.ui')[0]


class Login(QWidget, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.stackedWidget_3.setCurrentIndex(0)
        self.login.clicked.connect(self.MoveLoginPage)
        self.home1.clicked.connect(self.MainPage)
        self.home3.clicked.connect(self.MainPage)
        self.home4.clicked.connect(self.MainPage)
        self.attend.clicked.connect(self.Enter_check)
        self.schedule.clicked.connect(self.Schedule_check)
        self.logbtn.clicked.connect(self.Login)
        self.logout.clicked.connect(self.Logout)
        self.enter_btn_2.clicked.connect(self.attend_check)
        self.out.clicked.connect(self.attend_out)
        self.enter_btn.clicked.connect(self.outing)
        self.enter_btn_7.clicked.connect(self.Back)
        self.logyn = False
        self.calendarWidget.clicked.connect(self.calwrite)
        self.plus.clicked.connect(self.add_time)

    def add_time(self):
        self.line = self.lineEdit.text()

        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='00000000', db='beacon',
                                   charset='utf8')
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO calendar (번호,이름,내용,날짜) VALUES ('{(self.result[0][0])}','{self.result[0][1]}','{self.line}','{self.date}')")
        cursor.execute(f"SELECT * FROM calendar where 날짜 = '{self.date}'")
        self.a = cursor.fetchall()
        conn.commit()
        conn.close()
        # print(self.a,'날짜별로 저장된값 출력')
        # print(len(self.a),'저장된값 개수 파악')
        # print(self.a[0])
        # print(len(self.a[0]))
        Row = 0
        self.tableWidget.setRowCount(len(self.a))
        for i in self.a:
            # print(i,'해당날짜 db내용 전부 출력')
            self.tableWidget.setItem(Row, 0, QTableWidgetItem(i[3]))    # 날짜
            self.tableWidget.setItem(Row, 1, QTableWidgetItem(i[1]))    # 이름
            self.tableWidget.setItem(Row, 2, QTableWidgetItem(i[2]))    # 내용
            Row += 1
            # print(Row,'로우값에 따른 추가 반영 )
    def calwrite(self):
        self.cal = self.calendarWidget.selectedDate()
        self.date = (str(self.cal.year()) + '-' + str(self.cal.month()) + '-' + str(self.cal.day()))


    def MoveLoginPage(self):                        # 로그인 페이지로 이동하는 함수
        self.stackedWidget.setCurrentIndex(0)

    def MainPage(self):                             # 메인페이지로 이동하는 함수
        self.stackedWidget.setCurrentIndex(1)

    def Enter_check(self):                          # 입실 눌렀을때 함수
        if self.logyn == True:                      # 로그인 여부가 참일떄
            self.stackedWidget.setCurrentIndex(2)   # 입실 버튼누를수 있는 페이지로 이동
            self.enter_time.setText(f"{self.result[0][6]}") # 입실 누르면 데이터에 저장된 시간 라벨에 표시
            self.finish_time.setText(f"{self.result[0][7]}")    # 퇴실
            self.out_time.setText(f"{self.result[0][10]}")      # 외출
            self.back_time.setText(f"{self.result[0][11]}")     # 복귀
        else:                                                   # 로그인 여부가 거짓일때
            QMessageBox.information(self, "로그인", f"로그인 해야 출석체크 할수있습니다.") # 메세지 나오게 함

    def Schedule_check(self):                           # 출석체크 함수
        if self.logyn == True:                          # 로그인 여부가 참일때 출석체크 페이지로 이동
            self.stackedWidget.setCurrentIndex(3)
        else:
            QMessageBox.information(self, "로그인", f"로그인 해야 열람 가능합니다.")

    def Login(self):                                    # 로그인 할때

        self.id = self.idtext.text()                    # 입력한 값이 id
        self.pw = self.pwtext.text()                    # 입력한 값이 pw

        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='00000000', db='beacon',
                               charset='utf8')          # db 연결
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM beacon where 아이디 = %s",self.id)  # db에 있는 해당 아이디의 행의 값을 가져옴
        self.result = cursor.fetchall()
        print(self.result)
        conn.close()

        if self.id == '' or self.pw == '':                              # 아이디나 비밀번호가 공백일때  로그인 오류 표시
            QMessageBox.critical(self, "로그인 오류", "정보를 입력하세요")
            # return # 의미는 무엇인가

        elif self.result == ():                                         # 일치하는 값이 없으면 ()로 나옴 그때 오류 표시
            QMessageBox.critical(self, "로그인 오류", "일치하는 정보가 없습니다")

        elif self.result[0][2] == self.id and self.result[0][3] == self.pw:     # 아이디와 비밀번호가 일치했을때  로그인 성공 메시지 표시함
            QMessageBox.information(self, "로그인 성공", f"{self.result[0][1]}님 로그인 성공하셨습니다")
            self.stackedWidget_3.setCurrentIndex(1)                     # 로그인 버튼이 로그아웃 버튼으로 변경
            self.stackedWidget.setCurrentIndex(1)                       # 로그인시 메인페이지로 이동
            self.logyn = True                                           # 로그인 여부가 참

    def Logout(self):                                                   # 로그아웃
        QMessageBox.information(self, "로그아웃 성공", f"{self.result[0][1]}님 로그아웃하셨습니다")
        self.stackedWidget_3.setCurrentIndex(0)                         # 로그아웃 버튼이 로그인으로 변경
        # self.stackedWidget_4.setCurrentIndex(1)
        self.logyn = False                                              # 로그인 여부 거짓

    def attend_check(self):
        self.now = datetime.now()
        self.time = self.now.strftime('%Y-%m-%d %H:%M')
        print(self.time)
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='00000000', db='beacon',
                               charset='utf8')
        cursor = conn.cursor()
        # # 데이터 추가하기
        cursor.execute(f"update beacon set 입실시간 = '{self.time}' where 번호 = {self.result[0][0]}")
        # DB 저장
        conn.commit()
        # DB 닫기
        conn.close()
        QMessageBox.information(self, "입실", f"{self.result[0][1]}님 입실하셨습니다")
        self.enter_time.setText(self.now.strftime('%Y-%m-%d %H:%M'))

    def attend_out(self):
        self.now = datetime.now()
        self.time = self.now.strftime('%Y-%m-%d %H:%M')
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='00000000', db='beacon',
                               charset='utf8')
        cursor = conn.cursor()
        # # 데이터 추가하기
        cursor.execute(f"update beacon set 퇴실시간 = '{self.time}' where 번호 = {self.result[0][0]}")
        # DB 저장
        conn.commit()
        # DB 닫기
        conn.close()
        QMessageBox.information(self, "퇴실", f"{self.result[0][1]}님 퇴실하셨습니다")
        self.finish_time.setText(self.now.strftime('%Y-%m-%d %H:%M'))

    def outing(self):
        self.now = datetime.now()
        self.time = self.now.strftime('%Y-%m-%d %H:%M')
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='00000000', db='beacon',
                               charset='utf8')
        cursor = conn.cursor()
        # # 데이터 추가하기
        cursor.execute(f"update beacon set 외출시간 = '{self.time}' where 번호 = {self.result[0][0]}")
        # DB 저장
        conn.commit()
        # DB 닫기
        conn.close()
        QMessageBox.information(self, "외출", f"{self.result[0][1]}님 외출하셨습니다")
        self.out_time.setText(self.now.strftime('%Y-%m-%d %H:%M'))

    def Back(self):
        self.now = datetime.now()
        self.time = self.now.strftime('%Y-%m-%d %H:%M')
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='00000000', db='beacon',
                               charset='utf8')
        cursor = conn.cursor()
        # # 데이터 추가하기
        cursor.execute(f"update beacon set 복귀시간 = '{self.time}' where 번호 = {self.result[0][0]}")
        # DB 저장
        conn.commit()
        # DB 닫기
        conn.close()
        QMessageBox.information(self, "복귀", f"{self.result[0][1]}님 복귀하셨습니다")
        self.back_time.setText(self.now.strftime('%Y-%m-%d %H:%M'))



if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = QtWidgets.QStackedWidget()

    mainWindow = Login()

    widget.addWidget(mainWindow)

    widget.setFixedHeight(800)
    widget.setFixedWidth(1200)
    widget.show()
    app.exec_()