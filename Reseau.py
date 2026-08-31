from Terrain import Terrain, Case
from StrategieReseau import StrategieReseau, StrategieReseauAuto

class Reseau:
    def __init__(self):
        self.strat = StrategieReseauAuto()
        self.noeuds = {}
        self.arcs = []
        self.noeud_entree = -1

    def definir_entree(self, n: int) -> None:
        if n in self.noeuds:
            self.noeud_entree = n
        else:
            self.noeud_entree = -1

    def ajouter_noeud(self, n: int, coords: tuple[int, int]) -> None:
        if n >= 0 and n not in self.noeuds:
            self.noeuds[n] = coords

    def ajouter_arc(self, n1: int, n2: int) -> None:
        if n1 > n2:
            n1, n2 = n2, n1  # Assurez-vous que l'ordre est correct
        if n1 in self.noeuds and n2 in self.noeuds:
            if (n1, n2) not in self.arcs and (n2, n1) not in self.arcs:
                self.arcs.append((n1, n2))

    def set_strategie(self, strat: StrategieReseau) -> None:
        self.strat = strat

    def valider_reseau(self) -> bool:
        if self.noeud_entree == -1 or self.noeud_entree not in self.noeuds:
            return False

        visited = set()
        def dfs(noeud):
            if noeud in visited:
                return
            visited.add(noeud)
            for arc in self.arcs:
                if arc[0] == noeud:
                    dfs(arc[1])
                elif arc[1] == noeud:
                    dfs(arc[0])

        dfs(self.noeud_entree)
        return len(visited) == len(self.noeuds)

    def valider_distribution(self, t: Terrain) -> bool:
        if not isinstance(self.strat, StrategieReseau):
            raise TypeError("La stratégie doit être une instance de StrategieReseau")
        return self.strat.valider(self.noeuds, self.arcs, t)

    def configurer(self, t: Terrain):
        self.noeud_entree, self.noeuds, self.arcs = self.strat.configurer(t)

    def afficher(self) -> None:
        print("Noeuds:", self.noeuds)
        print("Arcs:", self.arcs)

    def calculer_cout(self, t: Terrain) -> float:
        cout = len(self.arcs) * 1.5
        for coords in self.noeuds.values():
            if t.cases[coords[0]][coords[1]] == Case.OBSTACLE:
                cout += 2
            else:
                cout += 1
        return cout
