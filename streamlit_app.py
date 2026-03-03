import streamlit as st
import re

# Sayfa Ayarları
st.set_page_config(page_title="Özgür Erişim PRO", layout="wide", page_icon="🚀")

st.title("🚀 Kesintisiz Video Erişimi (V4)")
st.markdown("---")

# Sunucu Listesi (Biri çalışmazsa diğerini seçebilmeniz için)
servers = {
    "Invidious (Lüksemburg)": "https://invidious.flokinet.to",
    "Invidious (Sırbistan)": "https://inv.tux.rs",
    "Invidious (Almanya)": "https://invidious.projectsegfau.lt",
    "Yewtu (Genel)": "https://yewtu.be",
    "Piped (Alternatif Altyapı)": "https://piped.video"
}

with st.sidebar:
    st.header("⚙️ Bağlantı Ayarları")
    selected_server_name = st.selectbox("Çalışmayan bir sunucu olursa değiştirin:", list(servers.keys()))
    selected_server = servers[selected_server_name]
    st.divider()
    st.info("💡 **İpucu:** Eğer video karesi boş kalırsa, listeden farklı bir sunucu seçip tekrar deneyin.")

url_input = st.text_input("YouTube Linkini Buraya Yapıştırın:", placeholder="https://www.youtube.com/watch?v=...")

def get_video_id(url):
    """Tüm YouTube formatlarından Video ID'sini çeker."""
    patterns = [
        r'(?:v=|\/)([0-9A-Za-z_-]{11}).*', # Standart ve Mobil
        r'shorts\/([0-9A-Za-z_-]{11})',     # Shorts
        r'live\/([0-9A-Za-z_-]{11})',       # Canlı yayın
        r'youtu\.be\/([0-9A-Za-z_-]{11})'    # Kısa link
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None

if url_input:
    vid_id = get_video_id(url_input)
    
    if vid_id:
        st.success(f"Video Algılandı! Sunucu: {selected_server_name}")
        
        # Piped sunucusu için farklı URL yapısı kullanılır
        if "piped" in selected_server:
            embed_url = f"{selected_server}/embed/{vid_id}"
        else:
            embed_url = f"{selected_server}/embed/{vid_id}"
            
        # Videoyu ekrana bas
        st.components.v1.iframe(embed_url, height=650, scrolling=False)
    else:
        st.error("Lütfen geçerli bir YouTube linki (URL) girin.")

st.markdown("---")
st.caption("Bu uygulama, trafiği farklı sunucular üzerinden tünellediği için yerel engelleri aşar.")
