# Spor Analiz Programi: Web Veri Tabanlı Spor Tahmin Sistemi + Gelişmiş Özellikler + Gerçek Skor ve Form Etkenli Yapay Zeka + Gelişmiş Filtreler + Giriş Sistemi
...
# ANA FONKSİYON
if __name__ == "__main__":
    veritabani_olustur()
    kullanici_kaydet("demo", "1234")
    df_sanal = rastgele_mac_uret()
    if not df_sanal.empty:
        veritabaniya_kaydet(df_sanal)
    app.run(debug=True)
