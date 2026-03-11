import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import os

# ============================================================
# 🧠 FUNGSI UNTUK MEMUAT MODEL
# ============================================================
@st.cache_resource  # cache model agar tidak load berulang
def load_model():
    model_path = os.path.join(os.path.dirname(__file__), "model_mobilenetv2_bird_augmented.h5")
    if not os.path.exists(model_path):
        st.error("❌ File model tidak ditemukan! Pastikan file terkait ada di folder project.")
        st.stop()
    try:
        # Pakai compile=False untuk mencegah error InputLayer batch_shape
        model = tf.keras.models.load_model(model_path, compile=False)
    except Exception as e:
        st.error(f"❌ Gagal memuat model. Error: {e}")
        st.stop()
    return model

# ============================================================
# 📚 DESKRIPSI SETIAP JENIS BURUNG
# ============================================================
BIRD_INFO = {
    "AMERICAN GOLDFINCH": "🟡 **American Goldfinch** merupakan burung kecil berwarna kuning cerah dari Amerika Utara. Makanannya biji-bijian, terutama bunga matahari dan thistle.",
    "BARN OWL": "🤍 **Barn Owl (Tyto alba)** adalah burung hantu berwajah hati yang tersebar luas di seluruh dunia. Mereka berburu tikus di malam hari.",
    "CARMINE BEE-EATER": "❤️ **Carmine Bee-eater** adalah burung merah muda terang dari Afrika selatan. Memangsa lebah dan serangga terbang lainnya.",
    "DOWNY WOODPECKER": "⚫ **Downy Woodpecker** adalah pelatuk terkecil di Amerika Utara, kepala hitam-putih dengan bintik merah di bagian belakang kepala jantan.",
    "EMPEROR PENGUIN": "🐧 **Emperor Penguin** penguin terbesar di dunia yang hidup di Antartika. Jantan menjaga telur di kaki sambil menunggu betina kembali dari laut.",
    "FLAMINGO": "🦩 **Flamingo** dikenal warna merah muda dari pigmen makanan. Hidup berkelompok besar di rawa atau laguna asin."
}

# ============================================================
# 🔍 FUNGSI UNTUK MEMBUAT PREDIKSI
# ============================================================
def predict_bird(model, img: Image.Image):
    try:
        img = img.resize((224, 224))
        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        predictions = model.predict(img_array)
        pred_idx = np.argmax(predictions)
        pred_label = sorted(list(BIRD_INFO.keys()))[pred_idx]
        confidence = float(np.max(predictions) * 100)
        return pred_label, confidence
    except Exception as e:
        raise RuntimeError(f"Gagal prediksi: {e}")

# ============================================================
# 🎨 HALAMAN STREAMLIT UNTUK PREDIKSI BURUNG
# ============================================================
def show():
    st.subheader("🕊️ Prediksi Jenis Burung")
    st.markdown("""
Unggah **satu atau beberapa gambar burung** dan sistem akan menampilkan jenis burung secara otomatis.  
Dataset referensi: **Bird Species Dataset (Kaggle)** 🐦
""")
    st.info("📸 Format yang didukung: JPG, JPEG, PNG (bisa lebih dari satu)")

    uploaded_files = st.file_uploader(
        "Unggah gambar burung di sini",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True
    )

    if uploaded_files:
        model = load_model()  # load model sekali saja

        for idx, uploaded_file in enumerate(uploaded_files):
            st.markdown(f"### 📷 Gambar {idx + 1}")
            col1, col2 = st.columns([1, 1])

            with col1:
                st.image(uploaded_file, caption=f"Gambar {idx + 1}", use_column_width=True)

            with col2:
                st.write("### 🔍 Hasil Prediksi")
                with st.spinner("Sedang memproses gambar..."):
                    try:
                        img = Image.open(uploaded_file).convert("RGB")
                        pred_label, confidence = predict_bird(model, img)
                    except Exception as e:
                        st.error(f"❌ Gagal memproses gambar: {e}")
                        continue

                st.success(f"🕊️ Jenis Burung: **{pred_label}**")
                st.metric(label="🎯 Tingkat Keyakinan", value=f"{confidence:.2f}%")
                st.progress(min(confidence / 100, 1.0))  # pastikan max 1.0

                st.markdown("### 📖 Keterangan")
                st.info(BIRD_INFO.get(pred_label, "❌ Informasi tidak tersedia"))

            st.markdown("---")
    else:
        st.warning("⬆️ Silakan unggah satu atau beberapa gambar untuk memulai prediksi.")
