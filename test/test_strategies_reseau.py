import unittest
import xmlrunner

from Terrain import Terrain
from Reseau import Reseau
from StrategieReseau import StrategieReseauAuto

class TestStrategiesReseau(unittest.TestCase):

    def test_config_auto(self):
        r = Reseau()
        r.set_strategie(StrategieReseauAuto())

        t = Terrain()
        t.charger("terrains/t1.txt")
        r.configurer(t)

        self.assertTrue(r.valider_reseau())
        self.assertTrue(r.valider_distribution(t))

        t.charger("terrains/t2.txt")
        r.configurer(t)

        self.assertTrue(r.valider_reseau())
        self.assertTrue(r.valider_distribution(t))

if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="test-reports"))

