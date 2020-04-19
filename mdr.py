import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
#############################################################################
class Quelclient(QWidget):
 
    def __init__(self, parent=None):
        super(Quelclient, self).__init__(parent)
        self.setWindowTitle(u"Quel client")
        print("dd")
        # créer un lineEdit
        self.lineEdit = QtWidgets.QLineEdit(self)
        # créer un bouton
        self.bouton = QtWidgets.QPushButton(u"Ok", self)
        self.bouton.clicked.connect(self.ok_m)
        # positionner les widgets dans la fenêtre
        posit = QtWidgets.QGridLayout()
        posit.addWidget(self.lineEdit, 0, 0)
        posit.addWidget(self.bouton, 1, 0)
        self.setLayout(posit)
 
    def ok_m(self):
        
        self.close()
    
#############################################################################
class Principal(QMainWindow):
 
    def __init__(self, parent=None):
        """Initialise la fenêtre"""
        super(Principal, self).__init__(parent)
        self.setWindowTitle(u"Code test")
 
        # mettre un fond (nécessaire avec un QMainWindow)
        self.setCentralWidget(QtWidgets.QFrame())
        # créer un lineEdit
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget())
        # créer un bouton
        self.bouton = QtWidgets.QPushButton(u"valider !", self.centralWidget())
        self.bouton.clicked.connect(self.quelclient_m)
        # positionner les widgets sur le fond de la fenêtre
        posit = QtWidgets.QGridLayout()
        posit.addWidget(self.lineEdit, 0, 0)
        posit.addWidget(self.bouton, 1, 0)
        self.centralWidget().setLayout(posit)
 
    def quelclient_m(self):
        """Lance la deuxième fenêtre"""
        self.quelclient = Quelclient()
        
        # en cas de signal "fermeturequelclient()" reçu de self.quelclient => exécutera clienchoisi 
        
        # la deuxième fenêtre sera 'modale' (la première fenêtre sera inactive)
        
        
        print("gg")
        self.quelclient.setWindowModality(QtCore.Qt.ApplicationModal)
        # appel de la deuxième fenêtre
        print("gg")
        self.quelclient.show()

        
    def clientchoisi(self, x):
        """affiche le résultat x transmis par le signal à l'arrêt de la deuxième fenêtre"""
        self.lineEdit.setText(x)

 
#############################################################################
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('plastique'))
    main = Principal()
    main.show()
    sys.exit(app.exec_())
