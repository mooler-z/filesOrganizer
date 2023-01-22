import os, time, shutil, sys, music_tag
from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5 import QtCore, QtGui, QtWidgets

possibleMusicExts = ['.mp3', '.ogg', '.wav', '.m4a', '.flac',]
possibleVideoExts = ['.mp4']

class ChangeThumbnail(QThread):
    updateValueSignal = pyqtSignal(int)
    updateTextEditSignal = pyqtSignal(str, str)
    
    def __init__(self, srcDir, thumbNail="", vidMusic=1, artist="", album="", year="", genre=""):
        super().__init__()
        self.srcDir = srcDir
        self.thumbnail = thumbNail
        self.vidMusic = vidMusic
        self.artist = artist
        self.album = album
        self.year = year
        self.genre = genre
        self.vidMusic = vidMusic

    def run(self):
        if self.vidMusic == 1:
            possibleFiles = [os.path.join(self.srcDir, i) for i in os.listdir(self.srcDir) if os.path.splitext(i)[1].lower() in possibleVideoExts]

            if self.thumbnail:
                try:
                    with open(self.thumbnail, 'rb') as pic:
                        self.loadArt = pic.read()
                except Exception:
                    print("something went wrong")
            
            for i, file in enumerate(possibleFiles):
                try:
                    theVideo = music_tag.load_file(file)
                except Exception:
                    pass
                if self.thumbnail:
                    theVideo['artwork'] = self.loadArt
                theVideo.save()
                time.sleep(0.01)
                
                self.updateValueSignal.emit(i+1)
                self.updateTextEditSignal.emit("",file)
            else:
                self.updateValueSignal.emit(0)
                self.updateTextEditSignal.emit("done",file)
                
        else:
            possibleFiles = [os.path.join(self.srcDir, i) for i in os.listdir(self.srcDir) if os.path.splitext(i)[1].lower() in possibleMusicExts]
            
            if self.thumbnail:
                try:
                    with open(self.thumbnail, 'rb') as pic:
                        self.loadArt = pic.read()
                except Exception:
                    print("something went wrong")
                
            for i, file in enumerate(possibleFiles):
                try:
                    theMusic = music_tag.load_file(file)
                except Exception:
                    passq
                if self.artist:
                    theMusic['artist'] = self.artist
                if self.album:
                    theMusic['album'] = self.album
                if self.year:
                    theMusic['year'] = self.year
                if self.genre:
                    theMusic['genre'] = self.genre
                if self.thumbnail:
                    theMusic['artwork'] = self.loadArt
                theMusic.save()
                
                time.sleep(0.01)
                self.updateValueSignal.emit(i+1)
                self.updateTextEditSignal.emit("",file)
            else:
                self.updateValueSignal.emit(0)
                self.updateTextEditSignal.emit("done",file)
                
                