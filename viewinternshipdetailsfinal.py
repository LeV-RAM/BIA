# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewinternshipdetailsfinal.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DetailsWindow(object):
    def showProfile(self):
        from profile import Ui_ProfileWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ProfileWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def goToMain(self):
        from mainpage import Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.showMaximized()
    def goToSearch(self):
        from searchpagefinal import Ui_SearchWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SearchWindow()
        self.ui.setupUi(self.window)
        self.window.showMaximized()
    def logout(self):
        from login import Ui_Login
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Login()
        self.ui.setupUi(self.window)
        self.window.showMaximized()
    def setupUi(self, DetailsWindow):
        DetailsWindow.setObjectName("DetailsWindow")
        DetailsWindow.resize(1252, 947)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DetailsWindow.sizePolicy().hasHeightForWidth())
        DetailsWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(DetailsWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy)
        self.header.setMaximumSize(QtCore.QSize(16777215, 241))
        self.header.setStyleSheet("background-color:white;")
        self.header.setTitle("")
        self.header.setObjectName("header")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.header)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.headerVLayout = QtWidgets.QVBoxLayout()
        self.headerVLayout.setSpacing(0)
        self.headerVLayout.setObjectName("headerVLayout")
        self.heder1 = QtWidgets.QGroupBox(self.header)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.heder1.sizePolicy().hasHeightForWidth())
        self.heder1.setSizePolicy(sizePolicy)
        self.heder1.setStyleSheet("*{\n"
"    background-color:white;\n"
"    border-bottom: 2px solid black;\n"
"}\n"
"\n"
"#BinusLabel{\n"
"border:none;\n"
"}\n"
"\n"
"#InternLabel{\n"
"border:none;\n"
"}\n"
"\n"
"#MoreLabel{\n"
"border:none;\n"
"}\n"
"\n"
"#Profilepng{\n"
"border:none;\n"
"}")
        self.heder1.setTitle("")
        self.heder1.setObjectName("heder1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.heder1)
        self.horizontalLayout_4.setContentsMargins(0, 0, 10, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.heder1HLayout = QtWidgets.QHBoxLayout()
        self.heder1HLayout.setObjectName("heder1HLayout")
        self.MoreLabel = QtWidgets.QLabel(self.heder1)
        self.MoreLabel.setMaximumSize(QtCore.QSize(50, 50))
        self.MoreLabel.setText("")
        self.MoreLabel.setPixmap(QtGui.QPixmap(":/logo/assets/aa.jpg"))
        self.MoreLabel.setScaledContents(True)
        self.MoreLabel.setObjectName("MoreLabel")
        self.heder1HLayout.addWidget(self.MoreLabel)
        self.BinusLabel = QtWidgets.QLabel(self.heder1)
        self.BinusLabel.setMaximumSize(QtCore.QSize(180, 39))
        self.BinusLabel.setBaseSize(QtCore.QSize(1, 0))
        self.BinusLabel.setText("")
        self.BinusLabel.setPixmap(QtGui.QPixmap(":/logo/assets/binuslogo.jpg"))
        self.BinusLabel.setScaledContents(True)
        self.BinusLabel.setObjectName("BinusLabel")
        self.heder1HLayout.addWidget(self.BinusLabel)
        self.InternLabel = QtWidgets.QLabel(self.heder1)
        self.InternLabel.setMaximumSize(QtCore.QSize(300, 30))
        self.InternLabel.setText("")
        self.InternLabel.setPixmap(QtGui.QPixmap(":/logo/assets/intern.jpg"))
        self.InternLabel.setScaledContents(True)
        self.InternLabel.setObjectName("InternLabel")
        self.heder1HLayout.addWidget(self.InternLabel)
        self.horizontalLayout_4.addLayout(self.heder1HLayout)
        self.BlenkH1 = QtWidgets.QGroupBox(self.heder1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BlenkH1.sizePolicy().hasHeightForWidth())
        self.BlenkH1.setSizePolicy(sizePolicy)
        self.BlenkH1.setStyleSheet("border: none;")
        self.BlenkH1.setTitle("")
        self.BlenkH1.setObjectName("BlenkH1")
        self.horizontalLayout_4.addWidget(self.BlenkH1)
        self.ProfButton = QtWidgets.QPushButton(self.heder1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ProfButton.sizePolicy().hasHeightForWidth())
        self.ProfButton.setSizePolicy(sizePolicy)
        self.ProfButton.setStyleSheet("border:none;")
        self.ProfButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/assets/1A.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ProfButton.setIcon(icon)
        self.ProfButton.setIconSize(QtCore.QSize(45, 45))
        self.ProfButton.setObjectName("ProfButton")
        self.ProfButton.clicked.connect(self.showProfile)
        self.horizontalLayout_4.addWidget(self.ProfButton)
        self.headerVLayout.addWidget(self.heder1)
        self.heder2 = QtWidgets.QGroupBox(self.header)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.heder2.sizePolicy().hasHeightForWidth())
        self.heder2.setSizePolicy(sizePolicy)
        self.heder2.setMinimumSize(QtCore.QSize(0, 125))
        self.heder2.setStyleSheet("*{\n"
"    border-top: 0.5px solid black;\n"
"    border-bottom: 0.5px solid black;\n"
"}")
        self.heder2.setTitle("")
        self.heder2.setObjectName("heder2")
        self.BinusLogo = QtWidgets.QLabel(self.heder2)
        self.BinusLogo.setGeometry(QtCore.QRect(40, 0, 181, 125))
        self.BinusLogo.setText("")
        self.BinusLogo.setPixmap(QtGui.QPixmap(":/logo/assets/login2.jpg"))
        self.BinusLogo.setScaledContents(True)
        self.BinusLogo.setObjectName("BinusLogo")
        self.headerVLayout.addWidget(self.heder2)
        self.heder3 = QtWidgets.QGroupBox(self.header)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.heder3.sizePolicy().hasHeightForWidth())
        self.heder3.setSizePolicy(sizePolicy)
        self.heder3.setMaximumSize(QtCore.QSize(16777215, 56))
        self.heder3.setStyleSheet("*{\n"
"    border-top: 0.5px solid black;\n"
"    border-bottom: 0.5px solid black;\n"
"}")
        self.heder3.setTitle("")
        self.heder3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.heder3.setObjectName("heder3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.heder3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.BLenk = QtWidgets.QGroupBox(self.heder3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BLenk.sizePolicy().hasHeightForWidth())
        self.BLenk.setSizePolicy(sizePolicy)
        self.BLenk.setStyleSheet("border:none;")
        self.BLenk.setObjectName("BLenk")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.BLenk)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.heder3HLayout = QtWidgets.QGroupBox(self.BLenk)
        self.heder3HLayout.setStyleSheet("border:none;\n"
"border-color: white;")
        self.heder3HLayout.setTitle("")
        self.heder3HLayout.setAlignment(QtCore.Qt.AlignCenter)
        self.heder3HLayout.setObjectName("heder3HLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.heder3HLayout)
        self.horizontalLayout_3.setContentsMargins(100, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(30)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.HomeButton = QtWidgets.QPushButton(self.heder3HLayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HomeButton.sizePolicy().hasHeightForWidth())
        self.HomeButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.HomeButton.setFont(font)
        self.HomeButton.setStyleSheet("border: none;\n"
"padding-bottom:10px;")
        self.HomeButton.setObjectName("HomeButton")
        self.HomeButton.clicked.connect(self.goToMain)
        self.HomeButton.clicked.connect(DetailsWindow.close)
        self.horizontalLayout_3.addWidget(self.HomeButton)
        self.SearchButton = QtWidgets.QPushButton(self.heder3HLayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SearchButton.sizePolicy().hasHeightForWidth())
        self.SearchButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.SearchButton.setFont(font)
        self.SearchButton.setStyleSheet("border: none;\n"
"border-bottom: 3px solid black;\n"
"padding-bottom:10px;")
        self.SearchButton.setObjectName("SearchButton")
        self.SearchButton.clicked.connect(self.goToSearch)
        self.SearchButton.clicked.connect(DetailsWindow.close)
        self.horizontalLayout_3.addWidget(self.SearchButton)
        self.horizontalLayout.addWidget(self.heder3HLayout)
        self.BlankH3 = QtWidgets.QGroupBox(self.BLenk)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BlankH3.sizePolicy().hasHeightForWidth())
        self.BlankH3.setSizePolicy(sizePolicy)
        self.BlankH3.setMinimumSize(QtCore.QSize(0, 0))
        self.BlankH3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.BlankH3.setStyleSheet("border:none;")
        self.BlankH3.setTitle("")
        self.BlankH3.setObjectName("BlankH3")
        self.horizontalLayout.addWidget(self.BlankH3)
        self.SignOutButton = QtWidgets.QPushButton(self.BLenk)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SignOutButton.sizePolicy().hasHeightForWidth())
        self.SignOutButton.setSizePolicy(sizePolicy)
        self.SignOutButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SignOutButton.setFont(font)
        self.SignOutButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.SignOutButton.setStyleSheet("border:none;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/log-out.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SignOutButton.setIcon(icon1)
        self.SignOutButton.setIconSize(QtCore.QSize(30, 30))
        self.SignOutButton.setCheckable(False)
        self.SignOutButton.setChecked(False)
        self.SignOutButton.setObjectName("SignOutButton")
        self.SignOutButton.clicked.connect(self.logout)
        self.SignOutButton.clicked.connect(DetailsWindow.close)
        self.horizontalLayout.addWidget(self.SignOutButton)
        self.horizontalLayout_2.addWidget(self.BLenk)
        self.headerVLayout.addWidget(self.heder3)
        self.verticalLayout_3.addLayout(self.headerVLayout)
        self.verticalLayout.addWidget(self.header)
        self.content = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.content.sizePolicy().hasHeightForWidth())
        self.content.setSizePolicy(sizePolicy)
        self.content.setMinimumSize(QtCore.QSize(0, 0))
        self.content.setAutoFillBackground(False)
        self.content.setStyleSheet("background-color:white;\n"
"")
        self.content.setTitle("")
        self.content.setObjectName("content")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.contentBigBox = QtWidgets.QGroupBox(self.content)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contentBigBox.sizePolicy().hasHeightForWidth())
        self.contentBigBox.setSizePolicy(sizePolicy)
        self.contentBigBox.setStyleSheet("border:none;")
        self.contentBigBox.setTitle("")
        self.contentBigBox.setObjectName("contentBigBox")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.contentBigBox)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.ContentBox = QtWidgets.QGroupBox(self.contentBigBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ContentBox.sizePolicy().hasHeightForWidth())
        self.ContentBox.setSizePolicy(sizePolicy)
        self.ContentBox.setAutoFillBackground(False)
        self.ContentBox.setStyleSheet("background-color:white;")
        self.ContentBox.setTitle("")
        self.ContentBox.setObjectName("ContentBox")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.ContentBox)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.BigContainer = QtWidgets.QGroupBox(self.ContentBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BigContainer.sizePolicy().hasHeightForWidth())
        self.BigContainer.setSizePolicy(sizePolicy)
        self.BigContainer.setMaximumSize(QtCore.QSize(600, 16777215))
        self.BigContainer.setSizeIncrement(QtCore.QSize(0, 0))
        self.BigContainer.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.BigContainer.setStyleSheet("border:none;")
        self.BigContainer.setTitle("")
        self.BigContainer.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.BigContainer.setObjectName("BigContainer")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.BigContainer)
        self.verticalLayout_2.setContentsMargins(25, 0, 50, 100)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Container = QtWidgets.QGroupBox(self.BigContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Container.sizePolicy().hasHeightForWidth())
        self.Container.setSizePolicy(sizePolicy)
        self.Container.setMinimumSize(QtCore.QSize(400, 400))
        self.Container.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Container.setStyleSheet("background-color: white;\n"
"border-style:solid;\n"
"border-width:2px;\n"
"color:white;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"")
        self.Container.setTitle("")
        self.Container.setAlignment(QtCore.Qt.AlignCenter)
        self.Container.setObjectName("Container")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.Container)
        self.verticalLayout_7.setContentsMargins(11, -1, -1, -1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.CompanyLogo = QtWidgets.QLabel(self.Container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CompanyLogo.sizePolicy().hasHeightForWidth())
        self.CompanyLogo.setSizePolicy(sizePolicy)
        self.CompanyLogo.setMinimumSize(QtCore.QSize(260, 100))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.CompanyLogo.setFont(font)
        self.CompanyLogo.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.CompanyLogo.setAutoFillBackground(False)
        self.CompanyLogo.setStyleSheet("border: none;")
        self.CompanyLogo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.CompanyLogo.setText("")
        self.CompanyLogo.setPixmap(QtGui.QPixmap(":/logo/assets/lgobca.jpg"))
        self.CompanyLogo.setScaledContents(True)
        self.CompanyLogo.setAlignment(QtCore.Qt.AlignCenter)
        self.CompanyLogo.setObjectName("CompanyLogo")
        self.verticalLayout_7.addWidget(self.CompanyLogo)
        self.CompanyBoxName = QtWidgets.QLabel(self.Container)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.CompanyBoxName.setFont(font)
        self.CompanyBoxName.setStyleSheet("border: none; color: black;")
        self.CompanyBoxName.setAlignment(QtCore.Qt.AlignCenter)
        self.CompanyBoxName.setWordWrap(True)
        self.CompanyBoxName.setObjectName("CompanyBoxName")
        self.verticalLayout_7.addWidget(self.CompanyBoxName)
        self.CompanyInternshipName = QtWidgets.QLabel(self.Container)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.CompanyInternshipName.setFont(font)
        self.CompanyInternshipName.setStyleSheet("border: none; color: black;")
        self.CompanyInternshipName.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.CompanyInternshipName.setWordWrap(True)
        self.CompanyInternshipName.setObjectName("CompanyInternshipName")
        self.verticalLayout_7.addWidget(self.CompanyInternshipName)
        self.CompanyAddress = QtWidgets.QLabel(self.Container)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CompanyAddress.setFont(font)
        self.CompanyAddress.setStyleSheet("border: none; color: black;")
        self.CompanyAddress.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.CompanyAddress.setWordWrap(True)
        self.CompanyAddress.setObjectName("CompanyAddress")
        self.verticalLayout_7.addWidget(self.CompanyAddress)
        self.verticalLayout_2.addWidget(self.Container)
        self.horizontalLayout_7.addWidget(self.BigContainer)
        self.Descriptionbox = QtWidgets.QVBoxLayout()
        self.Descriptionbox.setObjectName("Descriptionbox")
        self.nameLabel = QtWidgets.QLabel(self.ContentBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameLabel.sizePolicy().hasHeightForWidth())
        self.nameLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.nameLabel.setFont(font)
        self.nameLabel.setStyleSheet("color: #0097DA;")
        self.nameLabel.setWordWrap(True)
        self.nameLabel.setObjectName("nameLabel")
        self.Descriptionbox.addWidget(self.nameLabel)
        self.nameDesc = QtWidgets.QLabel(self.ContentBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameDesc.sizePolicy().hasHeightForWidth())
        self.nameDesc.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nameDesc.setFont(font)
        self.nameDesc.setStyleSheet("margin-bottom:25px;")
        self.nameDesc.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.nameDesc.setWordWrap(True)
        self.nameDesc.setObjectName("nameDesc")
        self.Descriptionbox.addWidget(self.nameDesc)
        self.reqLabel = QtWidgets.QLabel(self.ContentBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reqLabel.sizePolicy().hasHeightForWidth())
        self.reqLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.reqLabel.setFont(font)
        self.reqLabel.setStyleSheet("color: #0097DA;")
        self.reqLabel.setObjectName("reqLabel")
        self.Descriptionbox.addWidget(self.reqLabel)
        self.reqDesc = QtWidgets.QLabel(self.ContentBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reqDesc.sizePolicy().hasHeightForWidth())
        self.reqDesc.setSizePolicy(sizePolicy)
        self.reqDesc.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.reqDesc.setFont(font)
        self.reqDesc.setStyleSheet("margin-bottom:25px;")
        self.reqDesc.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.reqDesc.setWordWrap(True)
        self.reqDesc.setObjectName("reqDesc")
        self.Descriptionbox.addWidget(self.reqDesc)
        self.recLabel = QtWidgets.QLabel(self.ContentBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recLabel.sizePolicy().hasHeightForWidth())
        self.recLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.recLabel.setFont(font)
        self.recLabel.setStyleSheet("color: #0097DA;")
        self.recLabel.setWordWrap(True)
        self.recLabel.setObjectName("recLabel")
        self.Descriptionbox.addWidget(self.recLabel)
        self.recDesc = QtWidgets.QLabel(self.ContentBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recDesc.sizePolicy().hasHeightForWidth())
        self.recDesc.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.recDesc.setFont(font)
        self.recDesc.setStyleSheet("margin-bottom:25px;")
        self.recDesc.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.recDesc.setWordWrap(True)
        self.recDesc.setObjectName("recDesc")
        self.Descriptionbox.addWidget(self.recDesc)
        self.linkLabel = QtWidgets.QLabel(self.ContentBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.linkLabel.sizePolicy().hasHeightForWidth())
        self.linkLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.linkLabel.setFont(font)
        self.linkLabel.setStyleSheet("color: #0097DA;")
        self.linkLabel.setWordWrap(True)
        self.linkLabel.setObjectName("linkLabel")
        self.Descriptionbox.addWidget(self.linkLabel)
        self.linkDesc = QtWidgets.QLabel(self.ContentBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.linkDesc.sizePolicy().hasHeightForWidth())
        self.linkDesc.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.linkDesc.setFont(font)
        self.linkDesc.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.linkDesc.setObjectName("linkDesc")
        self.Descriptionbox.addWidget(self.linkDesc)
        self.horizontalLayout_7.addLayout(self.Descriptionbox)
        self.horizontalLayout_10.addWidget(self.ContentBox)
        self.horizontalLayout_8.addWidget(self.contentBigBox)
        self.verticalLayout.addWidget(self.content)
        self.footer = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.footer.sizePolicy().hasHeightForWidth())
        self.footer.setSizePolicy(sizePolicy)
        self.footer.setMinimumSize(QtCore.QSize(0, 0))
        self.footer.setMaximumSize(QtCore.QSize(16777215, 51))
        self.footer.setStyleSheet("*{\n"
"background-color:white;\n"
"}")
        self.footer.setTitle("")
        self.footer.setObjectName("footer")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.footer)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.isifuter = QtWidgets.QGroupBox(self.footer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.isifuter.sizePolicy().hasHeightForWidth())
        self.isifuter.setSizePolicy(sizePolicy)
        self.isifuter.setTitle("")
        self.isifuter.setObjectName("isifuter")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.isifuter)
        self.horizontalLayout_6.setContentsMargins(12, 0, 12, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.copyrightLogo = QtWidgets.QLabel(self.isifuter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.copyrightLogo.sizePolicy().hasHeightForWidth())
        self.copyrightLogo.setSizePolicy(sizePolicy)
        self.copyrightLogo.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.copyrightLogo.setFont(font)
        self.copyrightLogo.setText("")
        self.copyrightLogo.setPixmap(QtGui.QPixmap(":/logo/copyright.png"))
        self.copyrightLogo.setScaledContents(True)
        self.copyrightLogo.setObjectName("copyrightLogo")
        self.horizontalLayout_6.addWidget(self.copyrightLogo)
        self.binusUniversity = QtWidgets.QLabel(self.isifuter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.binusUniversity.sizePolicy().hasHeightForWidth())
        self.binusUniversity.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.binusUniversity.setFont(font)
        self.binusUniversity.setObjectName("binusUniversity")
        self.horizontalLayout_6.addWidget(self.binusUniversity)
        self.blenkFuter = QtWidgets.QGroupBox(self.isifuter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blenkFuter.sizePolicy().hasHeightForWidth())
        self.blenkFuter.setSizePolicy(sizePolicy)
        self.blenkFuter.setStyleSheet("border:none;")
        self.blenkFuter.setTitle("")
        self.blenkFuter.setObjectName("blenkFuter")
        self.horizontalLayout_6.addWidget(self.blenkFuter)
        self.binusMaya = QtWidgets.QLabel(self.isifuter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.binusMaya.sizePolicy().hasHeightForWidth())
        self.binusMaya.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.binusMaya.setFont(font)
        self.binusMaya.setAlignment(QtCore.Qt.AlignCenter)
        self.binusMaya.setObjectName("binusMaya")
        self.horizontalLayout_6.addWidget(self.binusMaya)
        self.horizontalLayout_5.addWidget(self.isifuter)
        self.verticalLayout.addWidget(self.footer)
        DetailsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(DetailsWindow)
        QtCore.QMetaObject.connectSlotsByName(DetailsWindow)

    def retranslateUi(self, DetailsWindow):
        _translate = QtCore.QCoreApplication.translate
        DetailsWindow.setWindowTitle(_translate("DetailsWindow", "DetailsWindow"))
        self.HomeButton.setText(_translate("DetailsWindow", "HOME"))
        self.SearchButton.setText(_translate("DetailsWindow", "SEARCH"))
        self.SignOutButton.setText(_translate("DetailsWindow", "Sign Out"))
        self.CompanyBoxName.setText(_translate("DetailsWindow", "BANG CENTIL ACIA"))
        self.CompanyInternshipName.setText(_translate("DetailsWindow", "Magang Bakti Internship Program"))
        self.CompanyAddress.setText(_translate("DetailsWindow", "GEDUNG MENARA BCA GRAND INDONESIA LT 18, JL. MH THAMRIN NO.1 JAKARTA 10310"))
        self.nameLabel.setText(_translate("DetailsWindow", "Name"))
        self.nameDesc.setText(_translate("DetailsWindow", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus volutpat eros libero, non dignissim ex mattis sed. Pellentesque non malesuada nulla, quis venenatis odio. Donec eget mi at dolor posuere hendrerit. Integer nisi mi, aliquam eget neque eget, posuere porttitor."))
        self.reqLabel.setText(_translate("DetailsWindow", "Requirements"))
        self.reqDesc.setText(_translate("DetailsWindow", "Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n"
"Max. 5 years old with 30 years of experience\n"
"GPA 4.999999999\n"
"Study abroad in South Africa"))
        self.recLabel.setText(_translate("DetailsWindow", "Why we recommend"))
        self.recDesc.setText(_translate("DetailsWindow", "Lorem ipsum dolor sit amet, consectetur adipiscing elit."))
        self.linkLabel.setText(_translate("DetailsWindow", "Registration"))
        self.linkDesc.setText(_translate("DetailsWindow", "[link]"))
        self.binusUniversity.setText(_translate("DetailsWindow", "2023 BINUS University"))
        self.binusMaya.setText(_translate("DetailsWindow", "BINUSMAYA"))
import test_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DetailsWindow = QtWidgets.QMainWindow()
    ui = Ui_DetailsWindow()
    ui.setupUi(DetailsWindow)
    DetailsWindow.showMaximized()
    sys.exit(app.exec_())
