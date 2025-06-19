import streamlit as st
import os
import base64

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def app():
    # Tambahkan logo jika ada
    logo_path = "tanaherba.png"
    # Header logo
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

    st.markdown('<h2 style="text-align: center; margin-top: -40px;">Jenis-Jenis Tanaman Rimpang 🌱</h2>', unsafe_allow_html=True)

    # Data tanaman rimpang
    data_rimpang = [
        {
            "judul": "1. Bengle (Zingiber purpureum Roxb.)",
            "isi": """
Bengle (Zingiber purpureum Roxb.) merupakan tanaman herba yang tumbuh membentuk rumpun yang rapat yaitu beberapa batang yang muncul dari satu rimpang tumbuh berdekatan dan membentuk kelompok tanaman yang menyatu. Tinggi tanaman dapat mencapai sekitar 150 cm, dengan batang semu berdiameter sekitar 1,5 cm. Daunnya memiliki permukaan yang halus dan tidak berbulu.

Rimpang bengle biasanya berwarna kuning kehijauan dan memiliki cita rasa yang khas, yaitu agak pahit dan pedas. Aromanya cenderung tajam dan tidak sedap, yang berasal dari kandungan minyak atsiri, damar, pati, dan tannin. Bagian tanaman bengle yang paling banyak dimanfaatkan untuk pengobatan adalah rimpangnya. Secara tradisional, rimpang bengle digunakan sebagai obat herbal untuk mengatasi berbagai gangguan kesehatan, seperti cacingan, sebagai karminatif (peluruh gas), sembelit, masuk angin, serta sebagai bahan obat gosok. 
"""
        },
        {
            "judul": "2. Dringo (Alpinia galanga) ",
            "isi": """
Dringo (Alpinia galanga) termasuk dalam famili Araceae dan dikenal sebagai tanaman dengan tinggi sekitar 55 hingga 80 cm. Daunnya berbentuk seperti pita dengan urat daun sejajar, memiliki panjang sekitar 80 cm dan lebar 7 hingga 20 mm. Tulang daun bagian tengahnya kuat, berujung lancip, serta mengeluarkan aroma harum. Perbungaannya tersusun dalam bentuk tongkol, dan buahnya berbentuk seperti gasing serta berlendir. Rimpanng  dringo berupa rimpang berwarna merah jambu dengan diameter antara 7,5 hingga 15 mm. 

Bagian yang dimanfaatkan untuk keperluan obat adalah rimpangnya yang mengandung minyak atsiri sebanyak 1,5 hingga 3,5%, asaron, serta senyawa zat pahit lainnya. Secara tradisional, dringo digunakan sebagai insektisida, pengobatan demam nifas, karminatif, disentri, pembengkakan limpa, dan sebagai penambah nafsu makan.
"""
        },
        {
            "judul": "3. Jahe (Zingiber officinale)",
            "isi": """
Jahe (Zingiber officinale) merupakan tanaman herba yang memiliki batang semu dan tumbuh secara berumpun dengan ketinggian antara 30 hingga 100 cm. Daunnya berbentuk seperti pita dan tersusun dalam dua baris berseling. Bunga jahe muncul dari rimpang dengan tangkai yang memanjang. Rimpangnya bercabang, memiliki kulit yang cukup keras dan bertekstur, serta daging berwarna kuning hingga jingga dengan aroma khas yang menyengat. Terdapat tiga jenis jahe yang umum dikenal, yaitu jahe gajah (jahe putih besar), jahe emprit, dan jahe merah (juga dikenal sebagai jahe sunti).

Bagian tanaman yang dimanfaatkan sebagai obat adalah rimpangnya, yang mengandung senyawa aktif seperti minyak atsiri, gingerol, zingeron, resin, pati, serta gula. Jahe memiliki berbagai manfaat bagi kesehatan, antara lain sebagai penurun demam, membantu melancarkan sistem pencernaan, meredakan gangguan pernapasan, mengencerkan dahak, memberikan sensasi hangat pada tubuh, serta mengatasi gejala seperti perut kembung, mulas, bronkitis, dan sakit kepal. 
"""
        },
        {
            "judul": "4. Kencur (Kaempferia galanga) ",
            "isi": """
Kencur (Kaempferia galanga) merupakan tanaman herba berukuran kecil yang tumbuh merayap dan tidak memiliki batang, dengan daun yang lebar dan berdaging. Daunnya biasanya memiliki pelepah yang tersembunyi di dalam tanah. Bunga kencur tersusun dalam bentuk bulir atau bongkol yang muncul dekat permukaan tanah. Rimpangnya bercabang banyak, bahkan sebagian tumbuh di atas permukaan tanah. Pada bagian akar juga sering dijumpai umbi yang berbentuk bulat.

Bagian tanaman yang dimanfaatkan sebagai bahan obat adalah rimpangnya. Rimpang kencur mengandung minyak atsiri sebesar 2,4–3,9%, dengan senyawa utama seperti borneol, kamfer, sineol, dan etil alkohol. Kencur memiliki berbagai manfaat untuk kesehatan, antara lain meredakan radang tenggorokan, batuk, pilek, nyeri perut, radang lambung, serta masuk angin. Selain itu, kencur juga digunakan untuk memperlancar haid, membantu melangsingkan tubuh, sebagai bahan obat gosok, dan untuk menurunkan panas dalam.
"""
        },
        {
            "judul": "5. Kunyit (Curcuma longa L.)",
            "isi": """
Kunyit (Curcuma longa L.) merupakan tanaman herba yang memiliki batang berwarna hijau keunguan dan daun berbentuk jumbai. Bunganya biasanya tumbuh di ujung batang semu dengan panjang sekitar 10–15 cm, berwarna putih hingga kuning pucat. Umbi utamanya berbentuk bulat memanjang, sedangkan rimpang-rimpang samping berukuran pendek dan tebal, tumbuh secara lurus maupun bengkok, serta bercabang membentuk rumpun. Bagian luar rimpang tampak jingga kecoklatan, sedangkan bagian dalamnya berwarna jingga terang atau kekuningan.

Bagian yang dimanfaatkan sebagai bahan obat adalah rimpangnya. Rimpang kunyit mengandung minyak atsiri sebesar 3–5%, serta senyawa aktif seperti kurkumin, pati, tannin, dan damar. Kunyit memiliki berbagai manfaat kesehatan, antara lain untuk mengatasi gangguan pencernaan seperti sakit perut dan diare, berfungsi sebagai pencahar, antiseptik, serta membantu mengatasi peradangan pada selaput lendir mulut, pendarahan, luka kulit (koreng), asma, dan juga sebagai stimulan nafsu makan.
"""
        },
        {
            "judul": "6. Lempuyang (Zingiber zerumbet L.)",
            "isi": """
Lempuyang (Zingiber zerumbet L.) adalah salah satu jenis tanaman rempah-rempah yang memiliki khasiat obat dan termasuk dalam famili Zingiberaceae. Terdapat tiga jenis utama lempuyang, yaitu lempuyang wangi, lempuyang emprit, dan lempuyang gajah. Secara morfologis, tanaman ini menyerupai laos, baik dari segi pohon maupun daunnya, namun memiliki bunga yang lebih indah. Tinggi tanaman lempuyang gajah bahkan bisa melebihi laos. Tanaman ini berbatang semu yang terbentuk dari pelepah daun berbentuk bulat. Daunnya berwarna hijau dengan susunan berseling, berbentuk bulat telur memanjang, berujung runcing, dan tepi rata. Bunganya muncul dari batang yang berada di dalam tanah dan berbentuk tandan berwarna hijau kemerahan atau keunguan. Akar tanaman ini berupa rimpang yang membesar menyerupai buah dan tumbuh di dalam tanah. 

Bagian tanaman yang umum dimanfaatkan sebagai obat adalah rimpangnya. Rimpang lempuyang mengandung berbagai senyawa aktif seperti minyak atsiri (zerumbone), alkaloid, fenolik, saponin, flavonoid, triterpenoid, dan tanin. Kandungan senyawa tersebut menjadikan lempuyang berkhasiat untuk mengatasi berbagai gangguan kesehatan, seperti penyakit asam lambung, meningkatkan peredaran darah, menambah stamina dan vitalitas, meningkatkan nafsu makan, serta membantu mengatasi ambeien, anemia, cacingan, dan bahkan memiliki potensi sebagai antikanker dan antitumor. 
"""
        },
        {
            "judul": "7. TLengkuas (Alpinia galanga)",
            "isi": """
Lengkuas (Alpinia galanga) merupakan tanaman herbal yang termasuk dalam kelompok rimpang, seperti halnya jahe dan kunyit. Tanaman ini memiliki batang yang dapat tumbuh hingga ketinggian lebih dari dua meter, dengan rimpang yang berada di dalam tanah dan akar yang kecil. Tunas batang muda biasanya tumbuh dari pangkal batang yang lebih tua. Daunnya berbentuk tunggal, memiliki tangkai pendek, ujung runcing, pangkal tumpul, dan tepi daun yang rata. Kulit rimpangnya tampak mengkilap, berbeda dari jenis rimpang lainnya. Rimpang lengkuas memiliki cita rasa yang khas, yaitu manis, pedas, dan sedikit panas.

Salah satu manfaat pentingnya adalah sebagai antijamur, berkat kandungan senyawa aktif seperti diterpene dan eugenol yang bersifat antimikroba. Parutan rimpangnya secara tradisional digunakan untuk mengobati berbagai masalah kulit akibat infeksi jamur, seperti panu, kurap, jerawat, eksim, bisul, dan korengan. Lengkuas juga mengandung senyawa minyak atsiri sekitar 1%, yang berwarna kuning kehijauan. Komponen utama dari minyak ini meliputi metil sinamat (48%), sineol (20–30%), eugenol, kamfer, serta berbagai senyawa lain seperti galangin, apinen, camphor, seskuiterpen, dan galangol. 
"""
        },
        {
            "judul": "8. Temu Hitam (Curcuma aeruginosa Roxb.) ",
            "isi": """
Temu Hitam (Curcuma aeruginosa Roxb.) merupakan tanaman yang memiliki batang semu dan dapat tumbuh tegak hingga mencapai ketinggian sekitar dua meter. Ciri khas tanaman ini terletak pada rimpangnya yang apabila diiris akan memperlihatkan lingkaran-lingkaran berwarna biru atau kelabu pada bagian dalam. Daun temu hitam berbentuk lebar menyerupai daun pisang dengan warna merah tua, serta pelepah daun yang biasanya menutupi seluruh batang. Bunganya tumbuh di sisi batang dengan mahkota berwarna merah mencolok. 

Bagian yang dimanfaatkan untuk keperluan pengobatan adalah rimpangnya, yang mengandung sekitar 2% minyak atsiri, pati, damar, dan lemak. Secara tradisional, temu hitam digunakan untuk mengobati cacingan, meningkatkan nafsu makan, meredakan nyeri akibat rematik, mengatasi penyakit kulit seperti kudis, serta membantu membersihkan darah setelah masa haid.
"""
        },
        {
            "judul": "9. Temu Kunci (Boesenbergia rotunda) ",
            "isi": """
Temu Kunci (Boesenbergia rotunda) merupskan tanaman yang umumnya tidak memiliki batang dan tumbuh dengan rimpang yang berada di dalam tanah. Rimpang temu kunci memiliki panjang antara 5 hingga 30 cm dengan diameter 0,5 hingga 2 cm, serta berwarna cokelat kekuningan. Tanaman ini biasanya memiliki 2 hingga 7 helai daun, dan bunganya muncul di pucuk daun.

Bagian tanaman yang dimanfaatkan sebagai obat adalah rimpangnya, yang mengandung minyak atsiri dengan kadar 0,06 hingga 0,32%, damar, dan pati. Secara tradisional, temu kunci digunakan untuk mengatasi berbagai keluhan kesehatan seperti diare, sariawan, batuk kering, serta sebagai obat untuk gatal-gatal atau kurap. Minyak atsiri yang diperoleh dari destilasi rimpang temu kunci hampir tidak berwarna dan memiliki aroma yang mirip dengan estragon dan basilikum.
"""
        },
        {
            "judul": "10. Temulawak (Curcuma xanthorrhiza Roxb.)",
            "isi": """
Temulawak (Curcuma xanthorrhiza Roxb.), yang juga dikenal sebagai koneng gede, merupakan tanaman dengan batang semu yang dapat tumbuh hingga mencapai ketinggian sekitar dua meter. Daunnya memiliki bentuk melebar menyerupai daun pisang dengan ujung yang lancip, dan pelepah daun yang tumbuh menutupi seluruh batang. Bunga temulawak muncul di sisi batang dengan mahkota berwarna merah mencolok. Rimpang induk temulawak berukuran besar dan berbentuk bulat, dengan bagian luar berwarna kuning tua atau cokelat kemerahan, sedangkan bagian dalamnya berwarna jingga kecoklatan. Rimpang ini memiliki cabang-cabang kecil dan menghasilkan aroma harum yang tajam. Rasa rimpang cenderung pahit dan agak pedas saat dikonsumsi.  

Bagian tanaman yang dimanfaatkan sebagai obat adalah rimpangnya karena mengandung zat aktif seperti kurkumin, minyak atsiri berupa kamfer, sikloisopren, xantorizal, damar, pati, dan mineral. Secara tradisional, temulawak digunakan untuk mengobati berbagai penyakit seperti diare, radang lambung, diabetes mellitus, gangguan ginjal, cacingan, cacar, serta sebagai penambah nafsu makan. 
"""
        },
    ]

    for tanaman in data_rimpang:
        with st.expander(tanaman["judul"]):
            st.markdown(tanaman["isi"])

# Menjalankan aplikasi
if __name__ == "__main__":
    app()
