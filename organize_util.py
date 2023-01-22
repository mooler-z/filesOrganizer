import os, time, shutil, sys
from copy import deepcopy
from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5 import QtCore, QtGui, QtWidgets

video_extensions = ['.264', '.3g2', '.3gp', '.arf', '.asf', '.asx', '.avi', '.bik', '.dash', 
'.dat', '.dvr', '.flv', '.h264', '.m2t', '.m2ts', '.m4v', '.mkv', '.mod', '.mov', '.mp4',
 '.mpeg', '.mpg', '.mts', '.ogv', '.proproj', '.rec', '.rmvb', '.swf', '.tod', '.tp', '.ts',
'.vob', '.webm', '.wlmp', '.wmv']

audio_extensions = ['.pcm', '.wav', '.aiff', '.mp3', '.aac', '.ogg', 
'.wma', '.flac', '.alac', '.cda', '.mid', '.midi', '.wpl', '.m4a']

picture_extensions = ['.ai', '.bmp', '.gif', '.ico', '.jpeg', '.jpg',
 '.png', '.ps', '.psd', '.svg', '.tif', '.tiff']

word_extensions = ['.doc', '.docx', '.odt', '.pdf', '.rtf', '.tex', '.txt', 
'.wks', '.wps', '.wpd', '.ods', '.xlr', '.xls', '.xlsx', '.key', '.odp', 
'.pps', '.ppt', '.pptx', '.epub', '.log']

data_persistance = ['.csv', '.json']

pl_extensions = ['.c', '.class', '.cpp', '.cs', '.h', '.java', '.sh', '.swift',
 '.vb', '.css', '.html', '.htm', '.js', '.jsp', '.php', '.py', '.rss', '.rb',
  '.xhtml', '.db', '.sql', '.xml', '.jar', '.md', '.cfg']
zip_extensions = ['.7z', '.arj', '.deb', '.pkg', '.rar', '.rpm', '.gz', '.z', '.zip', '.xz']
executeables = [".exe", ".msi", ".out"]

general_extensions = {
    "Pictures": picture_extensions,
    "Videos": video_extensions, 
    "Audios": audio_extensions, 
    "ProgLangs": pl_extensions, 
    "Compressed": zip_extensions, 
    "Words": word_extensions, 
    "Executeables": executeables, 
    "Persistance": data_persistance,
}

class Renamer(QThread):
    updateValueSignal = pyqtSignal(int)
    updateTextEditSignal = pyqtSignal(str, str)

    def __init__(self, dir, ext, prefix, whichOne):
        super().__init__()
        self.dir = dir
        self.ext = ext
        self.prefix = prefix
        # to add or rename
        self.whichOne = whichOne
        
    def run(self):
        for i, file in enumerate(os.listdir(self.dir)):
            _, file_ext = os.path.splitext(file)
            if self.whichOne == 1:
                if self.ext == 'all':
                    new_file_name = "{}_{}{}".format(self.prefix, str(i), file_ext)
                    src_path = os.path.join(self.dir, file)
                    dst_path = os.path.join(self.dir, new_file_name)
                    os.rename(src_path, dst_path)
                    time.sleep(0.015)
                    
                    self.updateValueSignal.emit(i+1)
                    self.updateTextEditSignal.emit(file, new_file_name)
                    
                if file_ext == self.ext and self.ext != 'all':
                    new_file_name = self.prefix + str(i) + self.ext
                    src_path = os.path.join(self.dir, file)
                    dst_path = os.path.join(self.dir, new_file_name)
                    os.rename(src_path, dst_path)
                    time.sleep(0.015)
                    
                    self.updateValueSignal.emit(i+1)
                    self.updateTextEditSignal.emit(file, new_file_name)
                else:
                    pass
            else:
                if self.ext == 'all':
                    new_file_name = "{}{}{}".format(_, self.prefix, file_ext)
                    src_path = os.path.join(self.dir, file)
                    dst_path = os.path.join(self.dir, new_file_name)
                    os.rename(src_path, dst_path)
                    time.sleep(0.015)
                    
                    self.updateValueSignal.emit(i+1)
                    self.updateTextEditSignal.emit(file, new_file_name)
                    
                if file_ext == self.ext and self.ext != 'all':
                    new_file_name = "{}{}{}".format(_, self.prefix, file_ext)
                    src_path = os.path.join(self.dir, file)
                    dst_path = os.path.join(self.dir, new_file_name)
                    os.rename(src_path, dst_path)
                    time.sleep(0.015)
                    
                    self.updateValueSignal.emit(i+1)
                    self.updateTextEditSignal.emit(file, new_file_name)
                else:
                    pass
        self.updateValueSignal.emit(0)
        self.updateTextEditSignal.emit("..done..", "◂"*12+" Done Renaming "+"▸"*12)

