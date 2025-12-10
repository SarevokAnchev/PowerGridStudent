from Terrain import Terrain, Case

class StrategieReseau:
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[tuple[int, int]]]:
        return -1, {}, []

class StrategieReseauManuelle(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[tuple[int, int]]]:
        """
        Interface simple en ligne de commande :
        - affiche le terrain
        - demande l'id du noeud d'entrée
        - permet d'ajouter des noeuds (id, ligne, colonne)
        - permet d'ajouter des arcs (id1, id2)
        (méthode interactive, non utilisée par les tests automatiques)
        """
        print("=== Configuration manuelle du réseau ===")
        t.afficher()

        # demander l'id du noeud d'entrée (on autorise -1 pour annuler)
        try:
            noeud_entree = int(input("Id du noeud d'entrée (entier >=0) : "))
        except Exception:
            print("Entrée invalide, configuration annulée.")
            return -1, {}, []

        noeuds = {}
        arcs = []

        print("Ajout des noeuds (laisser id vide pour terminer).")
        while True:
            s = input("Id du noeud (ou ENTER pour finir) : ").strip()
            if s == "":
                break
            try:
                nid = int(s)
                i = int(input("  ligne : "))
                j = int(input("  colonne : "))
                if nid in noeuds:
                    print("  id déjà utilisé, ignorer.")
                else:
                    noeuds[nid] = (i, j)
            except Exception:
                print("  entrée invalide, recommencez.")

        print("Ajout des arcs (laisser vide pour terminer).")
        while True:
            s = input("Arc (format: id1 id2) ou ENTER pour finir : ").strip()
            if s == "":
                break
            parts = s.split()
            if len(parts) != 2:
                print("  format invalide.")
                continue
            try:
                a = int(parts[0]); b = int(parts[1])
                if a > b:
                    a, b = b, a
                if a in noeuds and b in noeuds:
                    if (a, b) not in arcs:
                        arcs.append((a, b))
                else:
                    print("  un des noeuds n'existe pas.")
            except Exception:
                print("  valeurs invalides.")

        return noeud_entree, noeuds, arcs

class StrategieReseauAuto(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[tuple[int, int]]]:
        """
        Stratégie automatique simple :
        - noeud 0 -> entrée
        - pour chaque client, créer un noeud et le relier directement à l'entrée
        (topologie en étoile). Ceci garantit que tous les clients sont desservis.
        """
        noeuds = {}
        arcs = []

        entree = t.get_entree()
        if entree == (-1, -1):
            return -1, {}, []

        # id 0 = entrée
        noeuds[0] = entree
        noeud_entree = 0
        nid = 1

        # un noeud par client, relié à l'entrée
        for c in t.get_clients():
            noeuds[nid] = c
            arcs.append((noeud_entree, nid))
            nid += 1

        return noeud_entree, noeuds, arcs
