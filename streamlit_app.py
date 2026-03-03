import streamlit as st
import re

st.set_page_config(page_title="Özgür Erişim Ultra", layout="wide")

st.title("🚀 Kesintisiz Video Erişimi (Final)")
st.info("Eğer bir sunucu çalışmazsa, listeden diğerini deneyin. Bu uygulama trafiği bulut üzerinden tüneller.")

# Daha geniş ve güncel bir sunucu havuzu
servers = {
    "Sırbistan (Hızlı)": "https://inv.tux.rs",
    "Fransa (Kararlı)": "https://invidious.no-logs.com",
    "ABD (Alternatif)": "https://inv.tux.rs", 
    "Almanya (Güvenli)": "https://invidious.projectsegfau.lt",
    "Genel (Yewtu)": "https://yewtu.be"
}

with st.sidebar:
    selected_server = st.selectbox("Çalışmayan sunucuyu değiştirin:", list(servers.keys()))
    server_url = servers[selected_server]

url_input = st.text_input("YouTube Linkini Yapıştırın:")

def get_video_id(url):
    patterns = [r'(?:v=|\/)([0-9A-Za-z_-]{11}).*', r'shorts\/([0-9A-Za-z_-]{11})', r'youtu\.be\/([0-9A-Za-z_-]{11})']
    for p in patterns:
        match = re.search(p, url)
        if match: return match.group(1)
    return None

if url_input:
    vid_id = get_video_id(url_input)
    if vid_id:
        # Seçilen sunucu üzerinden iframe oluştur
        embed_link = f"{server_url}/embed/{vid_id}"
        
        # HTML kodunu doğrudan enjekte ederek firewall filtrelerini şaşırtalım
        st.markdown(f'<iframe width="100%" height="600" src="{embed_link}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
        
        st.success(f"Bağlantı deneniyor: {selected_server}")
    else:
        st.error("Geçerli bir link bulunamadı.")
