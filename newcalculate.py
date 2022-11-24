import sys
import numpy as np
from PyQt5.QtWidgets import *

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout =QVBoxLayout()

    ###레이아웃 틀 잡기 ###

        layout_operation_solution = QFormLayout()
        layout_part1 = QGridLayout()
        layout_number = QGridLayout()

    ### layout_number 과 버튼을 담을 layout_part2 ###
        layout_part2 = QGridLayout()


        self.setLayout(main_layout)
        self.resize(400, 400)
        self.show()

    ### main_layout 에 추가 ###
        main_layout.addLayout(layout_operation_solution)

if __name__ =='__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
