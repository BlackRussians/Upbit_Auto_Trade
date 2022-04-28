# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConfigUI.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(417, 305)
        Dialog.setModal(True)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(45, 281, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.config_tab = QTabWidget(Dialog)
        self.config_tab.setObjectName(u"config_tab")
        self.config_tab.setGeometry(QRect(10, 20, 381, 251))
        self.config_tab.setTabShape(QTabWidget.Rounded)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.key_list = QListWidget(self.tab)
        self.key_list.setObjectName(u"key_list")
        self.key_list.setGeometry(QRect(20, 20, 111, 181))
        self.key_list.setFrameShape(QFrame.StyledPanel)
        self.key_list.setFrameShadow(QFrame.Sunken)
        self.key_list.setLineWidth(1)
        self.key_list.setMidLineWidth(0)
        self.frame = QFrame(self.tab)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(140, 20, 221, 181))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.gridLayoutWidget_2 = QWidget(self.frame)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 10, 201, 81))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.SECRET_KEY = QLineEdit(self.gridLayoutWidget_2)
        self.SECRET_KEY.setObjectName(u"SECRET_KEY")
        self.SECRET_KEY.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.gridLayout_2.addWidget(self.SECRET_KEY, 3, 2, 1, 1)

        self.API_KEY = QLineEdit(self.gridLayoutWidget_2)
        self.API_KEY.setObjectName(u"API_KEY")
        self.API_KEY.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.gridLayout_2.addWidget(self.API_KEY, 1, 2, 1, 1)

        self.API_KEY_label = QLabel(self.gridLayoutWidget_2)
        self.API_KEY_label.setObjectName(u"API_KEY_label")

        self.gridLayout_2.addWidget(self.API_KEY_label, 1, 1, 1, 1)

        self.SECRET_KEY_label = QLabel(self.gridLayoutWidget_2)
        self.SECRET_KEY_label.setObjectName(u"SECRET_KEY_label")

        self.gridLayout_2.addWidget(self.SECRET_KEY_label, 3, 1, 1, 1)

        self.name = QLineEdit(self.gridLayoutWidget_2)
        self.name.setObjectName(u"name")

        self.gridLayout_2.addWidget(self.name, 0, 2, 1, 1)

        self.name_label = QLabel(self.gridLayoutWidget_2)
        self.name_label.setObjectName(u"name_label")

        self.gridLayout_2.addWidget(self.name_label, 0, 1, 1, 1)

        self.horizontalLayoutWidget_2 = QWidget(self.frame)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(50, 150, 171, 31))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_addKey = QPushButton(self.horizontalLayoutWidget_2)
        self.btn_addKey.setObjectName(u"btn_addKey")
        self.btn_addKey.setEnabled(True)
        self.btn_addKey.setMinimumSize(QSize(76, 24))
        self.btn_addKey.setMaximumSize(QSize(76, 24))

        self.horizontalLayout_2.addWidget(self.btn_addKey)

        self.btn_removeKey = QPushButton(self.horizontalLayoutWidget_2)
        self.btn_removeKey.setObjectName(u"btn_removeKey")
        self.btn_removeKey.setMinimumSize(QSize(76, 24))
        self.btn_removeKey.setMaximumSize(QSize(76, 24))

        self.horizontalLayout_2.addWidget(self.btn_removeKey)

        self.config_tab.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.watch_list = QListWidget(self.tab_2)
        self.watch_list.setObjectName(u"watch_list")
        self.watch_list.setGeometry(QRect(20, 20, 111, 181))
        self.frame_2 = QFrame(self.tab_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(140, 20, 221, 181))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Sunken)
        self.gridLayoutWidget = QWidget(self.frame_2)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 201, 71))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.watch_price_label = QLabel(self.gridLayoutWidget)
        self.watch_price_label.setObjectName(u"watch_price_label")

        self.gridLayout.addWidget(self.watch_price_label, 1, 0, 1, 1)

        self.ticker_cb_label = QLabel(self.gridLayoutWidget)
        self.ticker_cb_label.setObjectName(u"ticker_cb_label")
        self.ticker_cb_label.setLayoutDirection(Qt.LeftToRight)
        self.ticker_cb_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.ticker_cb_label, 0, 0, 1, 1)

        self.watch_price = QDoubleSpinBox(self.gridLayoutWidget)
        self.watch_price.setObjectName(u"watch_price")
        self.watch_price.setDecimals(4)
        self.watch_price.setMaximum(9999999999.000000000000000)
        self.watch_price.setStepType(QAbstractSpinBox.DefaultStepType)

        self.gridLayout.addWidget(self.watch_price, 1, 1, 1, 1)

        self.ticker_cb = QComboBox(self.gridLayoutWidget)
        self.ticker_cb.setObjectName(u"ticker_cb")
        self.ticker_cb.setEditable(True)

        self.gridLayout.addWidget(self.ticker_cb, 0, 1, 1, 1)

        self.horizontalLayoutWidget = QWidget(self.frame_2)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(50, 150, 171, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_addItem = QPushButton(self.horizontalLayoutWidget)
        self.btn_addItem.setObjectName(u"btn_addItem")
        self.btn_addItem.setMinimumSize(QSize(76, 24))
        self.btn_addItem.setMaximumSize(QSize(76, 24))

        self.horizontalLayout.addWidget(self.btn_addItem)

        self.btn_removeItem = QPushButton(self.horizontalLayoutWidget)
        self.btn_removeItem.setObjectName(u"btn_removeItem")
        self.btn_removeItem.setMinimumSize(QSize(76, 24))
        self.btn_removeItem.setMaximumSize(QSize(76, 24))

        self.horizontalLayout.addWidget(self.btn_removeItem)

        self.config_tab.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        self.config_tab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\ud658\uacbd\uc124\uc815", None))
        self.API_KEY_label.setText(QCoreApplication.translate("Dialog", u"API_KEY", None))
        self.SECRET_KEY_label.setText(QCoreApplication.translate("Dialog", u"SECRET_KEY", None))
        self.name_label.setText(QCoreApplication.translate("Dialog", u"\uc774\ub984", None))
        self.btn_addKey.setText(QCoreApplication.translate("Dialog", u"\ucd94\uac00", None))
        self.btn_removeKey.setText(QCoreApplication.translate("Dialog", u"\uc81c\uac70", None))
        self.config_tab.setTabText(self.config_tab.indexOf(self.tab), QCoreApplication.translate("Dialog", u"\ud0a4 \uc124\uc815", None))
        self.watch_price_label.setText(QCoreApplication.translate("Dialog", u"\uac10\uc2dc\uac00\uaca9", None))
        self.ticker_cb_label.setText(QCoreApplication.translate("Dialog", u"\uac10\uc2dc\ucf54\uc778", None))
        self.ticker_cb.setCurrentText("")
        self.btn_addItem.setText(QCoreApplication.translate("Dialog", u"\ucd94\uac00", None))
        self.btn_removeItem.setText(QCoreApplication.translate("Dialog", u"\uc81c\uac70", None))
        self.config_tab.setTabText(self.config_tab.indexOf(self.tab_2), QCoreApplication.translate("Dialog", u"\uac10\uc2dc", None))
    # retranslateUi

