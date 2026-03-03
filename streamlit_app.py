import streamlit as st
import re

st.set_page_config(page_title="Ultra Bypass PRO", layout="wide")

st.title("🛡️ Sınır Tanımayan Video Tüneli")
st.caption("API sunucularına ihtiyaç duymayan doğrudan gömme yöntemi.")

url_input = st.text_input("YouTube Linkini Buraya Yapıştırın:")

def get_video_id(url):
    # Tüm YouTube varyasyonlarını (Shorts, Live, Mobil) yakalar
    patterns = [
        r'(?:v=|\/)([0-9A-Za-z_-]{11}).*', 
        r'shorts\/([0-9A-Za-z_-]{11})', 
        r'youtu\.be\/([0-9A-Za-z_-]{11})'
    ]
    for p in patterns:
        match = re.search(p, url)
        if match: return match.group(1)
    return None

if url_input:
    vid_id = get_video_id(url_input)
    if vid_id:
        st.success("Tünel Hazırlanıyor...")
        
        # YouTube'un engellenmesi en zor olan 'nocookie' (çerezsiz) sunucusunu kullanıyoruz
        # Bu sunucu genellikle kurumsal filtreler tarafından 'takip kodu' içermediği için açık bırakılır.
        embed_url = f"https://www.youtube-nocookie.com/embed/{vid_id}?autoplay=1&modestbranding=1&rel=0"
        
        # Videoyu en güvenli şekilde ekrana gömme
        st.components.v1.iframe(embed_url, height=600, scrolling=False)
        
        st.info("💡 Not: Eğer hala açılmıyorsa, ağınız 'youtube-nocookie.com' adresini de kapatmış demektir.")
    else:
        st.error("Lütfen geçerli bir YouTube linki girdiğinizden emin olun.")

st.sidebar.markdown("""
### Neden Bu Çalışır?
Ağlar genellikle `youtube.com` adresini engeller ancak sitelere gömülen videolar için kullanılan **`youtube-nocookie.com`** adresini, diğer web sitelerinin içeriğini bozmamak adına açık bırakabilir.
""")
