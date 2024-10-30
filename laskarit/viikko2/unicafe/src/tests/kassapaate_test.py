import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.paate = Kassapaate()
        self.kortti = Maksukortti(1000)

    def test_rahamaara_on_oikea(self):
        self.assertEqual(self.paate.kassassa_rahaa, 100000)

    def test_lounaiden_maara_on_oikea(self):
        self.assertEqual(self.paate.edulliset + self.paate.maukkaat, 0)

    # Edulliset
    def test_edullisen_voi_ostaa_kateisella_raha_lisataan(self):
        self.paate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.paate.kassassa_rahaa, 100240)

    def test_edullisen_voi_ostaa_kateisella_lounas_lisataan(self):
        self.paate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.paate.edulliset, 1)

    def test_edullisen_vaihtoraha_oikea(self):
        self.assertEqual(self.paate.syo_edullisesti_kateisella(250), 10)

    def test_kateinen_ei_riita_edulliseen_rahaa_ei_lisata(self):
        self.paate.syo_edullisesti_kateisella(50)
        self.assertEqual(self.paate.kassassa_rahaa, 100000)

    def test_kateinen_ei_riita_edulliseen_lounasta_ei_lisata(self):
        self.paate.syo_edullisesti_kateisella(50)
        self.assertEqual(self.paate.edulliset, 0)

    def test_kateinen_ei_riita_edulliseen_vaihtoraha_annetaan(self):
        self.assertEqual(self.paate.syo_edullisesti_kateisella(50), 50)

    # Maukkaat
    def test_maukkaan_voi_ostaa_kateisella_raha_lisataan(self):
        self.paate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.paate.kassassa_rahaa, 100400)

    def test_maukkaan_voi_ostaa_kateisella_lounas_lisataan(self):
        self.paate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.paate.maukkaat, 1)

    def test_maukkaan_vaihtoraha_oikea(self):
        self.assertEqual(self.paate.syo_maukkaasti_kateisella(410), 10)

    def test_kateinen_ei_riita_maukkaaseen_rahaa_ei_lisata(self):
        self.paate.syo_maukkaasti_kateisella(50)
        self.assertEqual(self.paate.kassassa_rahaa, 100000)

    def test_kateinen_ei_riita_maukkaaseen_lounasta_ei_lisata(self):
        self.paate.syo_maukkaasti_kateisella(50)
        self.assertEqual(self.paate.edulliset, 0)

    def test_kateinen_ei_riita_maukkaaseen_vaihtoraha_annetaan(self):
        self.assertEqual(self.paate.syo_maukkaasti_kateisella(50), 50)

    # Kortti, edulliset
    def test_edullisen_voi_ostaa_kortilla(self):
        self.assertEqual(self.paate.syo_edullisesti_kortilla(self.kortti), True)

    def test_edullisen_voi_ostaa_kortilla_lounas_lisataan(self):
        self.paate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.paate.edulliset, 1)

    def test_kortin_saldo_ei_riita_edulliseen_lounasta_ei_lisata(self):
        kortti = Maksukortti(50)
        self.paate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.paate.edulliset, 0)

    def test_kortin_saldo_ei_riita_edulliseen_vaihtoraha_annetaan(self):
        kortti = Maksukortti(50)
        self.assertEqual(self.paate.syo_edullisesti_kortilla(kortti), False)

    # Kortti, maukkaat
    def test_maukkaan_voi_ostaa_kortilla(self):
        self.assertEqual(self.paate.syo_maukkaasti_kortilla(self.kortti), True)

    def test_maukkaan_voi_ostaa_kortilla_lounas_lisataan(self):
        self.paate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.paate.maukkaat, 1)

    def test_kortin_saldo_ei_riita_maukkaaseen_lounasta_ei_lisata(self):
        kortti = Maksukortti(50)
        self.paate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.paate.maukkaat, 0)

    def test_kortin_saldo_ei_riita_maukkaaseen_vaihtoraha_annetaan(self):
        kortti = Maksukortti(50)
        self.assertEqual(self.paate.syo_maukkaasti_kortilla(kortti), False)

    # Kortin metodit
    def test_rahaa_voi_ladata_kortille_kortin_saldo_muuttuu(self):
        self.paate.lataa_rahaa_kortille(self.kortti, 100)
        self.assertEqual(self.kortti.saldo_euroina(), 11.0)

    def test_rahaa_voi_ladata_kortille_kassan_raha_muuttuu(self):
        self.paate.lataa_rahaa_kortille(self.kortti, 100)
        self.assertEqual(self.paate.kassassa_rahaa, 100100)

    def test_ei_voi_ladata_negatiivista_kortille(self):
        self.paate.lataa_rahaa_kortille(self.kortti, -100)
        self.assertEqual(self.kortti.saldo_euroina(), 10.0)

    def test_ei_voi_ladata_negatiivista_kortille_kassan_raha_ei_muutu(self):
        self.paate.lataa_rahaa_kortille(self.kortti, -100)
        self.assertEqual(self.paate.kassassa_rahaa, 100000)

    def test_kassan_raha_euroina(self):
        self.assertEqual(self.paate.kassassa_rahaa_euroina(), 1000)
