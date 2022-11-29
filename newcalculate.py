import sys
import re
import numpy as np
from PyQt5.QtWidgets import *
import math

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

    ## #레이아웃 틀 잡기 ###

        layout_operation_solution = QFormLayout()
        layout_part1 = QGridLayout()
        layout_number = QGridLayout()

    ### layout_number 과 버튼을 담을 layout_part2 ###
        layout_part2 = QGridLayout()

    ### 수식 입력 & 결과 가 나타나는 operation_solution 창 구현 ###
        self.operation_solution = QLineEdit()
        layout_operation_solution.addRow("", self.operation_solution)
        self.operation_solution.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    ### layout_part1에 버튼 추가 ###
    ###나머지
        button_remainder = QPushButton("%")
    ### CE
        button_clear_entry = QPushButton("CE")
    ### C
        button_clear = QPushButton("C")
    ### backspace
        button_backspace = QPushButton("←")
        ### 1/x
        button_reciprocal = QPushButton("¹/x")
        ### 제곱
        button_square = QPushButton("x²")
        ### 제곱근
        button_square_root = QPushButton("²√x")
        ### 나누기
        button_division = QPushButton("÷")


        layout_part1.addWidget(button_remainder, 0, 0)
        layout_part1.addWidget(button_clear_entry, 0, 1)
        layout_part1.addWidget(button_clear, 0, 2)
        layout_part1.addWidget(button_backspace, 0, 3)
        layout_part1.addWidget(button_reciprocal, 1, 0)
        layout_part1.addWidget(button_square, 1, 1)
        layout_part1.addWidget(button_square_root, 1, 2)
        layout_part1.addWidget(button_division, 1, 3)

         ### layout_part에 넣을 버튼 구성하기 ###
        button_product = QPushButton("x")
        button_minus = QPushButton("-")
        button_plus = QPushButton("+")
        button_result = QPushButton("=")
        button_plus_minus = QPushButton("±")
        button_add_dot = QPushButton(".")
        button_result.setStyleSheet('QPushButton {background-color: #A3C1DA; color: blue;}')


        #이벤트 추가하기
        button_remainder.clicked.connect(self.button_remainder_clicked)
        button_backspace.clicked.connect(self.button_backspace_clicked)
        button_reciprocal.clicked.connect(self.button_reciprocal_clicked)
        button_clear.clicked.connect(self.button_clear_clicked)
        button_clear_entry.clicked.connect(self.button_clear_entry_clicked)
        button_square.clicked.connect(self.button_square_clicked)
        button_square_root.clicked.connect(self.button_square_root_clicked)
        button_plus_minus.clicked.connect(self.button_plus_minus_clicked)
        button_add_dot.clicked.connect(self.button_add_dot_clicked)
        button_result.clicked.connect(self.button_result_clicked)
       
        ##사칙연산 이벤트 추가하기 
        button_plus.clicked.connect(self.button_plus_clicked)
        button_minus.clicked.connect(self.button_minus_clicked)
        button_product.clicked.connect(self.button_product_clicked)
        button_division.clicked.connect(self.button_division_clicked)

         ### 숫자 버튼 추가 ###
        num = {}
        for number in range(0, 10):
            num[number] = QPushButton(str(number))
            num[number].clicked.connect(lambda state, num = number:
                                                       self.number_button_clicked(num))


            if number > 0:
                x, y = divmod(number - 1, 3)
                # 3으로 나눴을 때 몫과 나머지에 따라 배치를 하면 된다.
                if x == 0:
                    layout_number.addWidget(num[number], 2, y)
                    layout_part2.addWidget(num[number], 2, y)
                elif x == 2:
                    layout_number.addWidget(num[number], 0, y)
                    layout_part2.addWidget(num[number], 0, y)
                else:
                    layout_number.addWidget(num[number], x, y)
                    layout_part2.addWidget(num[number], x, y)

            elif number == 0:
                layout_number.addWidget(num[number], 3, 1)
                layout_part2.addWidget(num[number], 3, 1)

       
        ### 사칙연산버튼 (x , - , + =)과 +/- , .버튼 추가하기 ###
            layout_part2.addWidget(button_product, 0, 3)
            layout_part2.addWidget(button_minus, 1, 3)
            layout_part2.addWidget(button_plus, 2, 3)
            layout_part2.addWidget(button_result, 3, 3)
            layout_part2.addWidget(button_plus_minus, 3, 0)
            layout_part2.addWidget(button_add_dot, 3, 2)

      

        ### main_layout 에 추가 ###
        main_layout.addLayout(layout_operation_solution)
        main_layout.addLayout(layout_part1)
        main_layout.addLayout(layout_part2)
  
        self.setLayout(main_layout)
        self.resize(400, 400)
        self.show()

    def button_remainder_clicked(self):
        operation_solution = self.operation_solution.text()
        operation_solution += " % "
        self.operation_solution.setText(operation_solution)

    def button_backspace_clicked(self):
        operation_solution = self.operation_solution.text()
        operation_solution = operation_solution[:-1]
        self.operation_solution.setText(operation_solution)
    def number_button_clicked(self,num):
        if self.operation_solution.text() =="0":
            self.operation_solution.setText("")
        else:
            operation_solution = self.operation_solution.text()
            operation_solution += str(num)
            self.operation_solution.setText(operation_solution)

    def button_reciprocal_clicked(self):
        operation_solution = self.operation_solution.text()
        operation_solution = str(1/int(operation_solution))
        self.operation_solution.setText(operation_solution)
    def button_square_clicked(self):
        operation_solution=self.operation_solution.text()
        operation_solution = math.pow(int(operation_solution),2)
        self.operation_solution.setText(str(int(operation_solution)))
    def button_square_root_clicked(self):
        operation_solution=self.operation_solution.text()
        operation_solution = math.sqrt(int(operation_solution))
        self.operation_solution.setText(str(operation_solution))
    ### C버튼은 현재까지 입력한 것을 다 지우기 
    def button_clear_clicked(self):
        self.operation_solution.setText("")

    ### CE 버튼은 현재 입력한 수만 지우는 기능
    def button_clear_entry_clicked(self):
        operation_solution = self.operation_solution.text()
        numbers = re.split('([^0-9])',operation_solution)
        del numbers[-1]
        operation_solution = ''.join(s for s in numbers)
        self.operation_solution.setText(operation_solution)
          

    def button_plus_clicked(self):
        operation_solution = self.operation_solution.text()
        operation_solution += " + "
        self.operation_solution.setText(operation_solution)
    def button_minus_clicked(self):
        operation_solution = self.operation_solution.text()
        operation_solution += " - "
        self.operation_solution.setText(operation_solution)
    def button_product_clicked(self):
        operation_solution = self.operation_solution.text()
        operation_solution += " * "
        self.operation_solution.setText(operation_solution)
    def button_division_clicked(self):
        operation_solution = self.operation_solution.text()
        operation_solution += " / "
        self.operation_solution.setText(operation_solution)
    
    def button_plus_minus_clicked(self):
        operation_solution=self.operation_solution.text()
        if float(operation_solution) >0:
            if float(operation_solution).is_integer:
                operation_solution =int(operation_solution)*(-1)
            else:
                operation_solution =float(operation_solution)*(-1)
        else:
            if float(operation_solution).is_integer:
                operation_solution =int(operation_solution)*(-1)
            else:
                operation_solution=float(operation_solution)*(-1)
        self.operation_solution.setText(str(operation_solution))
    
    def button_add_dot_clicked(self):
        operation_solution=self.operation_solution.text()
        if '.' not in operation_solution:
            operation_solution+="."
        self.operation_solution.setText(str(operation_solution))


    def button_result_clicked(self):
        operation_solution=self.operation_solution.text()
        operation_solution_list = operation_solution.split()

        num_list=operation_solution_list[0::2]
        ope_list=operation_solution_list[1::2]
        res_list=[]
        ### 소수점 연산 코드 추가하기 ***
        for i in range(len(num_list)-1):
            if ope_list[i] =="+":
                if i<len(num_list)-1:
                    res = int(num_list[i])+int(num_list[i+1])
                    num_list[i+1]=res
            if ope_list[i] =="-":
                if i<len(num_list)-1:
                    res = int(num_list[i])-int(num_list[i+1])
                    num_list[i+1]=res

            if ope_list[i] =="*":
                if i<len(num_list)-1:
                    res = int(num_list[i])*int(num_list[i+1])
                    num_list[i+1]=res

            if ope_list[i] =="/":
                if i<len(num_list)-1:
                    res = int(num_list[i])/int(num_list[i+1])
                    num_list[i+1]=res
          
        self.operation_solution.setText(str(num_list[len(num_list)-1]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())

