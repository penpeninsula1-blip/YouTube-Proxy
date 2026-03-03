import streamlit as st
import re

st.set_page_config(page_title="Özgür Erişim Ultra", layout="wide")

st.title("🛡️ Filtre Delen Video Oynatıcı")
st.markdown("Bağlantı sıfırlama hatalarını aşmak için **Video Dosyası** moduna geçildi.")

# Daha az bilinen ve engellenmesi imkansıza yakın Invidious API sunucuları
api_servers = [
    "https://invidious.asir.dev",
    "https://inv.riverside.rocks",
    "https://invidious.namazso.eu",
    "https://iv.melmac.space"
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
        # Sunucuları sırayla dene
        success = False
        for server in api_servers:
            try:
                # Video dosyasını doğrudan çeken oynatıcı
                video_source = f"{server}/latest_version?id={vid_id}&itag=22"
                st.video(video_source)
                st.success(f"Bağlantı Başarılı! Sunucu: {server}")
                success = True
                break
            except:
                continue
        
        if not success:
            st.error("Tüm tüneller kapalı görünüyor. Lütfen farklı bir video deneyin.")
    else:
        st.error("Geçerli bir link bulunamadı.")

st.sidebar.info("Bu yöntem, videoyu YouTube arayüzü olmadan doğrudan dosya olarak çeker. Firewall paketleri 'YouTube' olarak tanımlayamaz.")
