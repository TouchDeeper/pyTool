#!/usr/bin/python3
#coding = utf-8
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon #便于图标解析
from PyQt5.QtCore import QCoreApplication
from curve_fitting import points_compute
from points_gui import Ui_MainWindow


class Action(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(Action, self).__init__(parent)  # 子类中含有__init__时，不会自动调用父类__init__，如需使用父类__init__中的变量，则需要在子类__init__中显式调用。

        self.setupUi(self)
        self.points_button.clicked.connect(self.showResult)

        self.show()
    # def initUI(self):
    #
    #     self.setGeometry(300, 300, 300, 220) # 前两个参数是窗口的x和y位置；第三个是宽度；第四个是窗口的高度
    #     self.setWindowTitle('学点编程吧出品')
    #     self.setWindowIcon(QIcon('xdbcb8.ico'))
    #
    #     # 退出窗口功能
    #     qbtn = QPushButton('退出', self)
    #     # PyQt5中的事件处理系统采用信号和槽机制构建。 如果我们点击按钮，点击的信号被发出。 槽可以是Qt槽函数或任何Python可调用的函数。
    #     # QCoreApplication包含主事件循环; 它处理和调度所有事件。 instance（）方法给我们当前的实例。
    #     # 请注意，QCoreApplication是通过QApplication创建的。 点击的信号连接到终止应用程序的quit（）方法。
    #     # 通信在两个对象之间完成：发送方和接收方。 发送方是按钮，接收者是应用对象。
    #     qbtn.clicked.connect(QCoreApplication.instance().quit)
    #     # qbtn.resize(70, 30)
    #     # qbtn.move(50, 50)
    #     qbtn.setGeometry(50, 100, 70, 30)
    #
    #     # 输入年龄
    #     self.age = QLineEdit('age', self)
    #     self.age.selectAll()
    #     self.age.setFocus()
    #     self.age.setGeometry(10, 50, 50, 30)
    #
    #     # 输入Troponin
    #     self.Troponin = QLineEdit('Troponin', self)
    #     self.Troponin.selectAll()
    #     self.Troponin.setFocus()
    #     self.Troponin.setGeometry(80, 50, 100, 30)
    #
    #     # 输入NT_ProBNP
    #     self.NT_ProBNP = QLineEdit('NT_ProBNP', self)
    #     self.NT_ProBNP.selectAll()
    #     self.NT_ProBNP.setFocus()
    #     self.NT_ProBNP.setGeometry(200, 50, 100, 30)
    #
    #     self.bt1 = QPushButton('得分', self)
    #     self.bt1.setGeometry(115, 150, 70, 30)
    #     self.bt1.setToolTip('<b>点击这里获取得分</b>')
    #     self.bt1.clicked.connect(self.showResult)
    #
    #     self.show()

    # 显示得分
    def showResult(self):
        age = int(self.age_lineEdit.text())
        Troponin = float(self.Troponin_lineEdit.text())
        NT_ProBNP = float(self.NT_ProBNP_lineEdit.text())
        stroke = int(self.stroke_lineEdit.text())
        QMessageBox.about(self, 'points', str(points_compute(stroke, age, Troponin, NT_ProBNP)))
        self.age_lineEdit.setFocus()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Action()
    sys.exit(app.exec_())

