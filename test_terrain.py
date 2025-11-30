
import unittest
import xmlrunner

from Terrain import Terrain, Case

class TestTerrain(unittest.TestCase):

    def test_chargement(self):
        import tempfile
        import os
        # Création d'un fichier temporaire contenant un petit terrain
        contenu = (
            "E~C\n"
            " C \n"
        )

        with tempfile.NamedTemporaryFile("w", delete=False) as f:
            f.write(contenu)
            requirement = f.name
        # Charger le terrain
        t = Terrain()
        t.charger(requirement)

        # Nettoyage du fichier temporaire
        os.remove(requirement)

        # Vérifications générales
        self.assertEqual(t.largeur, 3)   # 3 colonnes
        self.assertEqual(t.hauteur, 2)   # 2 lignes

        # Vérification des cases attendues
        self.assertEqual(t.cases[0][0], Case.ENTREE)
        self.assertEqual(t.cases[0][1], Case.VIDE)
        self.assertEqual(t.cases[0][2], Case.CLIENT)

        # Ligne 2
        self.assertEqual(t.cases[1][0], Case.OBSTACLE)
        self.assertEqual(t.cases[1][1], Case.CLIENT)
        self.assertEqual(t.cases[1][2], Case.OBSTACLE)

    def test_accesseur(self):
        t = Terrain()
        t.cases = [
                [Case.ENTREE, Case.VIDE, Case.VIDE],
                [Case.CLIENT, Case.CLIENT, Case.CLIENT],
        ]
        self.assertEqual(t[0][0], Case.ENTREE)
        self.assertEqual(t[0][1], Case.VIDE)
        self.assertEqual(t[1][2], Case.CLIENT)

if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="test-reports"))

