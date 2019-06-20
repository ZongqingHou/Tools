# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'capture_dataset.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(1188, 729)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
		self.gridLayout.setObjectName("gridLayout")
		spacerItem = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
		self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.video = QtWidgets.QLabel(self.centralwidget)
		self.video.setObjectName("video")
		self.horizontalLayout.addWidget(self.video)
		self.formLayout = QtWidgets.QFormLayout()
		self.formLayout.setObjectName("formLayout")
		spacerItem1 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
		self.formLayout.setItem(1, QtWidgets.QFormLayout.FieldRole, spacerItem1)
		self.imgBaseIndex = QtWidgets.QLabel(self.centralwidget)
		self.imgBaseIndex.setObjectName("imgBaseIndex")
		self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.imgBaseIndex)
		self.imgBaseIndex_enter = QtWidgets.QLineEdit(self.centralwidget)
		self.imgBaseIndex_enter.setObjectName("imgBaseIndex_enter")
		self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.imgBaseIndex_enter)
		spacerItem2 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
		self.formLayout.setItem(3, QtWidgets.QFormLayout.FieldRole, spacerItem2)
		self.pathSelectionButton = QtWidgets.QPushButton(self.centralwidget)
		self.pathSelectionButton.setObjectName("pathSelectionButton")
		self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.pathSelectionButton)
		spacerItem3 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
		self.formLayout.setItem(5, QtWidgets.QFormLayout.FieldRole, spacerItem3)
		self.capButton = QtWidgets.QPushButton(self.centralwidget)
		self.capButton.setObjectName("capButton")
		self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.capButton)
		self.imgpath = QtWidgets.QLabel(self.centralwidget)
		self.imgpath.setObjectName("imgpath")
		self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.imgpath)
		self.exitButton = QtWidgets.QPushButton(self.centralwidget)
		self.exitButton.setObjectName("exitButton")
		self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.exitButton)
		spacerItem4 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
		self.formLayout.setItem(9, QtWidgets.QFormLayout.LabelRole, spacerItem4)
		spacerItem5 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
		self.formLayout.setItem(7, QtWidgets.QFormLayout.LabelRole, spacerItem5)
		self.horizontalLayout.addLayout(self.formLayout)
		self.horizontalLayout.setStretch(0, 800)
		self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)
		spacerItem6 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.gridLayout.addItem(spacerItem6, 1, 0, 1, 1)
		spacerItem7 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.gridLayout.addItem(spacerItem7, 1, 2, 1, 1)
		spacerItem8 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
		self.gridLayout.addItem(spacerItem8, 2, 1, 1, 1)
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 1188, 25))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.video.setText(_translate("MainWindow", "TextLabel"))
		self.imgBaseIndex.setText(_translate("MainWindow", "ImgBaseIndex"))
		self.pathSelectionButton.setText(_translate("MainWindow", "Path"))
		self.capButton.setText(_translate("MainWindow", "Capture"))
		self.imgpath.setText(_translate("MainWindow", "TextLabel"))
		self.exitButton.setText(_translate("MainWindow", "Exit"))

# self defined
import os
import cv2
import sys
import time
import copy
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

global_frame = None
class CameraThread(QThread):
	def __init__(self, camera_address):
		super(CameraThread, self).__init__()
		self.running_flag = True
		self.capture = cv2.VideoCapture(camera_address)

	def run(self):
		global global_frame
		while self.running_flag:
			ret, global_frame = self.capture.read()

	def stop(self):
		self.running_flag = False
		time.sleep(0.1)

		self.capture.release()

class Tool(QMainWindow, Ui_MainWindow):
	def __init__(self, video_capture=0):
		super(Tool, self).__init__()
		self.setupUi(self)

		self.base_path = None
		self.tmp_frame = None
		self.img_index = 0
		self.previous_capture = None


		self.capButton.clicked.connect(self.capture)
		self.exitButton.clicked.connect(self.app_exit)
		self.pathSelectionButton.clicked.connect(self.select_base_path)

		self.imgpath.setText('Please select the image file path first!!!')

		self.video_signal = CameraThread("rtsp://admin:dw123456@192.168.50.201:554/cam/realmonitor?channel=1&subtype=0")
		self.video_signal.start()

		self.show_timer = QTimer(self)
		self.show_timer.timeout.connect(self.show_img)
		self.show_timer.start(125)

	def show_img(self):
		global global_frame

		self.tmp_frame = global_frame
		tmp = copy.deepcopy(self.tmp_frame)
		if self.previous_capture is not None:
			height, width, channle = self.previous_capture.shape
			tmp[0:height, 0:width] = self.previous_capture
		else:
			pass

		temp_image = QImage(cv2.cvtColor(cv2.resize(tmp, (800, 450)), cv2.COLOR_BGR2RGB).flatten(), 800, 450, QImage.Format_RGB888)
		self.video.setPixmap(QPixmap.fromImage(temp_image))

	def capture(self):
		if self.base_path is None or self.base_path == '' or self.imgBaseIndex_enter.text() == '':
			pass
		else:
			tmp_file_name = self.base_path + '/' + self.imgBaseIndex_enter.text() + '_' + str(self.img_index) + '.jpg'

			if os.path.exists(tmp_file_name):
				pass
			else:
				cv2.imwrite(tmp_file_name, self.tmp_frame)
				self.previous_capture = cv2.resize(self.tmp_frame, (0, 0), fx=0.25, fy=0.25)
				self.img_index += 1
	
	def select_base_path(self):
		export_show = QtWidgets.QFileDialog()
		self.base_path = export_show.getExistingDirectory(self)
		self.imgpath.setText(str(self.base_path))

	def app_exit(self):
		exit()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	mainwindow = Tool()
	mainwindow.show()
	sys.exit(app.exec_())