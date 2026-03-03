import streamlit as st
import re

st.set_page_config(page_title="Özgür Erişim", layout="wide")

st.title("🚀 Kesintisiz Video Erişimi")
st.info("Bu uygulama bulut üzerinden çalıştığı için yerel engellere takılmaz.")

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
        # Firewall'un en zor fark ettiği yöntem: Invidious Tüneli
        st.components.v1.iframe(f"https://yewtu.be/embed/{vid_id}", height=600)
    else:
        st.error("Geçerli bir link bulunamadı.")