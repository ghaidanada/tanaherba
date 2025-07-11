import streamlit as st
from PIL import Image
import base64
import os
import tensorflow as tf
import numpy as np
from tensorflow.keras.applications.efficientnet import preprocess_input  # type: ignore

def main():
    st.title("Prediksi Page")
    st.write("Welcome to the Prediksi Page.")

if __name__ == "__main__":
    main()

def app():
    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

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

    # Tambahan Styling Aman Dark Mode
    st.markdown('''
        <style>
        .stButton > button {
            background-color: #4863A0;
            color: white;
            border-radius: 8px;
            padding: 0.5em 1.5em;
            font-size: 16px;
            margin-top: 10px;
            margin-left: 100px;
        }
        .centered-header {
            text-align: center;
            font-size: 16px;
            margin-bottom: 10px;
            color: inherit;
        }
        .hasil-box {
            padding: 15px;
            border-radius: 10px;
            background-color: rgba(220, 255, 220, 0.1);
            color: white;
            border: 1px solid #4CAF50;
        }
        .hasil-title {
            color: #4CAF50;
            font-weight: bold;
            font-size: 20px;
        }
        .hasil-subtitle {
            color: #CCCCCC;
        }
        .hasil-prob {
            color: #FFD700;
            font-weight: bold;
        }
        @media (prefers-color-scheme: light) {
            .block-container {
                background-color: rgba(255, 255, 255, 0.95);
                color: black;
            }
            .hasil-box {
                background-color: #dff0d8;
                color: black;
            }
            .hasil-title {
                color: #2e6da4;
            }
            .hasil-subtitle {
                color: #333333;
            }
            .hasil-prob {
                color: #333333;
            }
        }
        @media (prefers-color-scheme: dark) {
            .block-container {
                background-color: rgba(30, 30, 30, 0.95);
                color: white;
            }
        }
        </style>
    ''', unsafe_allow_html=True)

    st.markdown('<h2 class="centered-header" style="margin-top: -40px;">Klasifikasi Tanaman Herbal 🌱</h2>', unsafe_allow_html=True)

    with st.expander("💡 Cara Menggunakan Aplikasi"):
        st.markdown("""
        1. Unggah gambar tanaman rimpang.
        2. Sistem akan menganalisis dan memprediksi jenis rimpang tersebut.
        3. Hasil klasifikasi dan tingkat kepercayaan ditampilkan secara otomatis.
        """)

    class_names = {
        0: 'bengle',
        1: 'dringo',
        2: 'jahe',
        3: 'kencur',
        4: 'kunyit',
        5: 'lempuyang',
        6: 'lengkuas',
        7: 'temu_hitam',
        8: 'temu_kunci',
        9: 'temulawak'
    }

    keras_model = tf.keras.models.load_model('best_model6augmen__EfficientnetB0rimpang.keras')

    def classify_image(image):
        image = image.convert('RGB')
        image = image.resize((224, 224))
        image = np.array(image).astype('float32')
        image = preprocess_input(image)
        image = np.expand_dims(image, axis=0)
        predictions = keras_model.predict(image)
        predicted_class_idx = np.argmax(predictions, axis=1)[0]
        predicted_class = class_names[predicted_class_idx]
        predicted_prob = predictions[0][predicted_class_idx]
        return predicted_class, predicted_prob, predictions[0]

    ciri_ciri_rimpang = {
        'bengle': 'Rimpang kuning kehijauan, aroma tajam, rasa agak pahit dan pedas.',
        'dringo': 'Rimpang merah jambu, aroma kuat seperti jahe.',
        'jahe': 'Rimpang bercabang, kulit keras, aroma pedas khas.',
        'kencur': 'Rimpang kecil, membulat, kulit kecokelatan, aroma tajam.',
        'kunyit': 'Rimpang jingga terang di dalam, kulit jingga kecoklatan.',
        'lempuyang': 'Rimpang besar memanjang, bagian dalam kuning pucat.',
        'lengkuas': 'Rimpang besar berserat, kulit mengkilap, rasa pedas manis.',
        'temu_hitam': 'Rimpang gelap keunguan, bagian dalam ada pola biru.',
        'temu_kunci': 'Rimpang ramping, warna cokelat kekuningan.',
        'temulawak': 'Rimpang besar, luar kuning tua, dalam jingga kecoklatan, aroma tajam.'
    }

    uploaded_file = st.file_uploader("📁 Unggah gambar tanaman rimpang Anda di sini:", type=['jpg', 'jpeg', 'png'])

    col1, col2, col3 = st.columns([1, 3, 1])

    with col2:
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            predicted_class, predicted_prob, all_probs = classify_image(image)

            st.image(image, caption='Gambar Tanaman Herbal', use_container_width=True)

            threshold = 0.5
            if predicted_prob >= threshold:
                st.success("✅ Tanaman Rimpang Terdeteksi")
                st.markdown(f"""
                    <div class='hasil-box'>
                        <h4 class='hasil-title'>Jenis Tanaman: {predicted_class.capitalize()}</h4>
                        <p class='hasil-subtitle'><b>Ciri-ciri:</b> {ciri_ciri_rimpang.get(predicted_class, '-')}</p>
                        <p class='hasil-prob'><b>Probabilitas:</b> {predicted_prob:.2%}</p>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.error("⚠️ Gambar tidak terdeteksi sebagai salah satu tanaman rimpang dalam sistem. Pastikan gambar jelas dan sesuai.")

    col_btn = st.columns(3)
    with col_btn[1]:
        if st.button("🔙 Kembali ke Beranda"):
            st.session_state.menu = "Beranda"
            st.rerun()
