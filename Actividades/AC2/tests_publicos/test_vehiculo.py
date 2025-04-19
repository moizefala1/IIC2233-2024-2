import unittest
from clases import Vehiculo


class VerificarClaseVehiculo(unittest.TestCase):

    def test_property_energia_definida(self):
        """
        Verifica que energia es property
        """
        self.assertIsInstance(Vehiculo.energia, property)

    def test_property_autonomia_definida(self):
        """
        Verifica que autonomia es property
        """
        self.assertIsInstance(Vehiculo.autonomia, property)

    def test_property_enegia_setter(self):
        """
        Verifica que la energía de vehículo no parta siendo 0
        """
        auto = Vehiculo(rendimiento=10, marca="chev", energia=32.1)
        self.assertEqual(auto.energia, 32.1)

        auto.energia = -1200.3
        self.assertEqual(auto.energia, 0)

    def test_init_con_restriccion_energia(self):
        """
        Verifica que la energía de vehículo no parta siendo 0
        """
        auto = Vehiculo(rendimiento=10, marca="chev", energia=-9999.2)
        self.assertEqual(auto.energia, 0)

    def test_init_con_atributos_correctos(self):
        """
        Verifica correcto setter de la property
        """
        auto = Vehiculo(rendimiento=10, marca="chev", energia=3)
        self.assertEqual(auto.rendimiento, 10)
        self.assertEqual(auto.marca, "chev")
        self.assertEqual(auto._energia, 3)

    def test_valor_energia_por_defecto_correcto(self):
        """
        Correcto valor por defecto de energia en AutoElectrico
        """
        auto = Vehiculo(rendimiento=10, marca="chev")
        self.assertEqual(auto.energia, 111.5)

    def test_init_identificador(self):
        """
        Verifica un correcto aumento del identificador
        """
        id_inicial = Vehiculo.identificador
        auto = Vehiculo(rendimiento=10, marca="chev", energia=100.2)
        self.assertEqual(auto.identificador, id_inicial)

        auto2 = Vehiculo(rendimiento=10, marca="chev2", energia=101.2)
        self.assertEqual(auto2.identificador, id_inicial + 1)
