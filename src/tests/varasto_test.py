import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negatiivinen_tilavuus_muutetaan_nollaksi(self):
        self.varasto = Varasto(-2)

        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_negatiivien_saldo_muutetaan_nollaksi(self):
        self.varasto = Varasto(10, -2)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_kun_saldo_on_isompaa_kuin_tilavuus_saldo_on_tilavuus(self):
        self.varasto = Varasto(10, 12)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_negatiivisen_arvon_lisaaminen_ei_muuta_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(-5)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_varastoon_lisataan_yli_vapaan_tilan_muuttuu_tila_taydeksi(self):
        self.varasto.lisaa_varastoon(200)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_negatiivisen_maaran_ottaminen_ei_muuta_varaston_tilaa(self):
        self.varasto.lisaa_varastoon(5)

        self.varasto.ota_varastosta(-1)

        # Varastossa edelleen 5 tavaraa
        self.assertAlmostEqual(str(self.varasto), "saldo = 5, vielä tilaa 5")

    def test_varastosta_otetaan_enemman_kuin_saldoa_on_saldo_nollaksi(self):
        self.varasto.lisaa_varastoon(5)

        vastaus = self.varasto.ota_varastosta(20)

        # Kaikki mitä voidaan ottaa on 5 kappaletta
        self.assertAlmostEqual(vastaus, 5)
