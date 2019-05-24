# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\think\Desktop\python 图形界面\phy.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
import math
from decimal import Decimal
T=5838
c = 3*(1e+10)
h = 6.6256*(1e-34)
k = 1.38*(1e-23)
hv=3.7337*(1e-19)
fov=(32*60)**2
rsun=6.963*(1e+10)
dis_sun_earth=1.49598*(1e+13)
hv=3.7337*(1e-19)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 340, 61, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(21, 52, 311, 231))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox.setRange(1, 500000)
        self.horizontalLayout.addWidget(self.doubleSpinBox)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.doubleSpinBox_2.setRange(1, 500000)
        self.horizontalLayout_2.addWidget(self.doubleSpinBox_2)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.doubleSpinBox_3.setDecimals(3)
        self.horizontalLayout_3.addWidget(self.doubleSpinBox_3)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        self.doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.horizontalLayout_5.addWidget(self.doubleSpinBox_5)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_5.addWidget(self.label_10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_6.addWidget(self.label_11)
        self.doubleSpinBox_6 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_6.setObjectName("doubleSpinBox_6")
        self.horizontalLayout_6.addWidget(self.doubleSpinBox_6)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_6.addWidget(self.label_12)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 280, 261, 31))
        self.label_8.setObjectName("label_8")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(21, 321, 311, 16))
        self.label_15.setObjectName("label_15")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.doubleSpinBox.valueChanged.connect(self.updateUI)
        self.doubleSpinBox_2.valueChanged.connect(self.updateUI)
        self.doubleSpinBox_3.valueChanged.connect(self.updateUI)
        self.doubleSpinBox_5.valueChanged.connect(self.updateUI)
        self.doubleSpinBox_6.valueChanged.connect(self.updateUI)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "黑体辐射公式求太阳望远镜光子数"))
        self.pushButton_2.setText(_translate("MainWindow", "退出"))
        self.label.setText(_translate("MainWindow", "波长开始位置"))
        self.label_2.setText(_translate("MainWindow", "单位：埃"))
        self.label_3.setText(_translate("MainWindow", "波长终止位置"))
        self.label_4.setText(_translate("MainWindow", "单位：埃"))
        self.label_5.setText(_translate("MainWindow", "望远镜系统透过率"))
        self.label_9.setText(_translate("MainWindow", "像元空间分辨率"))
        self.label_10.setText(_translate("MainWindow", "单位：角秒"))
        self.label_11.setText(_translate("MainWindow", "望远镜半径"))
        self.label_12.setText(_translate("MainWindow", "单位：米"))
        self.label_7.setText(_translate("MainWindow", "每毫秒每像元光子数  "))
        self.label_8.setText(_translate("MainWindow", "作者:Yiming Li&Xianyong Bai"))
        self.label_15.setText(_translate("MainWindow", "TEL:18811535378"))

    def updateUI(self):
        wav_l=self.doubleSpinBox.value()
        wav_r=self.doubleSpinBox_2.value()
        trans=self.doubleSpinBox_3.value()
        pix_x_res=self.doubleSpinBox_5.value()
        pix_y_res=self.doubleSpinBox_5.value()
        radius=self.doubleSpinBox_6.value()
        wav_range=Decimal(str(wav_r))-Decimal(str(wav_l))
        wav_interval=0.01
        n_element=Decimal(str(wav_range))/Decimal(str(wav_interval))
        #wav_lengths=np.arange(0,n_element,1,dtype=float)
        wav_lengths=[]
        for i in range(int(n_element)):
            wav_lengths.append(float(i))
        #wav_lengths*=wav_interval;wav_lengths+=wav_l;wav_lengths*=(1e-8)
        for i in range(int(n_element)):
            wav_lengths[i]*=wav_interval
            wav_lengths[i]+=wav_l
            wav_lengths[i]*=(1e-8)
        #spectrum=np.arange(0,wav_lengths.shape[0],1,dtype=float)
        spectrum=[]
        for i in range(int(n_element)):
            first_factor = 2*c*c*h/(wav_lengths[i]**5)
            string=str(c*h/(k*wav_lengths[i]*T))
            ans=math.exp(Decimal(string))
            second_factor = 1.0/(ans-1)
            spectrum.append( first_factor * second_factor*(1e-7))
        #radiance=spectrum
        radiance1=spectrum
        power=0
        for i in range(len(radiance1)):
            power+=(1e+1)*rsun*rsun*math.pi*radiance1[i]/(dis_sun_earth*dis_sun_earth)
        #S_lamda=(1e+4)*rsun*rsun*math.pi*radiance1/(dis_sun_earth*dis_sun_earth)
        #power=sum(S_lamda)*(1e-3)
        collected_power_sun=power*math.pi*(radius**2)
        photons=collected_power_sun/hv
        photons_pixel=trans*photons*pix_x_res*pix_y_res*(1e-3)/fov
        self.lineEdit.setText("{0:.2f}".format(photons_pixel))
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

