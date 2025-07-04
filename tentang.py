import streamlit as st
import os
import base64

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def app():
    logo_path = "tanaherba.png"
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

    # CSS Percantik
    st.markdown('''
        <style>
        .centered-header {
            text-align: center;
            margin-top: -40px;
            font-size: 24px;
            font-weight: bold;
        }
        .st-expander > summary {
            font-size: 18px;
            font-weight: bold;
            color: #4CAF50;
        }
        @media (prefers-color-scheme: dark) {
            .st-expander {
                background-color: rgba(40, 40, 40, 0.9);
                color: white;
            }
        }
        @media (prefers-color-scheme: light) {
            .st-expander {
                background-color: rgba(240, 240, 240, 0.9);
                color: black;
            }
        }
        </style>
    ''', unsafe_allow_html=True)

    st.markdown('<h2 class="centered-header">Jenis-Jenis Tanaman Rimpang 🌱</h2>', unsafe_allow_html=True)

    # Data Tanaman Lengkap
    data_rimpang = [
        {
            "judul": "1. Bengle (Zingiber purpureum Roxb.)",
            "isi": """
Bengle merupakan tanaman herba berumpun rapat, tinggi hingga 150 cm. Rimpangnya kuning kehijauan, rasa pahit pedas, aroma tajam. Dimanfaatkan untuk cacingan, masuk angin, sembelit, karminatif, obat gosok.
"""
        },
        {
            "judul": "2. Dringo (Alpinia galanga)",
            "isi": """
Dringo tinggi 55-80 cm, daun seperti pita, rimpang merah jambu, mengandung minyak atsiri dan senyawa pahit. Bermanfaat sebagai insektisida, pengobatan demam nifas, karminatif, disentri, pembengkakan limpa, penambah nafsu makan.
"""
        },
        {
            "judul": "3. Jahe (Zingiber officinale)",
            "isi": """
Jahe tumbuh berumpun, rimpang bercabang, aroma pedas khas. Ada jahe gajah, jahe emprit, jahe merah. Digunakan untuk pencernaan, mengencerkan dahak, perut kembung, bronkitis, demam, sakit kepala.
"""
        },
        {
            "judul": "4. Kencur (Kaempferia galanga)",
            "isi": """
Kencur tanaman kecil merayap, rimpang membulat, aroma tajam. Mengandung borneol, kamfer, sineol. Khasiatnya untuk radang tenggorokan, batuk, perut kembung, masuk angin, pelangsing, penurun panas dalam.
"""
        },
        {
            "judul": "5. Kunyit (Curcuma longa L.)",
            "isi": """
Kunyit rimpang jingga terang, batang hijau keunguan, bunga di ujung batang. Mengandung kurkumin, minyak atsiri. Digunakan untuk gangguan pencernaan, antiseptik, peradangan mulut, luka kulit, asma, penambah nafsu makan.
"""
        },
        {
            "judul": "6. Lempuyang (Zingiber zerumbet L.)",
            "isi": """
Lempuyang mirip laos, rimpang besar menyerupai buah, bunga indah. Mengandung zerumbone, alkaloid, flavonoid. Berkhasiat untuk asam lambung, sirkulasi darah, stamina, ambeien, anemia, antikanker, antitumor.
"""
        },
        {
            "judul": "7. Lengkuas (Alpinia galanga)",
            "isi": """
Lengkuas batang tinggi >2 meter, kulit rimpang mengkilap, rasa pedas manis. Mengandung eugenol, diterpene. Khasiatnya untuk antijamur, infeksi kulit, panu, jerawat, eksim, serta gangguan pencernaan.
"""
        },
        {
            "judul": "8. Temu Hitam (Curcuma aeruginosa Roxb.)",
            "isi": """
Temu Hitam tinggi 2 meter, rimpang pola biru keunguan, daun merah tua. Mengandung minyak atsiri, damar. Digunakan untuk cacingan, meningkatkan nafsu makan, rematik, penyakit kulit, pembersih darah.
"""
        },
        {
            "judul": "9. Temu Kunci (Boesenbergia rotunda)",
            "isi": """
Temu Kunci tanpa batang, rimpang panjang ramping warna coklat kekuningan. Mengandung minyak atsiri, damar, pati. Khasiatnya untuk diare, sariawan, batuk kering, gatal-gatal, obat kulit.
"""
        },
        {
            "judul": "10. Temulawak (Curcuma xanthorrhiza Roxb.)",
            "isi": """
Temulawak batang semu besar, daun lebar seperti pisang, bunga merah mencolok. Rimpang besar jingga kecoklatan, aroma tajam. Digunakan untuk gangguan pencernaan, radang lambung, diabetes, cacingan, penambah nafsu makan.
"""
        },
    ]

    for tanaman in data_rimpang:
        with st.expander(tanaman["judul"]):
            st.markdown(tanaman["isi"])

if __name__ == "__main__":
    app()
