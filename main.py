import numpy as np
import matplotlib.pyplot as plt
import random

# IDJER Samy Remy 21208501
# etudiant en ERASMUS
# projet sans binome parce que aucun personne etait disponible aussi si j'ai demandé beaucoup des fois


class Grille:

    def __init__(self):
        self.grille = np.zeros([10, 10], dtype=int)

        self.bateaux = [5, 4, 3, 3, 2]  # longueur des  bateaux
        self.bateauxplace = [False, False, False, False, False]  # si le bateau est place

    def peut_placer(self, bateau, positionX, positionY, direction):

        if self.bateauxplace[bateau - 1] == True:
            print("bateau deja placè")
            return False
        else:
            # 1 vertical
            # 2 horizontal
            if direction == 1:
                if positionX + self.bateaux[bateau - 1] > 10:
                    return False
                for x in range(positionX, (positionX + self.bateaux[bateau - 1])):
                    if self.grille[positionY][x] != 0:
                        return False
                return True

            else:
                if positionY + self.bateaux[bateau - 1] > 10:
                    return False
                for y in range(positionY, positionY + self.bateaux[bateau - 1]):
                    if self.grille[y][positionX] != 0:
                        return False
                return True


    def place(self, bateau, positionX, positionY, direction):
        if self.peut_placer(bateau, positionX, positionY, direction) == True: #avant de placer on controle
            self.bateauxplace[bateau - 1] = True
            if direction == 1:
                for x in range(positionX, positionX + self.bateaux[bateau - 1]):
                    self.grille[positionY][x] = bateau
                return True
            else:
                for y in range(positionY, positionY + self.bateaux[bateau - 1]):
                    self.grille[y][positionX] = bateau
                return True

        else:
            # print("tu ne peux pas!")
            return False

    def supprimer(self, bateau):
        for i in range(0, 10):
            for j in range(0, 10):
                if self.grille[i][j] == bateau: #car le bateaux sont placé avec leur ID dans la grille je peut les chercher
                    self.grille[i][j] = 0




    def place_alea(self, bateau):
        if (self.bateauxplace[bateau - 1] == False): #controle de ne l'avoir pas  dejà placé
            # self.bateauxplace[bateau - 1] == True
            while (self.place(bateau, random.randrange(0, 10), random.randrange(0, 10),
                              random.randrange(1, 3)) == False):  #random position and direction
                #print("trying\n")
                continue
            #print("placè le bateau", bateau, "aleatoriement\n")
            return True
        else:
            #print("bateau deja placè")
            return False

    def nombre_de_facons(self, bateau):
        #nombre de combination en que je peut placer un bateur sur la grille
        resultat = 0

        for i in range(0, 10):
            for j in range(0, 10):
                if self.peut_placer(bateau, i, j, 1) == True:
                    resultat = resultat + 1
                if self.peut_placer(bateau, i, j, 2) == True:
                    resultat = resultat + 1
        return resultat

    def nombre_de_facons_position(self, bateau, x, y):
        #Combien de fois un bateu va etre placé sur la position x y apres tous les combination possible
        resultat = 0

        for i in range(0, 10):
            for j in range(0, 10):
                if self.place(bateau, i, j, 1) == True:
                    if self.grille[x][y] != 0:
                        resultat += 1
                    self.supprimer(bateau)
                    self.bateauxplace[bateau - 1] = False
                if self.place(bateau, i, j, 2) == True:
                    if self.grille[x][y] != 0:
                        resultat += 1
                    self.supprimer(bateau)
                    self.bateauxplace[bateau - 1] = False
        return resultat


    def nombre_de_facons_liste(self, liste):
        #methode pour calculer le combination possible d'un liste des bateaux
        resultat = 0
        i = 0
        resultat = self.nombre_de_facons_recursive(liste, i, 0, 0, 1, resultat)
        print(resultat)

        return resultat

    def nombre_de_facons_recursive(self, liste, i, j, k, dir, resultat):

        if i != (len(liste) - 1): #tous les bateux except le dernier
            for j in range(10):
                for k in range(10):
                    for dir in [1,2]:
                        if self.place(liste[i], j, k, dir) == True:
                            resultat = self.nombre_de_facons_recursive(liste, i + 1, 0, 0, dir, resultat)
                            self.supprimer(liste[i])
                            self.bateauxplace[liste[i] - 1] = False
            return resultat
        else: #dernier bateau
            for j in range(0, 10):
                for k in range(0, 10):
                    for dir in [1,2]:

                        if self.place(liste[i], j, k, dir) == True:
                            resultat += 1
                            print(self.grille)
                            print(resultat)
                            self.supprimer(liste[i])
                            self.bateauxplace[liste[i] - 1] = False
            print(resultat)
            return resultat


    def tirerGrilledonne(self, grilleB):
        #methode pour generer grilles aleatoirement justu'à on arrive à un grille egual à la grille donnée
        i = 0
        while (self.equals(grilleB) == False):
            i += 1
            #print(i)
            self.genere_grille()
        return i;

    def approximerCombination(self, liste):
        #approximation de le combination possible donnée une liste
        resultat = 1
        for i in range(len(liste)):
            print(self.nombre_de_facons(liste[i]))
            resultat *= (self.nombre_de_facons(liste[i]) - liste[i -1])
            print(resultat)

        return resultat

    def affiche(self):
        #afficher la grille grace a matplotlib
        plt.imshow(self.grille)
        plt.show()

    def getGrille(self):
        return self.grille

    def equals(self, grilleB):
        return np.array_equal(self.grille, grilleB)

    def getPos(self, posx, posy):
        return self.grille[posx][posy]

    def genere_grille(self):
        #genere un grille avec les 5 bateaux en maniere random
        for i in range(0, 5):
            if self.bateauxplace[i] == False:
                self.place_alea(i + 1)

    def toString(self):
        print(self.grille)


