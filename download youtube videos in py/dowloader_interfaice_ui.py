# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dowloader_interfaice.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(461, 423)
        icon = QIcon()
        icon.addFile(u"icons/youtube_img.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QLineEdit{\n"
"    border: 1px solid rgba(255, 246, 246,80);\n"
"    border-radius: 10px;\n"
"    font-family: Comic Sans MS;\n"
"    font-size: 16px;\n"
"    color: white;\n"
"    background-color: rgb(62, 75, 75)\n"
"}\n"
"\n"
"QLabel{\n"
"    border-radius: 10px;\n"
"    font-family: Comic Sans MS;\n"
"    color:white;\n"
"    font-size: 16px;\n"
"    background-color: rgb(62, 75, 75);\n"
"    border:none;\n"
"} \n"
"\n"
"QWidget{\n"
"    background-color: rgb(22, 54, 56);\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: rgba(116, 63, 240,90);\n"
"    font-family: Comic Sans MS;\n"
"    font-size: 16px;\n"
"    border: 1px solid rgba(247,247,247,80);\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    opacity: 0.2;\n"
"    transition: all 0.5s;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgba(116, 63, 240,90);\n"
"	border: 1px solid rgba(247,247,247,80);\n"
"}\n"
"\n"
"QFrame{\n"
"    background-color: rgb(62, 75, 75);\n"
"    border-radius: 10"
                        "px;\n"
"    border: none;\n"
"} \n"
"\n"
"QComboBox{\n"
"    font-family: Comic Sans MS;\n"
"    font-size: 16px;\n"
"    background-color:rgb(86, 83, 90);\n"
"    border-radius: 10px;\n"
"    border:1px solid rgb(113, 111, 117);\n"
"	color:white;\n"
"}\n"
"\n"
"QPlainTextEdit{\n"
"	border: 1px solid rgba(247,247,247,80);\n"
"    border-radius: 10px;\n"
"    font-family: Comic Sans MS;\n"
"    font-size: 14px;\n"
"    color: white;\n"
"    background-color:rgb(86, 83, 90)\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.WORK_FRAME = QFrame(self.centralwidget)
        self.WORK_FRAME.setObjectName(u"WORK_FRAME")
        self.WORK_FRAME.setGeometry(QRect(10, 10, 441, 401))
        self.WORK_FRAME.setFrameShape(QFrame.StyledPanel)
        self.WORK_FRAME.setFrameShadow(QFrame.Raised)
        self.DOWNLOAD_BUTTON = QPushButton(self.WORK_FRAME)
        self.DOWNLOAD_BUTTON.setObjectName(u"DOWNLOAD_BUTTON")
        self.DOWNLOAD_BUTTON.setGeometry(QRect(140, 330, 151, 41))
        icon1 = QIcon()
        icon1.addFile(u"icons/download-img.png", QSize(), QIcon.Normal, QIcon.Off)
        self.DOWNLOAD_BUTTON.setIcon(icon1)
        self.DOWNLOAD_BUTTON.setIconSize(QSize(24, 24))
        self.HELLO_LABEL = QLabel(self.WORK_FRAME)
        self.HELLO_LABEL.setObjectName(u"HELLO_LABEL")
        self.HELLO_LABEL.setGeometry(QRect(100, 20, 251, 41))
        self.LINK_LABEL = QLabel(self.WORK_FRAME)
        self.LINK_LABEL.setObjectName(u"LINK_LABEL")
        self.LINK_LABEL.setGeometry(QRect(36, 92, 51, 31))
        self.LINK_CHOICE = QLineEdit(self.WORK_FRAME)
        self.LINK_CHOICE.setObjectName(u"LINK_CHOICE")
        self.LINK_CHOICE.setGeometry(QRect(82, 99, 331, 21))
        self.FILE_LABEL = QLabel(self.WORK_FRAME)
        self.FILE_LABEL.setObjectName(u"FILE_LABEL")
        self.FILE_LABEL.setGeometry(QRect(30, 170, 101, 31))
        self.FILE_CHOICE = QLineEdit(self.WORK_FRAME)
        self.FILE_CHOICE.setObjectName(u"FILE_CHOICE")
        self.FILE_CHOICE.setGeometry(QRect(130, 180, 281, 20))
        self.RESULT_LABEL = QLabel(self.WORK_FRAME)
        self.RESULT_LABEL.setObjectName(u"RESULT_LABEL")
        self.RESULT_LABEL.setGeometry(QRect(140, 250, 151, 31))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Downloader", None))
        self.DOWNLOAD_BUTTON.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.HELLO_LABEL.setText(QCoreApplication.translate("MainWindow", u"Welcome! Fill in the lines below", None))
        self.LINK_LABEL.setText(QCoreApplication.translate("MainWindow", u"Link :", None))
        self.FILE_LABEL.setText(QCoreApplication.translate("MainWindow", u"Road to file:", None))
        self.RESULT_LABEL.setText("")
    # retranslateUi

