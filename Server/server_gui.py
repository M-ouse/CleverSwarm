# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'server_gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1284, 740)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setObjectName("tableView")
        self.horizontalLayout.addWidget(self.tableView)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.check_button = QtWidgets.QPushButton(self.centralwidget)
        self.check_button.setEnabled(True)
        self.check_button.setObjectName("check_button")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.check_button)
        self.start_text = QtWidgets.QLabel(self.centralwidget)
        self.start_text.setObjectName("start_text")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.start_text)
        self.start_delay_spin = QtWidgets.QSpinBox(self.centralwidget)
        self.start_delay_spin.setObjectName("start_delay_spin")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.start_delay_spin)
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setEnabled(True)
        self.start_button.setFlat(False)
        self.start_button.setObjectName("start_button")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.start_button)
        self.pause_button = QtWidgets.QPushButton(self.centralwidget)
        self.pause_button.setObjectName("pause_button")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.pause_button)
        self.stop_button = QtWidgets.QPushButton(self.centralwidget)
        self.stop_button.setObjectName("stop_button")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.stop_button)
        self.emergency_button = QtWidgets.QPushButton(self.centralwidget)
        self.emergency_button.setObjectName("emergency_button")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.emergency_button)
        self.verticalLayout.addLayout(self.formLayout)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.takeoff_button = QtWidgets.QPushButton(self.centralwidget)
        self.takeoff_button.setEnabled(True)
        self.takeoff_button.setObjectName("takeoff_button")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.takeoff_button)
        self.land_button = QtWidgets.QPushButton(self.centralwidget)
        self.land_button.setObjectName("land_button")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.land_button)
        self.disarm_button = QtWidgets.QPushButton(self.centralwidget)
        self.disarm_button.setObjectName("disarm_button")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.disarm_button)
        self.leds_button = QtWidgets.QPushButton(self.centralwidget)
        self.leds_button.setObjectName("leds_button")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.leds_button)
        self.flip_button = QtWidgets.QPushButton(self.centralwidget)
        self.flip_button.setObjectName("flip_button")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.flip_button)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 1)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1284, 21))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.action_send_animations = QtWidgets.QAction(MainWindow)
        self.action_send_animations.setObjectName("action_send_animations")
        self.action_send_configurations = QtWidgets.QAction(MainWindow)
        self.action_send_configurations.setObjectName("action_send_configurations")
        self.action_send_Aruco_map = QtWidgets.QAction(MainWindow)
        self.action_send_Aruco_map.setObjectName("action_send_Aruco_map")
        self.menuOptions.addAction(self.action_send_animations)
        self.menuOptions.addAction(self.action_send_configurations)
        self.menuOptions.addAction(self.action_send_Aruco_map)
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Clever Drone Animation Player"))
        self.check_button.setText(_translate("MainWindow", "Preflight check"))
        self.start_text.setText(_translate("MainWindow", "Start after"))
        self.start_delay_spin.setSuffix(_translate("MainWindow", " seconds"))
        self.start_button.setText(_translate("MainWindow", "Start animation"))
        self.pause_button.setText(_translate("MainWindow", "Pause"))
        self.stop_button.setText(_translate("MainWindow", "Stop"))
        self.emergency_button.setText(_translate("MainWindow", "Emergency land"))
        self.takeoff_button.setText(_translate("MainWindow", "Takeoff"))
        self.land_button.setText(_translate("MainWindow", "Land"))
        self.disarm_button.setText(_translate("MainWindow", "Disarm"))
        self.leds_button.setText(_translate("MainWindow", "Test leds"))
        self.flip_button.setText(_translate("MainWindow", "Flip"))
        self.menuOptions.setTitle(_translate("MainWindow", "Actions"))
        self.action_send_animations.setText(_translate("MainWindow", "Send Animations"))
        self.action_send_configurations.setText(_translate("MainWindow", "Send Configurations"))
        self.action_send_Aruco_map.setText(_translate("MainWindow", "Send Aruco map"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

