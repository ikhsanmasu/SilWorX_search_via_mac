# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Write00.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(650, 380)
        Form.setStyleSheet("background-color: rgb(225, 225, 235);")
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.writepb = QtWidgets.QPushButton(Form)
        self.writepb.setObjectName("writepb")
        self.horizontalLayout_5.addWidget(self.writepb)
        self.canclepb = QtWidgets.QPushButton(Form)
        self.canclepb.setObjectName("canclepb")
        self.horizontalLayout_5.addWidget(self.canclepb)
        self.helppb = QtWidgets.QPushButton(Form)
        self.helppb.setObjectName("helppb")
        self.horizontalLayout_5.addWidget(self.helppb)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 10, 0, 1, 7)
        self.label_33 = QtWidgets.QLabel(Form)
        self.label_33.setText("")
        self.label_33.setObjectName("label_33")
        self.gridLayout_3.addWidget(self.label_33, 1, 12, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setMinimumSize(QtCore.QSize(200, 0))
        self.groupBox_2.setStyleSheet("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.accesmodeinput = QtWidgets.QComboBox(self.groupBox_2)
        self.accesmodeinput.setMinimumSize(QtCore.QSize(0, 0))
        self.accesmodeinput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.accesmodeinput.setObjectName("accesmodeinput")
        self.accesmodeinput.addItem("")
        self.accesmodeinput.addItem("")
        self.accesmodeinput.addItem("")
        self.accesmodeinput.addItem("")
        self.gridLayout_5.addWidget(self.accesmodeinput, 2, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.groupBox_2)
        self.label_21.setObjectName("label_21")
        self.gridLayout_5.addWidget(self.label_21, 2, 0, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.groupBox_2)
        self.label_30.setText("")
        self.label_30.setObjectName("label_30")
        self.gridLayout_5.addWidget(self.label_30, 3, 0, 1, 1)
        self.passwordinput = QtWidgets.QLineEdit(self.groupBox_2)
        self.passwordinput.setMinimumSize(QtCore.QSize(0, 0))
        self.passwordinput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.passwordinput.setObjectName("passwordinput")
        self.gridLayout_5.addWidget(self.passwordinput, 1, 1, 1, 1)
        self.userinput = QtWidgets.QLineEdit(self.groupBox_2)
        self.userinput.setMinimumSize(QtCore.QSize(0, 0))
        self.userinput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.userinput.setObjectName("userinput")
        self.gridLayout_5.addWidget(self.userinput, 0, 1, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.groupBox_2)
        self.label_38.setText("")
        self.label_38.setObjectName("label_38")
        self.gridLayout_5.addWidget(self.label_38, 4, 0, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.groupBox_2)
        self.label_32.setObjectName("label_32")
        self.gridLayout_5.addWidget(self.label_32, 0, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.groupBox_2)
        self.label_20.setObjectName("label_20")
        self.gridLayout_5.addWidget(self.label_20, 1, 0, 1, 1)
        self.label_39 = QtWidgets.QLabel(self.groupBox_2)
        self.label_39.setText("")
        self.label_39.setObjectName("label_39")
        self.gridLayout_5.addWidget(self.label_39, 5, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_2, 0, 4, 1, 1)
        self.closedialoginput = QtWidgets.QCheckBox(Form)
        self.closedialoginput.setObjectName("closedialoginput")
        self.gridLayout_3.addWidget(self.closedialoginput, 1, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"gridline-color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_29 = QtWidgets.QLabel(self.groupBox)
        self.label_29.setObjectName("label_29")
        self.gridLayout_4.addWidget(self.label_29, 8, 0, 1, 1)
        self.label_40 = QtWidgets.QLabel(self.groupBox)
        self.label_40.setObjectName("label_40")
        self.gridLayout_4.addWidget(self.label_40, 6, 0, 1, 4)
        self.label_19 = QtWidgets.QLabel(self.groupBox)
        self.label_19.setObjectName("label_19")
        self.gridLayout_4.addWidget(self.label_19, 7, 0, 1, 1)
        self.readpb = QtWidgets.QPushButton(self.groupBox)
        self.readpb.setStyleSheet("background-color: rgb(233, 235, 245);")
        self.readpb.setObjectName("readpb")
        self.gridLayout_4.addWidget(self.readpb, 10, 1, 1, 3)
        self.redudancyinput = QtWidgets.QCheckBox(self.groupBox)
        self.redudancyinput.setText("")
        self.redudancyinput.setObjectName("redudancyinput")
        self.gridLayout_4.addWidget(self.redudancyinput, 7, 1, 2, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_23 = QtWidgets.QLabel(self.groupBox)
        self.label_23.setMinimumSize(QtCore.QSize(0, 20))
        self.label_23.setScaledContents(True)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_2.addWidget(self.label_23)
        self.mac1ind = QtWidgets.QLabel(self.groupBox)
        self.mac1ind.setStyleSheet("background-color: rgb(212, 208, 200);")
        self.mac1ind.setText("")
        self.mac1ind.setAlignment(QtCore.Qt.AlignCenter)
        self.mac1ind.setObjectName("mac1ind")
        self.horizontalLayout_2.addWidget(self.mac1ind)
        self.label_24 = QtWidgets.QLabel(self.groupBox)
        self.label_24.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_24.setStyleSheet("background-color: rgb(212, 208, 200);\n"
"border: 1px solid black;")
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_2.addWidget(self.label_24)
        self.mac2ind = QtWidgets.QLabel(self.groupBox)
        self.mac2ind.setStyleSheet("background-color: rgb(212, 208, 200);")
        self.mac2ind.setText("")
        self.mac2ind.setAlignment(QtCore.Qt.AlignCenter)
        self.mac2ind.setObjectName("mac2ind")
        self.horizontalLayout_2.addWidget(self.mac2ind)
        self.label_25 = QtWidgets.QLabel(self.groupBox)
        self.label_25.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_25.setStyleSheet("background-color: rgb(212, 208, 200);\n"
"border: 1px solid black;")
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_2.addWidget(self.label_25)
        self.mac3ind = QtWidgets.QLabel(self.groupBox)
        self.mac3ind.setStyleSheet("background-color: rgb(212, 208, 200);")
        self.mac3ind.setText("")
        self.mac3ind.setAlignment(QtCore.Qt.AlignCenter)
        self.mac3ind.setObjectName("mac3ind")
        self.horizontalLayout_2.addWidget(self.mac3ind)
        self.label_26 = QtWidgets.QLabel(self.groupBox)
        self.label_26.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_26.setStyleSheet("background-color: rgb(212, 208, 200);\n"
"border: 1px solid black;")
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_2.addWidget(self.label_26)
        self.mac4ind = QtWidgets.QLabel(self.groupBox)
        self.mac4ind.setStyleSheet("background-color: rgb(212, 208, 200);")
        self.mac4ind.setText("")
        self.mac4ind.setAlignment(QtCore.Qt.AlignCenter)
        self.mac4ind.setObjectName("mac4ind")
        self.horizontalLayout_2.addWidget(self.mac4ind)
        self.label_27 = QtWidgets.QLabel(self.groupBox)
        self.label_27.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_27.setStyleSheet("background-color: rgb(212, 208, 200);\n"
"border: 1px solid black;")
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_2.addWidget(self.label_27)
        self.mac5ind = QtWidgets.QLabel(self.groupBox)
        self.mac5ind.setStyleSheet("background-color: rgb(212, 208, 200);")
        self.mac5ind.setText("")
        self.mac5ind.setAlignment(QtCore.Qt.AlignCenter)
        self.mac5ind.setObjectName("mac5ind")
        self.horizontalLayout_2.addWidget(self.mac5ind)
        self.label_28 = QtWidgets.QLabel(self.groupBox)
        self.label_28.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_28.setStyleSheet("background-color: rgb(212, 208, 200);\n"
"border: 1px solid black;")
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_2.addWidget(self.label_28)
        self.mac6ind = QtWidgets.QLabel(self.groupBox)
        self.mac6ind.setStyleSheet("background-color: rgb(212, 208, 200);")
        self.mac6ind.setText("")
        self.mac6ind.setAlignment(QtCore.Qt.AlignCenter)
        self.mac6ind.setObjectName("mac6ind")
        self.horizontalLayout_2.addWidget(self.mac6ind)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 0, 0, 1, 4)
        self.label_41 = QtWidgets.QLabel(self.groupBox)
        self.label_41.setObjectName("label_41")
        self.gridLayout_4.addWidget(self.label_41, 9, 0, 1, 4)
        self.subnetinput = QtWidgets.QLineEdit(self.groupBox)
        self.subnetinput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.subnetinput.setObjectName("subnetinput")
        self.gridLayout_4.addWidget(self.subnetinput, 4, 1, 1, 3)
        self.gatewayinput = QtWidgets.QLineEdit(self.groupBox)
        self.gatewayinput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gatewayinput.setObjectName("gatewayinput")
        self.gridLayout_4.addWidget(self.gatewayinput, 5, 1, 1, 3)
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setEnabled(True)
        self.label_14.setObjectName("label_14")
        self.gridLayout_4.addWidget(self.label_14, 5, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_12.setObjectName("label_12")
        self.gridLayout_4.addWidget(self.label_12, 4, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_13.setObjectName("label_13")
        self.gridLayout_4.addWidget(self.label_13, 3, 0, 1, 1)
        self.ipinput = QtWidgets.QLineEdit(self.groupBox)
        self.ipinput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ipinput.setObjectName("ipinput")
        self.gridLayout_4.addWidget(self.ipinput, 3, 1, 1, 3)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 2, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.systemidinput = QtWidgets.QLineEdit(self.groupBox)
        self.systemidinput.setMinimumSize(QtCore.QSize(50, 0))
        self.systemidinput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.systemidinput.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.systemidinput.setObjectName("systemidinput")
        self.horizontalLayout_9.addWidget(self.systemidinput)
        self.rackidinput = QtWidgets.QLineEdit(self.groupBox)
        self.rackidinput.setMinimumSize(QtCore.QSize(50, 0))
        self.rackidinput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.rackidinput.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rackidinput.setObjectName("rackidinput")
        self.horizontalLayout_9.addWidget(self.rackidinput)
        self.slotind = QtWidgets.QLabel(self.groupBox)
        self.slotind.setMinimumSize(QtCore.QSize(60, 0))
        self.slotind.setStyleSheet("background-color: rgb(212, 208, 200);")
        self.slotind.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.slotind.setObjectName("slotind")
        self.horizontalLayout_9.addWidget(self.slotind)
        self.gridLayout_4.addLayout(self.horizontalLayout_9, 2, 1, 1, 3)
        self.label_43 = QtWidgets.QLabel(self.groupBox)
        self.label_43.setObjectName("label_43")
        self.gridLayout_4.addWidget(self.label_43, 1, 0, 1, 4)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.accesmodeinput.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.writepb.setText(_translate("Form", "Write"))
        self.canclepb.setText(_translate("Form", "Cancel"))
        self.helppb.setText(_translate("Form", "Help"))
        self.groupBox_2.setTitle(_translate("Form", "Access Data"))
        self.accesmodeinput.setItemText(0, _translate("Form", "Administrator"))
        self.accesmodeinput.setItemText(1, _translate("Form", "Read"))
        self.accesmodeinput.setItemText(2, _translate("Form", "Read and Write"))
        self.accesmodeinput.setItemText(3, _translate("Form", "Read and Operator"))
        self.label_21.setText(_translate("Form", "Access Mode"))
        self.label_32.setText(_translate("Form", "User Group"))
        self.label_20.setText(_translate("Form", "Password"))
        self.closedialoginput.setText(_translate("Form", "Automatically close the dialog upon success."))
        self.groupBox.setTitle(_translate("Form", "Settings"))
        self.label_29.setText(_translate("Form", "for redudancy"))
        self.label_40.setText(_translate("Form", "_______________________________________________________________________"))
        self.label_19.setText(_translate("Form", "System bus module resposible"))
        self.readpb.setText(_translate("Form", "Read"))
        self.label_23.setText(_translate("Form", "MAC Address"))
        self.label_24.setText(_translate("Form", " - "))
        self.label_25.setText(_translate("Form", " - "))
        self.label_26.setText(_translate("Form", " - "))
        self.label_27.setText(_translate("Form", " - "))
        self.label_28.setText(_translate("Form", " - "))
        self.label_41.setText(_translate("Form", "_______________________________________________________________________"))
        self.label_14.setText(_translate("Form", "Gateway"))
        self.label_12.setText(_translate("Form", "Subnet Mask"))
        self.label_13.setText(_translate("Form", "IP Address"))
        self.label_11.setText(_translate("Form", "SRS"))
        self.slotind.setText(_translate("Form", "0"))
        self.label_43.setText(_translate("Form", "_______________________________________________________________________"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
