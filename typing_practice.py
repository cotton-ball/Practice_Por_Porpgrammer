from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit, QDialog, QRadioButton,QMessageBox
#해당 파일에 필요한 모듈을 불러온

import time
import keyword

class TypingPractice(QDialog):
    def __init__(self, parent, sentence_type):  # 부모 window 설정
        super(TypingPractice, self).__init__(parent)

        # 타자연습 변수 설정
        self.input_text = None
       
        #self.sentence_lst = keyword.kwlist[:]
        
        def read_words(path):
            f = open(path, "r")  
            lines = f.readlines()  
            for i in range(len(lines)):
                lines[i] = lines[i].strip('\n')
            f.close() 
            return lines



        if sentence_type == "short":  # 짧은 글 -> 파이썬 키워드
            self.sentence_lst = keyword.kwlist[:]
            
        elif sentence_type == "long":  # 긴글 설정 -> 파일 입력
            self.sentence_lst = read_words("longSentance.txt")
        
            
            
        self.sentence_idx = 0
        self.start = time.time()  # 시작 시간 저장
        self.input_text_length = 0
        self.cnt = 0

        # 내부 UI 설정
        self.initUI()

        # 창 설정
        self.setWindowTitle('타자연습')  # 창 제목
        self.resize(800, 500)
        self.move(600, 300)  # 창 이동
        self.show()

    def initUI(self):
        lbl = QLabel("@로 끝내기", self)
        lbl.move(60, 100)
        lbl.resize(300, 20)

        self.cnt_label = QLabel("맞힌 개수: 0", self)
        self.cnt_label.move(60, 200)
        self.cnt_label.resize(300, 20)

        self.true_stentence_label = QLabel(self)
        self.true_stentence_label.move(60, 300)
        self.true_stentence_label.resize(800, 20)
        self.true_stentence_label.setText(self.sentence_lst[self.sentence_idx])

        self.lbl = QLabel(self)
        self.lbl.move(60, 350)
        self.lbl.resize(300, 20)

        self.qle = QLineEdit(self)
        self.qle.move(60, 400)
        self.qle.resize(400, 20)
        self.qle.textChanged[str].connect(self.onChanged)  # 글자가 바꿨을 때
        self.qle.returnPressed.connect(self.complete_sentence)  # 엔터를 눌렀을 때

    def complete_sentence(self):
        print("enter")
        if self.input_text is None:
            return

        if self.input_text == "@":  # 산성비 게임 종료하기
            print("@ 입니다.")
            reply = QMessageBox.question(self, '정말 나가시겠습까?', "정말 나가시겠습까? \n\n  맞춘 개수: " + str(self.cnt),
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)  # 메세지 박스로 맞춘 개수 알려주기

            if reply == QMessageBox.Yes:  # yes 버튼을 눌렀으면 종료시키기
                self.close()
        else:  # 입력한 문장 타수 측정하기
            print("타수 측정하기")

            if self.input_text == self.sentence_lst[self.sentence_idx]:  # 입력한 문장이 맞았을때는
                self.input_text_length += len(self.input_text)
                self.sentence_idx += 1
                if self.sentence_idx >= len(self.sentence_lst):  # 길이 초과시 다시 0으로
                    self.sentence_idx = 0

                self.true_stentence_label.setText(self.sentence_lst[self.sentence_idx])  # 다음 문장으로

                # 맞힌 개수
                self.cnt += 1
                self.cnt_label.setText("맞힌 개수: " + str(self.cnt))
            self.qle.setText("")  # 입력창 비우기

    def onChanged(self, text):
        self.input_text = text
        print(text)

        type_per_sec = self.input_text_length / ((time.time() - self.start) / 60)  # 속도 계산 (타 / 분)
        self.lbl.setText(str(round(type_per_sec, 3)) + " (타 / 분)")
        self.lbl.adjustSize()
