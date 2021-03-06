# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pomodoro.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import pygame

time = QtCore.QTime(0, 25, 0)
working=True
worktime = QtCore.QTime(0, 25, 0)
breaktime = QtCore.QTime(0, 5, 0)

class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(360, 250)
        MainWindow.setWindowIcon(QtGui.QIcon("domates-removebg-preview.png"))
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        layout = QtWidgets.QGridLayout()

        self.lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd.setStyleSheet("background-color:#ed1c24; border-radius:5px; color:papayawhip")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("Başlat")
        
        self.pushButton.setStyleSheet("color:white; background-color:darkslateblue")
        self.pushButton.clicked.connect(self.ilkbutton)
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("Sıfırla")
        self.pushButton_2.clicked.connect(self.ikibutton)
        self.pushButton_2.setStyleSheet("color:white; background-color:darkslateblue")

        self.slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.slider.setStyleSheet("QSlider::handle:Horizontal { width:10px; border-radius:5px; background:darkslateblue; margin: -5px 0px -5px 0px; }")
        self.slider.setTickInterval(100)
        self.slider.sliderReleased.connect(self.musik)
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        
        MainWindow.setStatusBar(self.statusbar)
        
        self.timer0 = QtCore.QTimer()
        
        self.timer0.setInterval(1000)
        self.timer0.timeout.connect(self.calculo)
        
        layout.addWidget(self.lcd,0,0,1,2)
        layout.addWidget(self.pushButton,1,0)
        layout.addWidget(self.pushButton_2,1,1)
        layout.addWidget(self.slider,3,0,1,2)

        self.centralwidget.setLayout(layout)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pomodoro"))
        MainWindow.setStyleSheet("background-color:midnightblue")
        self.lcd.display(time.toString('mm:ss'))
        self.pushButton.setText(_translate("MainWindow", "Başlat"))
        self.pushButton_2.setText(_translate("MainWindow", "Sıfırla"))

    def calculo(self):
        global time,working,breaktime,worktime
        if time == QtCore.QTime(0, 0, 0) and working:
            time = breaktime
            working = False
            self.musik()
        if time == QtCore.QTime(0, 0, 0) and not working:
            time = worktime
            working = True
            self.musik()
        if working:
            self.lcd.setStyleSheet("background-color:#ed1c24; border-radius:5px; color:papayawhip")
            MainWindow.setWindowTitle("Çalışma Zamanı")
        else:
            self.lcd.setStyleSheet("background-color:#22b14c; border-radius:5px; color:papayawhip")
            MainWindow.setWindowTitle("Mola Zamanı")
        time = time.addSecs(-1)
        self.lcd.display(time.toString('mm:ss'))
        
        
                           
    def ilkbutton(self):
        global working,time,worktime
        if time == QtCore.QTime(0, 0, 0):
            time = worktime
            self.timer0.start()
            self.pushButton.setText("Durdur")
            working = True
            MainWindow.setWindowTitle("Bekletiliyor...")
            return
        if self.timer0.isActive():
            self.timer0.stop()
            self.pushButton.setText("Başlat")
            print("üst bruh",working)
        else:
            self.timer0.start()
            self.pushButton.setText("Durdur")
            print("alt bruh",working)

    def ikibutton(self):
        global time
        self.timer0.stop()
        time = QtCore.QTime(0, 0, 0)
        self.lcd.display(time.toString('mm:ss'))
        self.pushButton.setText("Başlat")
        working = False

    def musik(self):
        if not working:
            pygame.mixer.init()
            pygame.mixer.music.load("mixkit-positive-notification-951.wav")
            pygame.mixer.music.set_volume(self.slider.value()/100)
            pygame.mixer.music.play()
        else:
            pygame.mixer.init()
            pygame.mixer.music.load("mixkit-wrong-answer-fail-notification-946.wav")
            pygame.mixer.music.set_volume(self.slider.value()/100)
            pygame.mixer.music.play()
            
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    MainWindow.show()
    sys.exit(app.exec_())
