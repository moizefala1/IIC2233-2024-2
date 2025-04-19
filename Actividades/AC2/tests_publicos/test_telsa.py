import unittest
from unittest.mock import patch
from clases import AutoElectrico, Telsa


class VerificarClaseTelsa(unittest.TestCase):

    def test_herencia_vehiculo_Electrico(self):
        """
        Verifica que Telsa hereda de AutoElectrico
        """
        self.assertIn(AutoElectrico, Telsa.__mro__)

    def test_init_correcto(self):
        """
        Verifica una correcta instancia de Telsa
        """
        auto = Telsa(rendimiento=10, marca="c", energia=100, vida_util_bateria=3)
        self.assertEqual(auto.rendimiento, 10)
        self.assertEqual(auto.marca, "c")
        self.assertEqual(auto.energia, 100)
        self.assertEqual(auto.vida_util_bateria, 3)

        auto2 = Telsa(vida_util_bateria=1, rendimiento=1, marca="c2", energia=101)
        self.assertEqual(auto2.rendimiento, 1)
        self.assertEqual(auto2.marca, "c2")
        self.assertEqual(auto2.energia, 101)
        self.assertEqual(auto2.vida_util_bateria, 1)

    def test_llama_init_vehiculo(self):
        """
        Verifica que la herencia de Vehiculo se hace correctamente en Telsa
        """
        with patch("clases.Vehiculo.__init__") as mock:
            mock.return_value = None
            Telsa(
                capacidad_maleta=1,
                vida_util_bateria=1,
                rendimiento=1,
                marca="c2",
                energia=101,
            )
            mock.assert_called_once()

    def test_no_llama_init_auto_bencina(self):
        """
        Verifica que la herencia no viene de AutoBencina en Telsa
        """
        with patch("clases.AutoBencina.__init__") as mock:
            mock.return_value = None
            Telsa(vida_util_bateria=1, rendimiento=1, marca="c2", energia=101)
            mock.assert_not_called()

    def test_llama_init_auto_electrico(self):
        """
        Verifica que la herencia de AutoElectrico se hace correctamente en Telsa
        """
        with patch("clases.AutoElectrico.__init__") as mock:
            mock.return_value = None
            Telsa(vida_util_bateria=1, rendimiento=1, marca="c2", energia=101)
            mock.assert_called_once()

    def test_llama_recorrer_clase_padres(self):
        """
        Verifica que el metodo recorrer de Telsa utiliza correctamente
         el metodo de su clase padre AutoElectrico
        """
        try:
            with patch("clases.AutoElectrico.recorrer") as mock_1:
                mock_1.return_value = "test"
                auto = Telsa(
                    vida_util_bateria=1, rendimiento=1, marca="c2", energia=101
                )
                res = auto.recorrer(12.1)
                mock_1.assert_called_once_with(auto, 12.1)
                self.assertEqual(res, "test de forma muy inteligente")

        except AssertionError:
            with patch("clases.AutoElectrico.recorrer") as mock_1:
                mock_1.return_value = "test"
                auto = Telsa(
                    vida_util_bateria=1, rendimiento=1, marca="c2", energia=101
                )
                res = auto.recorrer(12.1)
                mock_1.assert_called_once_with(12.1)
                self.assertEqual(res, "test de forma muy inteligente")

    def test_recorrer_Telsa(self):
        """
        Verifica que el método recorrer de Telsa hace lo pedido
        """
        auto = Telsa(vida_util_bateria=1, rendimiento=1, marca="c2", energia=101.2)
        res = auto.recorrer(12.2)
        self.assertEqual(
            res, "Anduve 12.2Km y eso consume 12.2W de energia electrica de forma muy inteligente"
        )
