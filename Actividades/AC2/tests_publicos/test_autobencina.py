import unittest
from unittest.mock import patch
import types
from clases import Vehiculo, AutoBencina


class VerificarClaseAutoBencina(unittest.TestCase):

    def test_llama_init_vehiculo(self):
        """
        Verifica que la herencia se hace correctamente en AutoBencina
        """
        with patch("clases.Vehiculo.__init__") as mock:
            mock.return_value = None
            AutoBencina(bencina_favorita="93", rendimiento=10, marca="chev", energia=100.2)
            mock.assert_called_once()

    def test_herencia_vehiculo(self):
        """
        Verifica que AutoBencina hereda de Vehiculo
        """
        self.assertIn(Vehiculo, AutoBencina.__mro__)

    def test_init_correcto(self):
        """
        Verifica una correcta instancia de AutoBencina y sus atributos
        """
        auto = AutoBencina(
            bencina_favorita="93", rendimiento=10, marca="chev", energia=100.2
        )
        self.assertEqual(auto.bencina_favorita, "93")
        self.assertEqual(auto.rendimiento, 10)
        self.assertEqual(auto.marca, "chev")
        self.assertEqual(auto.energia, 100.2)

        auto2 = AutoBencina(
            bencina_favorita="95", rendimiento=11, marca="chev2", energia=2.2
        )
        self.assertEqual(auto2.bencina_favorita, "95")
        self.assertEqual(auto2.rendimiento, 11)
        self.assertEqual(auto2.marca, "chev2")
        self.assertEqual(auto2.energia, 2.2)

    def test_valor_energia_por_defecto_correcto_auto_bencina(self):
        """
        Correcto valor por defecto de energia en AutoBencina
        """
        auto = AutoBencina(bencina_favorita="93", rendimiento=10, marca="chev")
        self.assertEqual(auto.energia, 111.5)

    def test_metodo_recorrer_definido(self):
        """
        Verifica que el método de recorrer de AutoBencina esta bien definido
        """
        self.assertIsInstance(AutoBencina.recorrer, types.FunctionType)

    def test_recorrer_sobre_autonomia(self):
        """
        Verifica que AutoBencina recorre correctamente estando por sobre su autonomía
        """
        auto = AutoBencina(
            bencina_favorita="93", rendimiento=10, marca="chev", energia=50.2
        )
        resultado = auto.recorrer(100000.2)
        self.assertEqual(auto.energia, 0)
        self.assertEqual(auto.autonomia, 0)
        self.assertEqual(resultado, "Anduve 502.0Km y eso consume 50.2L de bencina")

    def test_recorrer_bajo_autonomia(self):
        """
        Verifica que AutoBencina recorre correctamente estando bajo su autonomía
        """
        auto = AutoBencina(
            bencina_favorita="93", rendimiento=2, marca="chev", energia=80.4
        )
        resultado = auto.recorrer(99.2)
        self.assertAlmostEqual(auto.energia, 30.8, delta=0.2)
        self.assertAlmostEqual(auto.autonomia, 61.6, delta=0.2)
        self.assertEqual(resultado, "Anduve 99.2Km y eso consume 49.6L de bencina")

    def test_recorrer_bajo_autonomia_2(self):
        """
        Verifica que AutoBencina recorre correctamente estando bajo su autonomía
        """
        auto = AutoBencina(
            bencina_favorita="93", rendimiento=3, marca="chev", energia=30.3
        )
        resultado = auto.recorrer(29.3)
        self.assertAlmostEqual(auto.energia, 20.5, delta=0.2)
        self.assertAlmostEqual(auto.autonomia, 61.5, delta=0.2)
        self.assertEqual(resultado, "Anduve 29.3Km y eso consume 9.8L de bencina")
