import telegram
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
import asyncio

# --- AYARLAR ---
TOKEN = "8215189457:AAGlWgkWMej368sJYmJwXuxrjTeONBSKfPM"
CHAT_ID = "6327114141"

app = FastAPI()
bot = telegram.Bot(token=TOKEN)

# 1. API KISMI (Telegram'a mesaj yollayan kapımız)
@app.post("/uyari-gonder")
async def uyari_gonder(mesaj: str):
    print(f"Siteden uyarı geldi: {mesaj}")
    try:
        await bot.send_message(chat_id=CHAT_ID, text=f"🚨 *ZENITH SİSTEM UYARISI* 🚨\n\n{mesaj}", parse_mode='Markdown')
        return {"durum": "Başarılı"}
    except Exception as e:
        return {"durum": "Hata", "detay": str(e)}
import random # Bunu en yukarıya importların arasına ekle

# ... (eski kodların)

@app.post("/kayit-kodu-gonder")
async def kayit_kodu_gonder(telefon: str):
    # Rastgele 4 haneli bir kod oluşturuyoruz
    dogrulama_kodu = random.randint(1000, 9999)
    print(f"Kayıt talebi! Telefon: {telefon}, Kod: {dogrulama_kodu}")
    
    try:
        # Sana (Sistem Adminine) kodu yolluyoruz
        mesaj = f"🔐 *ZENITH YENİ KAYIT TALEBİ*\n\n📱 Telefon: `{telefon}`\n🔑 Doğrulama Kodu: `{dogrulama_kodu}`"
        await bot.send_message(chat_id=CHAT_ID, text=mesaj, parse_mode='Markdown')
        # Frontend'e bu kodu gizlice yolluyoruz ki doğruluğunu kontrol etsin
        return {"durum": "Başarılı", "kod": str(dogrulama_kodu)}
    except Exception as e:
        return {"durum": "Hata", "detay": str(e)}

# 2. WEB SİTESİ KISMI (Arkadaşının kodlarını yayına alıyoruz)
# Bu satır, 'frontend' klasöründeki index.html ve image_1.png'yi web'e açar.
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

async def main():
    config = uvicorn.Config(app=app, host="127.0.0.1", port=8000, log_level="info")
    server = uvicorn.Server(config)
    print("\n🚀 ZENITH SİSTEMİ TAM KAPASİTE AKTİF!")
    print("👉 Siteye girmek için: http://127.0.0.1:8000")
    print("------------------------------------\n")
    await server.serve()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nSistem kapatıldı.")