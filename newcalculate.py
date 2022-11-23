import sys
import numpy as np
from PyQt5.QtWidgets import *

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout =QVBoxLayout()


        ## #레이아웃 틀 잡기 ###

        layout_operation_solution = QFormLayout()
        layout_funct1 = QGridLayout()
        layout_funct2 =QGridLayout()


        ### 수식 입력 & 결과 가 나타나는 operation_solution 창 구현 ###
        self.operation_solution = QLineEdit()
        layout_operation_solution.addRow("", self.operation_solution)
        self.operation_solution.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.setLayout(main_layout)
        self.resize(400, 400)
        self.show()

        ### 기능 funct1 버튼 구현 ###
        ###나머지
        self.remainder = QPushButton("%")
        ##CE
        self.clear_entry = QPushButton("CE")
        ## C
        self.clear = QPushButton("C")
        self.backspace = QPushButton("지우기")
        ### 1/x
        self.reciprocal =QPushButton("1/x")
        ### 제곱
        self.squre = QPushButton("제곱")
        ### 제곱근
        self.square_root=QPushButton("제곱근")
        ### 나누기
        self.devision = QPushButton("÷")

        layout_funct1.addWidget(self.remainder,0 , 0)
        layout_funct1.addWidget(self.clear_entry,0 , 1)
        layout_funct1.addWidget(self.clear,0 ,2)
        layout_funct1.addWidget(self.backspace,0 ,3)
        layout_funct1.addWidget(self.reciprocal,1 , 0)
        layout_funct1.addWidget(self.squre,1,1)
        layout_funct1.addWidget(self.square_root,1 ,2)
        layout_funct1.addWidget(self.devision,1 , 3)

        ### layout_number 구성하기 ###
        self.button_production = QPushButton("x")
        self.button_minus =QPushButton("-")
        self.button_plus = QPushButton("+")
        self.button_result = QPushButton("=")
        self.button_plus_minus = QPushButton("+/-")
        self.button_add_dot = QPushButton(".")

        layout_funct2.addWidget(self.button_production,0,3)
        layout_funct2.addWidget(self.button_minus,1,3)
        layout_funct2.addWidget(self.button_plus,2,3)
        layout_funct2.addWidget(self.button_result,3,3)
        layout_funct2.addWidget(self.button_plus_minus,3,0)
        layout_funct2.addWidget(self.button_add_dot,3,2)

    ###기능 추가하기 ###
        
        np = {}
        for number in range(0, 10):
            np[number] = QPushButton(str(number))

            if number > 0:
                x, y = divmod(number - 1, 3)
                # 3으로 나눴을 때 몫과 나머지에 따라 배치를 하면 된다.
                if x==0:
                    layout_funct2.addWidget(np[number], 2, y)
                elif x==2:
                    layout_funct2.addWidget(np[number], 0, y)
                else:
                    layout_funct2.addWidget(np[number], x, y)

            elif number == 0:
                layout_funct2.addWidget(np[number], 3, 1)

        ###main_layout에 추가 ###
        main_layout.addLayout(layout_operation_solution)
        main_layout.addLayout(layout_funct1)
        main_layout.addLayout(layout_funct2)



if __name__ =='__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())