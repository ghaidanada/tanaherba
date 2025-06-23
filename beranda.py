import streamlit as st
from streamlit_option_menu import option_menu
import os
from dotenv import load_dotenv
import beranda
import klasifikasi
import tentang

# Set konfigurasi halaman
st.set_page_config(page_title="TanaHerba", layout="wide", page_icon="🌿")

# Load environment variable
load_dotenv()
analytics_tag = os.getenv('analytics_tag')
if analytics_tag:
    st.markdown(f"""
    <script async src="https://www.googletagmanager.com/gtag/js?id={analytics_tag}"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){{dataLayer.push(arguments);}}
        gtag('js', new Date());
        gtag('config', '{analytics_tag}');
    </script>
    """, unsafe_allow_html=True)

# Inisialisasi session_state
if "menu" not in st.session_state:
    st.session_state.menu = "Beranda"

# Class MultiApp
class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})

    def run(self):
        with st.sidebar:
            st.sidebar.markdown('<h2 style="text-align: center; font-size: 28px;">TanaHerba</h2>', unsafe_allow_html=True)
            menu_list = ['Beranda', 'Tentang Tanaman']
            default_idx = menu_list.index(st.session_state.menu) if st.session_state.menu in menu_list else 0

            app = option_menu(
                menu_title='',
                options=menu_list,
                icons=['house-fill', 'info-circle-fill'],
                menu_icon='list',
                default_index=default_idx,
                styles={
                    "container": {"padding": "5!important", "background-color": "#98AFC7"},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left",
                                  "--hover-color": "#4863A0", "padding": "10px 15px", "border-radius": "8px"},
                    "nav-link-selected": {"background-color": "#4863A0", "color": "#fff", "font-weight": "bold",
                                          "border": "2px solid #2F539B", "box-shadow": "0 0 10px rgba(2,142,41,0.3)",
                                          "border-radius": "8px"}
                }
            )

            if app:
                st.session_state.menu = app

        # Routing ke halaman
        if st.session_state.menu == "Beranda":
            beranda.app()
        elif st.session_state.menu == "Tentang Tanaman":
            tentang.app()
        elif st.session_state.menu == "Klasifikasi":
            klasifikasi.app()

# Fungsi main
if __name__ == "__main__":
    app = MultiApp()
    app.run()
