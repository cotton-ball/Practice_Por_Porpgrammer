from PyQt5.QtWidgets import QDialog, QTableWidget, QTableWidgetItem, QVBoxLayout


class LeaderBoard(QDialog):
    def __init__(self, parent):  # 부모 window 설정
        super(LeaderBoard, self).__init__(parent)
        self.initUI()

    def initUI(self):

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(100)
        self.tableWidget.setColumnCount(4)

        # 첫번째 행 설정
        self.tableWidget.setItem(0, 0, QTableWidgetItem("이름"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("맞춘 개수"))
        self.tableWidget.setItem(0, 2, QTableWidgetItem("언어"))
        self.tableWidget.setItem(0, 3, QTableWidgetItem("난이도"))

        info = []

        # 리더보드 파일 불러오기
        f = open("leaderboard.txt", 'r')
        lines = f.readlines()
        for i in range(len(lines)):
            info.append(lines[i].split(','))  # 배열에 저장시키기
        f.close()

        # 테이블에 기록 표시하기
        for i in range(len(info)):
            for j in range(4):
                self.tableWidget.setItem(i + 1, j, QTableWidgetItem(info[i][j]))

        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)

        self.setWindowTitle('리더 보드')
        self.setGeometry(300, 100, 600, 400)
        self.show()
