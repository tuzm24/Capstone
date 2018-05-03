import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *

form_class1 = uic.loadUiType("Main.ui")[0]
form_class2 = uic.loadUiType("video.ui")[0]
form_class3 = uic.loadUiType("image.ui")[0]

class Image(QDialog, form_class3):
    def __init__(self):
        super().__init__()
        self.abc()

    def abc(self):
        self.setupUi(self)
        lay = QHBoxLayout()
        lay.addWidget(self.label)
        lay.addWidget(self.lineEdit)
        lay.addWidget(self.pushButton)

        lay2 = QVBoxLayout()
        lay2.addWidget(self.label_5)
        lay2.addWidget(self.groupBox_2)
        lay2.addWidget(self.label_6)
        lay2.addWidget(self.groupBox_3)
        lay2.addWidget(self.label_7)
        lay3 = QHBoxLayout()
        lay3.addWidget(self.horizontalSlider_2)
        lay3.addWidget(self.label_8)
        lay2.addLayout(lay3)
        lay4 = QHBoxLayout()
        lay4.addWidget(self.pushButton_4)
        lay4.addWidget(self.pushButton_5)
        lay2.addLayout(lay4)
        self.groupBox.setLayout(lay2)

        layout = QVBoxLayout()
        layout.addLayout(lay)
        layout.addWidget(self.groupBox)
        flayout = QHBoxLayout()
        flayout.addLayout(layout)
        self.lbl = QLabel(self)
        self.lbl.resize(400, 400)
        flayout.addWidget(self.lbl)
        self.setLayout(flayout)

        #self.setLayout(layout)

        self.pushButton.clicked.connect(self.pushButtonClicked)
        self.pushButton_5.clicked.connect(self.pushButtonClicked2)

        self.horizontalSlider_2.setMinimum(0)
        self.horizontalSlider_2.setMaximum(10)
        self.horizontalSlider_2.setTickInterval(1)
        self.horizontalSlider_2.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_2.valueChanged.connect(
            lambda v: self.label_8.setText(str(v))
        )
    def pushButtonClicked(self):
        self.fname = QFileDialog.getOpenFileName(self)
        self.lineEdit.setText(self.fname[0])
        if ("jpg" in self.fname[0]) | ("png" in self.fname[0]):
            pixmap = QPixmap(self.fname[0])
            pixmap = pixmap.scaledToWidth(300)
            self.setGeometry(650,370,700,400)
            self.lbl.setPixmap(QPixmap(pixmap))

    def pushButtonClicked2(self):
        main.show()
        self.close()

    def closeEvent(self, QCloseEvent):
        main.show()
        self.close()


class Video(QDialog, form_class2):

    def __init__(self):
        super().__init__()
        self.abc()

    def abc(self):
        self.setupUi(self)
        lay = QHBoxLayout()
        lay.addWidget(self.label)
        lay.addWidget(self.lineEdit)
        lay.addWidget(self.pushButton)

        lay2 = QVBoxLayout()
        lay2.addWidget(self.label_2)
        lay2.addWidget(self.groupBox_2)
        lay2.addWidget(self.label_3)
        lay2.addWidget(self.groupBox_3)
        lay2.addWidget(self.label_4)
        lay3 = QHBoxLayout()
        lay3.addWidget(self.horizontalSlider)
        lay3.addWidget(self.label_8)
        lay2.addLayout(lay3)
        lay4 = QHBoxLayout()
        lay4.addWidget(self.pushButton_2)
        lay4.addWidget(self.pushButton_3)
        lay2.addLayout(lay4)
        self.groupBox.setLayout(lay2)

        layout = QVBoxLayout()
        layout.addLayout(lay)
        layout.addWidget(self.groupBox)

        self.setLayout(layout)

        self.pushButton.clicked.connect(self.pushButtonClicked)
        self.pushButton_3.clicked.connect(self.pushButtonClicked2)

        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(10)
        self.horizontalSlider.setTickInterval(1)
        self.horizontalSlider.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider.valueChanged.connect(
            lambda v: self.label_8.setText(str(v))
        )

    def pushButtonClicked(self):
        fname = QFileDialog.getOpenFileName(self)
        self.lineEdit.setText(fname[0])

    def pushButtonClicked2(self):
         main.show()
         self.close()

    def closeEvent(self, QCloseEvent):
         main.show()
         self.close()



class Main(QWidget, form_class1):
    def __init__(self):
        super().__init__()
        self.abc()

    def abc(self):
        self.setupUi(self)
        layout = QVBoxLayout()
        layout.addWidget(self.pushButton_2)
        layout.addWidget(self.pushButton)
        self.setLayout(layout)

        self.pushButton.clicked.connect(self.pushButtonClicked)
        self.pushButton_2.clicked.connect(self.pushButtonClicked2)


    def pushButtonClicked(self):
        video = Video()
        main.hide()
        video.exec()

    def pushButtonClicked2(self):
        image = Image()
        main.hide()
        image.exec_()


    def closeEvent(self, QCloseEvent):
        ans = QMessageBox.question(self, "종료확인", "종료하시겠습니까?",
                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if ans == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    app.exec_()