# Imports
from PyQt5 import QtCore, QtGui, QtWidgets
import better_eval


"""
By moustafa.py
Not the most impressive app in the world, but I finally completed a simple project I set my goal as
Hopefully this is start of an exciting coding career!
"""


# Main class
class Ui_MainWindow(object):

    # class variables
    disp_str = " "
    nsp = better_eval.NumericStringParser()

    # Setup
    def setupUi(self, MainWindow):

        # Main Window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(355, 375)
        MainWindow.setMinimumSize(QtCore.QSize(355, 375))
        MainWindow.setMaximumSize(QtCore.QSize(355, 375))
        font = QtGui.QFont()
        font.setPointSize(20)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Display Screen
        self.disp_scrn = QtWidgets.QLabel(self.centralwidget)
        self.disp_scrn.setGeometry(QtCore.QRect(0, 0, 355, 80))
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(18)
        self.disp_scrn.setFont(font)
        self.disp_scrn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.disp_scrn.setFrameShape(QtWidgets.QFrame.Box)
        self.disp_scrn.setLineWidth(2)
        self.disp_scrn.setText(self.disp_str)
        self.disp_scrn.setScaledContents(False)
        self.disp_scrn.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.disp_scrn.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.disp_scrn.setObjectName("disp_scrn")

        # Button Layout
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(-1, 79, 180, 60))
        self.clear.setObjectName("clear")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(177, 79, 90, 60))
        self.back.setObjectName("back")
        self.div = QtWidgets.QPushButton(self.centralwidget)
        self.div.setGeometry(QtCore.QRect(266, 79, 90, 60))
        self.div.setObjectName("div")
        self.seven = QtWidgets.QPushButton(self.centralwidget)
        self.seven.setGeometry(QtCore.QRect(-1, 138, 90, 60))
        self.seven.setObjectName("seven")
        self.eight = QtWidgets.QPushButton(self.centralwidget)
        self.eight.setGeometry(QtCore.QRect(88, 138, 90, 60))
        self.eight.setObjectName("eight")
        self.mult = QtWidgets.QPushButton(self.centralwidget)
        self.mult.setGeometry(QtCore.QRect(266, 138, 90, 60))
        self.mult.setObjectName("mult")
        self.nine = QtWidgets.QPushButton(self.centralwidget)
        self.nine.setGeometry(QtCore.QRect(177, 138, 90, 60))
        self.nine.setObjectName("nine")
        self.four = QtWidgets.QPushButton(self.centralwidget)
        self.four.setGeometry(QtCore.QRect(-1, 197, 90, 60))
        self.four.setObjectName("four")
        self.five = QtWidgets.QPushButton(self.centralwidget)
        self.five.setGeometry(QtCore.QRect(88, 197, 90, 60))
        self.five.setObjectName("five")
        self.six = QtWidgets.QPushButton(self.centralwidget)
        self.six.setGeometry(QtCore.QRect(177, 197, 90, 60))
        self.six.setObjectName("six")
        self.sub = QtWidgets.QPushButton(self.centralwidget)
        self.sub.setGeometry(QtCore.QRect(266, 197, 90, 60))
        self.sub.setObjectName("sub")
        self.one = QtWidgets.QPushButton(self.centralwidget)
        self.one.setGeometry(QtCore.QRect(-1, 256, 90, 60))
        self.one.setObjectName("one")
        self.two = QtWidgets.QPushButton(self.centralwidget)
        self.two.setGeometry(QtCore.QRect(88, 256, 90, 60))
        self.two.setObjectName("two")
        self.three = QtWidgets.QPushButton(self.centralwidget)
        self.three.setGeometry(QtCore.QRect(177, 256, 90, 60))
        self.three.setObjectName("three")
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(266, 256, 90, 60))
        self.add.setObjectName("add")
        self.neg = QtWidgets.QPushButton(self.centralwidget)
        self.neg.setGeometry(QtCore.QRect(-1, 315, 90, 60))
        self.neg.setObjectName("neg")
        self.zero = QtWidgets.QPushButton(self.centralwidget)
        self.zero.setGeometry(QtCore.QRect(88, 315, 90, 60))
        self.zero.setObjectName("zero")
        self.dot = QtWidgets.QPushButton(self.centralwidget)
        self.dot.setGeometry(QtCore.QRect(177, 315, 90, 60))
        self.dot.setObjectName("dot")
        self.equal = QtWidgets.QPushButton(self.centralwidget)
        self.equal.setGeometry(QtCore.QRect(266, 315, 90, 60))
        self.equal.setObjectName("equal")

        # Background Stuff
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Function Calls
        self.exc()

    # Preferences function
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyCalc"))

        # Shortcuts and Titles
        self.clear.setText(_translate("MainWindow", "CE"))
        self.clear.setShortcut(_translate("MainWindow", "C"))
        self.back.setText(_translate("MainWindow", "<"))
        self.back.setShortcut(_translate("MainWindow", "Backspace"))
        self.div.setText(_translate("MainWindow", "/"))
        self.div.setShortcut(_translate("MainWindow", "/"))
        self.seven.setText(_translate("MainWindow", "7"))
        self.seven.setShortcut(_translate("MainWindow", "7"))
        self.eight.setText(_translate("MainWindow", "8"))
        self.eight.setShortcut(_translate("MainWindow", "8"))
        self.mult.setText(_translate("MainWindow", "x"))
        self.mult.setShortcut(_translate("MainWindow", "*"))
        self.nine.setText(_translate("MainWindow", "9"))
        self.nine.setShortcut(_translate("MainWindow", "9"))
        self.four.setText(_translate("MainWindow", "4"))
        self.four.setShortcut(_translate("MainWindow", "4"))
        self.five.setText(_translate("MainWindow", "5"))
        self.five.setShortcut(_translate("MainWindow", "5"))
        self.six.setText(_translate("MainWindow", "6"))
        self.six.setShortcut(_translate("MainWindow", "6"))
        self.sub.setText(_translate("MainWindow", "-"))
        self.sub.setShortcut(_translate("MainWindow", "-"))
        self.one.setText(_translate("MainWindow", "1"))
        self.one.setShortcut(_translate("MainWindow", "1"))
        self.two.setText(_translate("MainWindow", "2"))
        self.two.setShortcut(_translate("MainWindow", "2"))
        self.three.setText(_translate("MainWindow", "3"))
        self.three.setShortcut(_translate("MainWindow", "3"))
        self.add.setText(_translate("MainWindow", "+"))
        self.add.setShortcut(_translate("MainWindow", "+"))
        self.neg.setText(_translate("MainWindow", "+/-"))
        self.neg.setShortcut(_translate("MainWindow", "N"))
        self.zero.setText(_translate("MainWindow", "0"))
        self.zero.setShortcut(_translate("MainWindow", "0"))
        self.dot.setText(_translate("MainWindow", "."))
        self.dot.setShortcut(_translate("MainWindow", "."))
        self.equal.setText(_translate("MainWindow", "="))
        self.equal.setShortcut(_translate("MainWindow", "Return"))

    # Functions to alter display and calculate
    def equal_trig(self):
        self.disp_str = self.nsp.eval(self.disp_str)
        self.disp_scrn.setText(str(self.disp_str))

    def button_trig(self, t):
        if t == "<":
            self.disp_str = self.disp_str[:-1]
            self.disp_scrn.setText(self.disp_str)
        elif t == "C":
            del self.disp_str
            self.disp_scrn.setText(self.disp_str)
        else:
            self.disp_str = self.disp_str + t
            self.disp_scrn.setText(self.disp_str)

    def push(self, button, stri):
        return button.clicked.connect(lambda: self.button_trig(stri))

    # Placing it all in one place
    def exc(self):
        # row 1
        self.push(self.clear, "C")
        self.push(self.back, "<")
        self.push(self.div, "/")

        # row 2
        self.push(self.seven, "7")
        self.push(self.eight, "8")
        self.push(self.nine, "9")
        self.push(self.mult, "*")

        # row 3
        self.push(self.four, "4")
        self.push(self.five, "5")
        self.push(self.six, "6")
        self.push(self.sub, "-")

        # row 4
        self.push(self.one, "1")
        self.push(self.two, "2")
        self.push(self.three, "3")
        self.push(self.add, "+")

        # row 5
        self.push(self.neg, "-")
        self.push(self.zero, "0")
        self.push(self.dot, ".")
        self.equal.clicked.connect(lambda: self.equal_trig())


# Main Loop
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
