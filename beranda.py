import streamlit as st
import os
import base64

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def app():
    logo_path = "tanaherba.png"

    # Header dengan logo dan judul (TIDAK DIUBAH)
    if os.path.exists(logo_path):
        logo_base64 = get_base64_of_bin_file(logo_path)
        st.markdown(f'''
            <div style="display: flex; align-items: center; margin-bottom: 20px;">
                <div style="width: 35px; height: 35px; border-radius: 50%; overflow: hidden; margin-right: 5px; margin-top: 30px;">
                    <img src="data:image/png;base64,{logo_base64}" style="width: 100%; height: 100%; object-fit: cover;" />
                </div>
                <h1 style="color: #C19A6B; font-size: 16px; margin: 0; margin-top: 20px;">TanaHerba</h1>
            </div>
        ''', unsafe_allow_html=True)
    else:
        st.title("TanaHerba")

    # CSS styling tombol dan responsif terhadap dark/light mode
    st.markdown('''
        <style>
            .centered-section {
                text-align: center;
                max-width: 700px;
                margin: auto;
            }

            .stButton > button {
                background-color: #4863A0;
                color: white;
                border-radius: 8px;
                padding: 0.5em 1.5em;
                font-size: 16px;
                margin-top: 10px;
                margin-left: 300px;
            }

            /* Mode terang */
            @media (prefers-color-scheme: light) {
                .block-container {
                    background-color: rgba(255, 255, 255, 0.95);
                    color: black;
                }
            }

            /* Mode gelap */
            @media (prefers-color-scheme: dark) {
                .block-container {
                    background-color: rgba(30, 30, 30, 0.95);
                    color: white;
                }
            }
        </style>
    ''', unsafe_allow_html=True)

    # Konten utama (TIDAK DIUBAH)
    st.markdown("""
        <div class="block-container centered-section" style="margin-top: -40px;">
            <h2>Selamat datang di <b>TanaHerba</b> 🌱</h2>
        </div>
    """, unsafe_allow_html=True)

    # Tombol navigasi ke klasifikasi di tengah halaman
    st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
    if st.button("🔍 Mulai Klasifikasi Tanaman"):
        st.session_state.menu = "Klasifikasi Tanaman"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
