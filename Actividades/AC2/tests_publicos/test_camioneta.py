import unittest
from unittest.mock import patch
from clases import AutoBencina, Camioneta


class VerificarClaseCamioneta(unittest.TestCase):

    def test_herencia_vehiculo_bencina(self):
        """
        Verifica que Camioneta hereda de AutoBencina
        """
        self.assertIn(AutoBencina, Camioneta.__mro__)

    def test_init_correcto(self):
        """
        Verifica correcto instanciamiento de Camioneta
        """
        auto = Camioneta(
            capacidad_maleta=10,
            rendimiento=10,
            marca="c",
            energia=100.2,
            bencina_favorita="93",
        )
        self.assertEqual(auto.rendimiento, 10)
        self.assertEqual(auto.marca, "c")
        self.assertEqual(auto.bencina_favorita, "93")
        self.assertEqual(auto.energia, 100.2)

        auto2 = Camioneta(
            capacidad_maleta=1,
            rendimiento=1,
            marca="c2",
            energia=108.1,
            bencina_favorita="95",
        )
        self.assertEqual(auto2.rendimiento, 1)
        self.assertEqual(auto2.bencina_favorita, "95")
        self.assertEqual(auto2.marca, "c2")
        self.assertEqual(auto2.energia, 108.1)

    def test_llama_init_vehiculo(self):
        """
        Verifica que la herencia de Vehiculo se hace correctamente en Camioneta
        """
        with patch("clases.Vehiculo.__init__") as mock:
            mock.return_value = None
            Camioneta(
                capacidad_maleta=10,
                rendimiento=10,
                marca="c",
                energia=100.3,
                bencina_favorita="92",
            )
            mock.assert_called_once()

    def test_llama_init_auto_bencina(self):
        """
        Verifica que la herencia de AutoBencina se hace correctamente en Camioneta
        """
        with patch("clases.AutoBencina.__init__") as mock:
            mock.return_value = None
            Camioneta(
                capacidad_maleta=10,
                rendimiento=10,
                marca="c",
                energia=100,
                bencina_favorita=92,
            )
            mock.assert_called_once()

    def test_no_llama_init_auto_electrico(self):
        """
        Verifica que la herencia no viene de AutoElectrico en Camioneta
        """
        with patch("clases.AutoElectrico.__init__") as mock:
            mock.return_value = None
            Camioneta(
                capacidad_maleta=10,
                rendimiento=10,
                marca="c",
                energia=100,
                bencina_favorita=92,
            )
            mock.assert_not_called()

    def test_recorrer_Camioneta(self):
        """
        Verifica que el método recorrer de Camioneta hace lo pedido
        """
        auto2 = Camioneta(
            capacidad_maleta=1,
            rendimiento=1,
            marca="c2",
            energia=101.3,
            bencina_favorita="95",
        )
        res = auto2.recorrer(10.5)
        self.assertEqual(res, "Anduve 10.5Km y eso consume 10.5L de bencina")

    def test_recorrer_Camioneta_2(self):
        """
        Verifica que el método recorrer de Camioneta hace lo pedido cuando excede
        """
        auto2 = Camioneta(
            capacidad_maleta=1,
            rendimiento=1,
            marca="c2",
            energia=101.3,
            bencina_favorita="95",
        )
        res = auto2.recorrer(4444.1)
        self.assertEqual(res, "Anduve 101.3Km y eso consume 101.3L de bencina")
