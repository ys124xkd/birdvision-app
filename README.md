# BirdVision-App 🐦

**BirdVision-App** adalah aplikasi web berbasis **Computer Vision** untuk mengenali dan mengklasifikasikan jenis burung secara otomatis menggunakan **MobileNetV2**. Sistem ini dikembangkan menggunakan **Python** dan **Streamlit**, sehingga mudah digunakan oleh pengguna awam maupun peneliti pemula.

Aplikasi ini mendukung edukasi, konservasi, dan penelitian terkait keanekaragaman burung di Indonesia.

---

## 🔹 Fitur
- Prediksi jenis burung dari gambar secara otomatis.
- Mendukung 6 spesies burung:
  - **American Goldfinch**
  - **Barn Owl**
  - **Carmine Bee-eater**
  - **Downy Woodpecker**
  - **Emperor Penguin**
  - **Flamingo**
- Menampilkan tingkat akurasi prediksi (*confidence score*).
- Antarmuka pengguna interaktif dan mudah digunakan.
- Sistem berbasis web, dapat dijalankan secara lokal atau online.

---

## 🌐 Demo
Coba aplikasi secara langsung di:  
[BirdVision-App Online](https://birdvision-app.streamlit.app/)

---

## 🗂️ Dataset
Dataset yang digunakan dalam penelitian ini berasal dari platform **Kaggle** dengan judul **Bird Species Image Classification**. Dataset tersebut berisi berbagai citra burung yang digunakan untuk proses pelatihan dan pengujian model klasifikasi.

Dataset dapat diakses melalui tautan berikut:  
https://www.kaggle.com/datasets/rahmasleam/bird-speciees-dataset

Dalam penelitian ini, hanya **6 jenis burung** yang digunakan sebagai kelas klasifikasi, yaitu:

- American Goldfinch  
- Barn Owl  
- Carmine Bee-eater  
- Downy Woodpecker  
- Emperor Penguin  
- Flamingo  

Dataset kemudian diproses melalui beberapa tahapan, yaitu **preprocessing data**, **training model**, dan **evaluasi model** menggunakan arsitektur **MobileNetV2**.

---

## 🛠️ Instalasi

### 1. Clone repository
```bash
git clone https://github.com/username/birdvision-app.git
cd birdvision-app
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Jalankan aplikasi
```bash
streamlit run app.py
```

---

## ⚙️ Teknologi yang Digunakan
- Python
- TensorFlow / Keras
- MobileNetV2
- Streamlit
- NumPy
- Matplotlib

---

## 📌 Tujuan Pengembangan
Aplikasi ini dikembangkan untuk:
- Membantu proses identifikasi burung secara otomatis.
- Mendukung kegiatan edukasi dan penelitian di bidang **Computer Vision**.
- Memberikan contoh implementasi **Deep Learning berbasis web** yang mudah digunakan.

---

## 📄 Lisensi
Proyek ini dikembangkan untuk tujuan **edukasi dan penelitian**.
