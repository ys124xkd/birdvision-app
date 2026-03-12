# BirdVision-App 🐦

**BirdVision-App** adalah aplikasi web berbasis **Computer Vision** untuk mengenali dan mengklasifikasikan jenis burung secara otomatis menggunakan **MobileNetV2**. Sistem ini dikembangkan menggunakan **Python** dan **Streamlit**, sehingga mudah digunakan oleh pengguna awam maupun peneliti pemula.

Aplikasi ini mendukung edukasi, konservasi, dan penelitian terkait keanekaragaman burung di Indonesia.

---

## 🔹 Tampilan Aplikasi

### Halaman Utama
![Home Page](assets/home.png)

### Education
![Prediction Page](assets/education.png)

### Upload dan Prediksi Gambar
![Prediction Page](assets/prediction.png)

### Hasil Klasifikasi
![Result Page](assets/result.png)

---

## 📊 Evaluasi Model

Evaluasi model dilakukan untuk mengetahui performa model **MobileNetV2** dalam melakukan klasifikasi citra burung. Proses evaluasi meliputi analisis **akurasi training dan validation**, **kurva loss**, serta **confusion matrix** untuk melihat distribusi prediksi pada setiap kelas.

### Kurva Accuracy
Kurva accuracy menunjukkan perkembangan nilai akurasi selama proses training dan validation pada setiap epoch.

![Accuracy Curve](images/accuracy_curve.png)

---

### Kurva Loss
Kurva loss digunakan untuk melihat bagaimana model meminimalkan kesalahan selama proses training dan validation.

![Loss Curve](images/loss_curve.png)

---

### Metric Performa Model
Beberapa metrik evaluasi yang digunakan dalam penelitian ini meliputi:

- **Accuracy**
- **Precision**
- **Recall**
- **F1-score**

Metric ini digunakan untuk mengukur seberapa baik model dalam melakukan klasifikasi terhadap masing-masing kelas burung.

![Performance Metrics](images/performance_metrics.png)

---

### Confusion Matrix
Confusion matrix digunakan untuk menganalisis hasil prediksi model terhadap setiap kelas burung, sehingga dapat diketahui jumlah prediksi yang benar maupun kesalahan klasifikasi.

![Confusion Matrix](images/confusion_matrix.png)

Confusion matrix membantu dalam memahami distribusi kesalahan prediksi antar kelas serta mengevaluasi kemampuan model dalam membedakan setiap spesies burung.

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
