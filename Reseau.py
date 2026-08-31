from Terrain import Terrain, Case
from StrategieReseau import StrategieReseau, StrategieReseauAuto

class Reseau:
    def __init__(self):
        self.strat = StrategieReseauAuto()
        self.noeuds = {}
        self.arcs = []

        self.noeud_entree = -1

    def definir_entree(self, n: int) -> None:
        if n in self.noeuds.keys():
            self.noeud_entree = n
        else:
            self.noeud_entree = -1

    def ajouter_noeud(self, n: int, coords: tuple[int, int]):
        if n >= 0:
            self.noeuds[n] = coords

    def ajouter_arc(self, n1: int, n2: int) -> None:
        if n1 > n2:
            tmp = n2
            n2 = n1
            n1 = tmp
        if n1 not in self.noeuds.keys() or n2 not in self.noeuds.keys():
            return
        if (n1, n2) not in self.arcs:
            self.arcs.append((n1, n2))
            
    def set_strategie(self, strat: StrategieReseau):
        self.strat = strat

    def valider_reseau(self) -> bool:
    
    if self.noeud_entree == -1:
        print("Erreur : Aucun nœud d'entrée défini.")
        return False

    # Utilisation d'un algorithme de parcours pour vérifier la connectivité (parcours en largeur ici)
    visites = set()
    a_visiter = [self.noeud_entree]

    while a_visiter:
        noeud_courant = a_visiter.pop(0)
        if noeud_courant not in visites:
            visites.add(noeud_courant)
            # Ajouter tous les voisins connectés à visiter
            for arc in self.arcs:
                if noeud_courant == arc[0]:
                    a_visiter.append(arc[1])
                elif noeud_courant == arc[1]:
                    a_visiter.append(arc[0])

    # Vérifier si tous les nœuds sont visités
    if len(visites) == len(self.noeuds):
        return True
    else:
        print("Erreur : Certains nœuds ne sont pas connectés au nœud d'entrée.")
        return False



    def valider_distribution(self, terrain: "Terrain") -> bool:
    
    if self.noeud_entree == -1:
        print("Erreur : Aucun nœud d'entrée défini.")
        return False

    # Récupérer les coordonnées des clients sur le terrain
    clients = terrain.get_clients()  # Une liste de coordonnées des clients, ex : [(1, 2), (3, 4), ...]

    # Vérifier que chaque client est connecté au réseau
    for client in clients:
        est_alimente = False
        for noeud, coords in self.noeuds.items():
            if coords == client:
                # Vérifier que ce nœud est relié au réseau via le nœud d'entrée
                if self.est_connecte_au_noeud_entree(noeud):
                    est_alimente = True
                    break
        if not est_alimente:
            print(f"Erreur : Le client aux coordonnées {client} n'est pas alimenté.")
            return False

    return True


    def configurer(self, t: Terrain):
        self.noeud_entree, self.noeuds, self.arcs  = self.strat.configurer(t)
    
     def afficher(self) -> None:
    # Affichage des nœuds
    print("=== Configuration du Réseau ===")
    print("Nœuds :")
    for noeud, coords in self.noeuds.items():
        print(f"  - Nœud {noeud} : Coordonnées {coords}")
    
    # Affichage des arcs
    print("\nArcs :")
    if not self.arcs:
        print("  Aucun arc dans le réseau.")
    else:
        for arc in self.arcs:
            print(f"  - Arc entre les nœuds {arc[0]} et {arc[1]}")
    
    # Affichage du nœud d'entrée
    print("\nNœud d'entrée :")
    if self.noeud_entree == -1:
        print("  Aucun nœud d'entrée défini.")
    else:
        print(f"  Nœud d'entrée : {self.noeud_entree}")
    print("=== Fin de la Configuration ===")
    
    def afficher_avec_terrain(self, t: Terrain) -> None:
        for ligne, l in enumerate(t.cases):
            for colonne, c in enumerate(l):
                if (ligne, colonne) not in self.noeuds.values():
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
                else:
                    if c == Case.OBSTACLE:
                        print("T", end="")
                    if c == Case.CLIENT:
                        print("C", end="")
                    if c == Case.VIDE:
                        print("+", end="")
                    if c == Case.ENTREE:
                        print("E", end="")
                    else:
                        print(" ", end="")
            print()

    def calculer_cout(self, t: Terrain) -> float:
        cout = 0
        for _ in self.arcs:
            cout += 1.5
        for n in self.noeuds.values():
            if t[n[0]][n[1]] == Case.OBSTACLE:
                cout += 2
            else:
                cout += 1
        return cout
