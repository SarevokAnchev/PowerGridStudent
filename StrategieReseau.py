
from Terrain import Terrain, Case

class StrategieReseau:
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        return -1, {}, []

class StrategieReseauManuelle(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        print("=== Configuration manuelle du réseau ===")
        t.afficher()

        try:
            noeud_entree = int(input("Id du noeud d'entrée (>=0) : "))
        except Exception:
            print("Entrée invalide, configuration annulée.")
            return -1, {}, []

        noeuds = {}
        arcs = []

        # Ajouter des noeuds
        while True:
            s = input("Id du noeud (ou ENTER pour finir) : ").strip()
            if s == "":
                break
            try:
                nid = int(s)
                i = int(input("  ligne : "))
                j = int(input("  colonne : "))
                if nid in noeuds:
                    print("  id déjà utilisé")
                else:
                    noeuds[nid] = (i, j)
            except Exception:
                print("  entrée invalide")

        # Ajouter des arcs
        while True:
            s = input("Arc (format: id1 id2) ou ENTER pour finir : ").strip()
            if s == "":
                break
            parts = s.split()
            if len(parts) != 2:
                print("  format invalide")
                continue
            try:
                a, b = int(parts[0]), int(parts[1])
                if a > b:
                    a, b = b, a
                if a in noeuds and b in noeuds:
                    if (a, b) not in arcs:
                        arcs.append((a, b))
                else:
                    print("  un des noeuds n'existe pas")
            except Exception:
                print("  valeurs invalides")
        return noeud_entree, noeuds, arcs

class StrategieReseauAuto(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        noeuds = {}
        arcs = []

        entree = t.get_entree()
        if entree == (-1, -1):
            return -1, {}, []

        # noeud d'entrée
        noeud_entree = 0
        noeuds[0] = entree
        nid = 1

        # un noeud par client
        for c in t.get_clients():
            noeuds[nid] = c
            arcs.append((noeud_entree, nid))
            nid += 1

        return noeud_entree, noeuds, arcs

