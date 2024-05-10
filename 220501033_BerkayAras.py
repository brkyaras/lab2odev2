import pyodbc
import tkinter as tk
from tkinter import messagebox

class Gemi:
    def __init__(self, seri_numarasi, ad, agirlik, yapim_yili, kapasite, max_agirlik, tur):
        self.seri_numarasi = seri_numarasi
        self.ad = ad
        self.agirlik = agirlik
        self.yapim_yili = yapim_yili
        self.kapasite = kapasite
        self.max_agirlik = max_agirlik
        self.tur = tur

    def gemi_ekle(self):
        conn, cursor = sql_baglan()
        cursor.execute("INSERT INTO gemiler VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (self.seri_numarasi, self.ad, self.agirlik, self.yapim_yili, self.kapasite, self.max_agirlik, self.tur))
        conn.commit()
        conn.close()

class Sefer:
    def __init__(self, gemi_id, kaptanlar, murettabat, kalkis_tarihi, donus_tarihi, kalkis_limani):
        self.gemi_id = gemi_id
        self.kaptanlar = kaptanlar
        self.murettabat = murettabat
        self.kalkis_tarihi = kalkis_tarihi
        self.donus_tarihi = donus_tarihi
        self.kalkis_limani = kalkis_limani

    def sefer_ekle(self):
        conn, cursor = sql_baglan()
        cursor.execute("INSERT INTO seferler VALUES (?, ?, ?, ?, ?, ?)",
                       (self.gemi_id, self.kaptanlar, self.murettabat, self.kalkis_tarihi, self.donus_tarihi, self.kalkis_limani))
        conn.commit()
        conn.close()

class Liman:
    def __init__(self, liman_adi, ulke, nufus, pasaport_istiyor_mu, demirleme_ucreti):
        self.liman_adi = liman_adi
        self.ulke = ulke
        self.nufus = nufus
        self.pasaport_istiyor_mu = pasaport_istiyor_mu
        self.demirleme_ucreti = demirleme_ucreti

    def liman_ekle(self):
        conn, cursor = sql_baglan()
        cursor.execute("INSERT INTO limanlar VALUES (?, ?, ?, ?, ?)",
                       (self.liman_adi, self.ulke, self.nufus, self.pasaport_istiyor_mu, self.demirleme_ucreti))
        conn.commit()
        conn.close()

class Kaptan:
    def __init__(self, ad, soyad, adres, vatandaslik, dogum_tarihi, ise_giris_tarihi, lisanslar):
        self.ad = ad
        self.soyad = soyad
        self.adres = adres
        self.vatandaslik = vatandaslik
        self.dogum_tarihi = dogum_tarihi
        self.ise_giris_tarihi = ise_giris_tarihi
        self.lisanslar = lisanslar

    def kaptan_ekle(self):
        conn, cursor = sql_baglan()
        cursor.execute("INSERT INTO kaptanlar VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (self.ad, self.soyad, self.adres, self.vatandaslik, self.dogum_tarihi, self.ise_giris_tarihi, self.lisanslar))
        conn.commit()
        conn.close()

class Murettabat:
    def __init__(self, ad, soyad, adres, vatandaslik, dogum_tarihi, ise_giris_tarihi, gorev):
        self.ad = ad
        self.soyad = soyad
        self.adres = adres
        self.vatandaslik = vatandaslik
        self.dogum_tarihi = dogum_tarihi
        self.ise_giris_tarihi = ise_giris_tarihi
        self.gorev = gorev

    def murettabat_ekle(self):
        conn, cursor = sql_baglan()
        cursor.execute("INSERT INTO murettabat VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (self.ad, self.soyad, self.adres, self.vatandaslik, self.dogum_tarihi, self.ise_giris_tarihi, self.gorev))
        conn.commit()
        conn.close()

def sql_baglan():
    server = 'server_adresi'
    database = 'veritabani_adi'
    username = 'kullanici_adi'
    password = 'sifre'
    conn_str = f"DRIVER=SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}"
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    return conn, cursor

def gemi_ekle():
    seri_numarasi = seri_numarasi_entry.get()
    ad = ad_entry.get()
    agirlik = float(agirlik_entry.get())
    yapim_yili = int(yapim_yili_entry.get())
    kapasite = float(kapasite_entry.get())
    max_agirlik = float(max_agirlik_entry.get())
    tur = tur_entry.get()

    yeni_gemi = Gemi(seri_numarasi, ad, agirlik, yapim_yili, kapasite, max_agirlik, tur)
    yeni_gemi.gemi_ekle()
    messagebox.showinfo("Başarılı", "Gemi başarıyla eklendi!")

def sefer_olustur():
    gemi_id = int(gemi_id_entry.get())
    kaptanlar = kaptanlar_entry.get()
    murettabat = murettabat_entry.get()
    kalkis_tarihi = kalkis_tarihi_entry.get()
    donus_tarihi = donus_tarihi_entry.get()
    kalkis_limanı = kalkis_limanı_entry.get()

    yeni_sefer = Sefer(gemi_id, kaptanlar, murettabat, kalkis_tarihi, donus_tarihi, kalkis_limanı)
    yeni_sefer.sefer_ekle()
    messagebox.showinfo("Başarılı", "Sefer başarıyla oluşturuldu!")

def liman_ekle():
    liman_adi = liman_adi_entry.get()
    ulke = ulke_entry.get()
    nufus = int(nufus_entry.get())
    pasaport_istiyor_mu = pasaport_istiyor_mu_entry.get()
    demirleme_ucreti = float(demirleme_ucreti_entry.get())

    yeni_liman = Liman(liman_adi, ulke, nufus, pasaport_istiyor_mu, demirleme_ucreti)
    yeni_liman.liman_ekle()
    messagebox.showinfo("Başarılı", "Liman başarıyla eklendi!")

def kaptan_ekle():
    ad = ad_entry.get()
    soyad = soyad_entry.get()
    adres = adres_entry.get()
    vatandaslik = vatandaslik_entry.get()
    dogum_tarihi = dogum_tarihi_entry.get()
    ise_giris_tarihi = ise_giris_tarihi_entry.get()
    lisanslar = lisanslar_entry.get()

    yeni_kaptan = Kaptan(ad, soyad, adres, vatandaslik, dogum_tarihi, ise_giris_tarihi, lisanslar)
    yeni_kaptan.kaptan_ekle()
    messagebox.showinfo("Başarılı", "Kaptan başarıyla eklendi!")

def murettabat_ekle():
    ad = ad_entry.get()
    soyad = soyad_entry.get()
    adres = adres_entry.get()
    vatandaslik = vatandaslik_entry.get()
    dogum_tarihi = dogum_tarihi_entry.get()
    ise_giris_tarihi = ise_giris_tarihi_entry.get()
    gorev = gorev_entry.get()

    yeni_murettabat = Murettabat(ad, soyad, adres, vatandaslik, dogum_tarihi, ise_giris_tarihi, gorev)
    yeni_murettabat.murettabat_ekle()
    messagebox.showinfo("Başarılı", "Mürettebat başarıyla eklendi!")

# GUI
app = tk.Tk()
app.title("Denizcilik Şirketi Yönetim Sistemi")

# Gemi Ekleme Arayüzü
gemi_ekle_frame = tk.LabelFrame(app, text="Yeni Gemi Ekle")
gemi_ekle_frame.pack(padx=10, pady=10)

seri_numarasi_label = tk.Label(gemi_ekle_frame, text="Seri Numarası:")
seri_numarasi_label.grid(row=0, column=0)
seri_numarasi_entry = tk.Entry(gemi_ekle_frame)
seri_numarasi_entry.grid(row=0, column=1)

ad_label = tk.Label(gemi_ekle_frame, text="Ad:")
ad_label.grid(row=1, column=0)
ad_entry = tk.Entry(gemi_ekle_frame)
ad_entry.grid(row=1, column=1)

agirlik_label = tk.Label(gemi_ekle_frame, text="Ağırlık:")
agirlik_label.grid(row=2, column=0)
agirlik_entry = tk.Entry(gemi_ekle_frame)
agirlik_entry.grid(row=2, column=1)

yapim_yili_label = tk.Label(gemi_ekle_frame, text="Yapım Yılı:")
yapim_yili_label.grid(row=3, column=0)
yapim_yili_entry = tk.Entry(gemi_ekle_frame)
yapim_yili_entry.grid(row=3, column=1)

kapasite_label = tk.Label(gemi_ekle_frame, text="Kapasite:")
kapasite_label.grid(row=4, column=0)
kapasite_entry = tk.Entry(gemi_ekle_frame)
kapasite_entry.grid(row=4, column=1)

max_agirlik_label = tk.Label(gemi_ekle_frame, text="Max Ağırlık:")
max_agirlik_label.grid(row=5, column=0)
max_agirlik_entry = tk.Entry(gemi_ekle_frame)
max_agirlik_entry.grid(row=5, column=1)

tur_label = tk.Label(gemi_ekle_frame, text="Tür:")
tur_label.grid(row=6, column=0)
tur_entry = tk.Entry(gemi_ekle_frame)
tur_entry.grid(row=6, column=1)

gemi_ekle_button = tk.Button(gemi_ekle_frame, text="Gemi Ekle", command=gemi_ekle)
gemi_ekle_button.grid(row=7, columnspan=2)

# Sefer Oluşturma Arayüzü
sefer_olustur_frame = tk.LabelFrame(app, text="Yeni Sefer Oluştur")
sefer_olustur_frame.pack(padx=10, pady=10)

gemi_id_label = tk.Label(sefer_olustur_frame, text="Gemi ID:")
gemi_id_label.grid(row=0, column=0)
gemi_id_entry = tk.Entry(sefer_olustur_frame)
gemi_id_entry.grid(row=0, column=1)

kaptanlar_label = tk.Label(sefer_olustur_frame, text="Kaptanlar:")
kaptanlar_label.grid(row=1, column=0)
kaptanlar_entry = tk.Entry(sefer_olustur_frame)
kaptanlar_entry.grid(row=1, column=1)

murettabat_label = tk.Label(sefer_olustur_frame, text="Mürettebat:")
murettabat_label.grid(row=2, column=0)
murettabat_entry = tk.Entry(sefer_olustur_frame)
murettabat_entry.grid(row=2, column=1)

kalkis_tarihi_label = tk.Label(sefer_olustur_frame, text="Kalkış Tarihi:")
kalkis_tarihi_label.grid(row=3, column=0)
kalkis_tarihi_entry = tk.Entry(sefer_olustur_frame)
kalkis_tarihi_entry.grid(row=3, column=1)

donus_tarihi_label = tk.Label(sefer_olustur_frame, text="Dönüş Tarihi:")
donus_tarihi_label.grid(row=4, column=0)
donus_tarihi_entry = tk.Entry(sefer_olustur_frame)
donus_tarihi_entry.grid(row=4, column=1)

kalkis_limanı_label = tk.Label(sefer_olustur_frame, text="Kalkış Limanı:")
kalkis_limanı_label.grid(row=5, column=0)
kalkis_limanı_entry = tk.Entry(sefer_olustur_frame)
kalkis_limanı_entry.grid(row=5, column=1)

sefer_olustur_button = tk.Button(sefer_olustur_frame, text="Sefer Oluştur", command=sefer_olustur)
sefer_olustur_button.grid(row=6, columnspan=2)

# Liman Ekleme Arayüzü
liman_ekle_frame = tk.LabelFrame(app, text="Yeni Liman Ekle")
liman_ekle_frame.pack(padx=10, pady=10)

liman_adi_label = tk.Label(liman_ekle_frame, text="Liman Adı:")
liman_adi_label.grid(row=0, column=0)
liman_adi_entry = tk.Entry(liman_ekle_frame)
liman_adi_entry.grid(row=0, column=1)

ulke_label = tk.Label(liman_ekle_frame, text="Ülke:")
ulke_label.grid(row=1, column=0)
ulke_entry = tk.Entry(liman_ekle_frame)
ulke_entry.grid(row=1, column=1)

nufus_label = tk.Label(liman_ekle_frame, text="Nüfus:")
nufus_label.grid(row=2, column=0)
nufus_entry = tk.Entry(liman_ekle_frame)
nufus_entry.grid(row=2, column=1)

pasaport_istiyor_mu_label = tk.Label(liman_ekle_frame, text="Pasaport İstiyor mu?:")
pasaport_istiyor_mu_label.grid(row=3, column=0)
pasaport_istiyor_mu_entry = tk.Entry(liman_ekle_frame)
pasaport_istiyor_mu_entry.grid(row=3, column=1)

demirleme_ucreti_label = tk.Label(liman_ekle_frame, text="Demirleme Ücreti:")
demirleme_ucreti_label.grid(row=4, column=0)
demirleme_ucreti_entry = tk.Entry(liman_ekle_frame)
demirleme_ucreti_entry.grid(row=4, column=1)

liman_ekle_button = tk.Button(liman_ekle_frame, text="Liman Ekle", command=liman_ekle)
liman_ekle_button.grid(row=5, columnspan=2)

# Kaptan Ekleme Arayüzü
kaptan_ekle_frame = tk.LabelFrame(app, text="Yeni Kaptan Ekle")
kaptan_ekle_frame.pack(padx=10, pady=10)

ad_label = tk.Label(kaptan_ekle_frame, text="Ad:")
ad_label.grid(row=0, column=0)
ad_entry = tk.Entry(kaptan_ekle_frame)
ad_entry.grid(row=0, column=1)

soyad_label = tk.Label(kaptan_ekle_frame, text="Soyad:")
soyad_label.grid(row=1, column=0)
soyad_entry = tk.Entry(kaptan_ekle_frame)
soyad_entry.grid(row=1, column=1)

adres_label = tk.Label(kaptan_ekle_frame, text="Adres:")
adres_label.grid(row=2, column=0)
adres_entry = tk.Entry(kaptan_ekle_frame)
adres_entry.grid(row=2, column=1)

vatandaslik_label = tk.Label(kaptan_ekle_frame, text="Vatandaşlık:")
vatandaslik_label.grid(row=3, column=0)
vatandaslik_entry = tk.Entry(kaptan_ekle_frame)
vatandaslik_entry.grid(row=3, column=1)

dogum_tarihi_label = tk.Label(kaptan_ekle_frame, text="Doğum Tarihi:")
dogum_tarihi_label.grid(row=4, column=0)
dogum_tarihi_entry = tk.Entry(kaptan_ekle_frame)
dogum_tarihi_entry.grid(row=4, column=1)

ise_giris_tarihi_label = tk.Label(kaptan_ekle_frame, text="İşe Giriş Tarihi:")
ise_giris_tarihi_label.grid(row=5, column=0)
ise_giris_tarihi_entry = tk.Entry(kaptan_ekle_frame)
ise_giris_tarihi_entry.grid(row=5, column=1)

lisanslar_label = tk.Label(kaptan_ekle_frame, text="Lisanslar:")
lisanslar_label.grid(row=6, column=0)
lisanslar_entry = tk.Entry(kaptan_ekle_frame)
lisanslar_entry.grid(row=6, column=1)

kaptan_ekle_button = tk.Button(kaptan_ekle_frame, text="Kaptan Ekle", command=kaptan_ekle)
kaptan_ekle_button.grid(row=7, columnspan=2)

# Mürettebat Ekleme Arayüzü
murettabat_ekle_frame = tk.LabelFrame(app, text="Yeni Mürettebat Ekle")
murettabat_ekle_frame.pack(padx=10, pady=10)

ad_label = tk.Label(murettabat_ekle_frame, text="Ad:")
ad_label.grid(row=0, column=0)
ad_entry = tk.Entry(murettabat_ekle_frame)
ad_entry.grid(row=0, column=1)

soyad_label = tk.Label(murettabat_ekle_frame, text="Soyad:")
soyad_label.grid(row=1, column=0)
soyad_entry = tk.Entry(murettabat_ekle_frame)
soyad_entry.grid(row=1, column=1)

adres_label = tk.Label(murettabat_ekle_frame, text="Adres:")
adres_label.grid(row=2, column=0)
adres_entry = tk.Entry(murettabat_ekle_frame)
adres_entry.grid(row=2, column=1)

vatandaslik_label = tk.Label(murettabat_ekle_frame, text="Vatandaşlık:")
vatandaslik_label.grid(row=3, column=0)
vatandaslik_entry = tk.Entry(murettabat_ekle_frame)
vatandaslik_entry.grid(row=3, column=1)

dogum_tarihi_label = tk.Label(murettabat_ekle_frame, text="Doğum Tarihi:")
dogum_tarihi_label.grid(row=4, column=0)
dogum_tarihi_entry = tk.Entry(murettabat_ekle_frame)
dogum_tarihi_entry.grid(row=4, column=1)

ise_giris_tarihi_label = tk.Label(murettabat_ekle_frame, text="İşe Giriş Tarihi:")
ise_giris_tarihi_label.grid(row=5, column=0)
ise_giris_tarihi_entry = tk.Entry(murettabat_ekle_frame)
ise_giris_tarihi_entry.grid(row=5, column=1)

gorev_label = tk.Label(murettabat_ekle_frame, text="Görev:")
gorev_label.grid(row=6, column=0)
gorev_entry = tk.Entry(murettabat_ekle_frame)
gorev_entry.grid(row=6, column=1)

murettabat_ekle_button = tk.Button(murettabat_ekle_frame, text="Mürettebat Ekle", command=murettabat_ekle)
murettabat_ekle_button.grid(row=7, columnspan=2)

app.mainloop()