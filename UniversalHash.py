from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from PyQt5.QtCore import QDir
from PyQt5 import uic
import hashlib

class Gui(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('gui.ui',self)
        self.scelta.addItem('SHA1')
        self.scelta.addItem('SHA224')
        self.scelta.addItem('SHA256')
        self.scelta.addItem('SHA384')
        self.scelta.addItem('SHA512')
        self.scelta.addItem('SHA3-224')
        self.scelta.addItem('SHA3-256')
        self.scelta.addItem('SHA3-384')
        self.scelta.addItem('SHA3-512')
        self.scelta.addItem('MD5')

    def open(self):
        self.path.setText(QFileDialog.getOpenFileName(directory=QDir.homePath())[0])

    def fromgui(self):
        if self.radioButton.isChecked():
            self.bites = open(self.path.text(),'rb').read()
        else:
            self.bites = self.pte.toPlainText().encode()

    def calcola(self):
        self.fromgui()
        h = Hash(self.scelta.currentText(),self.bites).chooser()
        self.LEResult.setText(h)

class Hash:
    def __init__(self, type, text):
        self.text = text
        self.type = type
        self.hash = None

    def chooser(self):
        if self.type == 'SHA1':
            h = hashlib.sha1(self.text)
        elif self.type == 'SHA224':
            h = hashlib.sha224(self.text)
        elif self.type == 'SHA256':
            h = hashlib.sha256(self.text)
        elif self.type == 'SHA384':
            h = hashlib.sha384(self.text)
        elif self.type == 'SHA512':
            h = hashlib.sha512(self.text)
        elif self.type == 'SHA3-224':
            h = hashlib.sha3_224(self.text)
        elif self.type == 'SHA3-256':
            h = hashlib.sha3_256(self.text)
        elif self.type == 'SHA3-384':
            h = hashlib.sha3_384(self.text)
        elif self.type == 'SHA3-512':
            h = hashlib.sha3_512(self.text)
        elif self.type == 'MD5':
            h = hashlib.md5(self.text)
        return h.hexdigest()

app = QApplication([])
window = Gui()
window.show()
app.exec()