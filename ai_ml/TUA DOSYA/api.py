from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# API Sunucusunu başlat
app = FastAPI(title="TUA Fırtına Tahmin Motoru")

# Eğittiğin dev modelleri belleğe al
print("Modeller Yükleniyor, Lütfen Bekleyin...")
lgbm = joblib.load('lgbm_model.pkl')
xgb = joblib.load('xgb_model.pkl')
cat = joblib.load('cat_model.pkl')
features = joblib.load('feature_names.pkl')
print("SİSTEM HAZIR! Gelecek tahmin edilebilir.")

# İnternet sitesinden gelecek verinin formatı
class SolarData(BaseModel):
    sensor_verileri: dict

@app.post("/tahmin_et")
def predict_storm(payload: SolarData):
    # Gelen veriyi tabloya (DataFrame) çevir
    df = pd.DataFrame([payload.sensor_verileri])
    
    # Modelin istediği kolonlar eksikse hata vermesin, 0 doldursun
    for col in features:
        if col not in df.columns:
            df[col] = 0.0
            
    # Sütunları tam olarak eğitimdeki sıraya diz (Çok önemli!)
    df = df[features]
    
    # 3 Modelden 12 saat sonrası için risk tahminlerini al
    p1 = lgbm.predict_proba(df)[:, 1]
    p2 = xgb.predict_proba(df)[:, 1]
    p3 = cat.predict_proba(df)[:, 1]
    
    # Ortalama riski hesapla
    risk_skoru = float((p1 + p2 + p3) / 3)
    risk_yuzdesi = round(risk_skoru * 100, 2)
    
    # Risk durumuna göre mesaj belirle
    if risk_yuzdesi > 70:
        durum = "KIRMIZI ALARM: 12 Saat İçinde Şiddetli Fırtına Bekleniyor!"
    elif risk_yuzdesi > 40:
        durum = "SARI UYARI: Güneş'te Hareketlilik Var, Uzay Araçları İzlemede Kalmalı."
    else:
        durum = "YEŞİL: Uzay Havası Sakin. Önümüzdeki 12 Saat Risk Yok."
        
    return {"risk": risk_yuzdesi, "mesaj": durum}