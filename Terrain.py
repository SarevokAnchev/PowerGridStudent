
from enum import Enum

class Case(Enum):
    VIDE = 0
    OBSTACLE = 1
    CLIENT = 2
    ENTREE = 4

class Terrain:
    def __init__(self):
        self.largeur = 0
        self.hauteur = 0
        self.cases = []

    def charger(self, fichier):
        self.cases.clear()
        with open(fichier, "r") as f:
            ligne_max = 0
            for ligne in f:
                ligne = list(ligne)[:-1]
                ligne_cases = []
                n = 0
                for c in ligne:
                    n += 1
                    if c == " ":
                        ligne_cases.append(Case.OBSTACLE)
                    elif c == "C":
                        ligne_cases.append(Case.CLIENT)
                    elif c == "~":
                        ligne_cases.append(Case.VIDE)
                    elif c == "E":
                        ligne_cases.append(Case.ENTREE)
                    else:
                        ligne_cases.append(Case.OBSTACLE)
                self.cases.append(ligne_cases)
                if ligne_max < n:
                    ligne_max = n
        for i, l in enumerate(self.cases):
            while len(l) < ligne_max:
                self.cases[i].append(Case.OBSTACLE)
        self.largeur = ligne_max
        self.hauteur = len(self.cases)

    def __getitem__(self, l):
        return self.cases[l]

    def get_clients(self) -> list[tuple[int, int]]:
        clients = []
        for i, l in enumerate(self.cases):
            for j, c in enumerate(l):
                if c == Case.CLIENT:
                    clients.append((i, j))
        return clients

    def get_entree(self) -> tuple[int, int]:
        for i, l in enumerate(self.cases):
            for j, c in enumerate(l):
                if c == Case.ENTREE:
                    return (i, j)
        return (-1, -1)

    def afficher(self):
        for l in self.cases:
            for c in l:
                if c == Case.OBSTACLE:
                    print("X", end="")
                if c == Case.CLIENT:
                    print("C", end="")
                if c == Case.VIDE:
                    print("~", end="")
                if c == Case.ENTREE:
                    print("E", end="")
                else:
                    print(" ", end="")
            print()

