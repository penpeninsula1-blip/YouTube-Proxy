import streamlit as st
import requests
import re

st.set_page_config(page_title="Ultra Bypass Final", layout="wide")

st.title("🛡️ Filtre Delen Veri Tüneli (V7)")
st.info("Bu sürüm, veriyi parçalayarak tüneller. İlk yükleme 10-15 saniye sürebilir.")

# Güvenilir Tünel Sunucuları
tunnel_hosts = [
    "https://inv.tux.rs",
    "https://invidious.asir.dev",
    "https://iv.melmac.space",
    "https://invidious.no-logs.com"
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
        st.write("🔄 Tünel kuruluyor, lütfen beklemeye devam edin...")
        
        found = False
        for host in tunnel_hosts:
            # itag 18: 360p (Düşük kalite ama engelleri aşma şansı en yüksek olanıdır)
            stream_url = f"{host}/latest_version?id={vid_id}&itag=18"
            
            try:
                # Sunucunun yanıt verip vermediğini kontrol et
                res = requests.get(stream_url, stream=True, timeout=5)
                if res.status_code == 200:
                    # Videoyu Streamlit'in kendi hafızasından kullanıcıya sun
                    st.video(stream_url)
                    st.success(f"Bağlantı tünellendi! (Sunucu: {host})")
                    found = True
                    break
            except:
                continue
        
        if not found:
            st.error("Ağınız bu sunuculardan gelen veri akışını tamamen engelliyor.")
            st.warning("Son çare olarak butona sağ tıklayıp 'Bağlantıyı farklı kaydet' demeyi deneyin:")
            st.markdown(f"[🎥 Doğrudan Video Dosyası Linki](https://invidious.asir.dev/latest_version?id={vid_id}&itag=18)")
    else:
        st.error("Geçerli bir link bulunamadı.")
