import unittest
from unittest.mock import patch
from clases import AutoBencina, AutoElectrico, FaitHibrido


class VerificarClaseFaitHibrido(unittest.TestCase):

    def test_herencia_vehiculo_Electrico(self):
        """
        Verifica que FaitHibrido hereda de AutoElectrico
        """
        self.assertIn(AutoElectrico, FaitHibrido.__mro__)

    def test_herencia_vehiculo_Bencina(self):
        """
        Verifica que FaitHibrido hereda de AutoBencina
        """
        self.assertIn(AutoBencina, FaitHibrido.__mro__)

    def test_init_correcto(self):
        """
        Verifica una correcta instancia de FaitHibrido
        """
        auto = FaitHibrido(rendimiento=7, marca="c", energia=101.9, bencina_favorita=95)
        self.assertEqual(auto.rendimiento, 7)
        self.assertEqual(auto.marca, "c")
        self.assertEqual(auto.energia, 101.9)
        self.assertEqual(auto.vida_util_bateria, 5)

        auto2 = FaitHibrido(
            rendimiento=2, marca="c2", energia=131.3, bencina_favorita=95
        )
        self.assertEqual(auto2.rendimiento, 2)
        self.assertEqual(auto2.marca, "c2")
        self.assertEqual(auto2.energia, 131.3)
        self.assertEqual(auto2.vida_util_bateria, 5)

    def test_llama_init_vehiculo_solo_una_vez(self):
        """
        Verifica que la herencia de Vehiculo se hace correctamente en FaitHibrido
        """
        with patch("clases.Vehiculo.__init__") as mock:
            mock.return_value = None
            FaitHibrido(rendimiento=1, marca="c2", energia=101.3, bencina_favorita=95)
            mock.assert_called_once()

    def test_llama_recorrer_clases_padres_sobre_10_km(self):
        """
        Verifica que el método recorrer de FaitHibrido llama correctamente
         el método de sus clases padres AutoElectrico y AutoBencina cuando
         recorre sobre 10 kilómetros
        """
        with patch("clases.AutoBencina.recorrer") as mock:
            mock.return_value = "a"
            with patch("clases.AutoElectrico.recorrer") as mock2:
                mock2.return_value = "b"
                auto = FaitHibrido(
                    rendimiento=1, marca="c2", energia=101.2, bencina_favorita="95"
                )
                auto.recorrer(12.0)
                mock.assert_called_once_with(auto, 10.0)
                mock2.assert_called_once_with(auto, 2.0)

    def test_llama_recorrer_clases_padres_bajo_10_km(self):
        """
        Verifica que el método recorrer de FaitHibrido llama correctamente
         el método de sus clases padres AutoElectrico y AutoBencina cuando
         recorre bajo 10 kilómetros
        """
        with patch("clases.AutoBencina.recorrer") as mock:
            mock.return_value = "d"
            with patch("clases.AutoElectrico.recorrer") as mock2:
                mock2.return_value = "c"
                auto2 = FaitHibrido(
                    rendimiento=1, marca="c2", energia=101, bencina_favorita=95
                )
                auto2.recorrer(4.2)
                mock.assert_not_called()
                mock2.assert_called_once_with(auto2, 4.2)

    def test_llama_recorrer_clases_padres_justo_10_km(self):
        """
        Verifica que el método recorrer de FaitHibrido llama correctamente
         el método de sus clases padres AutoElectrico y AutoBencina cuando
         recorre justo 10 kilómetros
        """
        with patch("clases.AutoBencina.recorrer") as mock:
            mock.return_value = "d"
            with patch("clases.AutoElectrico.recorrer") as mock2:
                mock2.return_value = "c"
                auto2 = FaitHibrido(
                    rendimiento=1, marca="c2", energia=101, bencina_favorita=95
                )
                auto2.recorrer(10.0)
                mock.assert_not_called()
                mock2.assert_called_once_with(auto2, 10.0)

    def test_no_llama_init_auto_bencina(self):
        """
        Verifica que la herencia de AutoBencina se hace correctamente en FaitHibrido
        """
        with patch("clases.AutoBencina.__init__") as mock:
            mock.return_value = None
            FaitHibrido(rendimiento=1, marca="c2", energia=101, bencina_favorita=95)
            mock.assert_called_once()

    def test_llama_init_auto_electrico(self):
        """
        Verifica que la herencia de AutoElectrico se hace correctamente en FaitHibrido
        """
        with patch("clases.AutoElectrico.__init__") as mock:
            mock.return_value = None
            FaitHibrido(rendimiento=1, marca="c2", energia=101, bencina_favorita=95)
            mock.assert_called_once()

    def test_recorrer_FaitHibrido_sobre_10_km(self):
        """
        Verifica que el método recorrer de FaitHibrido retorne lo esperado
        cuando se recorre sobre 10km
        """
        auto = FaitHibrido(
            rendimiento=1, marca="c2", energia=102.2, bencina_favorita=95
        )
        res = auto.recorrer(10.5)
        self.assertEqual(
            res,
            "Anduve 10Km y eso consume 10.0L de bencina Anduve 0.5Km y eso consume 0.5W de energia electrica",
        )

    def test_recorrer_FaitHibrido_bajo_10_km(self):
        """
        Verifica que el método recorrer de FaitHibrido retorne lo esperado
        cuando se recorre bajo 10km
        """
        auto = FaitHibrido(
            rendimiento=2, marca="c2", energia=102.2, bencina_favorita=95
        )
        res = auto.recorrer(5.2)
        self.assertEqual(res, "Anduve 5.2Km y eso consume 2.6W de energia electrica")

    def test_recorrer_FaitHibrido_justo_10_km(self):
        """
        Verifica que el método recorrer de FaitHibrido retorne lo esperado
        cuando se recorre bajo 10km
        """
        auto = FaitHibrido(
            rendimiento=2, marca="c2", energia=102.2, bencina_favorita=95
        )
        res = auto.recorrer(10.0)
        self.assertEqual(res, "Anduve 10.0Km y eso consume 5.0W de energia electrica")
