from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication, Qt, QTimer

from PyQt5.QtWidgets import QLabel, QLineEdit
import random
import keyword


class AcidRainGame(QDialog):
    def __init__(self, parent, mode, level, name):  # 부모 window 설정
        super(AcidRainGame, self).__init__(parent)
        self.initUI()
        self.setWindowTitle('산성비 게임')  # 창 제목
        self.resize(500, 500)
        self.move(600, 300)  # 창 이동
        self.show()

        self.timer = QTimer(self)  # timer 변수에 QTimer 할당
        self.timer.start(200)  # 200msec(0.2sec) 마다 반복
        self.timer.timeout.connect(self.move_word)  # start time out시 연결할 함수

        self.make_word_timer = QTimer(self)  # timer 변수에 QTimer 할당
        self.make_word_timer.start(2000)  # 1000msec(10sec) 마다 반복
        self.make_word_timer.timeout.connect(self.make_word)  # start time out시 연결할 함수

        # 산성비 라벨 리스트
        self.word_lst = []
        self.cnt = 0

        def make_word(string, parent):
            # 산성비를 만드는 함수
            word = QLabel(string, parent)
            word.move(60, 10)
            word.resize(300, 30)
            word.setVisible(False)
            return word

        def read_words(path):
            f = open(path, "r")  # 읽기 모드로 파일을 엽니다.
            lines = f.readlines()  # 파일을 한줄씩 리스트로 가져옵니다.
            for i in range(len(lines)):
                lines[i] = lines[i].strip('\n')
            f.close()  # 파일 닫기
            return lines

        # 단어 리스트 생성하기
        if mode == "C++":  # C++ 모드
            words = read_words("C++.txt")

        elif mode == "Java":  # Java 모드
            words = read_words("Java.txt")
        elif mode == "Python":  # 파이썬 모드일때
            words = keyword.kwlist[:]
        else:  # 모드 없을 때
            words = [str(i) for i in range(10)]

        # 만들어진 단어들을 반복문으로 산성비 생성 후 리스트에 넣기
        for i in range(len(words)):
            self.word_lst.append(make_word(words[i], self))

        # 난이도 설정하기
        if level == "easy":
            self.speed = 4
        elif level == "hard":
            self.speed = 8

        # 이름 저장
        self.name = name
        self.mode = mode
        self.level = level

    def initUI(self):
        lbl = QLabel("@로 끝내기", self)
        lbl.move(60, 450)
        lbl.resize(300, 20)

        # 맞춘 개수 라벨
        self.cnt_label = QLabel("맞힌 개수: 0", self)
        self.cnt_label.move(60, 420)
        self.cnt_label.resize(300, 20)

        # 입력칸 생성
        self.qle = QLineEdit(self)
        self.qle.move(60, 400)
        self.qle.resize(400, 20)
        self.qle.returnPressed.connect(self.complete_word)  # 엔터를 눌렀을 때

    def complete_word(self):
        print("complete_word")

        if self.qle.text() == "@":  # 종료 조건
            reply = QMessageBox.question(self, '정말 나가시겠습까?', "정말 나가시겠습까? \n\n  맞춘 개수: " + str(self.cnt),
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)  # 메세지 박스로 맞춘 개수 알려주기

            if reply == QMessageBox.Yes:  # yes 버튼을 눌렀으면 종료시키기
                with open('leaderboard.txt', 'a') as file:
                        file.write(self.name + ',' + str(self.cnt) + ',' + self.mode + ',' + self.level + '\n')
                self.close()
            else:  # 계속 진행
                pass

        for word in self.word_lst:
            if word.isVisible():
                if self.qle.text() == word.text():  # 입력한 글자가 산성비와 동일하면
                    word.setVisible(False)  # 가리기

                    # 맞춘 개수 업데이트
                    self.cnt += 1
                    self.cnt_label.setText("맞힌 개수: " + str(self.cnt))
                    break

        self.qle.setText("")  # 입력칸 비우기

    def make_word(self):
        wait_word_lst = []

        for word in self.word_lst:
            if not word.isVisible():  # 보이지 않는 산성비면?
                wait_word_lst.append(word)

        if len(wait_word_lst) == 0:  # 보이지 않는 단어가 하나도 없으면?
            return  # 함수 종료

        sampleList = random.sample(wait_word_lst, 1)
        for word in sampleList:
            word.setVisible(True)
            word.move(random.randrange(50, 350, 20), 0)  # 랜덤 위치에 산성비 생성
            word.show()

    def move_word(self):
        for word in self.word_lst:
            if word.isVisible():  # 보이는 산성비면?
                word.move(word.x(), word.y() + self.speed)  # 산성비 내리기

                if word.y() > 400:  # 비가 바닥에 떨어졌으면 게임 오버
                    word.setVisible(False)
                    QMessageBox.information(self, "GAME OVER", "GAME OVER \n\n  맞춘 개수: " + str(self.cnt))

                    with open('leaderboard.txt', 'a') as file:
                        file.write(self.name + ',' + str(self.cnt) + ',' + self.mode + ',' + self.level + '\n')


                    self.close()
