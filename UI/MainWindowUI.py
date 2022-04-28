# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowUI.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from Widgets.OverviewWidget import OverviewWidget
from Widgets.InvestListWidget import InvestListWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(630, 485)
        MainWindow.setMinimumSize(QSize(630, 390))
        MainWindow.setMaximumSize(QSize(635, 16777215))
        self.config_sub_menu = QAction(MainWindow)
        self.config_sub_menu.setObjectName(u"config_sub_menu")
        self.exit_sub_menu = QAction(MainWindow)
        self.exit_sub_menu.setObjectName(u"exit_sub_menu")
        self.info_sub_menu = QAction(MainWindow)
        self.info_sub_menu.setObjectName(u"info_sub_menu")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.OverviewWidget = OverviewWidget(self.centralwidget)
        self.OverviewWidget.setObjectName(u"OverviewWidget")
        self.OverviewWidget.setMinimumSize(QSize(630, 0))
        self.OverviewWidget.setMaximumSize(QSize(16777215, 122))

        self.verticalLayout.addWidget(self.OverviewWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.keyId_cb = QComboBox(self.centralwidget)
        self.keyId_cb.setObjectName(u"keyId_cb")

        self.horizontalLayout.addWidget(self.keyId_cb)

        self.login_btn = QPushButton(self.centralwidget)
        self.login_btn.setObjectName(u"login_btn")

        self.horizontalLayout.addWidget(self.login_btn)

        self.start_trading_btn = QPushButton(self.centralwidget)
        self.start_trading_btn.setObjectName(u"start_trading_btn")

        self.horizontalLayout.addWidget(self.start_trading_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.InvestListWidget = InvestListWidget(self.centralwidget)
        self.InvestListWidget.setObjectName(u"InvestListWidget")
        self.InvestListWidget.setMinimumSize(QSize(630, 174))
        self.InvestListWidget.setMaximumSize(QSize(630, 174))

        self.verticalLayout.addWidget(self.InvestListWidget)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(611, 100))
        self.textEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEdit)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 630, 22))
        self.config_menu = QMenu(self.menubar)
        self.config_menu.setObjectName(u"config_menu")
        self.help_menu = QMenu(self.menubar)
        self.help_menu.setObjectName(u"help_menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.config_menu.menuAction())
        self.menubar.addAction(self.help_menu.menuAction())
        self.config_menu.addAction(self.config_sub_menu)
        self.config_menu.addAction(self.exit_sub_menu)
        self.help_menu.addAction(self.info_sub_menu)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Upbit \uc790\ub3d9\ub9e4\ub9e4", None))
        self.config_sub_menu.setText(QCoreApplication.translate("MainWindow", u"\ud658\uacbd\uc124\uc815", None))
        self.exit_sub_menu.setText(QCoreApplication.translate("MainWindow", u"\uc885\ub8cc", None))
        self.info_sub_menu.setText(QCoreApplication.translate("MainWindow", u"\uc815\ubcf4", None))
        self.login_btn.setText(QCoreApplication.translate("MainWindow", u"\ub85c\uadf8\uc778", None))
        self.start_trading_btn.setText(QCoreApplication.translate("MainWindow", u"\ub9e4\ub9e4 \uc2dc\uc791", None))
        self.config_menu.setTitle(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.help_menu.setTitle(QCoreApplication.translate("MainWindow", u"\ub3c4\uc6c0\ub9d0", None))
    # retranslateUi

