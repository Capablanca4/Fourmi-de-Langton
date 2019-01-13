__author__ = 'Pierre VIX'
from enum import Enum

class Coordonnee():
    def __init__ (self,x,y):
        self.x = x
        self.y = y

class Couleur(Enum):
    Blanc =0
    Noir =1

class Direction(Enum):
    Est = 0
    Ouest = 1
    Nord = 2
    Sud = 3

class plateau():

    def __init__(self,nbLigne, nbColonne):
        self._nbLigne = nbLigne
        self._nbColonne = nbColonne
        self._echiquier=[]
        for j in range(nbLigne):
            liste=[]
            for i in range(nbColonne):
                liste.append(case(Couleur.Blanc, Coordonnee(i,j)))
            self._echiquier.append(liste)
        self.emplacementFourmi = Coordonnee(nbLigne//2,nbColonne//2)
        self._echiquier[self.emplacementFourmi.x][self.emplacementFourmi.y]=fourmi(Couleur.Blanc,self.emplacementFourmi,Direction.Est)
        self.inMove=True

    @property
    def nbLigne(self):
        return self._nbLigne

    @property
    def nbColonne(self):
        return self._nbColonne

    @property
    def echiquier(self):
        return self._echiquier

    def __getitem__(self,x,y):
        return self._echiquier[x][y]

    def getCell(self,x,y):
        return self._echiquier[x][y]

    def move(self):
        nextFourmiCoord = self.nextEmplacement( self.getCell(self.emplacementFourmi.x,self.emplacementFourmi.x))
        if(nextFourmiCoord!=None):
            nextFourmi = self.getCell(nextFourmiCoord.x,nextFourmiCoord.y)
            self._echiquier = nextFourmi.touch(self.getCell(self.emplacementFourmi.x,self.emplacementFourmi.y))
            self._echiquier = self._echiquier(self.emplacementFourmi).transformIntoCase()

    def nextEmplacement(self,case):
        if(case.direction==Direction.Est):
            if(case.coordonnee.y+1<self._nbColonne):
                return Coordonnee(case.coordonnee.x,case.coordonnee.y+1)
            else:
                self.inMove=False

        elif(case.direction == Direction.Ouest):
            if(case.coordonnee.y-1>=0):
                return Coordonnee(case.coordonnee.x,case.coordonnee.y-1)
            else:
                self.inMove=False

        elif(case.direction == Direction.Nord):
            if(case.coordonnee.x-1>=0):
                return Coordonnee(case.coordonnee.x-1,case.coordonnee.y)
            else:
                self.inMove=False

        else :
            if(case.coordonnee.x+1<self._nbLigne):
                return Coordonnee(case.coordonnee.x+1,case.coordonnee.y)
            else:
                self.inMove=False

class case():
    def  __init__(self,color,coord):
        assert isinstance(color ,Couleur)
        self.d_couleur=color
        assert isinstance(coord ,Coordonnee)
        self.d_coordonnee=coord

    @property
    def couleur(self):
        return self.d_couleur

    @couleur.setter
    def couleur(self,color):
        assert isinstance(color ,Couleur)
        self.d_couleur=color

    @property
    def coordonnee(self):
        return self.d_coordonnee

    @coordonnee.setter
    def coordonnee(self,coord):
        assert isinstance(coord ,Coordonnee)
        self.d_coordonnee=coord

    def touch(self,fourmi):

        if(self.couleur==Couleur.Blanc):
            if(fourmi == Direction.Est):
                return fourmi(Couleur.Blanc,self.coordonnee,Direction.Sud)
            elif(fourmi == Direction.Ouest):
                return fourmi(Couleur.Blanc,self.coordonnee,Direction.Nord)
            elif(fourmi == Direction.Nord):
                return fourmi(Couleur.Blanc,self.coordonnee,Direction.Est)
            else :
                return fourmi(Couleur.Blanc,self.coordonnee,Direction.Ouest)

        else:
            if(fourmi == Direction.Est):
                return fourmi(Couleur.Noir,self.coordonnee,Direction.Nord)
            elif(fourmi == Direction.Ouest):
                return fourmi(Couleur.Noir,self.coordonnee,Direction.Sud)
            elif(fourmi == Direction.Nord):
                return fourmi(Couleur.Noir,self.coordonnee,Direction.Ouest)
            else :
                return fourmi(Couleur.Noir,self.coordonnee,Direction.Est)

class fourmi(case):
    def __init__(self,color,coord,direc):
        super().__init__(color,coord)
        self.d_direction = direc

    @property
    def direction(self):
        return self.d_direction

    @direction.setter
    def direction(self,direct):
        assert isinstance(direct,Direction)
        self.d_direction=direct

    def transformIntoCase(self):
        if(self.couleur==Couleur.Blanc):
            return case(Couleur.Noir,self.coordonnee)
        else:
            return case(Couleur.Blanc,self.coordonnee)