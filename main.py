def harf_notu_hesapla(ortalama):
    if ortalama >= 90:
        return "AA (Mükemmel)"
    elif ortalama >= 85:
        return "BA (Çok İyi)"
    elif ortalama >= 80:
        return "BB (İyi)"
    elif ortalama >= 75:
        return "CB (Orta-İyi)"
    elif ortalama >= 70:
        return "CC (Orta)"
    elif ortalama >= 60:
        return "DC (Sorumlu Geçer)"
    elif ortalama >= 50:
        return "DD (Geçer)"
    else:
        return "FF (Kaldı)"

  def ana_program():
    print("--- Not Hesaplama Sistemine Hoş Geldiniz ---")
    
    ders_adi = input("Dersin Adını Giriniz: ")
    vize_notu = float(input("Vize Notunuzu Giriniz (0-100): "))
    final_notu = float(input("Final Notunuzu Giriniz (0-100): "))

    # Vize %40, Final %60 etkili
    ortalama = (vize_notu * 0.40) + (final_notu * 0.60)
    durum = harf_notu_hesapla(ortalama)

    print("\n-------------------------------------------")
    print(f"Ders: {ders_adi}")
    print(f"Başarı Ortalamanız: {ortalama:.2f}")
    print(f"Harf Notunuz ve Durumunuz: {durum}")
    print("-------------------------------------------")

if __name__ == "__main__":
    ana_program()
