hesapMert = {
    'isim': 'Mert',
    'hesapNo': '123456789',
    'sifre': '2434',
    'bakiye': 2000,
    'artiPara': 3500
}

hesapEren = {
    'isim': 'Eren',
    'hesapNo': '234567890',
    'sifre': '2424',
    'bakiye': 1000,
    'artiPara': 1500
}

hesapYigit = {
    'isim': 'Yigit',
    'hesapNo': '345678901',
    'sifre': '2424',
    'bakiye': 3000,
    'artiPara': 1750
}

hesapYagiz = {
    'isim': 'Yagiz',
    'hesapNo': '456789012',
    'sifre': '2424',
    'bakiye': 4500,
    'artiPara': 6250
}

def girisYap(hesap):
    sifre = input("Lutfen sifrenizi giriniz: ")
    if not sifre.isdigit():
        print("Sifre sayilardan olusmalidir.")
        return False
    if len(sifre) == 4:
        if sifre == hesap['sifre']:
            print(f"Hosgeldiniz {hesap['isim']}")
            return True
        else:
            print("Hatali sifre girdiniz.")
            return False
    else:
        print("Sifre dort haneli olmalidir.")
        return False


def bakiyeSorgulama(hesap):
    toplamBakiye = hesap['bakiye'] + hesap['artiPara']
    print(f"Hesabinizda bulunan bakiye: {hesap['bakiye']} TL, arti para: {hesap['artiPara']} TL, toplam kullanilabilir bakiye: {toplamBakiye} TL")

def paraCek(hesap, miktar):
    if not girisYap(hesap):
        return
    
    if miktar <= 0:
        print("Cekmek istediginiz miktar sifirdan buyuk olmalidir. Lutfen gecerli bir tutar giriniz.")
        return
    
    bakiyeSorgulama(hesap)

    if hesap['bakiye'] >= miktar:
        hesap['bakiye'] -= miktar
        print("Paraniz hazirlaniyor. Lutfen paranizi aliniz.")
    else:
        toplamBakiye = hesap['bakiye'] + hesap['artiPara']
        
        if toplamBakiye >= miktar:
            artiParaIsterMisiniz = input("Hesabinizda yeterli bakiye bulunmamaktadir. Arti para kullanmak ister misiniz? (Evet/Hayir)").strip().lower()

            if artiParaIsterMisiniz in ["evet", "e"]:
                artiParaKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['artiPara'] -= artiParaKullanilacakMiktar
                print("Arti para kullanilarak paraniz hazirlaniyor. Lutfen paranizi aliniz.")
            elif artiParaIsterMisiniz in ["hayir", "h"]:
                print(f"{hesap['hesapNo']} nolu hesabinizda bulunan bakiye miktari {hesap['bakiye']} TL'dir.")
            else:
                print("Lutfen 'Evet' veya 'Hayir' olarak cevap veriniz.")
        else:
            print("Bakiye yetersiz.")

def paraYatirma(hesap, miktar):
    if not girisYap(hesap):
        return
    
    if miktar <= 0:
        print("Yatirmak istediginiz miktar 0'dan buyuk olmalidir. Lutfen gecerli bir tutar giriniz.")
        return
    
    hesap['bakiye'] += miktar
    print(f"Hesabiniza {miktar} TL para yatirilmistir. Guncel bakiyeniz: {hesap['bakiye']}")