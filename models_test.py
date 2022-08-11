# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DetalIndeksCecha(models.Model):
    c_docnum = models.CharField(db_column='C_DocNum', max_length=50, blank=True, null=True)  # Field name made lowercase.
    i_itemnum = models.CharField(db_column='I_ItemNum', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rodzajmaterialu = models.DecimalField(db_column='rodzajMaterialu', max_digits=17, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    gruboscmaterialu = models.TextField(db_column='gruboscMaterialu', blank=True, null=True)  # Field name made lowercase.
    szerokoscmaterialu = models.TextField(db_column='szerokoscMaterialu', blank=True, null=True)  # Field name made lowercase.
    dlugoscmaterialu = models.TextField(db_column='dlugoscMaterialu', blank=True, null=True)  # Field name made lowercase.
    cechamaterialu = models.CharField(db_column='cechaMaterialu', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'Detal_Indeks_Cecha'


class DetalWagaPowierzchnia(models.Model):
    indeks = models.CharField(db_column='Indeks', max_length=50)  # Field name made lowercase.
    powierzchnia = models.DecimalField(db_column='Powierzchnia', max_digits=18, decimal_places=9)  # Field name made lowercase.
    waga = models.DecimalField(db_column='Waga', max_digits=18, decimal_places=9)  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'Detal_Waga_Powierzchnia'


class DetalZamiennik(models.Model):
    indeks_numeroperacji = models.CharField(db_column='indeks_NumerOperacji', max_length=25, blank=True, null=True)  # Field name made lowercase.
    zamiennikamada = models.CharField(db_column='zamiennikAmada', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idoperacji = models.IntegerField(db_column='idOperacji', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'Detal_Zamiennik'


class Eksportbom(models.Model):
    m_twrgidnr = models.IntegerField(db_column='M_TwrGidNr', blank=True, null=True)  # Field name made lowercase.
    m_twrkod = models.CharField(db_column='M_TwrKod', max_length=50, blank=True, null=True)  # Field name made lowercase.
    m_numeroperacji = models.IntegerField(db_column='M_NumerOperacji', blank=True, null=True)  # Field name made lowercase.
    m_kodprocesu = models.CharField(db_column='M_KodProcesu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    m_lppozycjibom = models.CharField(db_column='M_LpPozycjiBOM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    m_idpozycjibom = models.IntegerField(db_column='M_IDPozycjiBOM', blank=True, null=True)  # Field name made lowercase.
    m_indekspozycjibom = models.CharField(db_column='M_IndeksPozycjiBOM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    m_ilosc = models.DecimalField(db_column='M_Ilosc', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EksportBOM'


class EksportbomDel(models.Model):
    m_twrgidnr = models.IntegerField(db_column='M_TwrGidNr', blank=True, null=True)  # Field name made lowercase.
    m_twrkod = models.CharField(db_column='M_TwrKod', max_length=50, blank=True, null=True)  # Field name made lowercase.
    m_numeroperacji = models.IntegerField(db_column='M_NumerOperacji', blank=True, null=True)  # Field name made lowercase.
    m_kodprocesu = models.CharField(db_column='M_KodProcesu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    m_lppozycjibom = models.CharField(db_column='M_LpPozycjiBOM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    m_idpozycjibom = models.IntegerField(db_column='M_IDPozycjiBOM', blank=True, null=True)  # Field name made lowercase.
    m_indekspozycjibom = models.CharField(db_column='M_IndeksPozycjiBOM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    m_ilosc = models.DecimalField(db_column='M_Ilosc', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EksportBOM-del'


class Eksportbom2(models.Model):
    m_twrgidnumer = models.IntegerField(db_column='M_TwrGIDNumer')  # Field name made lowercase.
    m_twrkod = models.CharField(db_column='M_TwrKod', max_length=40, blank=True, null=True)  # Field name made lowercase.
    m_numeroperacji = models.CharField(db_column='M_NumerOperacji', max_length=5, blank=True, null=True)  # Field name made lowercase.
    m_kodprocesu = models.CharField(db_column='M_KodProcesu', max_length=200, blank=True, null=True)  # Field name made lowercase.
    m_lppozycjibom = models.CharField(db_column='M_LpPozycjiBOM', max_length=7)  # Field name made lowercase.
    m_idpozycjibom = models.IntegerField(db_column='M_IdPozycjiBOM')  # Field name made lowercase.
    m_indekspozycjibom = models.CharField(db_column='M_IndeksPozycjiBOM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    m_ilosc = models.DecimalField(db_column='M_Ilosc', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EksportBOM2'


class Eksportbomzlecenie(models.Model):
    m_idzlecprodukcyjnego = models.IntegerField(db_column='M_IdZlecProdukcyjnego', blank=True, null=True)  # Field name made lowercase.
    m_lppozycjizlecprodukcyjnego = models.IntegerField(db_column='M_LpPozycjiZlecProdukcyjnego', blank=True, null=True)  # Field name made lowercase.
    m_nrzlecprod = models.CharField(db_column='M_NrZlecProd', max_length=50, blank=True, null=True)  # Field name made lowercase.
    m_orbomid = models.IntegerField(db_column='M_OrBomID', blank=True, null=True)  # Field name made lowercase.
    m_parentbomid = models.IntegerField(db_column='M_ParentBomID', blank=True, null=True)  # Field name made lowercase.
    m_twrgidnr = models.IntegerField(db_column='M_TwrGidNr', blank=True, null=True)  # Field name made lowercase.
    m_twrkod = models.CharField(db_column='M_TwrKod', max_length=50, blank=True, null=True)  # Field name made lowercase.
    m_numeroperacji = models.IntegerField(db_column='M_NumerOperacji', blank=True, null=True)  # Field name made lowercase.
    m_kodprocesu = models.CharField(db_column='M_KodProcesu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    m_lppozycjibom = models.IntegerField(db_column='M_LpPozycjiBOM', blank=True, null=True)  # Field name made lowercase.
    m_idpozycjibom = models.IntegerField(db_column='M_IDPozycjiBOM', blank=True, null=True)  # Field name made lowercase.
    m_indekspozycjibom = models.CharField(db_column='M_IndeksPozycjiBOM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    m_ilosc = models.DecimalField(db_column='M_Ilosc', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    m_iloscnarw = models.DecimalField(db_column='M_IloscNaRW', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EksportBOMZlecenie'


class Eksportbomzlecenie2(models.Model):
    m_idzlecprodukcyjnego = models.IntegerField(db_column='M_IdZlecProdukcyjnego', blank=True, null=True)  # Field name made lowercase.
    m_lppozycjizlecprodukcyjnego = models.IntegerField(db_column='M_LpPozycjiZlecProdukcyjnego', blank=True, null=True)  # Field name made lowercase.
    m_nrzlecprod = models.CharField(db_column='M_NrZlecProd', max_length=50, blank=True, null=True)  # Field name made lowercase.
    m_orbomid = models.IntegerField(db_column='M_OrBomID', blank=True, null=True)  # Field name made lowercase.
    m_parentbomid = models.IntegerField(db_column='M_ParentBomID', blank=True, null=True)  # Field name made lowercase.
    m_twrgidnr = models.IntegerField(db_column='M_TwrGidNr', blank=True, null=True)  # Field name made lowercase.
    m_twrkod = models.CharField(db_column='M_TwrKod', max_length=50, blank=True, null=True)  # Field name made lowercase.
    m_numeroperacji = models.IntegerField(db_column='M_NumerOperacji', blank=True, null=True)  # Field name made lowercase.
    m_kodprocesu = models.CharField(db_column='M_KodProcesu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    m_lppozycjibom = models.IntegerField(db_column='M_LpPozycjiBOM', blank=True, null=True)  # Field name made lowercase.
    m_idpozycjibom = models.IntegerField(db_column='M_IDPozycjiBOM', blank=True, null=True)  # Field name made lowercase.
    m_indekspozycjibom = models.CharField(db_column='M_IndeksPozycjiBOM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    m_ilosc = models.DecimalField(db_column='M_Ilosc', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    m_iloscnarw = models.DecimalField(db_column='M_IloscNaRW', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EksportBOMZlecenie2'


class Eksportkontrahenci(models.Model):
    c_kodkontrahenta = models.CharField(db_column='C_KodKontrahenta', max_length=50, blank=True, null=True)  # Field name made lowercase.
    c_nazwakontrahenta = models.CharField(db_column='C_NazwaKontrahenta', max_length=50, blank=True, null=True)  # Field name made lowercase.
    c_priorytet = models.CharField(db_column='C_Priorytet', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EksportKontrahenci'


class Eksportparametry(models.Model):
    idprzewodnikaorh = models.IntegerField(db_column='idPrzewodnikaORH')  # Field name made lowercase.
    knt_akronim = models.CharField(db_column='knt_Akronim', max_length=50, blank=True, null=True)  # Field name made lowercase.
    numerzlecenia = models.TextField(db_column='numerZlecenia', blank=True, null=True)  # Field name made lowercase.
    twr_kod = models.CharField(db_column='twr_Kod', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idprzewodnikaprh = models.IntegerField(db_column='idPrzewodnikaPRH')  # Field name made lowercase.
    ititem = models.IntegerField(db_column='itItem')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EksportParametry'


class Eksportpostepprodukcji(models.Model):
    o_idoperacji = models.IntegerField(db_column='O_IdOperacji', blank=True, null=True)  # Field name made lowercase.
    o_kodzasobu = models.CharField(db_column='O_KodZasobu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    o_rdata_rozpoczecia = models.DateTimeField(db_column='O_RData_rozpoczecia', blank=True, null=True)  # Field name made lowercase.
    o_rdata_zakonczenia = models.DateTimeField(db_column='O_RData_zakonczenia', blank=True, null=True)  # Field name made lowercase.
    o_iloscwyprodukowanadobrych = models.DecimalField(db_column='O_IloscWyprodukowanaDobrych', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    o_iloscwyprodukowanybrakow = models.DecimalField(db_column='O_IloscWyprodukowanyBrakow', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    o_statusprzewodnika = models.CharField(db_column='O_StatusPrzewodnika', max_length=1, blank=True, null=True)  # Field name made lowercase.
    o_nazwastatusuprzewodnika = models.CharField(db_column='O_NazwaStatusuPrzewodnika', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EksportPostepProdukcji'


class Eksportpozycje(models.Model):
    p_twrgidnr = models.IntegerField(db_column='P_TwrGidNr', blank=True, null=True)  # Field name made lowercase.
    p_twrkod = models.CharField(db_column='P_TwrKod', max_length=50, blank=True, null=True)  # Field name made lowercase.
    p_twrnazwa = models.CharField(db_column='P_TwrNazwa', max_length=255, blank=True, null=True)  # Field name made lowercase.
    p_icodeid = models.CharField(db_column='P_ICodeID', max_length=1, blank=True, null=True)  # Field name made lowercase.
    p_grupytowarow = models.CharField(db_column='P_GrupyTowarow', max_length=255, blank=True, null=True)  # Field name made lowercase.
    p_priorytetpozycji = models.DecimalField(db_column='P_PriorytetPozycji', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    p_twcwartosc = models.DecimalField(db_column='P_TwcWartosc', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    p_czasdostawy = models.IntegerField(db_column='P_CzasDostawy', blank=True, null=True)  # Field name made lowercase.
    p_zapasminimalny = models.DecimalField(db_column='P_ZapasMinimalny', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    p_zapasmaksymalny = models.DecimalField(db_column='P_ZapasMaksymalny', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    p_partiazakupmin = models.DecimalField(db_column='P_PartiaZakupMin', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    p_partiazakupmax = models.DecimalField(db_column='P_PartiaZakupMax', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    p_specyfikacjetxt001 = models.CharField(db_column='P_SpecyfikacjeTxt001', max_length=50, blank=True, null=True)  # Field name made lowercase.
    p_specyfikacjenum001 = models.DecimalField(db_column='P_SpecyfikacjeNum001', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    p_specyfikacjetxt002 = models.CharField(db_column='P_SpecyfikacjeTxt002', max_length=50, blank=True, null=True)  # Field name made lowercase.
    p_specyfikacjenum002 = models.DecimalField(db_column='P_SpecyfikacjeNum002', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    p_specyfikacjetxt003 = models.CharField(db_column='P_SpecyfikacjeTxt003', max_length=50, blank=True, null=True)  # Field name made lowercase.
    p_specyfikacjenum003 = models.DecimalField(db_column='P_SpecyfikacjeNum003', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    p_specyfikacjetxt004 = models.CharField(db_column='P_SpecyfikacjeTxt004', max_length=50, blank=True, null=True)  # Field name made lowercase.
    p_specyfikacjenum004 = models.DecimalField(db_column='P_SpecyfikacjeNum004', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    p_specyfikacjetxt005 = models.CharField(db_column='P_SpecyfikacjeTxt005', max_length=50, blank=True, null=True)  # Field name made lowercase.
    p_specyfikacjenum005 = models.CharField(db_column='P_SpecyfikacjeNum005', max_length=200, blank=True, null=True)  # Field name made lowercase.
    p_specyfikacjetxt006 = models.CharField(db_column='P_SpecyfikacjeTxt006', max_length=50, blank=True, null=True)  # Field name made lowercase.
    p_specyfikacjenum006 = models.CharField(db_column='P_SpecyfikacjeNum006', max_length=200, blank=True, null=True)  # Field name made lowercase.
    p_uwagi = models.CharField(db_column='P_Uwagi', max_length=255, blank=True, null=True)  # Field name made lowercase.
    p_jednostkamiary = models.CharField(db_column='P_JednostkaMiary', max_length=50, blank=True, null=True)  # Field name made lowercase.
    p_obecnosctechnologa = models.CharField(db_column='P_ObecnoscTechnologa', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EksportPozycje'


class Eksporttechnologia(models.Model):
    m_twrgidnr = models.IntegerField(db_column='M_TwrGidNr', blank=True, null=True)  # Field name made lowercase.
    m_twrkod = models.CharField(db_column='M_TwrKod', max_length=255, blank=True, null=True)  # Field name made lowercase.
    m_polepowierzchni = models.DecimalField(db_column='M_PolePowierzchni', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    m_sposobrealizacjioperacji = models.CharField(db_column='M_SposobRealizacjiOperacji', max_length=255, blank=True, null=True)  # Field name made lowercase.
    m_numeroperacji = models.IntegerField(db_column='M_NumerOperacji', blank=True, null=True)  # Field name made lowercase.
    m_kodprocesu = models.CharField(db_column='M_KodProcesu', max_length=255, blank=True, null=True)  # Field name made lowercase.
    m_opisoperacji = models.CharField(db_column='M_OpisOperacji', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    m_sekwencja = models.IntegerField(db_column='M_Sekwencja', blank=True, null=True)  # Field name made lowercase.
    m_idzasobu = models.IntegerField(db_column='M_IDZasobu', blank=True, null=True)  # Field name made lowercase.
    m_kodzasobu = models.CharField(db_column='M_KodZasobu', max_length=255, blank=True, null=True)  # Field name made lowercase.
    m_kodgniazda = models.CharField(db_column='M_KodGniazda', max_length=255, blank=True, null=True)  # Field name made lowercase.
    m_kodinstrukcji = models.CharField(db_column='M_KodInstrukcji', max_length=255, blank=True, null=True)  # Field name made lowercase.
    m_priorytetzasobu = models.DecimalField(db_column='M_PriorytetZasobu', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    m_wymaganailosczasobu = models.DecimalField(db_column='M_WymaganaIloscZasobu', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    m_bathdlaprocesu = models.CharField(db_column='M_BathDlaProcesu', max_length=255, blank=True, null=True)  # Field name made lowercase.
    m_tpdlabathaprocesu = models.CharField(db_column='M_TpDlaBathaProcesu', max_length=255, blank=True, null=True)  # Field name made lowercase.
    m_bathdlaoperacji = models.CharField(db_column='M_BathDlaOperacji', max_length=255, blank=True, null=True)  # Field name made lowercase.
    m_tpdlabathaoperacji = models.CharField(db_column='M_TpDlaBathaOperacji', max_length=255, blank=True, null=True)  # Field name made lowercase.
    m_czasprzezbrojeniaoperacji = models.CharField(db_column='M_CzasPrzezbrojeniaOperacji', max_length=255, blank=True, null=True)  # Field name made lowercase.
    m_czasprodukcji = models.CharField(db_column='M_CzasProdukcji', max_length=255, blank=True, null=True)  # Field name made lowercase.
    m_relacjadopoprzedniejoperacji = models.CharField(db_column='M_RelacjaDoPoprzedniejOperacji', max_length=255, blank=True, null=True)  # Field name made lowercase.
    m_organiczenietminodpoprzedniejoperacji = models.IntegerField(db_column='M_OrganiczenieTminOdPoprzedniejOperacji', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EksportTechnologia'


class Eksporttechnologiazleceniowa(models.Model):
    m_idzlecprodukcyjnego = models.IntegerField(db_column='M_IdZlecProdukcyjnego', blank=True, null=True)  # Field name made lowercase.
    m_idpozycjizlecprodukcyjnego = models.IntegerField(db_column='M_IdPozycjiZlecProdukcyjnego', blank=True, null=True)  # Field name made lowercase.
    m_lppozycjizlecprodukcyjnego = models.IntegerField(db_column='M_LpPozycjiZlecProdukcyjnego', blank=True, null=True)  # Field name made lowercase.
    m_nrzlecprod = models.CharField(db_column='M_NrZlecProd', max_length=50, blank=True, null=True)  # Field name made lowercase.
    m_orbomid = models.IntegerField(db_column='M_OrBomID', blank=True, null=True)  # Field name made lowercase.
    m_orbomparentid = models.IntegerField(db_column='M_OrBomParentID', blank=True, null=True)  # Field name made lowercase.
    m_twrgidnr = models.IntegerField(db_column='M_TwrGidNr', blank=True, null=True)  # Field name made lowercase.
    m_twrkod = models.CharField(db_column='M_TwrKod', max_length=50, blank=True, null=True)  # Field name made lowercase.
    m_polepowierzchni = models.DecimalField(db_column='M_PolePowierzchni', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    m_sposobrealizacjioperacji = models.CharField(db_column='M_SposobRealizacjiOperacji', max_length=50, blank=True, null=True)  # Field name made lowercase.
    m_idprzewodnika = models.IntegerField(db_column='M_IdPrzewodnika', blank=True, null=True)  # Field name made lowercase.
    m_idoperacji = models.IntegerField(db_column='M_IdOperacji', blank=True, null=True)  # Field name made lowercase.
    m_numeroperacji = models.IntegerField(db_column='M_NumerOperacji', blank=True, null=True)  # Field name made lowercase.
    m_kodprocesu = models.CharField(db_column='M_KodProcesu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    m_opisoperacji = models.CharField(db_column='M_OpisOperacji', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    m_sekwencja = models.IntegerField(db_column='M_Sekwencja', blank=True, null=True)  # Field name made lowercase.
    m_kodzasobu = models.CharField(db_column='M_KodZasobu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    m_kodinstrukcji = models.CharField(db_column='M_KodInstrukcji', max_length=50, blank=True, null=True)  # Field name made lowercase.
    m_wymaganailosczasobu = models.DecimalField(db_column='M_WymaganaIloscZasobu', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    m_bathdlaprocesu = models.CharField(db_column='M_BathDlaProcesu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    m_tpdlabathaprocesu = models.CharField(db_column='M_TpDlaBathaProcesu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    m_bathdlaoperacji = models.CharField(db_column='M_BathDlaOperacji', max_length=50, blank=True, null=True)  # Field name made lowercase.
    m_tpdlabathaoperacji = models.CharField(db_column='M_TpDlaBathaOperacji', max_length=50, blank=True, null=True)  # Field name made lowercase.
    m_czasprzezbrojeniaoperacji = models.CharField(db_column='M_CzasPrzezbrojeniaOperacji', max_length=50, blank=True, null=True)  # Field name made lowercase.
    m_czasprodukcji = models.CharField(db_column='M_CzasProdukcji', max_length=50, blank=True, null=True)  # Field name made lowercase.
    m_relacjadopoprzedniejoperacji = models.CharField(db_column='M_RelacjaDoPoprzedniejOperacji', max_length=50, blank=True, null=True)  # Field name made lowercase.
    m_organiczenietminodpoprzedniejoperacji = models.IntegerField(db_column='M_OrganiczenieTminOdPoprzedniejOperacji', blank=True, null=True)  # Field name made lowercase.
    m_idzasobuwoperacji = models.IntegerField(db_column='M_IdZasobuWOperacji', blank=True, null=True)  # Field name made lowercase.
    m_obecnosctechnologa = models.CharField(db_column='M_ObecnoscTechnologa', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EksportTechnologiaZleceniowa'


class Eksportzamowieniasprzedazy(models.Model):
    o_idzlecsprzedazy = models.IntegerField(db_column='O_IdZlecSprzedazy', blank=True, null=True)  # Field name made lowercase.
    o_idpozycjizlecsprzedazy = models.IntegerField(db_column='O_IdPozycjiZlecSprzedazy', blank=True, null=True)  # Field name made lowercase.
    o_numerzlecsprzedazy = models.CharField(db_column='O_NumerZlecSprzedazy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    o_kodkontrahenta = models.CharField(db_column='O_KodKontrahenta', max_length=50, blank=True, null=True)  # Field name made lowercase.
    o_twrgidnr = models.IntegerField(db_column='O_TwrGidNr', blank=True, null=True)  # Field name made lowercase.
    o_twrkod = models.CharField(db_column='O_TwrKod', max_length=50, blank=True, null=True)  # Field name made lowercase.
    o_ilosczamowiona = models.DecimalField(db_column='O_IloscZamowiona', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    o_datarealizacjipozadana = models.DateTimeField(db_column='O_DataRealizacjiPozadana', blank=True, null=True)  # Field name made lowercase.
    o_jestzlecenieprodukcyjne = models.IntegerField(db_column='O_JestZlecenieProdukcyjne', blank=True, null=True)  # Field name made lowercase.
    o_typzlecenia = models.CharField(db_column='O_TypZlecenia', max_length=1, blank=True, null=True)  # Field name made lowercase.
    o_numerukontrahenta = models.CharField(db_column='O_NumerUKontrahenta', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EksportZamowieniaSprzedazy'


class Eksportzamowieniazakupu(models.Model):
    o_numerzamowienia = models.CharField(db_column='O_NumerZamowienia', max_length=255, blank=True, null=True)  # Field name made lowercase.
    o_lppozycji = models.IntegerField(db_column='O_LpPozycji', blank=True, null=True)  # Field name made lowercase.
    o_kodkontrahenta = models.CharField(db_column='O_KodKontrahenta', max_length=50, blank=True, null=True)  # Field name made lowercase.
    o_twrgidnr = models.IntegerField(db_column='O_TwrGidNr', blank=True, null=True)  # Field name made lowercase.
    o_twrkod = models.CharField(db_column='O_TwrKod', max_length=50, blank=True, null=True)  # Field name made lowercase.
    o_ilosczamowiona = models.DecimalField(db_column='O_IloscZamowiona', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    o_data = models.DateField(db_column='O_Data', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EksportZamowieniaZakupu'


class Eksportzapasy(models.Model):
    o_twrgidnr = models.IntegerField(db_column='O_TwrGidNr', blank=True, null=True)  # Field name made lowercase.
    o_twrkod = models.CharField(db_column='O_TwrKod', max_length=50, blank=True, null=True)  # Field name made lowercase.
    o_wielkosczapasu = models.DecimalField(db_column='O_WielkoscZapasu', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EksportZapasy'


class Eksportzasoby(models.Model):
    r_idzasobu = models.IntegerField(db_column='R_IDZasobu', blank=True, null=True)  # Field name made lowercase.
    r_kodzasobu = models.CharField(db_column='R_KodZasobu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    r_nazwazasobu = models.CharField(db_column='R_NazwaZasobu', max_length=255, blank=True, null=True)  # Field name made lowercase.
    r_wydzial = models.CharField(db_column='R_Wydzial', max_length=255, blank=True, null=True)  # Field name made lowercase.
    r_gniazdo = models.CharField(db_column='R_Gniazdo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    r_typowaoperacja = models.CharField(db_column='R_TypowaOperacja', max_length=255, blank=True, null=True)  # Field name made lowercase.
    r_grupazasobu = models.CharField(db_column='R_GrupaZasobu', max_length=255, blank=True, null=True)  # Field name made lowercase.
    r_kosztroboczogodziny = models.DecimalField(db_column='R_KosztRoboczogodziny', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    r_awaria = models.CharField(db_column='R_Awaria', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EksportZasoby'


class Eksportzleceniaprodukcyjne(models.Model):
    o_idzlecprodukcyjnego = models.IntegerField(db_column='O_IdZlecProdukcyjnego', blank=True, null=True)  # Field name made lowercase.
    o_idpozycjizlecprodukcyjnego = models.IntegerField(db_column='O_IdPozycjiZlecProdukcyjnego', blank=True, null=True)  # Field name made lowercase.
    o_nrzlecprod = models.CharField(db_column='O_NrZlecProd', max_length=50, blank=True, null=True)  # Field name made lowercase.
    o_idpozzlecprod = models.IntegerField(db_column='O_IdPozZlecProd', blank=True, null=True)  # Field name made lowercase.
    o_orbomid = models.IntegerField(db_column='O_OrBomID', blank=True, null=True)  # Field name made lowercase.
    o_kodkontrahenta = models.CharField(db_column='O_KodKontrahenta', max_length=50, blank=True, null=True)  # Field name made lowercase.
    o_twrgidnr = models.IntegerField(db_column='O_TwrGidNr', blank=True, null=True)  # Field name made lowercase.
    o_twrkod = models.CharField(db_column='O_TwrKod', max_length=50, blank=True, null=True)  # Field name made lowercase.
    o_ilosczleconadoprodukcji = models.DecimalField(db_column='O_IloscZleconaDoProdukcji', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    o_datarealizacjipozadana = models.DateTimeField(db_column='O_DataRealizacjiPozadana', blank=True, null=True)  # Field name made lowercase.
    o_idzlecsprzedazy = models.IntegerField(db_column='O_IdZlecSprzedazy', blank=True, null=True)  # Field name made lowercase.
    o_idpozycjizlecsprzedazy = models.IntegerField(db_column='O_IdPozycjiZlecSprzedazy', blank=True, null=True)  # Field name made lowercase.
    o_numerzlecsprzedazy = models.CharField(db_column='O_NumerZlecSprzedazy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    o_iloscnapw = models.DecimalField(db_column='O_IloscNaPW', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    o_statuszlecprodmonaco = models.CharField(db_column='O_StatusZlecProdMonaco', max_length=50, blank=True, null=True)  # Field name made lowercase.
    o_datawysylki = models.DateTimeField(db_column='O_DataWysylki', blank=True, null=True)  # Field name made lowercase.
    o_numerukontrahenta = models.CharField(db_column='O_NumerUKontrahenta', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EksportZleceniaProdukcyjne'


class EmployeeappDepartments(models.Model):
    departmentid = models.AutoField(db_column='DepartmentId', primary_key=True)  # Field name made lowercase.
    departmentname = models.CharField(db_column='DepartmentName', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EmployeeApp_departments'


class EmployeeappEmployees(models.Model):
    employeeid = models.AutoField(db_column='EmployeeId', primary_key=True)  # Field name made lowercase.
    employeename = models.CharField(db_column='EmployeeName', max_length=500)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=500)  # Field name made lowercase.
    dateofjoining = models.DateField(db_column='DateOfJoining')  # Field name made lowercase.
    photofilename = models.CharField(db_column='PhotoFileName', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EmployeeApp_employees'


class Monacokalkulacjaczasprocesow(models.Model):
    id = models.AutoField(db_column='ID')  # Field name made lowercase.
    indeks = models.CharField(db_column='Indeks', max_length=100)  # Field name made lowercase.
    ilosc = models.IntegerField(db_column='Ilosc')  # Field name made lowercase.
    gniazdo = models.CharField(db_column='Gniazdo', max_length=100)  # Field name made lowercase.
    grupamaszyn = models.CharField(db_column='GrupaMaszyn', max_length=100)  # Field name made lowercase.
    oznaczeniemaszyny = models.CharField(db_column='OznaczenieMaszyny', max_length=100)  # Field name made lowercase.
    nazwamaszyny = models.CharField(db_column='NazwaMaszyny', max_length=100)  # Field name made lowercase.
    typ = models.CharField(db_column='Typ', max_length=50)  # Field name made lowercase.
    csum = models.DecimalField(db_column='CSum', max_digits=18, decimal_places=2)  # Field name made lowercase.
    msum = models.DecimalField(db_column='MSum', max_digits=18, decimal_places=2)  # Field name made lowercase.
    tsum = models.DecimalField(db_column='TSum', max_digits=18, decimal_places=2)  # Field name made lowercase.
    r1num = models.CharField(db_column='R1Num', max_length=50, blank=True, null=True)  # Field name made lowercase.
    r1name = models.CharField(db_column='R1Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    r2num = models.CharField(db_column='R2Num', max_length=50, blank=True, null=True)  # Field name made lowercase.
    r2name = models.CharField(db_column='R2Name', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MonacoKalkulacjaCzasProcesow'


class Rejestracjamonaco(models.Model):
    ozn = models.BooleanField(blank=True, null=True)
    rid = models.IntegerField(db_column='Rid')  # Field name made lowercase.
    prheadsoperationsid = models.IntegerField(db_column='PRHeadsOperationsId')  # Field name made lowercase.
    prheadid = models.IntegerField(db_column='PRHEadID')  # Field name made lowercase.
    prheadnum = models.CharField(db_column='PRHeadNum', max_length=50)  # Field name made lowercase.
    teoperationid = models.IntegerField(db_column='TEOperationId')  # Field name made lowercase.
    teoperationobjid = models.IntegerField(db_column='TEOperationObjId')  # Field name made lowercase.
    teopnum = models.CharField(db_column='TEOpNum', max_length=5)  # Field name made lowercase.
    teopname = models.CharField(db_column='TEOpName', max_length=200)  # Field name made lowercase.
    quantitydemand = models.DecimalField(db_column='QuantityDemand', max_digits=18, decimal_places=6)  # Field name made lowercase.
    estta = models.DecimalField(db_column='EstTa', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    esttauomid = models.CharField(db_column='EstTaUomId', max_length=5, blank=True, null=True)  # Field name made lowercase.
    esttauomname = models.CharField(db_column='EstTaUomName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    esttb = models.DecimalField(db_column='EstTb', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    esttbuomid = models.CharField(db_column='EstTbUomId', max_length=5, blank=True, null=True)  # Field name made lowercase.
    esttbuomname = models.CharField(db_column='EstTbUomName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    esttc = models.DecimalField(db_column='EstTc', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    esttcuomid = models.CharField(db_column='EstTcUomId', max_length=5, blank=True, null=True)  # Field name made lowercase.
    esttcuomname = models.CharField(db_column='EstTcUomName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ppresources_rid = models.IntegerField(db_column='PPResources_Rid', blank=True, null=True)  # Field name made lowercase.
    ppresources_rnum = models.CharField(db_column='PPResources_RNum', max_length=25, blank=True, null=True)  # Field name made lowercase.
    ppresources_rname = models.CharField(db_column='PPResources_RName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    pho_datefrom = models.DateTimeField(db_column='PHO_DateFrom')  # Field name made lowercase.
    pho_dateto = models.DateTimeField(db_column='PHO_DateTo')  # Field name made lowercase.
    teocodeflag = models.IntegerField(db_column='TEOCodeFlag', blank=True, null=True)  # Field name made lowercase.
    teocodeflagoriginal = models.IntegerField(db_column='TEOCodeFlagOriginal')  # Field name made lowercase.
    teocodeid = models.CharField(db_column='TEOCodeId', max_length=5)  # Field name made lowercase.
    teocodename = models.CharField(db_column='TEOCodeName', max_length=50)  # Field name made lowercase.
    ppresources_machinerid = models.IntegerField(db_column='PPResources_MachineRid')  # Field name made lowercase.
    ppresources_machinernum = models.CharField(db_column='PPResources_MachineRNum', max_length=25)  # Field name made lowercase.
    ppresources_machinername = models.CharField(db_column='PPResources_MachineRName', max_length=200)  # Field name made lowercase.
    prregheadersourceid = models.IntegerField(db_column='PRRegHeaderSourceId')  # Field name made lowercase.
    prregheadersource = models.CharField(db_column='PRRegHeaderSource', max_length=1)  # Field name made lowercase.
    quantityregistered = models.DecimalField(db_column='QuantityRegistered', max_digits=18, decimal_places=6)  # Field name made lowercase.
    quantityregisteredrejected = models.DecimalField(db_column='QuantityRegisteredRejected', max_digits=18, decimal_places=6)  # Field name made lowercase.
    quantityregisteredupper = models.DecimalField(db_column='QuantityRegisteredUpper', max_digits=38, decimal_places=6)  # Field name made lowercase.
    quantityregisteredupperrejected = models.DecimalField(db_column='QuantityRegisteredUpperRejected', max_digits=38, decimal_places=6)  # Field name made lowercase.
    quantityproposal = models.DecimalField(db_column='QuantityProposal', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    quantityproposalrejected = models.DecimalField(db_column='QuantityProposalRejected', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    orheadsid = models.IntegerField(db_column='ORHeadsId')  # Field name made lowercase.
    ohnum = models.CharField(db_column='OHNum', max_length=50)  # Field name made lowercase.
    ohname = models.CharField(db_column='OHName', max_length=500)  # Field name made lowercase.
    ohrid = models.IntegerField(db_column='OHRid')  # Field name made lowercase.
    oinum = models.CharField(db_column='OINum', max_length=5)  # Field name made lowercase.
    oirid = models.IntegerField(db_column='OIRid')  # Field name made lowercase.
    oistatusid = models.CharField(db_column='OIStatusId', max_length=5)  # Field name made lowercase.
    oistatusname = models.CharField(db_column='OIStatusName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ititemnum = models.CharField(db_column='ITItemNum', max_length=50, blank=True, null=True)  # Field name made lowercase.
    itname = models.CharField(db_column='ITName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    itrid = models.IntegerField(db_column='ItRid', blank=True, null=True)  # Field name made lowercase.
    ppsigningid = models.CharField(db_column='PPSigningId', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ppsigningname = models.CharField(db_column='PPSigningName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    iticodeid = models.CharField(db_column='ITICodeId', max_length=5, blank=True, null=True)  # Field name made lowercase.
    iticodename = models.CharField(db_column='ITICodeName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ituomid = models.CharField(db_column='ITUomId', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ituomname = models.CharField(db_column='ITUomName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    itobjid = models.IntegerField(db_column='ITObjId', blank=True, null=True)  # Field name made lowercase.
    finishdate = models.DateTimeField(db_column='FinishDate')  # Field name made lowercase.
    timeduration = models.IntegerField(db_column='TimeDuration')  # Field name made lowercase.
    prheads_stateid = models.CharField(db_column='PRHeads_StateId', max_length=5)  # Field name made lowercase.
    prheads_statename = models.CharField(db_column='PRHeads_StateName', max_length=50)  # Field name made lowercase.
    operation_flag = models.IntegerField(db_column='Operation_Flag')  # Field name made lowercase.
    isdoc = models.IntegerField(db_column='IsDoc')  # Field name made lowercase.
    oherpid = models.IntegerField(db_column='OHErpId')  # Field name made lowercase.
    prregheadertype = models.CharField(db_column='PRRegHeaderType', max_length=5)  # Field name made lowercase.
    prreghederstate = models.SmallIntegerField(db_column='PRRegHederState')  # Field name made lowercase.
    propdemands_preference = models.IntegerField(db_column='PROpDemands_Preference')  # Field name made lowercase.
    ohtypeid = models.CharField(db_column='OHTypeId', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ohtypename = models.CharField(db_column='OHTypeName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    verificationemployee = models.IntegerField(db_column='VerificationEmployee', blank=True, null=True)  # Field name made lowercase.
    verificationdate = models.DateTimeField(db_column='VerificationDate', blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.
    regtype = models.CharField(db_column='RegType', max_length=5)  # Field name made lowercase.
    regtypename = models.CharField(db_column='RegTypeName', max_length=50)  # Field name made lowercase.
    regcustomint = models.IntegerField(db_column='RegCustomInt', blank=True, null=True)  # Field name made lowercase.
    regcustomdeci = models.DecimalField(db_column='RegCustomDeci', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    regcustomfloat = models.FloatField(db_column='RegCustomFloat', blank=True, null=True)  # Field name made lowercase.
    regcustomc10 = models.CharField(db_column='RegCustomC10', max_length=10, blank=True, null=True)  # Field name made lowercase.
    regcustomc25 = models.CharField(db_column='RegCustomC25', max_length=25, blank=True, null=True)  # Field name made lowercase.
    regcustomc100 = models.CharField(db_column='RegCustomC100', max_length=100, blank=True, null=True)  # Field name made lowercase.
    regcustomdate = models.DateTimeField(db_column='RegCustomDate', blank=True, null=True)  # Field name made lowercase.
    thcustom_unid1 = models.CharField(db_column='THCustom_UnId1', max_length=5, blank=True, null=True)  # Field name made lowercase.
    thcustom_unname1 = models.CharField(db_column='THCustom_UnName1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    thcustom_unid2 = models.CharField(db_column='THCustom_UnId2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    thcustom_unname2 = models.CharField(db_column='THCustom_UnName2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    thcustom_rid1 = models.IntegerField(db_column='THCustom_Rid1', blank=True, null=True)  # Field name made lowercase.
    thcustomint = models.IntegerField(db_column='THCustomInt', blank=True, null=True)  # Field name made lowercase.
    thcustomfloat = models.DecimalField(db_column='THCustomFloat', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    thcustomc10 = models.CharField(db_column='THCustomC10', max_length=10, blank=True, null=True)  # Field name made lowercase.
    thcustomc25 = models.CharField(db_column='THCustomC25', max_length=25, blank=True, null=True)  # Field name made lowercase.
    thcustomc100 = models.CharField(db_column='THCustomC100', max_length=100, blank=True, null=True)  # Field name made lowercase.
    thcustomtext = models.TextField(db_column='THCustomText', blank=True, null=True)  # Field name made lowercase.
    oilabelid = models.IntegerField(db_column='OILabelId', blank=True, null=True)  # Field name made lowercase.
    oilabelname = models.CharField(db_column='OILabelName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    matrixamount = models.DecimalField(db_column='MatrixAmount', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    teodescr = models.TextField(db_column='TEODescr')  # Field name made lowercase.
    prcaqheads_id = models.IntegerField(db_column='PRCAQHeads_Id', blank=True, null=True)  # Field name made lowercase.
    os_numandpos = models.CharField(db_column='OS_NumAndPos', max_length=100, blank=True, null=True)  # Field name made lowercase.
    teoperationsbatch = models.DecimalField(db_column='TEOperationsBatch', max_digits=10, decimal_places=3)  # Field name made lowercase.
    teheadsbatch = models.DecimalField(db_column='TEHeadsBatch', max_digits=10, decimal_places=3)  # Field name made lowercase.
    phtypeid = models.CharField(db_column='PHTypeId', max_length=5)  # Field name made lowercase.
    oipriority = models.IntegerField(db_column='OIPriority', blank=True, null=True)  # Field name made lowercase.
    mapnum = models.CharField(db_column='MapNum', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RejestracjaMonaco'


class Technolodzyprototypy(models.Model):
    osobaodpowiedzialna = models.CharField(db_column='OsobaOdpowiedzialna', max_length=200)  # Field name made lowercase.
    nr_zlecenia = models.CharField(db_column='Nr Zlecenia', max_length=200)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    klient = models.CharField(db_column='Klient', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ilosc_pozycji_zlec = models.IntegerField(db_column='Ilosc pozycji zlec')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_stan_field = models.CharField(db_column=' Stan ', max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'TechnolodzyPrototypy'


class Technologprowadzacy(models.Model):
    nr_zapytania = models.CharField(db_column='Nr Zapytania', max_length=1024, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    klient = models.CharField(db_column='Klient', max_length=20, blank=True, null=True)  # Field name made lowercase.
    zajetosc_godzinowa = models.IntegerField(db_column='Zajetosc Godzinowa')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    handlowiec = models.CharField(db_column='Handlowiec', max_length=255, blank=True, null=True)  # Field name made lowercase.
    obiecana_data_kalkulacji = models.DateTimeField(db_column='Obiecana Data Kalkulacji', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    status = models.CharField(db_column='Status', max_length=512, blank=True, null=True)  # Field name made lowercase.
    technolog_odpowiedzialny = models.CharField(db_column='Technolog Odpowiedzialny', max_length=512)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'TechnologProwadzacy'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Indeksyrekrusjaklient(models.Model):
    klient = models.CharField(max_length=100)
    kod_wg = models.CharField(max_length=100)
    kod_element = models.CharField(max_length=100)
    rid_wg = models.IntegerField()
    rid_element = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'indeksyRekrusjaKlient'


class Itmagazynbiedronka(models.Model):
    zlecenie = models.CharField(db_column='Zlecenie', max_length=50)  # Field name made lowercase.
    kod_surowca = models.CharField(db_column='Kod surowca', max_length=40, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ile = models.DecimalField(db_column='Ile', max_digits=18, decimal_places=6)  # Field name made lowercase.
    pozosta³o = models.DecimalField(db_column='Pozosta³o', max_digits=38, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    jedn = models.CharField(db_column='JEDN', max_length=50)  # Field name made lowercase.
    przewodnik = models.CharField(db_column='Przewodnik', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nrop = models.CharField(db_column='NrOp', max_length=5, blank=True, null=True)  # Field name made lowercase.
    nazwa_operacji = models.CharField(db_column='Nazwa operacji', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    maszyna = models.CharField(db_column='Maszyna', max_length=25, blank=True, null=True)  # Field name made lowercase.
    data_operacji = models.DateTimeField(db_column='Data operacji', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rodzaj = models.CharField(db_column='Rodzaj', max_length=50)  # Field name made lowercase.
    nazwa_opisowa = models.CharField(db_column='Nazwa opisowa', max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'itMagazynBiedronka'


class Itwidokharmonogramu(models.Model):
    gniazdo_nazwa = models.CharField(db_column='Gniazdo_nazwa', max_length=200, blank=True, null=True)  # Field name made lowercase.
    maszyna_numer = models.CharField(db_column='Maszyna_numer', max_length=25, blank=True, null=True)  # Field name made lowercase.
    maszyna_nazwa = models.CharField(db_column='Maszyna_nazwa', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kod_elementu = models.CharField(db_column='Kod_elementu', max_length=50)  # Field name made lowercase.
    nazwa_elementu = models.CharField(db_column='Nazwa_elementu', max_length=100)  # Field name made lowercase.
    numer_zamowienia = models.CharField(db_column='Numer_zamowienia', max_length=200, blank=True, null=True)  # Field name made lowercase.
    status_pozycji_zlecenia = models.CharField(db_column='Status_pozycji_zlecenia', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ilosc = models.DecimalField(db_column='Ilosc', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    numer_przewodnika = models.CharField(db_column='Numer_przewodnika', max_length=50)  # Field name made lowercase.
    numer_operacji = models.CharField(db_column='Numer_operacji', max_length=5)  # Field name made lowercase.
    nazwa_operacji = models.CharField(db_column='Nazwa_operacji', max_length=200)  # Field name made lowercase.
    data_rozpoczecia = models.DateTimeField(db_column='Data_rozpoczecia', blank=True, null=True)  # Field name made lowercase.
    data_zakonczenia = models.DateTimeField(db_column='Data_zakonczenia', blank=True, null=True)  # Field name made lowercase.
    gid_przewodnika1 = models.IntegerField(db_column='GID_przewodnika1')  # Field name made lowercase.
    gid_operacji = models.IntegerField(db_column='GID_operacji')  # Field name made lowercase.
    pacholek = models.BooleanField(blank=True, null=True)
    probaustawieniowa = models.BooleanField(db_column='ProbaUstawieniowa', blank=True, null=True)  # Field name made lowercase.
    customdeci3 = models.DecimalField(db_column='CustomDeci3', max_digits=18, decimal_places=9)  # Field name made lowercase.
    kod_materialu = models.CharField(db_column='Kod_materialu', max_length=50)  # Field name made lowercase.
    nazwa_materialu = models.CharField(db_column='Nazwa_materialu', max_length=100)  # Field name made lowercase.
    ilosc_materialu = models.DecimalField(db_column='Ilosc_materialu', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ilosc_zaokraglona = models.DecimalField(db_column='Ilosc_zaokraglona', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    jm = models.CharField(db_column='JM', max_length=50)  # Field name made lowercase.
    status_materialu = models.CharField(db_column='Status_materialu', max_length=50)  # Field name made lowercase.
    waga_materialu = models.DecimalField(db_column='Waga_materialu', max_digits=18, decimal_places=6)  # Field name made lowercase.
    gid_przewodnika2 = models.IntegerField(db_column='GID_przewodnika2', blank=True, null=True)  # Field name made lowercase.
    orbom_id = models.IntegerField(db_column='ORBom_id', blank=True, null=True)  # Field name made lowercase.
    rid = models.IntegerField(db_column='Rid', blank=True, null=True)  # Field name made lowercase.
    odpad = models.CharField(db_column='Odpad', max_length=5)  # Field name made lowercase.
    rewizja1 = models.CharField(max_length=25, blank=True, null=True)
    rewizja2 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'itWidokHarmonogramu'


class Itzadaniakonserwacji(models.Model):
    expr1 = models.CharField(db_column='Expr1', max_length=1)  # Field name made lowercase.
    expr2 = models.CharField(db_column='Expr2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    expr3 = models.CharField(db_column='Expr3', max_length=1)  # Field name made lowercase.
    expr4 = models.CharField(db_column='Expr4', max_length=1)  # Field name made lowercase.
    expr5 = models.CharField(db_column='Expr5', max_length=1)  # Field name made lowercase.
    komentarz = models.CharField(max_length=200, blank=True, null=True)
    expr6 = models.CharField(db_column='Expr6', max_length=1)  # Field name made lowercase.
    expr7 = models.IntegerField(db_column='Expr7')  # Field name made lowercase.
    expr8 = models.CharField(db_column='Expr8', max_length=1)  # Field name made lowercase.
    expr9 = models.CharField(db_column='Expr9', max_length=1)  # Field name made lowercase.
    expr10 = models.CharField(db_column='Expr10', max_length=1)  # Field name made lowercase.
    data_od = models.CharField(max_length=16, blank=True, null=True)
    data_do = models.CharField(max_length=16, blank=True, null=True)
    expr11 = models.IntegerField(db_column='Expr11')  # Field name made lowercase.
    expr12 = models.IntegerField(db_column='Expr12')  # Field name made lowercase.
    expr13 = models.CharField(db_column='Expr13', max_length=1)  # Field name made lowercase.
    expr14 = models.CharField(db_column='Expr14', max_length=1)  # Field name made lowercase.
    expr15 = models.IntegerField(db_column='Expr15')  # Field name made lowercase.
    expr16 = models.CharField(db_column='Expr16', max_length=1)  # Field name made lowercase.
    expr17 = models.CharField(db_column='Expr17', max_length=1)  # Field name made lowercase.
    expr18 = models.IntegerField(db_column='Expr18')  # Field name made lowercase.
    expr19 = models.IntegerField(db_column='Expr19')  # Field name made lowercase.
    expr20 = models.CharField(db_column='Expr20', max_length=1)  # Field name made lowercase.
    expr21 = models.CharField(db_column='Expr21', max_length=1)  # Field name made lowercase.
    expr22 = models.IntegerField(db_column='Expr22')  # Field name made lowercase.
    expr23 = models.IntegerField(db_column='Expr23')  # Field name made lowercase.
    expr24 = models.IntegerField(db_column='Expr24')  # Field name made lowercase.
    expr25 = models.IntegerField(db_column='Expr25')  # Field name made lowercase.
    expr26 = models.CharField(db_column='Expr26', max_length=1)  # Field name made lowercase.
    expr27 = models.CharField(db_column='Expr27', max_length=1)  # Field name made lowercase.
    expr28 = models.CharField(db_column='Expr28', max_length=1)  # Field name made lowercase.
    expr29 = models.IntegerField(db_column='Expr29')  # Field name made lowercase.
    expr30 = models.IntegerField(db_column='Expr30')  # Field name made lowercase.
    expr31 = models.IntegerField(db_column='Expr31')  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'itZadaniaKonserwacji'


class Itzadaniapodstawowe(models.Model):
    gniazdo_nazwa = models.CharField(db_column='Gniazdo_nazwa', max_length=200, blank=True, null=True)  # Field name made lowercase.
    maszyna_numer = models.CharField(db_column='Maszyna_numer', max_length=25, blank=True, null=True)  # Field name made lowercase.
    maszyna_nazwa = models.CharField(db_column='Maszyna_nazwa', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kod_elementu = models.CharField(db_column='Kod_elementu', max_length=50)  # Field name made lowercase.
    nazwa_elementu = models.CharField(db_column='Nazwa_elementu', max_length=100)  # Field name made lowercase.
    numer_zamowienia = models.CharField(db_column='Numer_zamowienia', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status_pozycji_zlecenia = models.CharField(db_column='Status_pozycji_zlecenia', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ilosc = models.DecimalField(db_column='Ilosc', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    numer_przewodnika = models.CharField(db_column='Numer_przewodnika', max_length=50)  # Field name made lowercase.
    numer_operacji = models.CharField(db_column='Numer_operacji', max_length=5)  # Field name made lowercase.
    nazwa_operacji = models.CharField(db_column='Nazwa_operacji', max_length=200)  # Field name made lowercase.
    data_rozpoczecia = models.CharField(db_column='Data_rozpoczecia', max_length=16, blank=True, null=True)  # Field name made lowercase.
    data_zakonczenia = models.CharField(db_column='Data_zakonczenia', max_length=16, blank=True, null=True)  # Field name made lowercase.
    gid_przewodnika1 = models.IntegerField(db_column='GID_przewodnika1')  # Field name made lowercase.
    gid_operacji = models.IntegerField(db_column='GID_operacji')  # Field name made lowercase.
    pacholek = models.BooleanField(blank=True, null=True)
    probaustawieniowa = models.BooleanField(db_column='ProbaUstawieniowa', blank=True, null=True)  # Field name made lowercase.
    customdeci3 = models.DecimalField(db_column='CustomDeci3', max_digits=18, decimal_places=9)  # Field name made lowercase.
    kod_materialu = models.CharField(db_column='Kod_materialu', max_length=50)  # Field name made lowercase.
    nazwa_materialu = models.CharField(db_column='Nazwa_materialu', max_length=100)  # Field name made lowercase.
    ilosc_materialu = models.DecimalField(db_column='Ilosc_materialu', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ilosc_zaokraglona = models.DecimalField(db_column='Ilosc_zaokraglona', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    jm = models.CharField(db_column='JM', max_length=50)  # Field name made lowercase.
    status_materialu = models.CharField(db_column='Status_materialu', max_length=50)  # Field name made lowercase.
    waga_materialu = models.DecimalField(db_column='Waga_materialu', max_digits=18, decimal_places=6)  # Field name made lowercase.
    gid_przewodnika2 = models.IntegerField(db_column='GID_przewodnika2', blank=True, null=True)  # Field name made lowercase.
    orbom_id = models.IntegerField(db_column='ORBom_id', blank=True, null=True)  # Field name made lowercase.
    rid = models.IntegerField(db_column='Rid', blank=True, null=True)  # Field name made lowercase.
    odpad = models.CharField(db_column='Odpad', max_length=5)  # Field name made lowercase.
    rewizja1 = models.CharField(max_length=25, blank=True, null=True)
    rewizja2 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'itZadaniaPodstawowe'


class Itzadaniapostep(models.Model):
    o_idoperacji = models.IntegerField(db_column='O_IdOperacji', blank=True, null=True)  # Field name made lowercase.
    o_iloscwyprodukowanadobrych = models.DecimalField(db_column='O_IloscWyprodukowanaDobrych', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    o_iloscwyprodukowanybrakow = models.DecimalField(db_column='O_IloscWyprodukowanyBrakow', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'itZadaniaPostep'


class ItBomoperacje(models.Model):
    o_kodoperaps = models.TextField(db_column='O_KodOperAPS', blank=True, null=True)  # Field name made lowercase.
    o_idzlecenia = models.IntegerField(db_column='O_IdZlecenia', blank=True, null=True)  # Field name made lowercase.
    o_datarozpoczêcia = models.DateTimeField(db_column='O_DataRozpoczêcia', blank=True, null=True)  # Field name made lowercase.
    o_orbomid = models.IntegerField(db_column='O_ORBomId', blank=True, null=True)  # Field name made lowercase.
    o_indeksmat = models.CharField(db_column='O_IndeksMat', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'it_BOMOperacje'


class ItEtykiety(models.Model):
    kod = models.CharField(db_column='Kod', max_length=280, blank=True, null=True)  # Field name made lowercase.
    komentarz = models.CharField(db_column='Komentarz', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    operacja = models.CharField(db_column='Operacja', max_length=280, blank=True, null=True)  # Field name made lowercase.
    instrukcjauzycia = models.CharField(db_column='InstrukcjaUzycia', max_length=1)  # Field name made lowercase.
    kolortla = models.CharField(db_column='KolorTla', max_length=16)  # Field name made lowercase.
    kolorobramowania = models.CharField(db_column='KolorObramowania', max_length=16)  # Field name made lowercase.
    szerokoscprostok¹ta = models.IntegerField(db_column='SzerokoscProstok¹ta')  # Field name made lowercase.
    zrodlo = models.CharField(db_column='Zrodlo', max_length=11)  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'it_Etykiety'


class ItKonserwacjeprzeglady(models.Model):
    zasob = models.CharField(db_column='Zasob', max_length=20, blank=True, null=True)  # Field name made lowercase.
    datarozpoczecia = models.DateTimeField(db_column='DataRozpoczecia', blank=True, null=True)  # Field name made lowercase.
    datazakonczenia = models.DateTimeField(db_column='DataZakonczenia', blank=True, null=True)  # Field name made lowercase.
    wyswietlanytekst = models.CharField(db_column='WyswietlanyTekst', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dostepnailosczasobow = models.IntegerField(db_column='DostepnaIloscZasobow', blank=True, null=True)  # Field name made lowercase.
    kod = models.CharField(db_column='Kod', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'it_KonserwacjePrzeglady'


class ItKorektakalendarza(models.Model):
    zasob = models.CharField(max_length=100, blank=True, null=True)
    data_od = models.DateTimeField(blank=True, null=True)
    data_do = models.DateTimeField(blank=True, null=True)
    komentarz = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'it_KorektaKalendarza'


class ItOperacje(models.Model):
    o_kodoperaps = models.TextField(db_column='O_KodOperAPS', blank=True, null=True)  # Field name made lowercase.
    o_nrzamsprzed = models.CharField(db_column='O_NrZamSprzed', max_length=100, blank=True, null=True)  # Field name made lowercase.
    o_nrzlecpord = models.CharField(db_column='O_NrZlecPord', max_length=100, blank=True, null=True)  # Field name made lowercase.
    o_indeks = models.CharField(db_column='O_Indeks', max_length=100, blank=True, null=True)  # Field name made lowercase.
    o_iloscprod = models.DecimalField(db_column='O_IloscProd', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    o_idpozzlecprod = models.IntegerField(db_column='O_IdPozZlecprod', blank=True, null=True)  # Field name made lowercase.
    o_idzlecenia = models.IntegerField(db_column='O_IdZlecenia', blank=True, null=True)  # Field name made lowercase.
    o_datarozpoczêcia = models.DateTimeField(db_column='O_DataRozpoczêcia', blank=True, null=True)  # Field name made lowercase.
    o_datazakovczenia = models.DateTimeField(db_column='O_DataZakovczenia', blank=True, null=True)  # Field name made lowercase.
    o_idzasobu = models.IntegerField(db_column='O_IdZasobu', blank=True, null=True)  # Field name made lowercase.
    o_zasobglowny = models.CharField(db_column='O_ZasobGlowny', max_length=100, blank=True, null=True)  # Field name made lowercase.
    o_nazwazasobu = models.CharField(db_column='O_NazwaZasobu', max_length=100, blank=True, null=True)  # Field name made lowercase.
    o_flagazamrozenia = models.IntegerField(db_column='O_FlagaZamrozenia', blank=True, null=True)  # Field name made lowercase.
    o_idoperacji = models.IntegerField(db_column='O_IdOperacji', blank=True, null=True)  # Field name made lowercase.
    o_idprzewodnika = models.IntegerField(db_column='O_IdPrzewodnika', blank=True, null=True)  # Field name made lowercase.
    o_czasproduckcji = models.DecimalField(db_column='O_CzasProduckcji', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    o_czasprzezbrojenia = models.DecimalField(db_column='O_CzasPrzezbrojenia', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    o_czasjednostkowy = models.DecimalField(db_column='O_CzasJednostkowy', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    o_idzasobuwoperacji = models.IntegerField(db_column='O_IdZasobuWOperacji', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'it_Operacje'


class ItOperacjezobectech(models.Model):
    operacja = models.CharField(db_column='Operacja', max_length=100, blank=True, null=True)  # Field name made lowercase.
    komentarz = models.CharField(db_column='Komentarz', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'it_OperacjeZObecTech'


class ItOperacjezasoby(models.Model):
    o_kodoperaps = models.CharField(db_column='O_KodOperAPS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    o_zasob = models.CharField(db_column='O_Zasob', max_length=100, blank=True, null=True)  # Field name made lowercase.
    o_zasobnazwa = models.CharField(db_column='O_ZasobNazwa', max_length=100, blank=True, null=True)  # Field name made lowercase.
    o_idoperacji = models.IntegerField(db_column='O_IdOperacji', blank=True, null=True)  # Field name made lowercase.
    o_idzasobu = models.IntegerField(db_column='O_IdZasobu', blank=True, null=True)  # Field name made lowercase.
    o_idzasobuwoperacji = models.IntegerField(db_column='O_IdZasobuWOperacji', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'it_OperacjeZasoby'


class ItPostepprodukcji(models.Model):
    o_idoperacji = models.IntegerField(db_column='O_IdOperacji', blank=True, null=True)  # Field name made lowercase.
    o_kodzasobu = models.CharField(db_column='O_KodZasobu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    o_rdata_rozpoczecia = models.DateTimeField(db_column='O_RData_rozpoczecia', blank=True, null=True)  # Field name made lowercase.
    o_rdata_zakonczenia = models.DateTimeField(db_column='O_RData_zakonczenia', blank=True, null=True)  # Field name made lowercase.
    o_iloscwyprodukowanadobrych = models.DecimalField(db_column='O_IloscWyprodukowanaDobrych', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    o_iloscwyprodukowanybrakow = models.DecimalField(db_column='O_IloscWyprodukowanyBrakow', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    o_statusprzewodnika = models.CharField(db_column='O_StatusPrzewodnika', max_length=1, blank=True, null=True)  # Field name made lowercase.
    o_nazwastatusuprzewodnika = models.CharField(db_column='O_NazwaStatusuPrzewodnika', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'it_PostepProdukcji'


class ItPozycje(models.Model):
    p_twrgidnr = models.IntegerField(db_column='P_TwrGidNr', blank=True, null=True)  # Field name made lowercase.
    p_twrkod = models.CharField(db_column='P_TwrKod', max_length=50, blank=True, null=True)  # Field name made lowercase.
    p_twrnazwa = models.CharField(db_column='P_TwrNazwa', max_length=100, blank=True, null=True)  # Field name made lowercase.
    p_icodeid = models.CharField(db_column='P_ICodeID', max_length=1, blank=True, null=True)  # Field name made lowercase.
    p_grupytowarow = models.CharField(db_column='P_GrupyTowarow', max_length=255, blank=True, null=True)  # Field name made lowercase.
    p_priorytetpozycji = models.DecimalField(db_column='P_PriorytetPozycji', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    p_twcwartosc = models.DecimalField(db_column='P_TwcWartosc', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    p_czasdostawy = models.CharField(db_column='P_CzasDostawy', max_length=11, blank=True, null=True)  # Field name made lowercase.
    p_zapasminimalny = models.DecimalField(db_column='P_ZapasMinimalny', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    p_zapasmaksymalny = models.DecimalField(db_column='P_ZapasMaksymalny', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    p_partiazakupmin = models.IntegerField(db_column='P_PartiaZakupMin', blank=True, null=True)  # Field name made lowercase.
    p_partiazakupmax = models.IntegerField(db_column='P_PartiaZakupMax', blank=True, null=True)  # Field name made lowercase.
    p_specyfikacjetxt001 = models.CharField(db_column='P_SpecyfikacjeTxt001', max_length=50, blank=True, null=True)  # Field name made lowercase.
    p_specyfikacjenum001 = models.DecimalField(db_column='P_SpecyfikacjeNum001', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    p_uwagi = models.CharField(db_column='P_Uwagi', max_length=200, blank=True, null=True)  # Field name made lowercase.
    p_jednostkamiary = models.CharField(db_column='P_JednostkaMiary', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rodzaj = models.IntegerField(db_column='Rodzaj', blank=True, null=True)  # Field name made lowercase.
    grubosc = models.CharField(db_column='Grubosc', max_length=5, blank=True, null=True)  # Field name made lowercase.
    szerokosc = models.IntegerField(db_column='Szerokosc', blank=True, null=True)  # Field name made lowercase.
    dlugosc = models.IntegerField(db_column='Dlugosc', blank=True, null=True)  # Field name made lowercase.
    cecha = models.CharField(db_column='Cecha', max_length=200, blank=True, null=True)  # Field name made lowercase.
    indeksfarby = models.CharField(db_column='IndeksFarby', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kolor = models.CharField(db_column='Kolor', max_length=50, blank=True, null=True)  # Field name made lowercase.
    obecnosctechnologa = models.CharField(db_column='ObecnoscTechnologa', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'it_Pozycje'


class ItPrototypy(models.Model):
    pozycja = models.CharField(max_length=100, blank=True, null=True)
    selektor_technologii = models.CharField(max_length=100, blank=True, null=True)
    numer_operacji = models.IntegerField(blank=True, null=True)
    kod_procesu = models.CharField(max_length=100, blank=True, null=True)
    rodzaj_instrukcji = models.CharField(max_length=10, blank=True, null=True)
    kod_instrukcji = models.CharField(max_length=10, blank=True, null=True)
    zasob_pozycja = models.CharField(max_length=100, blank=True, null=True)
    produkcja = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'it_Prototypy'


class ItPrzebiegczasowy(models.Model):
    zasob = models.CharField(max_length=100, blank=True, null=True)
    kod_operacji = models.CharField(max_length=100, blank=True, null=True)
    typ1 = models.CharField(max_length=100, blank=True, null=True)
    typ2 = models.CharField(max_length=100, blank=True, null=True)
    czas = models.DateTimeField(blank=True, null=True)
    id_zasobu = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'it_PrzebiegCzasowy'


class ItStanmagazynowy(models.Model):
    numerzamówienia = models.CharField(db_column='NumerZamówienia', max_length=55, blank=True, null=True)  # Field name made lowercase.
    o_twrkod = models.CharField(db_column='O_TwrKod', max_length=50, blank=True, null=True)  # Field name made lowercase.
    o_wielkosczapasu = models.DecimalField(db_column='O_WielkoscZapasu', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'it_StanMagazynowy'


class ItStanmagazynowyZp(models.Model):
    numerzamówienia = models.CharField(db_column='NumerZamówienia', max_length=55, blank=True, null=True)  # Field name made lowercase.
    o_twrkod = models.CharField(db_column='O_TwrKod', max_length=50, blank=True, null=True)  # Field name made lowercase.
    o_wielkosczapasu = models.DecimalField(db_column='O_WielkoscZapasu', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'it_StanMagazynowy_ZP'


class ItTechnologia(models.Model):
    m_twrkod = models.CharField(db_column='M_TwrKod', max_length=255, blank=True, null=True)  # Field name made lowercase.
    m_selektor = models.CharField(db_column='M_Selektor', max_length=92, blank=True, null=True)  # Field name made lowercase.
    m_numeroperacji = models.IntegerField(db_column='M_NumerOperacji', blank=True, null=True)  # Field name made lowercase.
    m_kodprocesu = models.CharField(db_column='M_KodProcesu', max_length=255, blank=True, null=True)  # Field name made lowercase.
    typ_instrukcji = models.CharField(db_column='TYP_instrukcji', max_length=1)  # Field name made lowercase.
    m_kodinstrukcji = models.CharField(db_column='M_KodInstrukcji', max_length=255, blank=True, null=True)  # Field name made lowercase.
    m_zasob_pozycja = models.CharField(db_column='M_Zasob_Pozycja', max_length=306, blank=True, null=True)  # Field name made lowercase.
    m_numerpoprzedniejoper = models.IntegerField(db_column='M_NumerPoprzedniejOper', blank=True, null=True)  # Field name made lowercase.
    przezbrojenie = models.CharField(db_column='Przezbrojenie', max_length=255, blank=True, null=True)  # Field name made lowercase.
    produkcja = models.CharField(db_column='Produkcja', max_length=255, blank=True, null=True)  # Field name made lowercase.
    m_idpozycjizlecprodukcyjnego = models.IntegerField(db_column='M_IdPozycjiZlecProdukcyjnego', blank=True, null=True)  # Field name made lowercase.
    m_orbomid = models.IntegerField(db_column='M_OrBomID', blank=True, null=True)  # Field name made lowercase.
    m_parentbomid = models.IntegerField(db_column='M_ParentBomID', blank=True, null=True)  # Field name made lowercase.
    m_iloscnarw = models.DecimalField(db_column='M_IloscNaRW', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    m_polepowierzchni = models.DecimalField(db_column='M_PolePowierzchni', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    m_idprzewodnika = models.IntegerField(db_column='M_IdPrzewodnika', blank=True, null=True)  # Field name made lowercase.
    m_idoperacji = models.IntegerField(db_column='M_IdOperacji', blank=True, null=True)  # Field name made lowercase.
    m_idzasobuwoperacji = models.IntegerField(db_column='M_IdZasobuWOperacji', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'it_Technologia'


class ItTechnologiaaps(models.Model):
    m_twrkod = models.TextField(db_column='M_TwrKod', blank=True, null=True)  # Field name made lowercase.
    m_selektor = models.TextField(db_column='M_Selektor', blank=True, null=True)  # Field name made lowercase.
    m_numeroperacji = models.IntegerField(db_column='M_NumerOperacji', blank=True, null=True)  # Field name made lowercase.
    m_kodprocesu = models.TextField(db_column='M_KodProcesu', blank=True, null=True)  # Field name made lowercase.
    typ_instrukcji = models.CharField(db_column='TYP_instrukcji', max_length=100, blank=True, null=True)  # Field name made lowercase.
    m_kodinstrukcji = models.CharField(db_column='M_KodInstrukcji', max_length=100, blank=True, null=True)  # Field name made lowercase.
    m_zasob_pozycja = models.TextField(db_column='M_Zasob_Pozycja', blank=True, null=True)  # Field name made lowercase.
    m_numerpoprzedniejoper = models.IntegerField(db_column='M_NumerPoprzedniejOper', blank=True, null=True)  # Field name made lowercase.
    przezbrojenie = models.TextField(db_column='Przezbrojenie', blank=True, null=True)  # Field name made lowercase.
    produkcja = models.TextField(db_column='Produkcja', blank=True, null=True)  # Field name made lowercase.
    m_idpozycjizlecprodukcyjnego = models.IntegerField(db_column='M_IdPozycjiZlecProdukcyjnego', blank=True, null=True)  # Field name made lowercase.
    m_orbomid = models.IntegerField(db_column='M_OrBomID', blank=True, null=True)  # Field name made lowercase.
    m_parentbomid = models.IntegerField(db_column='M_ParentBomID', blank=True, null=True)  # Field name made lowercase.
    m_iloscnarw = models.DecimalField(db_column='M_IloscNaRW', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    m_polepowierzchni = models.DecimalField(db_column='M_PolePowierzchni', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    m_idprzewodnika = models.IntegerField(db_column='M_IdPrzewodnika', blank=True, null=True)  # Field name made lowercase.
    m_idoperacji = models.IntegerField(db_column='M_IdOperacji', blank=True, null=True)  # Field name made lowercase.
    m_nr_zlec_sprzed = models.CharField(db_column='M_Nr_zlec_sprzed', max_length=100, blank=True, null=True)  # Field name made lowercase.
    m_idzasobuwoperacji = models.IntegerField(db_column='M_IdZasobuWOperacji', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'it_TechnologiaAPS'


class ItTechnologiaprototypy(models.Model):
    pozycja = models.CharField(max_length=100, blank=True, null=True)
    selektor_technologii = models.CharField(max_length=100, blank=True, null=True)
    numer_operacji = models.IntegerField(blank=True, null=True)
    kod_procesu = models.CharField(max_length=100, blank=True, null=True)
    rodzaj_instrukcji = models.CharField(max_length=10, blank=True, null=True)
    kod_instrukcji = models.CharField(max_length=10, blank=True, null=True)
    zasob_pozycja = models.CharField(max_length=100, blank=True, null=True)
    produkcja = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'it_TechnologiaPrototypy'


class ItTechnologiaV3(models.Model):
    m_twrkod = models.TextField(db_column='M_TwrKod', blank=True, null=True)  # Field name made lowercase.
    m_selektor = models.TextField(db_column='M_Selektor', blank=True, null=True)  # Field name made lowercase.
    m_numeroperacji = models.IntegerField(db_column='M_NumerOperacji', blank=True, null=True)  # Field name made lowercase.
    m_kodprocesu = models.CharField(db_column='M_KodProcesu', max_length=107, blank=True, null=True)  # Field name made lowercase.
    typ_instrukcji = models.CharField(db_column='TYP_instrukcji', max_length=100, blank=True, null=True)  # Field name made lowercase.
    m_kodinstrukcji = models.CharField(db_column='M_KodInstrukcji', max_length=255, blank=True, null=True)  # Field name made lowercase.
    m_zasob_pozycja = models.TextField(db_column='M_Zasob_Pozycja', blank=True, null=True)  # Field name made lowercase.
    m_numerpoprzedniejoper = models.IntegerField(db_column='M_NumerPoprzedniejOper', blank=True, null=True)  # Field name made lowercase.
    przezbrojenie = models.TextField(db_column='Przezbrojenie', blank=True, null=True)  # Field name made lowercase.
    produkcja = models.TextField(db_column='Produkcja', blank=True, null=True)  # Field name made lowercase.
    m_idpozycjizlecprodukcyjnego = models.IntegerField(db_column='M_IdPozycjiZlecProdukcyjnego', blank=True, null=True)  # Field name made lowercase.
    m_orbomid = models.IntegerField(db_column='M_OrBomID', blank=True, null=True)  # Field name made lowercase.
    m_parentbomid = models.IntegerField(db_column='M_ParentBomID', blank=True, null=True)  # Field name made lowercase.
    m_iloscnarw = models.DecimalField(db_column='M_IloscNaRW', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    m_polepowierzchni = models.DecimalField(db_column='M_PolePowierzchni', max_digits=19, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    m_idprzewodnika = models.IntegerField(db_column='M_IdPrzewodnika', blank=True, null=True)  # Field name made lowercase.
    m_idoperacji = models.IntegerField(db_column='M_IdOperacji', blank=True, null=True)  # Field name made lowercase.
    m_nr_zlec_sprzed = models.CharField(db_column='M_Nr_zlec_sprzed', max_length=276, blank=True, null=True)  # Field name made lowercase.
    m_idzasobuwoperacji = models.IntegerField(db_column='M_IdZasobuWOperacji', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'it_Technologia_v3'


class ItUruchomwyznaczkonserwacje(models.Model):
    kod = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'it_UruchomWyznaczKonserwacje'


class ItUruchomzasileniemonaco(models.Model):
    kod = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'it_UruchomZasilenieMONACO'


class ItUruchomzasileniepostepuprodukcji(models.Model):
    kod = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'it_UruchomZasileniePostepuProdukcji'


class ItUruchomzasilenietabel(models.Model):
    kod = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'it_UruchomZasilenieTabel'


class ItZamowieniadaty(models.Model):
    z_idzlecsprzed = models.IntegerField(db_column='Z_IdZlecSprzed', blank=True, null=True)  # Field name made lowercase.
    z_idpozzlecsprzed = models.IntegerField(db_column='Z_IdPozZlecSprzed', blank=True, null=True)  # Field name made lowercase.
    z_idzlecprod = models.IntegerField(db_column='Z_IdZlecProd', blank=True, null=True)  # Field name made lowercase.
    z_nr_zamaps = models.CharField(db_column='Z_Nr_ZamAPS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    z_warianttechnologii = models.CharField(db_column='Z_WariantTechnologii', max_length=100, blank=True, null=True)  # Field name made lowercase.
    z_nr_zlecprod = models.CharField(db_column='Z_Nr_ZlecProd', max_length=100, blank=True, null=True)  # Field name made lowercase.
    z_klient = models.CharField(db_column='Z_Klient', max_length=100, blank=True, null=True)  # Field name made lowercase.
    z_pozycja = models.CharField(db_column='Z_Pozycja', max_length=100, blank=True, null=True)  # Field name made lowercase.
    z_ilosc = models.DecimalField(db_column='Z_Ilosc', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    z_statuszlecwmonaco = models.CharField(db_column='Z_StatusZlecWMonaco', max_length=100, blank=True, null=True)  # Field name made lowercase.
    z_statusplanowania = models.CharField(db_column='Z_StatusPlanowania', max_length=100, blank=True, null=True)  # Field name made lowercase.
    z_let = models.DateField(db_column='Z_Let', blank=True, null=True)  # Field name made lowercase.
    z_letcdn = models.DateField(db_column='Z_LetCDN', blank=True, null=True)  # Field name made lowercase.
    z_est = models.DateField(db_column='Z_EST', blank=True, null=True)  # Field name made lowercase.
    z_potwdatazprodukcji = models.DateField(db_column='Z_PotwDataZProdukcji', blank=True, null=True)  # Field name made lowercase.
    z_opoznionadatazprodukcji = models.DateField(db_column='Z_OpoznionaDataZProdukcji', blank=True, null=True)  # Field name made lowercase.
    z_idpozzlecprod = models.IntegerField(db_column='Z_IdPozZlecProd', blank=True, null=True)  # Field name made lowercase.
    z_letczas = models.DateTimeField(db_column='Z_LetCzas', blank=True, null=True)  # Field name made lowercase.
    z_komentarz = models.TextField(db_column='Z_Komentarz', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'it_ZamowieniaDaty'


class ItZamowieniadodostawcow(models.Model):
    numerzamowienia = models.CharField(db_column='NumerZamowienia', max_length=276, blank=True, null=True)  # Field name made lowercase.
    o_lppozycji = models.IntegerField(db_column='O_LpPozycji', blank=True, null=True)  # Field name made lowercase.
    o_kodkontrahenta = models.CharField(db_column='O_KodKontrahenta', max_length=50, blank=True, null=True)  # Field name made lowercase.
    o_twrgidnr = models.IntegerField(db_column='O_TwrGidNr', blank=True, null=True)  # Field name made lowercase.
    o_twrkod = models.CharField(db_column='O_TwrKod', max_length=50, blank=True, null=True)  # Field name made lowercase.
    o_ilosczamowiona = models.DecimalField(db_column='O_IloscZamowiona', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    o_data = models.DateTimeField(db_column='O_Data', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'it_ZamowieniaDoDostawcow'


class ItZamowieniasprzedazy(models.Model):
    o_idzlecsprzedazy = models.IntegerField(db_column='O_IdZlecSprzedazy', blank=True, null=True)  # Field name made lowercase.
    o_numerzlecsprzedazy = models.CharField(db_column='O_NumerZlecSprzedazy', max_length=71, blank=True, null=True)  # Field name made lowercase.
    o_numerzlecprodukcyjnego = models.CharField(db_column='O_NumerZlecProdukcyjnego', max_length=8)  # Field name made lowercase.
    o_kodkontrahenta = models.CharField(db_column='O_KodKontrahenta', max_length=50, blank=True, null=True)  # Field name made lowercase.
    o_twrgidnr = models.IntegerField(db_column='O_TwrGidNr', blank=True, null=True)  # Field name made lowercase.
    o_twrkod = models.CharField(db_column='O_TwrKod', max_length=50, blank=True, null=True)  # Field name made lowercase.
    o_ilosczamowiona = models.DecimalField(db_column='O_IloscZamowiona', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    o_datarealizacjipozadana = models.DateTimeField(db_column='O_DataRealizacjiPozadana', blank=True, null=True)  # Field name made lowercase.
    o_jestzlecenieprodukcyjne = models.IntegerField(db_column='O_JestZlecenieProdukcyjne', blank=True, null=True)  # Field name made lowercase.
    o_typzlecenia = models.CharField(db_column='O_TypZlecenia', max_length=1, blank=True, null=True)  # Field name made lowercase.
    warianttechnologii = models.CharField(db_column='WariantTechnologii', max_length=8)  # Field name made lowercase.
    status_zlecenia = models.CharField(db_column='Status_zlecenia', max_length=13)  # Field name made lowercase.
    o_idpozycjizlecsprzedazy = models.IntegerField(db_column='O_IdPozycjiZlecSprzedazy', blank=True, null=True)  # Field name made lowercase.
    o_numerukontrahenta = models.CharField(db_column='O_NumerUKontrahenta', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'it_ZamowieniaSprzedazy'


class ItZamowieniazaplanowane(models.Model):
    nr_zamowienia = models.CharField(max_length=100, blank=True, null=True)
    wariant_technologii = models.CharField(max_length=100, blank=True, null=True)
    status_planowania = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'it_ZamowieniaZaplanowane'


class ItZasoby(models.Model):
    r_idzasobu = models.IntegerField(db_column='R_IDZasobu', blank=True, null=True)  # Field name made lowercase.
    r_kodzasobu = models.CharField(db_column='R_KodZasobu', max_length=100, blank=True, null=True)  # Field name made lowercase.
    r_nazwazasobu = models.CharField(db_column='R_NazwaZasobu', max_length=100, blank=True, null=True)  # Field name made lowercase.
    r_wydzial = models.CharField(db_column='R_Wydzial', max_length=100, blank=True, null=True)  # Field name made lowercase.
    r_gniazdo = models.CharField(db_column='R_Gniazdo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    r_typowaoperacja = models.CharField(db_column='R_TypowaOperacja', max_length=100, blank=True, null=True)  # Field name made lowercase.
    r_grupazasobu = models.CharField(db_column='R_GrupaZasobu', max_length=100, blank=True, null=True)  # Field name made lowercase.
    r_kosztroboczogodziny = models.DecimalField(db_column='R_KosztRoboczogodziny', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    r_awaria = models.CharField(db_column='R_Awaria', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'it_Zasoby'


class ItZasobyparamprzegl(models.Model):
    zasob = models.CharField(db_column='Zasob', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kstart = models.IntegerField(db_column='KStart', blank=True, null=True)  # Field name made lowercase.
    kstop = models.IntegerField(db_column='KStop', blank=True, null=True)  # Field name made lowercase.
    kdzien = models.CharField(db_column='KDzien', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kdatado = models.DateTimeField(db_column='KDataDo', blank=True, null=True)  # Field name made lowercase.
    pstart = models.IntegerField(db_column='PStart', blank=True, null=True)  # Field name made lowercase.
    pstop = models.IntegerField(db_column='PStop', blank=True, null=True)  # Field name made lowercase.
    pdzien = models.IntegerField(db_column='PDzien', blank=True, null=True)  # Field name made lowercase.
    pdatado = models.DateTimeField(db_column='PDataDo', blank=True, null=True)  # Field name made lowercase.
    genp = models.CharField(db_column='GenP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    genk = models.CharField(db_column='GenK', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'it_ZasobyParamPrzegl'


class ItZleceniaprodukcyjne(models.Model):
    o_idzlecsprzedazy = models.IntegerField(db_column='O_IdZlecSprzedazy', blank=True, null=True)  # Field name made lowercase.
    o_numerzlecsprzedazy = models.CharField(db_column='O_NumerZlecSprzedazy', max_length=276, blank=True, null=True)  # Field name made lowercase.
    o_nrzlecprod = models.CharField(db_column='O_NrZlecProd', max_length=71, blank=True, null=True)  # Field name made lowercase.
    o_kodkontrahenta = models.CharField(db_column='O_KodKontrahenta', max_length=50, blank=True, null=True)  # Field name made lowercase.
    o_twrgidnr = models.IntegerField(db_column='O_TwrGidNr', blank=True, null=True)  # Field name made lowercase.
    o_twrkod = models.CharField(db_column='O_TwrKod', max_length=50, blank=True, null=True)  # Field name made lowercase.
    o_iloscdoprodukcji = models.DecimalField(db_column='O_IloscDoProdukcji', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    o_datarealizacjipozadana = models.DateTimeField(db_column='O_DataRealizacjiPozadana', blank=True, null=True)  # Field name made lowercase.
    o_idzlecprodukcyjnego = models.IntegerField(db_column='O_IdZlecProdukcyjnego', blank=True, null=True)  # Field name made lowercase.
    warainttechnologii = models.CharField(db_column='WaraintTechnologii', max_length=92, blank=True, null=True)  # Field name made lowercase.
    o_statuszlecprodmonaco = models.CharField(db_column='O_StatusZlecProdMonaco', max_length=50, blank=True, null=True)  # Field name made lowercase.
    o_idpozycjizlecsprzedazy = models.IntegerField(db_column='O_IdPozycjiZlecSprzedazy', blank=True, null=True)  # Field name made lowercase.
    o_idpozzlecprod = models.IntegerField(db_column='O_IdPozZlecProd', blank=True, null=True)  # Field name made lowercase.
    o_iloscnapw = models.DecimalField(db_column='O_IloscNaPW', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    o_datawysylki = models.DateTimeField(db_column='O_DataWysylki', blank=True, null=True)  # Field name made lowercase.
    o_numerukontrahenta = models.CharField(db_column='O_NumerUKontrahenta', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'it_ZleceniaProdukcyjne'


class Monacostartstop(models.Model):
    pracownik = models.CharField(db_column='Pracownik', max_length=100)  # Field name made lowercase.
    pochodzenierejestracji = models.CharField(db_column='PochodzenieRejestracji', max_length=50)  # Field name made lowercase.
    czas = models.DecimalField(db_column='Czas', max_digits=18, decimal_places=2)  # Field name made lowercase.
    dzien = models.IntegerField(db_column='Dzien')  # Field name made lowercase.
    miesiac = models.IntegerField(db_column='Miesiac')  # Field name made lowercase.
    rok = models.IntegerField(db_column='Rok')  # Field name made lowercase.
    start = models.DateTimeField(db_column='Start')  # Field name made lowercase.
    stop = models.DateTimeField(db_column='Stop')  # Field name made lowercase.
    kodelementuwiadacego = models.CharField(db_column='KodElementuWiadacego', max_length=100)  # Field name made lowercase.
    kodelementu = models.CharField(db_column='KodElementu', max_length=100)  # Field name made lowercase.
    ilosc = models.DecimalField(db_column='Ilosc', max_digits=18, decimal_places=0)  # Field name made lowercase.
    iloscsuma = models.DecimalField(db_column='IloscSuma', max_digits=18, decimal_places=0)  # Field name made lowercase.
    zlecenie = models.CharField(db_column='Zlecenie', max_length=50)  # Field name made lowercase.
    przewodnik = models.CharField(db_column='Przewodnik', max_length=50)  # Field name made lowercase.
    numeroperacji = models.CharField(db_column='NumerOperacji', max_length=50)  # Field name made lowercase.
    nazwaoperacji = models.CharField(db_column='NazwaOperacji', max_length=50)  # Field name made lowercase.
    notatka = models.TextField(db_column='Notatka')  # Field name made lowercase.
    zmiana = models.CharField(db_column='Zmiana', max_length=50)  # Field name made lowercase.
    zasobkod = models.CharField(db_column='ZasobKod', max_length=50)  # Field name made lowercase.
    zasobnazwa = models.CharField(db_column='ZasobNazwa', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'monacoStartStop'


class Monacostartstopluki(models.Model):
    id = models.IntegerField(blank=True, null=True)
    pracownik = models.CharField(db_column='Pracownik', max_length=100)  # Field name made lowercase.
    pochodzenierejestracji = models.CharField(db_column='PochodzenieRejestracji', max_length=50)  # Field name made lowercase.
    czas = models.DecimalField(db_column='Czas', max_digits=18, decimal_places=2)  # Field name made lowercase.
    dzien = models.IntegerField(db_column='Dzien')  # Field name made lowercase.
    miesiac = models.IntegerField(db_column='Miesiac')  # Field name made lowercase.
    rok = models.IntegerField(db_column='Rok')  # Field name made lowercase.
    start = models.DateTimeField(db_column='Start')  # Field name made lowercase.
    stop = models.DateTimeField(db_column='Stop')  # Field name made lowercase.
    kodelementuwiadacego = models.CharField(db_column='KodElementuWiadacego', max_length=100)  # Field name made lowercase.
    kodelementu = models.CharField(db_column='KodElementu', max_length=100)  # Field name made lowercase.
    ilosc = models.DecimalField(db_column='Ilosc', max_digits=18, decimal_places=0)  # Field name made lowercase.
    iloscsuma = models.DecimalField(db_column='IloscSuma', max_digits=18, decimal_places=0)  # Field name made lowercase.
    zlecenie = models.CharField(db_column='Zlecenie', max_length=50)  # Field name made lowercase.
    przewodnik = models.CharField(db_column='Przewodnik', max_length=50)  # Field name made lowercase.
    numeroperacji = models.CharField(db_column='NumerOperacji', max_length=50)  # Field name made lowercase.
    nazwaoperacji = models.CharField(db_column='NazwaOperacji', max_length=50)  # Field name made lowercase.
    notatka = models.TextField(db_column='Notatka')  # Field name made lowercase.
    zmiana = models.CharField(db_column='Zmiana', max_length=50)  # Field name made lowercase.
    zasobkod = models.CharField(db_column='ZasobKod', max_length=50)  # Field name made lowercase.
    zasobnazwa = models.CharField(db_column='ZasobNazwa', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'monacoStartStopLuki'


class MonacoZlecprodukcyjne(models.Model):
    prhrid = models.IntegerField(db_column='PRHRid')  # Field name made lowercase.
    teorid = models.IntegerField(db_column='TeoRid')  # Field name made lowercase.
    zs = models.CharField(db_column='ZS', max_length=100)  # Field name made lowercase.
    numerzlecenia = models.CharField(db_column='Numerzlecenia', max_length=100)  # Field name made lowercase.
    numerprzewodnika = models.CharField(db_column='Numerprzewodnika', max_length=50)  # Field name made lowercase.
    kodelementuwiodacego = models.CharField(db_column='KodElementuWiodacego', max_length=100)  # Field name made lowercase.
    nazwaelementuwiod¹cego = models.CharField(db_column='NazwaElementuWiod¹cego', max_length=250)  # Field name made lowercase.
    kodelementu = models.CharField(db_column='KodElementu', max_length=100)  # Field name made lowercase.
    nazwaelementu = models.CharField(db_column='NazwaElementu', max_length=250)  # Field name made lowercase.
    numeroperacji = models.CharField(db_column='NumerOperacji', max_length=10)  # Field name made lowercase.
    nazwaoperacji = models.CharField(db_column='NazwaOperacji', max_length=250)  # Field name made lowercase.
    iloscplanowana = models.DecimalField(db_column='IloscPlanowana', max_digits=18, decimal_places=4)  # Field name made lowercase.
    tj = models.DecimalField(db_column='TJ', max_digits=18, decimal_places=4)  # Field name made lowercase.
    tpz = models.DecimalField(db_column='TPZ', max_digits=18, decimal_places=4)  # Field name made lowercase.
    jednostkaczasu = models.CharField(db_column='jednostkaCzasu', max_length=50)  # Field name made lowercase.
    czasplanowany = models.DecimalField(db_column='czasPlanowany', max_digits=18, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'monaco_ZlecProdukcyjne'


class MonacoPracownicy(models.Model):
    prac_id = models.IntegerField(db_column='Prac_ID')  # Field name made lowercase.
    prac_nazwisko = models.CharField(db_column='Prac_Nazwisko', max_length=70)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'monaco_pracownicy'


class MonacoZarejstrowaneoperacje(models.Model):
    prheadid = models.IntegerField(db_column='PRHeadID')  # Field name made lowercase.
    prheadoperationid = models.IntegerField(db_column='PRHeadOperationID')  # Field name made lowercase.
    quantity = models.DecimalField(db_column='Quantity', max_digits=18, decimal_places=2)  # Field name made lowercase.
    quantityrejected = models.DecimalField(db_column='QuantityRejected', max_digits=18, decimal_places=2)  # Field name made lowercase.
    timefrom = models.DateTimeField(db_column='TimeFrom')  # Field name made lowercase.
    timeto = models.DateTimeField(db_column='TimeTo')  # Field name made lowercase.
    timeduration = models.DecimalField(db_column='TimeDuration', max_digits=18, decimal_places=0)  # Field name made lowercase.
    resourcesname = models.CharField(db_column='ResourcesName', max_length=50)  # Field name made lowercase.
    resourcesnumber = models.CharField(db_column='ResourcesNumber', max_length=50)  # Field name made lowercase.
    shiftid = models.CharField(db_column='ShiftId', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'monaco_zarejstrowaneOperacje'


class PlumLogowania(models.Model):
    userid = models.IntegerField()
    username = models.CharField(db_column='userName', max_length=64)  # Field name made lowercase.
    timein = models.CharField(db_column='timeIn', max_length=19)  # Field name made lowercase.
    type = models.CharField(max_length=16)
    previd = models.IntegerField(db_column='prevId')  # Field name made lowercase.
    sessionid = models.IntegerField(db_column='sessionId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'plum_logowania'


class PlumPracownicy(models.Model):
    name = models.CharField(max_length=64)
    cardid = models.IntegerField(db_column='cardId')  # Field name made lowercase.
    description = models.CharField(max_length=255)
    hasadmin = models.BooleanField(db_column='hasAdmin')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'plum_pracownicy'


class Sliwauser(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=50, blank=True, null=True)
    cardid = models.CharField(db_column='cardId', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sliwaUser'


class Sliwawejscia(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=50, blank=True, null=True)
    timein = models.DateTimeField(db_column='timeIn')  # Field name made lowercase.
    userid = models.IntegerField(db_column='userId')  # Field name made lowercase.
    type = models.CharField(max_length=50, blank=True, null=True)
    previd = models.IntegerField(db_column='prevID', blank=True, null=True)  # Field name made lowercase.
    sessionid = models.IntegerField(db_column='sessionId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sliwaWejscia'
