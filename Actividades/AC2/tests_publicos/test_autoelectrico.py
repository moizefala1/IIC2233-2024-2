import unittest
from unittest.mock import patch
import types
from clases import Vehiculo, AutoElectrico


class VerificarClaseAutoElectrico(unittest.TestCase):

    def test_llama_init_vehiculo(self):
        """
        Verifica que la herencia se hace correctamente en AutoElectrico
        """
        with patch("clases.Vehiculo.__init__") as mock:
            mock.return_value = None
            AutoElectrico(vida_util_bateria=2, rendimiento=10, marca="c", energia=100.4)
            mock.assert_called_once()

    def test_herencia_vehiculo(self):
        """
        Verifica que AutoElectrico hereda de Vehiculo
        """
        self.assertIn(Vehiculo, AutoElectrico.__mro__)

    def test_init_correcto(self):
        """
        Verifica una correcta instancia de AutoElectrico y sus atributos
        """
        auto = AutoElectrico(
            vida_util_bateria=11, rendimiento=10, marca="c", energia=29.4
        )
        self.assertEqual(auto.rendimiento, 10)
        self.assertEqual(auto.vida_util_bateria, 11)
        self.assertEqual(auto.marca, "c")
        self.assertEqual(auto.energia, 29.4)

        auto2 = AutoElectrico(
            vida_util_bateria=1, rendimiento=11, marca="c2", energia=129.1
        )
        self.assertEqual(auto2.rendimiento, 11)
        self.assertEqual(auto2.vida_util_bateria, 1)
        self.assertEqual(auto2.marca, "c2")
        self.assertEqual(auto2.energia, 129.1)

    def test_valor_energia_por_defecto_correcto_auto_bencina(self):
        """
        Correcto valor por defecto de energia en AutoElectrico
        """
        auto = AutoElectrico(vida_util_bateria=1, rendimiento=11, marca="c2")
        self.assertEqual(auto.energia, 111.5)

    def test_metodo_recorrer_definido(self):
        """
        Verifica que el método de recorrer de AutoElectrico esta bien definido
        """
        self.assertIsInstance(AutoElectrico.recorrer, types.FunctionType)

    def test_recorrer_sobre_autonomia(self):
        """
        Verifica que AutoElectrico recorre correctamente estando por sobre su autonomía
        """
        auto = AutoElectrico(
            vida_util_bateria=93, rendimiento=10, marca="chev", energia=23.2
        )
        resultado = auto.recorrer(10000.3)
        self.assertEqual(auto.energia, 0)
        self.assertEqual(
            resultado, "Anduve 232.0Km y eso consume 23.2W de energia electrica"
        )

    def test_recorrer_bajo_autonomia(self):
        """
        Verifica que AutoElectrico recorre correctamente estando bajo su autonomía
        """
        auto = AutoElectrico(
            vida_util_bateria=93, rendimiento=11, marca="chev", energia=10.6
        )
        resultado = auto.recorrer(99.0)
        self.assertEqual(auto.energia, 1.6)
        self.assertEqual(
            resultado, "Anduve 99.0Km y eso consume 9.0W de energia electrica"
        )

    def test_recorrer_bajo_autonomia_2(self):
        """
        Verifica que AutoBencina recorre correctamente estando bajo su autonomía
        """
        auto = AutoElectrico(
            vida_util_bateria=93, rendimiento=3, marca="chev", energia=30.3
        )
        resultado = auto.recorrer(29.3)
        self.assertAlmostEqual(auto.energia, 20.5, delta=0.2)
        self.assertAlmostEqual(auto.autonomia, 61.5, delta=0.2)
        self.assertEqual(resultado, "Anduve 29.3Km y eso consume 9.8W de energia electrica")

