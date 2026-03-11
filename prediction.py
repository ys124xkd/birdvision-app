import streamlit as st
from tensorflow.keras.preprocessing import image
import tensorflow as tf
import numpy as np
from PIL import Image
import os

# ============================================================
# 🧠 FUNGSI UNTUK MEMUAT & MEMPROSES PREDIKSI
# ============================================================
@st.cache_resource
def load_model():
    model_path = "model_mobilenetv2_bird_augmented.h5"  # tetap file model internal
    if not os.path.exists(model_path):
        st.error("❌ File prediksi tidak ditemukan! Pastikan file terkait ada di folder project.")
        st.stop()
    return tf.keras.models.load_model(model_path)


# ============================================================
# 📚 DESKRIPSI SETIAP JENIS BURUNG
# ============================================================
BIRD_INFO = {
    "AMERICAN GOLDFINCH": """
    🟡 **American Goldfinch** merupakan burung kecil berwarna kuning cerah yang berasal dari Amerika Utara.  
    Burung ini suka berpindah tempat sesuai musim — bermigrasi ke selatan saat musim dingin.  
    Makanannya berupa biji-bijian, terutama bunga matahari dan thistle.
    """,

    "BARN OWL": """
    🤍 **Barn Owl (Tyto alba)** adalah burung hantu berwajah hati yang tersebar luas di hampir seluruh dunia.  
    Mereka berburu tikus di malam hari dengan pendengaran tajam.  
    Biasanya ditemukan di lumbung, ladang, dan area pedesaan.
    """,

    "CARMINE BEE-EATER": """
    ❤️ **Carmine Bee-eater** adalah burung merah muda terang yang berasal dari Afrika bagian selatan.  
    Mereka memangsa lebah dan serangga terbang lainnya yang ditangkap di udara.  
    Burung ini sering terlihat berkelompok di tebing sungai atau dataran terbuka.
    """,

    "DOWNY WOODPECKER": """
    ⚫ **Downy Woodpecker** adalah jenis pelatuk terkecil di Amerika Utara.  
    Kepala hitam-putih dengan bintik merah di bagian belakang kepala jantan adalah ciri khasnya.  
    Mereka suka mematuk batang pohon untuk mencari serangga kecil.
    """,

    "EMPEROR PENGUIN": """
    🐧 **Emperor Penguin** merupakan penguin terbesar di dunia dan hidup di Antartika.  
    Burung ini terkenal dengan kebiasaan bertelur dan mengerami di musim dingin ekstrem.  
    Jantan menjaga telur di kaki sambil menunggu betina kembali dari laut.
    """,

    "FLAMINGO": """
    🦩 **Flamingo** dikenal dengan warna merah muda khasnya yang berasal dari pigmen pada makanan, seperti udang.  
    Hidup berkelompok besar di daerah rawa atau laguna asin, dengan kaki panjang dan paruh melengkung untuk menyaring makanan dari air.
    """
}


# ============================================================
# 🔍 FUNGSI UNTUK MEMBUAT PREDIKSI BURUNG
# ============================================================
def predict_bird(model, img):
    img = img.resize((224, 224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    predictions = model.predict(img_array)
    pred_idx = np.argmax(predictions)
    pred_label = sorted(list(BIRD_INFO.keys()))[pred_idx]
    confidence = float(np.max(predictions) * 100)
    return pred_label, confidence


# ============================================================
# 🎨 HALAMAN STREAMLIT UNTUK PREDIKSI BURUNG
# ============================================================
def show():
    st.subheader("🕊️ Prediksi Jenis Burung")

    st.markdown("""
    Unggah **satu atau beberapa gambar burung** dan sistem akan menampilkan jenis burung secara otomatis.  
    Dataset referensi: **Bird Species Dataset (Kaggle)** 🐦.
    """)

    st.info("📸 Format yang didukung: JPG, JPEG, PNG (bisa lebih dari satu)")

    uploaded_files = st.file_uploader(
        "Unggah gambar burung di sini",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True
    )

    if uploaded_files:
        model = load_model()

        for idx, uploaded_file in enumerate(uploaded_files):
            st.markdown(f"### 📷 Gambar {idx + 1}")
            col1, col2 = st.columns([1, 1])

            with col1:
                st.image(uploaded_file, caption=f"Gambar {idx + 1}", width=250)

            with col2:
                st.write("### 🔍 Hasil Prediksi")
                with st.spinner("Sedang memproses gambar..."):
                    img = Image.open(uploaded_file).convert("RGB")
                    pred_label, confidence = predict_bird(model, img)

                st.success(f"🕊️ Jenis Burung: **{pred_label}**")
                st.metric(label="🎯 Tingkat Keyakinan", value=f"{confidence:.2f}%")
                st.progress(confidence / 100)

                st.markdown("### 📖 Keterangan")
                st.info(BIRD_INFO[pred_label])

            st.markdown("---")

    else:
        st.warning("⬆️ Silakan unggah satu atau beberapa gambar untuk memulai prediksi.")