class Organizer(QThread):
    updateValueSignal = pyqtSignal(int)
    updateTextEditSignal = pyqtSignal(str, str, str)
    
    def __init__(self, srcDir, destDir):
        super().__init__()
        self.srcDir = srcDir
        self.destDir = destDir
        
    def run(self):
        filesToOrganize = [i for i in os.listdir(self.srcDir) if os.path.isfile(os.path.join(self.srcDir,i))]
        
        self.deepCopyFile = deepcopy(filesToOrganize)
        
        typesOfFiles = list(
            set([os.path.splitext(i)[1] for i in filesToOrganize])
            )
        
        folders = [
                [
                folder for ext in typesOfFiles if ext in exts
                ] for folder, exts in general_extensions.items()
            ]
        folders = [folder for folder in folders if folder]
        folders = [folder[0] for folder in folders]
        
        self.whereToMove = []

        for file in filesToOrganize:
            for folder in folders:
                if os.path.splitext(file)[1] in general_extensions[folder]:
                    # tuple of the file and where to move it
                    self.whereToMove.append(
                        (os.path.join(self.srcDir, file), os.path.join(self.destDir, folder))
                        )
                    self.deepCopyFile.remove(file)
                    # create a folder if it doesn't already exit
                    if folder not in os.listdir(self.destDir):
                        os.mkdir(os.path.join(self.destDir, folder))
        
        # for unknown files                         
        if self.deepCopyFile:
            for file in self.deepCopyFile:
                if "Unknowns" not in os.listdir(self.destDir):
                    os.mkdir(os.path.join(self.destDir, "Unknowns"))
                self.whereToMove.append(
                    (os.path.join(self.srcDir, file), os.path.join(self.destDir, "Unknowns"))
                    )
                
        self.organizeFiles()
                
    def organizeFiles(self):
        
        for i, j in enumerate(self.whereToMove):
            if os.path.basename(j[0]) not in os.listdir(j[1]):
                shutil.move(j[0], j[1])
                self.updateValueSignal.emit(i+1)
                self.updateTextEditSignal.emit("",os.path.basename(j[0]), os.path.basename(j[1]))
                time.sleep(0.015)
            else:
                self.updateTextEditSignal.emit("fileExists",os.path.basename(j[0]), os.path.basename(j[1]))
                
                
        # except shutil.Error:
        #     find_text, ok = QtWidgets.QInputDialog.getText(self, "File Already Exists", "Find:")
            #     # app = QtWidgets.QApplication(sys.argv)
            #     self.updateTextEditSignal.emit("fileExists",os.path.basename(j[0]), os.path.basename(j[1]))
                # self.dialog = Ui_Dialog(os.path.basename(j[0]), os.path.basename(j[1]))
                # self.dialog.start()
                # os.path.basename(j[0]), os.path.basename(j[1])
                # self.dialog.renameLineEdit()
                # self.dialog.renameLineEdit()
                # self.dialog.show()
                # app.exec_()
        
        self.updateValueSignal.emit(0)
        self.updateTextEditSignal.emit("","..done..", "◂"*12+" Done Organizing "+"▸"*12)

class Ui_Dialog(QtWidgets.QDialog):
    def __init__(self, src, dest):
        super().__init__()
        self.src, self.dest = src, dest
        self.setupUi(self)
        # self.run()
        
    def run(self):
        pass
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(498, 177)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_4.addWidget(self.pushButton_4)
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_4.addWidget(self.pushButton_6)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "OrginalFile"))
        self.pushButton.setText(_translate("Dialog", "Rename"))
        self.label_2.setText(_translate("Dialog", "NewFile    "))
        self.pushButton_2.setText(_translate("Dialog", "Rename"))
        self.pushButton_3.setText(_translate("Dialog", "Skip"))
        self.pushButton_5.setText(_translate("Dialog", "Replace"))
        self.pushButton_4.setText(_translate("Dialog", "SkipAll"))
        self.pushButton_6.setText(_translate("Dialog", "ReplaceAll"))
        # self.lineEdit.setText(self.src)
        # self.lineEdit_2.setText(self.dest)
        # print(self.src, self.dest)
        # self.show()
        # self.run()
        
    def renameLineEdit(self):
        self.lineEdit.setText(self.src)
        self.lineEdit_2.setText(self.dest)

# class DisplayDialog(QtWidgets.QDialog, Ui_Dialog):
#     def __init__(self, src, dest):
#         super().__init__()
#         self.src = src
#         self.dest = dest
#         self.setupUi(self)
