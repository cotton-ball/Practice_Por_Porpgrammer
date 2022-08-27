from PyQt5.QtWidgets import QPushButton, QDialog, QRadioButton


class TypingRadioMenu(QDialog):
    def __init__(self, parent, func):  # 부모 window 설정
        super(TypingRadioMenu, self).__init__(parent)
        self.setWindowTitle('선택')  # 창 제목
        self.resize(200, 200)
        self.move(300, 300)  # 창 이동
        self.initUI()
        self.show()
        self.func = func  # 시작하기 버튼 누를 시 실행할 함수

    def initUI(self):
        self.radio1 = QRadioButton('긴 글', self)
        self.radio1.move(20, 20)
        self.radio1.setChecked(True)

        self.radio2 = QRadioButton('짧은 글', self)
        self.radio2.move(20, 40)

        start_btn = QPushButton('시작하기', self)  # 푸쉬버튼 생성
        start_btn.move(20, 60)
        start_btn.clicked.connect(self.start)

    def start(self):
        print("시작하기")
        if self.radio1.isChecked():
            self.func('long')
        elif self.radio2.isChecked():
            self.func('short')

        self.close()
