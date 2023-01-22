import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets
from thumbnails import ChangeThumbnail


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 666)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/Picture.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background-color: rgba(224, 224, 224, 222);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setFocusPolicy(QtCore.Qt.TabFocus)
        self.groupBox.setStyleSheet("QGroupBox {\n"
" background-color: rgb(224, 224, 224);\n"
" color: rgb(114, 159, 207);\n"
"}")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_9.addWidget(self.lineEdit_6)
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6.clicked.connect(self.musicsPath)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"    background-color: rgb(52, 101, 164);\n"
"    color: white;\n"
"    font-weight: bolder;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/folder-open.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon1)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_9.addWidget(self.pushButton_6)
        self.verticalLayout_8.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"    border: 2px black solid;\n"
"}")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/Music.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.clicked.connect(self.musicAlbumArt)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(52, 101, 164);\n"
"    color: white;\n"
"    font-weight: bolder;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/images.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_2.addWidget(self.lineEdit_3)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_3.addWidget(self.lineEdit_4)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_4.addWidget(self.lineEdit_2)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_7.addLayout(self.verticalLayout)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.clicked.connect(self.applyToMusic)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    background-color: rgb(52, 101, 164);\n"
"    color: white;\n"
"    font-weight: bolder;\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/music.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_7.addWidget(self.pushButton_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        self.verticalLayout_8.addLayout(self.horizontalLayout_5)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.line = QtWidgets.QFrame(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_9.addWidget(self.line)
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_9.addWidget(self.textEdit)
        self.progressBar = QtWidgets.QProgressBar(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("QProgressBar{\n"
" background-color: rgba(64, 155, 191, 118);\n"
" color: #FFFFFF;\n"
" border: 1px solid grey;\n"
" padding: 3px;\n"
" height: 15px;\n"
" text-align: center;\n"
" }\n"
" QProgressBar::chunk{\n"
" background: rgb(52, 101, 164);\n"
" width: 5px;\n"
" margin: 0.5px\n"
" }")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_9.addWidget(self.progressBar)
        self.gridLayout.addWidget(self.groupBox, 0, 1, 1, 1)
        self.groupBox1 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox1.setFont(font)
        self.groupBox1.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.groupBox1.setStyleSheet("QGroupBox {\n"
" background-color: rgb(224, 224, 224);\n"
" color: rgb(115, 210, 22);\n"
"}")
        self.groupBox1.setObjectName("groupBox1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox1)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_6.addWidget(self.lineEdit_5)
        self.pushButton = QtWidgets.QPushButton(self.groupBox1)
        self.pushButton.clicked.connect(self.videoPath)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(115, 210, 22);\n"
"    color: white;\n"
"    font-weight: bolder;\n"
"}")
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_6.addWidget(self.pushButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_3 = QtWidgets.QLabel(self.groupBox1)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel {\n"
"    border: 2px black solid;\n"
"}")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("images/Video_alt.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.groupBox1)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox1)
        self.pushButton_4.clicked.connect(self.videoAlbumArt)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    background-color: rgb(115, 210, 22);\n"
"    color: white;\n"
"    font-weight: bolder;\n"
"}")
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_8.addWidget(self.pushButton_4, 0, QtCore.Qt.AlignLeft)
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox1)
        self.pushButton_5.clicked.connect(self.applyToVideo)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    background-color: rgb(115, 210, 22);\n"
"    color: white;\n"
"    font-weight: bolder;\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/video.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_8.addWidget(self.pushButton_5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.line_2 = QtWidgets.QFrame(self.groupBox1)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.line_2.setFont(font)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_6.addWidget(self.line_2)
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox1)
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout_6.addWidget(self.textEdit_2)
        self.progressBar_2 = QtWidgets.QProgressBar(self.groupBox1)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.progressBar_2.setFont(font)
        self.progressBar_2.setStyleSheet("QProgressBar{\n"
" background-color: rgba(67, 191, 64, 86);\n"
" color: #FFFFFF;\n"
" border: 1px solid grey;\n"
" padding: 3px;\n"
" height: 15px;\n"
" text-align: center;\n"
" }\n"
" QProgressBar::chunk{\n"
" background: rgb(0, 200, 83);\n"
" width: 5px;\n"
" margin: 0.5px\n"
" }")
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setInvertedAppearance(False)
        self.progressBar_2.setObjectName("progressBar_2")
        self.verticalLayout_6.addWidget(self.progressBar_2)
        self.gridLayout.addWidget(self.groupBox1, 0, 2, 1, 1)
        self.groupBox2 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox2.setFont(font)
        self.groupBox2.setStyleSheet("QGroupBox {\n"
" background-color: rgb(224, 224, 224);\n"
" color: rgb(114, 159, 207);\n"
"}")
        self.groupBox2.setObjectName("groupBox2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.groupBox2)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox2)
        self.pushButton_8.setStyleSheet("QPushButton {\n"
"    background-color: rgb(252, 175, 62, 152);\n"
"    border: 3px solid rgb(252, 175, 62, 215);\n"
"    border-radius: 9px;\n"
"    font-family: courier;\n"
"    font-weight: 700;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(252, 175, 62, 255);\n"
"}")
        self.pushButton_8.setText("")
        self.pushButton_8.setIcon(icon4)
        self.pushButton_8.setIconSize(QtCore.QSize(90, 90))
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_10.addWidget(self.pushButton_8)
        self.line_3 = QtWidgets.QFrame(self.groupBox2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_10.addWidget(self.line_3)
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox2)
        self.pushButton_9.setStyleSheet("QPushButton {\n"
"    background-color: rgb(173, 127, 168, 152);\n"
"    border: 3px solid rgb(173, 127, 168, 215);\n"
"    border-radius: 9px;\n"
"    font-family: courier;\n"
"    font-weight: 700;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(173, 127, 168, 255);\n"
"}")
        self.pushButton_9.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/docker.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon5)
        self.pushButton_9.setIconSize(QtCore.QSize(99, 99))
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_10.addWidget(self.pushButton_9)
        self.line_4 = QtWidgets.QFrame(self.groupBox2)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_10.addWidget(self.line_4)
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox2)
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"    background-color: rgb(138, 226, 52, 152);\n"
"    border: 3px solid rgb(138, 226, 52, 215);\n"
"    border-radius: 9px;\n"
"    font-family: courier;\n"
"    font-weight: 700;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(138, 226, 52, 255);\n"
"}")
        self.pushButton_7.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/photo-video.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon6)
        self.pushButton_7.setIconSize(QtCore.QSize(90, 90))
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_10.addWidget(self.pushButton_7)
        self.line_5 = QtWidgets.QFrame(self.groupBox2)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_10.addWidget(self.line_5)
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox2)
        self.pushButton_10.setStyleSheet("QPushButton {\n"
"    background-color: rgba(64, 158, 191, 153);\n"
"    border: 3px solid rgba(64, 158, 191, 215);\n"
"    border-radius: 9px;\n"
"    font-family: courier;\n"
"    font-weight: 700;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(64, 158, 191, 255);\n"
"}")
        self.pushButton_10.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images/toolbox.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_10.setIcon(icon7)
        self.pushButton_10.setIconSize(QtCore.QSize(90, 90))
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_10.addWidget(self.pushButton_10)
        self.gridLayout.addWidget(self.groupBox2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionHere = QtWidgets.QAction(MainWindow)
        self.actionHere.setObjectName("actionHere")
        self.menuMenu.addAction(self.actionHere)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Music"))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "path to the musics"))
        self.pushButton_6.setText(_translate("MainWindow", "..."))
        self.label_2.setText(_translate("MainWindow", "..."))
        self.pushButton_2.setText(_translate("MainWindow", "  albumart"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "artist name"))
        self.label_8.setText(_translate("MainWindow", "artist  "))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "album name"))
        self.label_7.setText(_translate("MainWindow", "album "))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "production year"))
        self.label_6.setText(_translate("MainWindow", " year   "))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "genre of the music"))
        self.label_5.setText(_translate("MainWindow", " genre "))
        self.pushButton_3.setText(_translate("MainWindow", "   apply to music/s"))
        self.progressBar.setFormat(_translate("MainWindow", "progress: %p%"))
        self.groupBox1.setTitle(_translate("MainWindow", "Video"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "path to the videos"))
        self.pushButton.setText(_translate("MainWindow", "..."))
        self.label_4.setText(_translate("MainWindow", "..."))
        self.pushButton_4.setText(_translate("MainWindow", "  thumbnail"))
        self.pushButton_5.setText(_translate("MainWindow", "  apply to video/s"))
        self.progressBar_2.setFormat(_translate("MainWindow", "progress: %p%"))
        self.groupBox2.setTitle(_translate("MainWindow", "Utilities"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionHere.setText(_translate("MainWindow", "Here"))
        
    def musicsPath(self):
        file_dialog = QtWidgets.QFileDialog(self)
        file_dialog.setFileMode(QtWidgets.QFileDialog.Directory)
        self.srcMusicDir = file_dialog.getExistingDirectory(self, "Open Directory", "", QtWidgets.QFileDialog.ShowDirsOnly)
        self.lineEdit_6.setText(self.srcMusicDir)
        
        if self.srcMusicDir:
            noOfFiles = len([name for name in os.listdir(self.srcMusicDir) if os.path.isfile(os.path.join(self.srcMusicDir, name))])
            self.progressBar.setRange(0, noOfFiles)

    def videoPath(self):
        file_dialog = QtWidgets.QFileDialog(self)
        file_dialog.setFileMode(QtWidgets.QFileDialog.Directory)
        self.srcVideoDir = file_dialog.getExistingDirectory(self, "Open Directory", "", QtWidgets.QFileDialog.ShowDirsOnly)
        self.lineEdit_5.setText(self.srcVideoDir)
        
        if self.srcVideoDir:
            noOfFiles = len([name for name in os.listdir(self.srcVideoDir) if os.path.isfile(os.path.join(self.srcVideoDir, name))])
            self.progressBar_2.setRange(0, noOfFiles)
            
    def musicAlbumArt(self):
        file_dialog = QtWidgets.QFileDialog(self)
        file_dialog.setFileMode(QtWidgets.QFileDialog.ExistingFiles)
        self.srcMusicImgFile = file_dialog.getOpenFileName(self, "Open Picture", "")[0]
        self.label_2.setText(os.path.basename(self.srcMusicImgFile))
        pixmap = QtGui.QPixmap(self.srcMusicImgFile)
        pixmap = pixmap.scaled(136, 136)
        self.label.setPixmap(pixmap)
        
    def videoAlbumArt(self):
        file_dialog = QtWidgets.QFileDialog(self)
        file_dialog.setFileMode(QtWidgets.QFileDialog.ExistingFiles)
        self.srcVideoImgFile = file_dialog.getOpenFileName(self, "Open Picture", "")[0]
        self.label_4.setText(os.path.basename(self.srcVideoImgFile))
        pixmap = QtGui.QPixmap(self.srcVideoImgFile)
        pixmap = pixmap.scaled(136, 136)
        self.label_3.setPixmap(pixmap)
        
    def updateMusicTextEdit(self, status, file):
        if not status:
           self.textEdit.append("⚶UPDATED⚶ {}".format(os.path.basename(file)))
        else:
           self.textEdit.append("\n⚶⚶⚶⚶⚶⚶⚶⚶ DONE UPDATING FILES ⚶⚶⚶⚶⚶⚶⚶⚶")
           
    def updateMusicBar(self, value):
        self.progressBar.setValue(value)

    def updateVideoTextEdit(self, status, file):
        if not status:
           self.textEdit_2.append("⚶UPDATED⚶ {}".format(os.path.basename(file)))
        else:
           self.textEdit_2.append("\n⚶⚶⚶⚶⚶⚶⚶⚶ DONE UPDATING FILES ⚶⚶⚶⚶⚶⚶⚶⚶")
           
    def updateVideoBar(self, value):
        self.progressBar_2.setValue(value)
        
    def applyToMusic(self):
        src = self.lineEdit_6.text()
        artist = self.lineEdit.text()
        album = self.lineEdit_3.text()
        year = self.lineEdit_4.text()
        genre = self.lineEdit_2.text()
        self.textEdit.clear()
        
        if src:
            print(year)
            self.applyMusic = ChangeThumbnail(src, self.srcMusicImgFile,vidMusic=2, artist=artist, album=album, year=year, genre=genre)
            self.applyMusic.updateValueSignal.connect(self.updateMusicBar)
            self.applyMusic.updateTextEditSignal.connect(self.updateMusicTextEdit)
            self.applyMusic.start()
            
    def applyToVideo(self):
        src = self.lineEdit_5.text()
        self.textEdit_2.clear()

        if src:
            self.applyMusic = ChangeThumbnail(src, self.srcVideoImgFile)
            self.applyMusic.updateValueSignal.connect(self.updateVideoBar)
            self.applyMusic.updateTextEditSignal.connect(self.updateVideoTextEdit)
            self.applyMusic.start()
        

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.setupUi(self)
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()