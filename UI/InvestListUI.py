# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InvestListUI.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(630, 174)
        Form.setMaximumSize(QSize(630, 241))
        self.investListTable = QTableWidget(Form)
        if (self.investListTable.columnCount() < 6):
            self.investListTable.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.investListTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.investListTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.investListTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.investListTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.investListTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.investListTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.investListTable.setObjectName(u"investListTable")
        self.investListTable.setEnabled(True)
        self.investListTable.setGeometry(QRect(0, 0, 630, 174))
        self.investListTable.setMinimumSize(QSize(0, 0))
        self.investListTable.setMaximumSize(QSize(630, 241))
        self.investListTable.setFrameShape(QFrame.NoFrame)
        self.investListTable.setAutoScrollMargin(16)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        ___qtablewidgetitem = self.investListTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\ubcf4\uc720\uc790\uc0b0", None));
        ___qtablewidgetitem1 = self.investListTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\ubcf4\uc720\uc218\ub7c9", None));
        ___qtablewidgetitem2 = self.investListTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\ub9e4\uc218\ud3c9\uade0", None));
        ___qtablewidgetitem3 = self.investListTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"\ub9e4\uc218\uae08\uc561", None));
        ___qtablewidgetitem4 = self.investListTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"\ud3c9\uac00\uae08\uc561", None));
        ___qtablewidgetitem5 = self.investListTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"\ud3c9\uac00\uc190\uc775(%)", None));
    # retranslateUi

