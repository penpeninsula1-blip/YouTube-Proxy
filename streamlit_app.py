import streamlit as st
import re
import requests

st.set_page_config(page_title="Özgür Erişim Ultra", layout="wide")

st.title("🛡️ Filtre Delen Video Oynatıcı")
st.caption("Bağlantı sıfırlama hatasını aşmak için video dosyası doğrudan sunucudan çekiliyor.")

# Farklı bölgelerden daha sağlam API sunucuları
api_servers = [
    "https://invidious.asir.dev",
    "https://inv.riverside.rocks",
    "https://invidious.namazso.eu",
    "https://iv.melmac.space",
    "https://invidious.sethforprivacy.com"
]

url_input = st.text_input("YouTube Video Linkini Girin:")

def get_video_id(url):
    patterns = [r'(?:v=|\/)([0-9A-Za-z_-]{11}).*', r'shorts\/([0-9A-Za-z_-]{11})', r'youtu\.be\/([0-9A-Za-z_-]{11})']
    for p in patterns:
        match = re.search(p, url)
        if match: return match.group(1)
    return None

if url_input:
    vid_id = get_video_id(url_input)
    if vid_id:
        st.write("🔄 Uygun tünel aranıyor, lütfen bekleyin...")
        
        success = False
        # Hem sunucuları hem de kalite ayarlarını (itag) deniyoruz
        # itag 22 = 720p, itag 18 = 360p
        for server in api_servers:
            for quality in ["22", "18"]:
                video_source = f"{server}/latest_version?id={vid_id}&itag={quality}"
                try:
                    # Sunucunun canlı olup olmadığını hızlıca kontrol et
                    res = requests.head(video_source, timeout=3)
                    if res.status_code < 400:
                        st.video(video_source)
                        st.success(f"Bağlantı kuruldu! Sunucu: {server} (Kalite: {quality})")
                        success = True
                        break
                except:
                    continue
            if success: break
        
        if not success:
            st.error("Şu an tüm tüneller yoğun veya ağınız tarafından engelleniyor.")
            st.info("💡 İpucu: Sayfayı yenileyip 10-15 saniye sonra tekrar deneyin.")
    else:
        st.error("Geçerli bir link bulunamadı.")

st.sidebar.warning("Eğer video hala açılmıyorsa, ağınız video veri akışını (stream) tespit edip kesiyor olabilir.")
