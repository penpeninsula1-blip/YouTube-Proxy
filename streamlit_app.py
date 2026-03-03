import streamlit as st
import re

st.set_page_config(page_title="Özgür Erişim İndirici", layout="wide")

st.title("🛡️ Filtre Delen Video İndirici")
st.markdown("Eğer video oynatılamıyorsa, bu yöntemle **dosya olarak indirip** izleyebilirsiniz.")

# En sağlam API tünelleri
api_servers = [
    "https://invidious.asir.dev",
    "https://inv.tux.rs",
    "https://invidious.namazso.eu",
    "https://iv.melmac.space"
]

url_input = st.text_input("YouTube Linkini Buraya Yapıştırın:")

def get_video_id(url):
    patterns = [r'(?:v=|\/)([0-9A-Za-z_-]{11}).*', r'shorts\/([0-9A-Za-z_-]{11})', r'youtu\.be\/([0-9A-Za-z_-]{11})']
    for p in patterns:
        match = re.search(p, url)
        if match: return match.group(1)
    return None

if url_input:
    vid_id = get_video_id(url_input)
    if vid_id:
        st.subheader("📥 İndirme Bağlantıları")
        st.write("Aşağıdaki butonlara sağ tıklayıp 'Farklı Kaydet' diyebilir veya direkt tıklayarak indirmeyi başlatabilirsiniz.")
        
        # Her sunucu için bir indirme butonu oluştur
        for server in api_servers:
            # itag 22: 720p, itag 18: 360p
            dl_url_720 = f"{server}/latest_version?id={vid_id}&itag=22"
            dl_url_360 = f"{server}/latest_version?id={vid_id}&itag=18"
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f'<a href="{dl_url_720}" target="_blank" style="text-decoration:none;"><button style="width:100%; padding:10px; background-color:#ff4b4b; color:white; border:none; border-radius:5px;">Yüksek Kalite İndir (720p)</button></a>', unsafe_allow_html=True)
            with col2:
                st.markdown(f'<a href="{dl_url_360}" target="_blank" style="text-decoration:none;"><button style="width:100%; padding:10px; background-color:#4b4bff; color:white; border:none; border-radius:5px;">Düşük Kalite İndir (360p)</button></a>', unsafe_allow_html=True)
            
            st.caption(f"Sunucu Kaynağı: {server}")
            st.divider()
    else:
        st.error("Geçerli bir YouTube linki bulunamadı.")

st.sidebar.info("💡 **Nasıl Kullanılır?**\n\nButona bastığınızda indirme başlamazsa, butona sağ tıklayıp 'Bağlantıyı farklı kaydet' seçeneğini deneyin.")
