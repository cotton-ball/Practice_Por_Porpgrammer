from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QCoreApplication

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

from acid_rain_game import AcidRainGame  # 산성비 게임
from typing_practice import TypingPractice  # 타자연습

from rain_radio_menu import RainRadioMenu  # 산성비 게임 난이도, 언어 선택 메뉴
from typing_radio_menu import TypingRadioMenu  # 타자연습 긴글, 짧은글 선택 메뉴
from leaderboard import LeaderBoard   #리더보드 저장


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        self.btn_changeText = QPushButton("btn", self)
        self.btn_changeText.move(200, 200)

    def make_typing_practice(self, mode):
        TypingPractice(self, mode)

    def make_acid_rain(self, mode, level, name):
        AcidRainGame(self, mode, level, name)

    def typing_practice(self):
        print("타자 연습")
        TypingRadioMenu(self, self.make_typing_practice)

    def acid_rain_game(self):
        print("산성비 게임")
        RainRadioMenu(self, self.make_acid_rain)

    def leader_board(self):
        print("리더 보드")
        LeaderBoard(self)

    def initUI(self):
        # 타자 연습 글씨
        label1 = QLabel('main menu', self)
        label1.move(50, 20)

        # 타자연습 버튼
        typing_practice_btn = QPushButton('타자 연습', self)  # 푸쉬버튼 생성
        typing_practice_btn.move(50, 50)
        typing_practice_btn.clicked.connect(self.typing_practice)

        # 산성비 게임 버튼
        acid_rain_btn = QPushButton('산성비 게임', self)  # 푸쉬버튼 생성
        acid_rain_btn.move(50, 100)
        acid_rain_btn.clicked.connect(self.acid_rain_game)

        # 리더 보드
        quit_btn = QPushButton('리더보드', self)  # 푸쉬버튼 생성
        quit_btn.move(50, 150)
        quit_btn.clicked.connect(self.leader_board)

        # 종료 버튼
        quit_btn = QPushButton('종료', self)  # 푸쉬버튼 생성
        quit_btn.move(50, 200)
        quit_btn.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowTitle('TYPING PRATICE for Programers ')  # 창 제목
        self.move(300, 300)  # 창 이동
        self.resize(400, 300)  # 창 크기
        self.show()  # 띄우기


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
