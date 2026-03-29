# Zenith

🌌 Zenith Erken Uyarı Paneli
Bursa Teknik Üniversitesi | TUA Astro Hackathon 2026 Projesi

Zenith Erken Uyarı Paneli, uzay havasındaki anormallikleri ve olası Güneş fırtınalarını (Koronal Kütle Atımı - CME) makine öğrenmesi algoritmaları ile önceden tespit etmeyi amaçlayan otonom bir sistemdir. Uydularımızın ve küresel enerji şebekelerimizin zarar görmesini engellemek amacıyla, karar alıcılara 12 saat öncesinden proaktif önlem alma fırsatı sunar.

Sadece geçmiş verileri görselleştiren statik bir web paneli değil; veri mühendisliği, bulut mimarisi ve anlık bildirim ağıyla entegre çalışan uçtan uca bir yapay zeka sistemidir.

🚀 Temel Özellikler
Öngörücü Yapay Zeka: Sistem, Güneş fırtınalarını ve CME olaylarını 12 saat önceden %84 doğruluk oranıyla tahmin eder.

Otonom Uyarı Mekanizması: Tehlike anında sisteme entegre Telegram botu üzerinden yetkili kişilere saniyeler içinde acil durum raporu iletilir.

Optimize Edilmiş Veri İşleme: NASA'nın sağladığı 6 milyon satırlık karmaşık ham veri, istatistiksel yöntemlerle anlamlı ve dengeli 1 milyon satırlık bir sete indirgenmiştir.

Canlı Dashboard: Dinamik HTML arayüzü sayesinde uzay havası metrikleri anlık ve kullanıcı dostu bir şekilde takip edilebilir.

🧠 Makine Öğrenmesi & Veri Bilimi Yaklaşımı
Projemizde tek bir modelin kısıtlamalarından kaçınmak için güçlü gradyan artırma algoritmalarından oluşan bir Ensemble (Topluluk) yaklaşımı benimsenmiştir:

Modeller: XGBoost, CatBoost ve LightGBM

Zamansal Analiz: Pandas üzerinden shift(-12) fonksiyonu ile veriye zaman kaydırma uygulanarak, sistemin matematiksel olarak geleceği görmesi sağlanmıştır.

🛠 Mimari ve Teknolojiler
Projemiz, "clean code" (temiz kod) prensiplerine sadık kalınarak modüler bir yapıda geliştirilmiştir.

Veri İşleme ve Modelleme: Python, Pandas, Scikit-learn, Joblib

Tahmin Algoritmaları: XGBoost, CatBoost, LightGBM

Bulut ve Dağıtım: Render (Yüksek erişilebilirlik sağlayan bulut altyapısı)

Frontend: Dinamik HTML, CSS, JavaScript tabanlı kullanıcı arayüzü

Entegrasyon: Telegram Bot API (Otonom acil durum bildirimleri)

👥 Takım Üyeleri
Bu proje, farklı disiplinlerin bir araya gelmesiyle ortaya çıkmıştır:

Ayberk - Yapay Zeka ve Model Geliştirme

İsmail Emre - Veri Mühendisliği ve Optimizasyon

Elif Sude - Backend Mimarisi ve Bulut Entegrasyonu

Gizem - Frontend ve UI/UX Tasarımı

⚙️ Kurulum ve Çalıştırma
(Projeyi yerel ortamda çalıştırmak için aşağıdaki adımları izleyebilirsiniz)

Depoyu klonlayın:

Bash
git clone https://github.com/kullaniciadi/zenith-erken-uyari.git
Gerekli kütüphaneleri yükleyin:

Bash
pip install -r requirements.txt
Uygulamayı başlatın:

Bash
python app.py
