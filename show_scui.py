import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

import scui


def display():
    app = QApplication(sys.argv)
    my_window = QMainWindow()
    ui = scui.Ui_MainWindow()
    ui.setupUi(my_window)
    my_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':  # 当模块被直接运行时，以下代码块将被运行，当模块是被导入时，代码块不被运行
    display()
