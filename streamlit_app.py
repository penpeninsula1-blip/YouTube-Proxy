import streamlit as st
import requests
import base64
import re

st.set_page_config(page_title="Ultra Bypass", layout="wide")

st.title("🛡️ Metin Tüneli ile Kesintisiz Erişim")
st.info("Bu yöntem, videoyu 'metin' formatında tünellediği için en katı filtreleri bile aşabilir.")

# Alternatif API'lar
servers = ["https://invidious.asir.dev", "https://inv.tux.rs", "https://iv.melmac.space"]

url_input = st.text_input("YouTube Linkini Girin:")

def get_video_id(url):
    patterns = [r'(?:v=|\/)([0-9A-Za-z_-]{11}).*', r'shorts\/([0-9A-Za-z_-]{11})', r'youtu\.be\/([0-9A-Za-z_-]{11})']
    for p in patterns:
        match = re.search(p, url)
        if match: return match.group(1)
    return None

if url_input:
    vid_id = get_video_id(url_input)
    if vid_id:
        st.write("🔄 Veri tüneli oluşturuluyor, lütfen bekleyin...")
        
        # En hızlı sunucuyu bul ve veriyi çek
        video_url = f"{servers[0]}/latest_version?id={vid_id}&itag=18"
        
        try:
            # Sunucudan videoyu çekiyoruz (Streamlit sunucusu üzerinden)
            response = requests.get(video_url, timeout=15)
            
            if response.status_code == 200:
                # Videoyu metne (Base64) dönüştürerek firewall'u şaşırtıyoruz
                b64_video = base64.b64encode(response.content).decode()
                video_tag = f'<video width="100%" height="500" controls><source src="data:video/mp4;base64,{b64_video}" type="video/mp4"></video>'
                
                st.markdown(video_tag, unsafe_allow_html=True)
                st.success("Tünel başarıyla kuruldu! Video metin olarak paketlendi.")
                
                # Ayrıca indirme butonu
                st.download_button("Dosyayı Kaydet (.mp4)", data=response.content, file_name=f"video_{vid_id}.mp4")
            else:
                st.error("Sunucu yanıt vermedi. Lütfen sayfayı yenileyip tekrar deneyin.")
        except Exception as e:
            st.error(f"Tünel hatası: Ağınız bu tür bir veri transferini engelliyor olabilir.")
    else:
        st.error("Geçerli bir link bulunamadı.")
