import streamlit as st
import requests
import joblib

# Sayfanın sekme adını ve genişliğini ayarla
st.set_page_config(page_title="TUA Erken Uyarı Sistemi", layout="centered")

# Başlık ve Açıklamalar
st.title("☀️ TUA Güneş Fırtınası Erken Uyarı Sistemi")
st.markdown("**Bu yapay zeka sistemi, anlık manyetik verilere bakarak 12 saat sonrasındaki Güneş Patlaması (Flare) riskini hesaplar.**")
st.divider()

# Özellik isimlerini dosyadan çek
features = joblib.load('feature_names.pkl')

st.header("📡 Anlık Uydu Verileri (Manuel Giriş)")
st.info("Aşağıdaki değerleri değiştirerek 12 saat sonrası için farklı senaryoları test edebilirsiniz.")

# Sadece ilk 4 önemli kolonu ekranda gösterelim (Jürinin kafası karışmasın)
user_input = {}
col1, col2 = st.columns(2)

# Dinamik olarak kolonları ekrana diz
for i, col in enumerate(features[:4]):
    if i % 2 == 0:
        user_input[col] = col1.number_input(f"{col} Değeri:", value=0.0)
    else:
        user_input[col] = col2.number_input(f"{col} Değeri:", value=0.0)

st.write("") # Boşluk bırak

# TAHMİN BUTONU
if st.button("🚀 12 Saatlik Riski Analiz Et", use_container_width=True, type="primary"):
    payload = {"sensor_verileri": user_input}
    
    try:
        # Backend'e (api.py) veriyi yolla ve cevabı bekle
        with st.spinner("Yapay Zeka Geleceği Hesaplıyor..."):
            response = requests.post("http://127.0.0.1:8000/tahmin_et", json=payload)
            sonuc = response.json()
        
        risk = sonuc['risk']
        mesaj = sonuc['mesaj']
        
        # Sonuçları Ekrana Bas
        st.divider()
        st.subheader(f"Tahmini Risk (12 Saat Sonrası): %{risk}")
        
        if risk > 70:
            st.error(mesaj)
        elif risk > 40:
            st.warning(mesaj)
        else:
            st.success(mesaj)
            
        st.progress(risk / 100) # İlerleme çubuğu
        
    except Exception as e:
        st.error("Bağlantı Hatası! Terminalden 'api.py' dosyasının (Backend) çalıştığına emin olun.")