import streamlit as st
import re

st.set_page_config(page_title="Özgür Erişim Max", layout="wide")

st.title("🛡️ Engel Tanımayan Video Erişimi")
st.warning("Eğer ekran boş kalırsa, sayfayı yenileyip farklı bir 'Proxy Kanalı' seçin.")

# Bu servisler dünya genelinde milyonlarca kişi tarafından kullanıldığı için engellenmesi zordur
proxy_services = {
    "Kanal 1 (Croxy)": "https://www.croxyproxy.com/_tr/proxy?url=",
    "Kanal 2 (BlockAway)": "https://www.blockaway.net/_tr/proxy?url=",
    "Kanal 3 (WebProxy)": "https://www.webproxy.net/view?url="
}

with st.sidebar:
    st.header("Bağlantı Tüneli")
    selected_proxy = st.selectbox("Proxy Kanalı Seçin:", list(proxy_services.keys()))
    proxy_url = proxy_services[selected_proxy]

url_input = st.text_input("YouTube Video Linki:")

if url_input:
    # URL'yi proxy formatına uygun hale getirelim
    encoded_url = url_input.replace(":", "%3A").replace("/", "%2F").replace("?", "%3F").replace("=", "%3D")
    final_url = f"{proxy_url}{encoded_url}"
    
    st.info(f"Bağlantı kuruluyor: {selected_proxy}")
    
    # Iframe içine proxy sitesini gömüyoruz
    st.components.v1.iframe(final_url, height=800, scrolling=True)
else:
    st.write("Lütfen bir link girerek tüneli başlatın.")

with st.sidebar:
    st.divider()
    st.write("💡 **Neden Bu Çalışır?**")
    st.write("Ağınız YouTube'u engeller ama bu büyük proxy servislerini 'iş amaçlı' veya 'genel amaçlı' gördüğü için açık bırakabilir.")
