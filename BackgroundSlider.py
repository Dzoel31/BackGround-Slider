from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()
    
    def setupUI(self):
        self.setWindowTitle("Background Changer")
        self.resize(450,450)
        self.setStyleSheet("background-color : rgb(0,0,0);")

        self.RedSlider = QSlider(Qt.Orientation.Horizontal,valueChanged = self.UpdateWindow)
        self.RedSlider.setRange(0,255)
        self.RedSlider.setPageStep(1)
        self.RedSlider.setStyleSheet("QSlider::handle::horizontal {background-color:red;}")

        self.GreenSlider = QSlider(Qt.Orientation.Horizontal, valueChanged = self.UpdateWindow)
        self.GreenSlider.setRange(0,255)
        self.GreenSlider.setPageStep(1)
        self.GreenSlider.setStyleSheet("QSlider::handle::horizontal {background-color:green;}")

        self.BlueSlider = QSlider(Qt.Orientation.Horizontal, valueChanged = self.UpdateWindow)
        self.BlueSlider.setRange(0,255)
        self.BlueSlider.setPageStep(1)
        self.BlueSlider.setStyleSheet("QSlider::handle::horizontal {background-color:blue;}")

        self.RedLabel = QLabel("0")
        self.GreenLabel = QLabel("0")
        self.BlueLabel = QLabel("0")

        vslider = QVBoxLayout()
        vslider.addWidget(self.RedSlider)
        vslider.addWidget(self.GreenSlider)
        vslider.addWidget(self.BlueSlider)

        vValue = QVBoxLayout()
        vValue.addWidget(self.RedLabel)
        vValue.addWidget(self.GreenLabel)
        vValue.addWidget(self.BlueLabel)

        hwidget = QHBoxLayout()
        hwidget.addLayout(vslider)
        hwidget.addSpacing(20)
        hwidget.addLayout(vValue)

        self.setLayout(hwidget)
    
    def UpdateWindow(self):
        Red = self.RedSlider.value()
        Green = self.GreenSlider.value()
        Blue = self.BlueSlider.value()
        self.setStyleSheet(f"background-color : rgb({Red},{Green},{Blue});")
    
        self.RedLabel.setText(str(Red))
        self.GreenLabel.setText(str(Green))
        self.BlueLabel.setText(str(Blue))

App = QApplication(sys.argv)
Window = MainWindow()
Window.show()
App.exec_()