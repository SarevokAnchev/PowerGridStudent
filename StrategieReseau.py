from collections import deque
from Terrain import Terrain, Case

class StrategieReseau:
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[tuple[int, int]]]:
        return -1, {}, []

class StrategieReseauManuelle(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[tuple[int, int]]]:
        # TODO
        return -1, {}, []

class StrategieReseauAuto(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[tuple[int, int]]]:
        entree = t.get_entree()
        if entree is None:
            return -1, {}, []
        ids = {entree: 0}          
        arcs = []
        for client in t.get_clients():
            chemin = self.plus_court_chemin(t, entree, client)
            for prec, cour in zip(chemin, chemin[1:]):
                if cour not in ids:
                    ids[cour] = len(ids)
                arc = tuple(sorted((ids[prec], ids[cour])))
                if arc not in arcs:
                    arcs.append(arc)

        noeuds = {n: coords for coords, n in ids.items()}
        return 0, noeuds, arcs

    def plus_court_chemin(self, t: Terrain, depart: tuple[int, int], arrivee: tuple[int, int]) -> list[tuple[int, int]]:
        parents = {depart: None}
        file = deque([depart])
        while file:
            l, c = file.popleft()
            if (l, c) == arrivee:
                break
            for dl, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                v = (l + dl, c + dc)
                if (0 <= v[0] < t.hauteur and 0 <= v[1] < t.largeur
                        and v not in parents and t[v[0]][v[1]] != Case.OBSTACLE):
                    parents[v] = (l, c)
                    file.append(v)

        if arrivee not in parents:
            return []
        chemin = []
        p = arrivee
        while p is not None:
            chemin.append(p)
            p = parents[p]
        return chemin[::-1]