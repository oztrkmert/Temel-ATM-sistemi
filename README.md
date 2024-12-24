ATM Sistemi

Bu proje temel bankacılık işlemlerini gerçekleştiren bir ATM sistemidir. Kullanıcılar hesaplarına giriş yaparak bakiye sorgulama, para çekme ve para yatırma gibi işlemleri gerçekleştirebilir. Program Python ile yazılmıştır.

------------------------------------------------------------------------------------------------------------------------------------------

Özellikler

Giriş Yapma: Kullanıcılar, doğru şifre girerek hesaplarına giriş yapabilir. Şifre yanlış girilirse belirli bir deneme hakkı tanınır.

Bakiye Sorgulama: Kullanıcılar, hesap bakiyelerini ve artı para limitlerini görebilir.

Para Çekme: Kullanıcılar hesaplarından para çekebilir. Yetersiz bakiye durumunda artı para kullanımına izin verilir.

Para Yatırma: Kullanıcılar hesaplarına para yatırabilir.

Hata Yönetimi: Geçersiz girişler veya hatalı işlemler için kullanıcıya açıklayıcı geri bildirim sağlanır.

------------------------------------------------------------------------------------------------------------------------------------------

Fonksiyonlar

1) girisYap(hesap)

Kullanıcıdan şifre alır ve doğruluğunu kontrol eder. Şifre yanlışsa deneme hakkı tanır.

2) bakiyeSorgulama(hesap)

Kullanıcının hesap bakiyesi, artı para limiti ve toplam kullanılabilir bakiyesini görüntüler.

3) paraCek(hesap, miktar)

Hesaptan belirtilen miktarda para çeker. Yetersiz bakiye durumunda artı para kullanımı için kullanıcıya seçenek sunar.

4) paraYatirma(hesap, miktar)

Hesaba belirtilen miktarda para yatırır.

------------------------------------------------------------------------------------------------------------------------------------------

Çalıştırma Talimatları

1) Gereksinimler:

Python 3.x yüklü olmalıdır.

2) Kodun Çalıştırılması:

Proje dosyasını indirin veya kopyalayın.

Terminal veya komut istemcisinde aşağıdaki komutu çalıştırın:

python atm.py

3) Kullanıcı Girişi:

Kullanıcıdan şifre girmesi istenir.

Doğru şifre girildiğinde kullanıcı işlemlerine devam edebilir.
