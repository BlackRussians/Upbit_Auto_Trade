# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'OverviewUI.ui'
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
        Form.resize(630, 149)
        Form.setMinimumSize(QSize(630, 0))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.current_krw_label = QLabel(Form)
        self.current_krw_label.setObjectName(u"current_krw_label")
        font = QFont()
        font.setPointSize(9)
        font.setBold(False)
        self.current_krw_label.setFont(font)

        self.horizontalLayout.addWidget(self.current_krw_label)

        self.current_krw = QLabel(Form)
        self.current_krw.setObjectName(u"current_krw")
        self.current_krw.setMinimumSize(QSize(100, 0))
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        self.current_krw.setFont(font1)
        self.current_krw.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.current_krw)

        self.trade_price = QLabel(Form)
        self.trade_price.setObjectName(u"trade_price")
        self.trade_price.setMinimumSize(QSize(135, 0))
        self.trade_price.setMaximumSize(QSize(16777215, 33))
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(True)
        self.trade_price.setFont(font2)
        self.trade_price.setStyleSheet(u"color: red")
        self.trade_price.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.trade_price)

        self.change_rate = QLabel(Form)
        self.change_rate.setObjectName(u"change_rate")
        self.change_rate.setMinimumSize(QSize(50, 0))
        self.change_rate.setMaximumSize(QSize(50, 33))
        self.change_rate.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.change_rate)

        self.ticker_cb = QComboBox(Form)
        self.ticker_cb.setObjectName(u"ticker_cb")
        self.ticker_cb.setEditable(True)
        self.ticker_cb.setInsertPolicy(QComboBox.NoInsert)

        self.horizontalLayout.addWidget(self.ticker_cb)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.prev_closing_price_title = QLabel(Form)
        self.prev_closing_price_title.setObjectName(u"prev_closing_price_title")

        self.gridLayout.addWidget(self.prev_closing_price_title, 0, 2, 1, 1)

        self.prev_closing_price = QLabel(Form)
        self.prev_closing_price.setObjectName(u"prev_closing_price")

        self.gridLayout.addWidget(self.prev_closing_price, 0, 3, 1, 1)

        self.high_price_title = QLabel(Form)
        self.high_price_title.setObjectName(u"high_price_title")

        self.gridLayout.addWidget(self.high_price_title, 1, 2, 1, 1)

        self.trade_volume_24H_title = QLabel(Form)
        self.trade_volume_24H_title.setObjectName(u"trade_volume_24H_title")

        self.gridLayout.addWidget(self.trade_volume_24H_title, 1, 0, 1, 1)

        self.high_price = QLabel(Form)
        self.high_price.setObjectName(u"high_price")
        self.high_price.setStyleSheet(u"color: red")

        self.gridLayout.addWidget(self.high_price, 1, 3, 1, 1)

        self.volume = QLabel(Form)
        self.volume.setObjectName(u"volume")

        self.gridLayout.addWidget(self.volume, 0, 1, 1, 1)

        self.trade_volume_24H = QLabel(Form)
        self.trade_volume_24H.setObjectName(u"trade_volume_24H")

        self.gridLayout.addWidget(self.trade_volume_24H, 1, 1, 1, 1)

        self.volume_title = QLabel(Form)
        self.volume_title.setObjectName(u"volume_title")

        self.gridLayout.addWidget(self.volume_title, 0, 0, 1, 1)

        self.volume_power_title = QLabel(Form)
        self.volume_power_title.setObjectName(u"volume_power_title")

        self.gridLayout.addWidget(self.volume_power_title, 2, 0, 1, 1)

        self.volume_power = QLabel(Form)
        self.volume_power.setObjectName(u"volume_power")

        self.gridLayout.addWidget(self.volume_power, 2, 1, 1, 1)

        self.low_price_title = QLabel(Form)
        self.low_price_title.setObjectName(u"low_price_title")

        self.gridLayout.addWidget(self.low_price_title, 2, 2, 1, 1)

        self.low_price = QLabel(Form)
        self.low_price.setObjectName(u"low_price")
        self.low_price.setStyleSheet(u"color: blue")

        self.gridLayout.addWidget(self.low_price, 2, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.current_krw_label.setText(QCoreApplication.translate("Form", u"\ubcf4\uc720 KRW", None))
        self.current_krw.setText(QCoreApplication.translate("Form", u"0", None))
        self.trade_price.setText(QCoreApplication.translate("Form", u"0", None))
        self.change_rate.setText(QCoreApplication.translate("Form", u"0%", None))
        self.prev_closing_price_title.setText(QCoreApplication.translate("Form", u"\uc804\uc77c\uc885\uac00", None))
        self.prev_closing_price.setText("")
        self.high_price_title.setText(QCoreApplication.translate("Form", u"\ub2f9\uc77c\uace0\uac00", None))
        self.trade_volume_24H_title.setText(QCoreApplication.translate("Form", u"\uac70\ub798\ub300\uae08(24H)", None))
        self.high_price.setText("")
        self.volume.setText("")
        self.trade_volume_24H.setText("")
        self.volume_title.setText(QCoreApplication.translate("Form", u"\uac70\ub798\ub7c9", None))
        self.volume_power_title.setText(QCoreApplication.translate("Form", u"\uccb4\uacb0\uac15\ub3c4", None))
        self.volume_power.setText("")
        self.low_price_title.setText(QCoreApplication.translate("Form", u"\ub2f9\uc77c\uc800\uac00", None))
        self.low_price.setText("")
    # retranslateUi

