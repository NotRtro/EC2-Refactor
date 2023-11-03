import unittest
from app import CalculaGanador 

#Creamos una clase para las pruebas unitarias
class TestCalculaGanador(unittest.TestCase):
    def setUp(self):
        self.cg = CalculaGanador()
        self.datatest = [
            ['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '0'],
            ['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1']
        ]

    def test_contar_votos(self):
        votos = self.cg.contar_votos(self.datatest)
        self.assertEqual(votos, {'Eddie Hinesley': 1, 'Aundrea Grace': 2}) #comparamos el conteo con el esperado

    def test_calcularganador(self):
        ganador = self.cg.calcularganador(self.datatest)
        self.assertEqual(ganador, ['Eddie Hinesley', 'Aundrea Grace']) #comparamos el ganador con el esperado

if __name__ == '__main__':
    unittest.main()