class Bataille:

    def __init__(self):
        self.grille = Grille()
        self.grille.genere_grille()

        self.grilleJoue = np.zeros([10, 10], dtype=int) # grille avec les positions que on a touchè

    def joue(self, positionX, positionY):
        if positionX >= 10 or positionY >= 10 or positionY < 0 or positionX < 0:
            return False

        if self.grille.getPos(positionX, positionY) != 0:
            self.grilleJoue[positionX][positionY] = self.grille.getPos(positionX, positionY)
            return True
        else:
            return False

    def victoire(self):
        return self.grille.equals(self.grilleJoue)  #controle si on a gagné

    def reset(self):
        self.grilleJoue = np.zeros([10, 10], dtype=int)
        print(self.grilleJoue)
        #self.grille.genere_grille()


class JoueurAleatoire:

    def __init__(self):
        self.bataille = Bataille()

    def start(self):
        i = 0
        while self.bataille.victoire() == False:
            self.bataille.joue(random.randrange(0,10), random.randrange(0,10)) #position random
            i += 1
            #print(i)
            #print(self.bataille.grilleJoue)
        return i

class JoueurHeuristique:

    def __init__(self):
        self.bataille = Bataille()

    def start(self):
        i = 0
        while self.bataille.victoire() == False:
            posx = random.randrange(0,10)    #on commence en maniere random
            posy = random.randrange(0,10)
            i += 1
            #print(i)
            if self.bataille.joue(posx, posy) == True: #si on touche un bateau on essaye tous le position pres de lui

                #print(self.bataille.grilleJoue)
                for j in range(0,4):
                    guess = True
                    posxcopy = posx
                    posycopy = posy
                    while (guess == True):
                            if j == 0:
                                posxcopy += 1
                                i += 1

                                if self.bataille.joue(posxcopy, posycopy) == False:
                                    guess =  False

                            elif j == 1:
                                posxcopy -= 1
                                i += 1

                                if self.bataille.joue(posxcopy, posycopy) == False:
                                    guess =  False

                            elif j == 2:
                                posycopy += 1
                                i += 1

                                if self.bataille.joue(posxcopy, posycopy) == False:
                                    guess =  False

                            else:
                                posycopy -= 1
                                i += 1

                                if self.bataille.joue(posxcopy, posycopy) == False:
                                    guess = False

                            #print(i)
                            #print(self.bataille.grilleJoue)
                #print(self.bataille.grilleJoue)
        return i

class JoueurProbabiliste:
    def __init__(self):
        self.bataille = Bataille()

        self.grilleProba = np.ones([10, 10], dtype=float)
        self.grille = Grille()

    def searchHighest(self):

        #pour obtenir la position avec la probabilité plus grande
        x = 0
        y = 0
        for i in range(0, 10):
            for j in range(0, 10):
                if self.grilleProba[i][j] > self.grilleProba[x][y]:
                    x = i
                    y = j

        self.grilleProba[x][y] = 0
        return x, y



    def start(self):


        for bateau in [1,2,3,4,5]:
            for i in range(0,10):
                for j in range(0,10):
                    #calcul la probabilitée
                    self.grilleProba[i][j] += self.grille.nombre_de_facons_position(bateau, i, j) / self.grille.nombre_de_facons(bateau)
            #print(self.grilleProba)


        while self.bataille.victoire() == False:
            posx, posy = self.searchHighest() #on joue la position avec la probabilitèe plus grande
            i += 1
            #print(i)
            if self.bataille.joue(posx, posy) == True: # si on touche un bateau on procede comme dans la versione Heuristique

                #print(self.bataille.grilleJoue)
                for j in range(0,4):
                    guess = True
                    posxcopy = posx
                    posycopy = posy
                    while (guess == True):
                            if j == 0:
                                posxcopy += 1
                                i += 1

                                if self.bataille.joue(posxcopy, posycopy) == False:
                                    guess =  False

                            elif j == 1:
                                posxcopy -= 1
                                i += 1

                                if self.bataille.joue(posxcopy, posycopy) == False:
                                    guess =  False

                            elif j == 2:
                                posycopy += 1
                                i += 1

                                if self.bataille.joue(posxcopy, posycopy) == False:
                                    guess =  False

                            else:
                                posycopy -= 1
                                i += 1

                                if self.bataille.joue(posxcopy, posycopy) == False:
                                    guess = False

                            #print(i)
                            #print(self.bataille.grilleJoue)
                #print(self.bataille.grilleJoue)
        return i






# ------------------------------------- MAIN -----------------------------------------------------



alea = JoueurAleatoire()
heur = JoueurHeuristique()
proba = JoueurProbabiliste()

print("aleaatoire: ", alea.start())
print("heuristique: ", heur.start())
print("probabiliste: ", proba.start())


