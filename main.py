import streamlit as st
from streamlit_option_menu import option_menu
import os
from dotenv import load_dotenv
import beranda
import klasifikasi
import tentang

# Set konfigurasi halaman
st.set_page_config(
    page_title="TanaHerba",
    layout="wide",
    page_icon="🌿"
)

# Load .env
load_dotenv()

# Ambil Google Analytics Tag dari .env
analytics_tag = os.getenv('analytics_tag')
if analytics_tag:
    st.markdown(
        f"""
        <!-- Global site tag (gtag.js) - Google Analytics -->
        <script async src="https://www.googletagmanager.com/gtag/js?id={analytics_tag}"></script>
        <script>
            window.dataLayer = window.dataLayer || [];
            function gtag(){{dataLayer.push(arguments);}}
            gtag('js', new Date());
            gtag('config', '{analytics_tag}');
        </script>
        """,
        unsafe_allow_html=True
    )

# Inisialisasi menu state
if "menu" not in st.session_state:
    st.session_state.menu = "Beranda"

# Class MultiApp
class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        if st.session_state.menu != "Klasifikasi Tanaman":
            with st.sidebar:
                st.sidebar.markdown(
                    '<h2 style="text-align: center; font-size: 28px;">TanaHerba</h2>',
                    unsafe_allow_html=True
                )
                app = option_menu(
                    menu_title='',
                    options=['Beranda', 'Tentang Tanaman'],
                    icons=['house-fill', 'info-circle-fill'],
                    menu_icon='list',
                    default_index=['Beranda', 'Tentang Tanaman'].index(st.session_state.menu),
                    styles={
                        "container": {"padding": "5!important", "background-color": "#98AFC7"},
                        "icon": {"color": "white", "font-size": "23px"},
                        "nav-link": {
                            "color": "white", "font-size": "20px", "text-align": "left",
                            "margin": "0px", "--hover-color": "#4863A0",
                            "padding": "10px 15px", "border-radius": "8px"
                        },
                        "nav-link-selected": {
                            "background-color": "#4863A0", "color": "#ffffff",
                            "font-weight": "bold", "border": "2px solid #2F539B",
                            "box-shadow": "0 0 10px rgba(2, 142, 41, 0.3)",
                            "border-radius": "8px"
                        }
                    }
                )
                st.session_state.menu = app  # Update menu state sesuai pilihan

        # Routing halaman
        if st.session_state.menu == "Beranda":
            beranda.app()
        elif st.session_state.menu == "Tentang Tanaman":
            tentang.app()
        elif st.session_state.menu == "Klasifikasi Tanaman":
            klasifikasi.app()

# Fungsi main
def main():
    app = MultiApp()
    app.run()

if __name__ == "__main__":
    main()
