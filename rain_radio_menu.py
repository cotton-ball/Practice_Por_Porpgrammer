from PyQt5.QtWidgets import QPushButton, QDialog, QRadioButton, QButtonGroup, QLineEdit, QLabel


class RainRadioMenu(QDialog):
    def __init__(self, parent, func):  # 부모 window 설정
        super(RainRadioMenu, self).__init__(parent)
        self.setWindowTitle('선택')  # 창 제목
        self.resize(200, 200)
        self.move(300, 300)  # 창 이동
        self.initUI()
        self.show()
        self.func = func  # 시작하기 버튼 누를 시 실행할 함수

    def initUI(self):
        # 모드 선택 버튼
        self.radio1 = QRadioButton('C++', self)
        self.radio1.move(20, 20)
        self.radio1.setChecked(True)

        self.radio2 = QRadioButton('Java', self)
        self.radio2.move(20, 40)

        self.radio3 = QRadioButton('Python', self)
        self.radio3.move(20, 60)

        mode_group = QButtonGroup(self)
        mode_group.addButton(self.radio1)
        mode_group.addButton(self.radio2)
        mode_group.addButton(self.radio3)

        # 난이도 선택 버튼
        self.level_radio1 = QRadioButton('easy', self)
        self.level_radio1.move(120, 20)
        self.level_radio1.setChecked(True)

        self.level_radio2 = QRadioButton('hard', self)
        self.level_radio2.move(120, 50)

        level_group = QButtonGroup(self)
        level_group.addButton(self.level_radio1)
        level_group.addButton(self.level_radio2)

        start_btn = QPushButton('시작하기', self)  # 푸쉬버튼 생성
        start_btn.move(20, 120)
        start_btn.clicked.connect(self.start)

        # 타자 연습 글씨
        label1 = QLabel('이름 입력', self)
        label1.move(120, 100)

        # 이름 입력칸 생성
        self.qle = QLineEdit(self)
        self.qle.move(120, 120)
        self.qle.resize(50, 20)

    def start(self):
        print("시작하기")
        mode = None
        level = None

        if self.level_radio1.isChecked():
            level = "easy"
        elif self.level_radio2.isChecked():
            level = "hard"

        if self.radio1.isChecked():
            mode = "C++"
        elif self.radio2.isChecked():
            mode = "Java"
        elif self.radio3.isChecked():
            mode = "Python"

        self.func(mode, level, self.qle.text())
        self.close()
