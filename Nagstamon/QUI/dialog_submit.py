# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_submit.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_dialog_submit(object):

    def setupUi(self, dialog_submit):
        dialog_submit.setObjectName("dialog_submit")
        dialog_submit.resize(473, 449)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dialog_submit.sizePolicy().hasHeightForWidth())
        dialog_submit.setSizePolicy(sizePolicy)
        dialog_submit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        dialog_submit.setSizeGripEnabled(True)
        dialog_submit.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(dialog_submit)
        self.gridLayout.setObjectName("gridLayout")
        self.input_lineedit_performance_data = QtWidgets.QLineEdit(dialog_submit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_lineedit_performance_data.sizePolicy().hasHeightForWidth())
        self.input_lineedit_performance_data.setSizePolicy(sizePolicy)
        self.input_lineedit_performance_data.setObjectName("input_lineedit_performance_data")
        self.gridLayout.addWidget(self.input_lineedit_performance_data, 5, 2, 1, 1)
        self.label_check_output = QtWidgets.QLabel(dialog_submit)
        self.label_check_output.setObjectName("label_check_output")
        self.gridLayout.addWidget(self.label_check_output, 3, 0, 1, 1, QtCore.Qt.AlignVCenter)
        self.input_lineedit_check_output = QtWidgets.QLineEdit(dialog_submit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_lineedit_check_output.sizePolicy().hasHeightForWidth())
        self.input_lineedit_check_output.setSizePolicy(sizePolicy)
        self.input_lineedit_check_output.setObjectName("input_lineedit_check_output")
        self.gridLayout.addWidget(self.input_lineedit_check_output, 3, 2, 1, 1)
        self.label_performance_data = QtWidgets.QLabel(dialog_submit)
        self.label_performance_data.setObjectName("label_performance_data")
        self.gridLayout.addWidget(self.label_performance_data, 5, 0, 1, 1, QtCore.Qt.AlignVCenter)
        self.check_result_groupbox = QtWidgets.QGroupBox(dialog_submit)
        self.check_result_groupbox.setObjectName("check_result_groupbox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.check_result_groupbox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.input_radiobutton_result_ok = QtWidgets.QRadioButton(self.check_result_groupbox)
        self.input_radiobutton_result_ok.setChecked(True)
        self.input_radiobutton_result_ok.setObjectName("input_radiobutton_result_ok")
        self.verticalLayout.addWidget(self.input_radiobutton_result_ok)
        self.input_radiobutton_result_up = QtWidgets.QRadioButton(self.check_result_groupbox)
        self.input_radiobutton_result_up.setObjectName("input_radiobutton_result_up")
        self.verticalLayout.addWidget(self.input_radiobutton_result_up)
        self.input_radiobutton_result_information = QtWidgets.QRadioButton(self.check_result_groupbox)
        self.input_radiobutton_result_information.setObjectName("input_radiobutton_result_information")
        self.verticalLayout.addWidget(self.input_radiobutton_result_information)
        self.input_radiobutton_result_warning = QtWidgets.QRadioButton(self.check_result_groupbox)
        self.input_radiobutton_result_warning.setObjectName("input_radiobutton_result_warning")
        self.verticalLayout.addWidget(self.input_radiobutton_result_warning)
        self.input_radiobutton_result_average = QtWidgets.QRadioButton(self.check_result_groupbox)
        self.input_radiobutton_result_average.setObjectName("input_radiobutton_result_average")
        self.verticalLayout.addWidget(self.input_radiobutton_result_average)
        self.input_radiobutton_result_high = QtWidgets.QRadioButton(self.check_result_groupbox)
        self.input_radiobutton_result_high.setObjectName("input_radiobutton_result_high")
        self.verticalLayout.addWidget(self.input_radiobutton_result_high)
        self.input_radiobutton_result_critical = QtWidgets.QRadioButton(self.check_result_groupbox)
        self.input_radiobutton_result_critical.setObjectName("input_radiobutton_result_critical")
        self.verticalLayout.addWidget(self.input_radiobutton_result_critical)
        self.input_radiobutton_result_disaster = QtWidgets.QRadioButton(self.check_result_groupbox)
        self.input_radiobutton_result_disaster.setObjectName("input_radiobutton_result_disaster")
        self.verticalLayout.addWidget(self.input_radiobutton_result_disaster)
        self.input_radiobutton_result_unreachable = QtWidgets.QRadioButton(self.check_result_groupbox)
        self.input_radiobutton_result_unreachable.setObjectName("input_radiobutton_result_unreachable")
        self.verticalLayout.addWidget(self.input_radiobutton_result_unreachable)
        self.input_radiobutton_result_unknown = QtWidgets.QRadioButton(self.check_result_groupbox)
        self.input_radiobutton_result_unknown.setObjectName("input_radiobutton_result_unknown")
        self.verticalLayout.addWidget(self.input_radiobutton_result_unknown)
        self.input_radiobutton_result_down = QtWidgets.QRadioButton(self.check_result_groupbox)
        self.input_radiobutton_result_down.setObjectName("input_radiobutton_result_down")
        self.verticalLayout.addWidget(self.input_radiobutton_result_down)
        self.gridLayout.addWidget(self.check_result_groupbox, 1, 0, 1, 4)
        self.label_comment = QtWidgets.QLabel(dialog_submit)
        self.label_comment.setObjectName("label_comment")
        self.gridLayout.addWidget(self.label_comment, 7, 0, 1, 1, QtCore.Qt.AlignVCenter)
        self.input_label_description = QtWidgets.QLabel(dialog_submit)
        self.input_label_description.setObjectName("input_label_description")
        self.gridLayout.addWidget(self.input_label_description, 0, 0, 1, 4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_change_defaults_submit_check_result = QtWidgets.QPushButton(dialog_submit)
        self.button_change_defaults_submit_check_result.setObjectName("button_change_defaults_submit_check_result")
        self.horizontalLayout.addWidget(self.button_change_defaults_submit_check_result)
        self.button_box = QtWidgets.QDialogButtonBox(dialog_submit)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.horizontalLayout.addWidget(self.button_box)
        self.gridLayout.addLayout(self.horizontalLayout, 11, 0, 2, 4)
        self.input_lineedit_comment = QtWidgets.QLineEdit(dialog_submit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_lineedit_comment.sizePolicy().hasHeightForWidth())
        self.input_lineedit_comment.setSizePolicy(sizePolicy)
        self.input_lineedit_comment.setObjectName("input_lineedit_comment")
        self.gridLayout.addWidget(self.input_lineedit_comment, 7, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 10, 0, 1, 1)

        self.retranslateUi(dialog_submit)
        self.button_box.accepted.connect(dialog_submit.accept)
        self.button_box.rejected.connect(dialog_submit.reject)
        QtCore.QMetaObject.connectSlotsByName(dialog_submit)
        dialog_submit.setTabOrder(self.input_radiobutton_result_ok, self.input_radiobutton_result_up)
        dialog_submit.setTabOrder(self.input_radiobutton_result_ok, self.input_radiobutton_result_information)
        dialog_submit.setTabOrder(self.input_radiobutton_result_information, self.input_radiobutton_result_warning)
        dialog_submit.setTabOrder(self.input_radiobutton_result_warning, self.input_radiobutton_result_average)
        dialog_submit.setTabOrder(self.input_radiobutton_result_average, self.input_radiobutton_result_high)
        dialog_submit.setTabOrder(self.input_radiobutton_result_high, self.input_radiobutton_result_critical)
        dialog_submit.setTabOrder(self.input_radiobutton_result_critical, self.input_radiobutton_result_disaster)
        dialog_submit.setTabOrder(self.input_radiobutton_result_disaster, self.input_radiobutton_result_unreachable)
        dialog_submit.setTabOrder(self.input_radiobutton_result_unreachable, self.input_radiobutton_result_unknown)
        dialog_submit.setTabOrder(self.input_radiobutton_result_unknown, self.input_radiobutton_result_down)
        dialog_submit.setTabOrder(self.input_radiobutton_result_down, self.input_lineedit_check_output)
        dialog_submit.setTabOrder(self.input_lineedit_check_output, self.input_lineedit_performance_data)
        dialog_submit.setTabOrder(self.input_lineedit_performance_data, self.input_lineedit_comment)
        dialog_submit.setTabOrder(self.input_lineedit_comment, self.button_change_defaults_submit_check_result)

    def retranslateUi(self, dialog_submit):
        _translate = QtCore.QCoreApplication.translate
        dialog_submit.setWindowTitle(_translate("dialog_submit", "Submit check result"))
        self.label_check_output.setText(_translate("dialog_submit", "Check output:"))
        self.label_performance_data.setText(_translate("dialog_submit", "Performance data:"))
        self.check_result_groupbox.setTitle(_translate("dialog_submit", "Check result"))
        self.input_radiobutton_result_ok.setText(_translate("dialog_submit", "OK"))
        self.input_radiobutton_result_up.setText(_translate("dialog_submit", "UP"))
        self.input_radiobutton_result_information.setText(_translate("dialog_submit", "INFORMATION"))
        self.input_radiobutton_result_warning.setText(_translate("dialog_submit", "WARNING"))
        self.input_radiobutton_result_average.setText(_translate("dialog_submit", "AVERAGE"))
        self.input_radiobutton_result_high.setText(_translate("dialog_submit", "HIGH"))
        self.input_radiobutton_result_critical.setText(_translate("dialog_submit", "CRITICAL"))
        self.input_radiobutton_result_disaster.setText(_translate("dialog_submit", "DISASTER"))
        self.input_radiobutton_result_unreachable.setText(_translate("dialog_submit", "UNREACHABLE"))
        self.input_radiobutton_result_unknown.setText(_translate("dialog_submit", "UNKNOWN"))
        self.input_radiobutton_result_down.setText(_translate("dialog_submit", "DOWN"))
        self.label_comment.setText(_translate("dialog_submit", "Comment:"))
        self.input_label_description.setText(_translate("dialog_submit", "description - set by QUI.py"))
        self.button_change_defaults_submit_check_result.setText(_translate("dialog_submit", "Change submit check result defaults..."))
