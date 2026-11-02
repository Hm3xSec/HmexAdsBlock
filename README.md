Program Name: HmexAdsBlock
Version:      0.1.0
Coder:        Hm3x

Python destekli reklam engelleme aracı.

HmexAdsBlock, Chrome tarayıcısında istenmeyen reklam isteklerini engellemek ve kullanıcıların kendi reklam filtrelerini Python üzerinden yönetebilmesini sağlamak amacıyla geliştirilmiş açık kaynaklı bir projedir.


Kurulum
Repository'yi bilgisayarınıza indirin.
Google Chrome'u açın.
chrome://extensions adresine gidin.
Geliştirici modunu etkinleştirin.
Paketlenmemiş öğe yükle seçeneğine tıklayın.
Projedeki extension klasörünü seçin.

Python Kullanımı

Reklam alan adı engellemek:

python python/main.py block reklam-sunucusu.com

Engellemeyi kaldırmak:

python python/main.py unblock reklam-sunucusu.com

Engellenen alan adlarını listelemek:

python python/main.py list

Kullanım-Python

Bağlantı engellemek için:
python main.py block reklam-sunucusu.com
Bağlantı engeli kaldırmak için:
python main.py unblock reklam-sunucusu.com
Engellenen bağlantıları görmek için
python main.py list

