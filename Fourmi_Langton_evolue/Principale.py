__author__ = 'Pierre VIX'
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
from fenetre import Ui_MainWindow

from random import *
from copy import *
from Plateau import *
nbcases=91
taillecellule=7

class fenetre(QMainWindow,Ui_MainWindow):
    def __init__(self,taillecellule,parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.canvas=zoneGraphique(taillecellule,self)
        self.plateau= plateau(nbcases,nbcases)
        self.canvas.setGeometry(10,10,700,700)
        self.setGeometry(600,100,1200,850)
        self.clock = QTimer()
        self.canvas.Dessin(self.plateau)
        self.clock.timeout.connect(self.deplacement)

    def Demarrage(self):
        self.clock.start(1000)

    def deplacement(self):
        if(self.plateau.inMove):
            self.plateau.move()
            self.canvas.Dessin(self.plateau)
        else:
            self.clock.stop()


class zoneGraphique(QWidget):
    def __init__(self,taillecellule,parent=None):
        super().__init__(parent)
        self.canvasZG=QPixmap(700,700)
        self.tailleCase=taillecellule

    def Dessin(self,echiquier):
        assert isinstance(echiquier,plateau)
        p=QPainter(self.canvasZG)
        self.canvasZG.fill(Qt.white)
        p.setPen(Qt.black)
        for ligne in range(echiquier.nbLigne):
            for colonne in range(echiquier.nbColonne):
                if (echiquier.echiquier[ligne][colonne].couleur==Couleur.Blanc):
                    p.setBrush(Qt.white)
                    p.drawRect(ligne*self.tailleCase,colonne*self.tailleCase,self.tailleCase,self.tailleCase)
                else :
                    p.setBrush(Qt.black)
                    p.drawRect(ligne*self.tailleCase,colonne*self.tailleCase,self.tailleCase,self.tailleCase)
        p.setBrush(Qt.red)
        p.drawRect(echiquier.emplacementFourmi.x*self.tailleCase,echiquier.emplacementFourmi.y*self.tailleCase,self.tailleCase,self.tailleCase)

    def paintEvent(self, QPaintEvent):
        p=QPainter(self)
        p.drawPixmap(0,0,self.canvasZG)

app = QApplication(sys.argv)
essai = fenetre(taillecellule)
essai.show()
app.exec()