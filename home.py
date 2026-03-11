import streamlit as st

def show():
    # ===== HEADER UTAMA =====
    st.subheader("🌟 Selamat datang di **BirdVision**")
    st.write("""
    BirdVision adalah platform berbasis AI yang membantu Anda mengenali berbagai 
    spesies burung secara **mudah, cepat, dan interaktif**.

    Anda hanya perlu mengunggah gambar burung, dan sistem akan melakukan identifikasi 
    secara otomatis. Sangat cocok untuk pelajar, peneliti, pecinta burung, maupun 
    pengguna umum yang ingin mengenal dunia burung lebih jauh.
    """)

    # ===== CSS RESPONSIVE + PERBAIKAN CARD =====
    st.markdown("""
        <style>
        /* Gambar hero responsif */
        .hero-img img {
            max-width: 100%;
            height: auto;
            border-radius: 12px;
        }

        /* Responsif untuk mobile */
        @media (max-width: 768px) {
            div[data-testid="column"] {
                width: 100% !important;
                display: block;
                margin-bottom: 1rem;
            }
        }

        /* Caption deskripsi burung */
        .caption-text {
            text-align: justify;
            font-size: 0.9rem;
            margin-bottom: 1rem;
        }

        /* Card fitur utama – warna putih */
        .feature-card {
            background-color: #ffffff !important;
            color: #000000 !important;   /* 🔥 Fix utama: teks jadi hitam */
            border-radius: 12px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 10px rgba(0,0,0,0.15);
            text-align: center;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # ==============================
    # 🐦 SPESIES BURUNG
    # ==============================
    st.subheader("🐦 Spesies Burung dalam Dataset")

    birds = [
        {
            "img": "assets/american_goldfinch.jpeg",
            "emoji": "💛",
            "name": "American Goldfinch",
            "desc": "Burung kuning cerah dengan sayap hitam. Umum ditemukan di taman dan ladang bunga matahari."
        },
        {
            "img": "assets/carmine_bee_eater.jpeg",
            "emoji": "❤️",
            "name": "Carmine Bee-eater",
            "desc": "Burung merah cerah pemakan lebah. Hidup berkelompok dan sering terlihat terbang cepat di Afrika."
        },
        {
            "img": "assets/emperor_penguin.jpeg",
            "emoji": "🐧",
            "name": "Emperor Penguin",
            "desc": "Pinguin terbesar yang hidup di Antartika dan mampu bertahan pada suhu ekstrem."
        },
        {
            "img": "assets/barn_owl.jpeg",
            "emoji": "🦉",
            "name": "Barn Owl",
            "desc": "Burung hantu berwajah hati dengan kemampuan melihat sangat baik di malam hari."
        },
        {
            "img": "assets/downy_woodpecker.jpeg",
            "emoji": "🪶",
            "name": "Downy Woodpecker",
            "desc": "Burung pelatuk kecil dari Amerika Utara yang mencari serangga dengan mematuk batang pohon."
        },
        {
            "img": "assets/flamingo.jpeg",
            "emoji": "🦩",
            "name": "Flamingo",
            "desc": "Burung berwarna merah muda yang sering berdiri dengan satu kaki di perairan dangkal."
        }
    ]

    # Tampilkan 2 baris, 3 kolom per baris
    for i in range(0, len(birds), 3):
        cols = st.columns(3, gap="large")
        for col, bird in zip(cols, birds[i:i+3]):
            with col:
                st.image(bird["img"], width=250) 
                st.markdown(
                    f"<p class='caption-text'>{bird['emoji']} <b>{bird['name']}</b> — {bird['desc']}</p>",
                    unsafe_allow_html=True
                )

    st.markdown("---")

    # ===== CARA KERJA =====
    st.subheader("🔍 Bagaimana BirdVision Bekerja?")
    st.write("""
    BirdVision menggunakan teknologi **Computer Vision** dan **Deep Learning** untuk mengenali spesies burung dari gambar.  
    Prosesnya meliputi:
    """)

    st.markdown("""
    1. 🖼️ **Unggah gambar burung**  
    2. 🧠 Sistem melakukan **ekstraksi fitur** seperti warna, pola, dan bentuk  
    3. 🔎 Model memproses gambar menggunakan jaringan CNN  
    4. 📌 Hasil prediksi ditampilkan lengkap dengan informasi spesies  
    """)

    st.markdown("---")

    # ===== TUJUAN & MANFAAT =====
    st.subheader("🎯 Tujuan dan Manfaat Aplikasi")
    st.info("""
    **BirdVision bermanfaat untuk:**  
    - 🎒 Pembelajaran identifikasi burung  
    - 🔬 Penelitian bidang ornitologi  
    - 📸 Pecinta burung untuk mengenali temuan baru  
    - 🌍 Edukasi dan pelestarian keanekaragaman burung  
    """)

    st.markdown("---")

    # ===== FITUR UTAMA =====
    st.subheader("🛠️ Fitur Utama")

    colA, colB, colC = st.columns(3)
    with colA:
        st.markdown("<div class='feature-card'>📤<br><b>Upload Gambar</b><br>Unggah foto burung dari galeri atau kamera.</div>", unsafe_allow_html=True)
    with colB:
        st.markdown("<div class='feature-card'>⚡<br><b>Identifikasi Cepat</b><br>Prediksi spesies burung hanya dalam hitungan detik.</div>", unsafe_allow_html=True)
    with colC:
        st.markdown("<div class='feature-card'>📚<br><b>Informasi Detail</b><br>Dilengkapi deskripsi lengkap dari setiap spesies.</div>", unsafe_allow_html=True)

    st.markdown("---")

    # ===== AJAKAN MENCUBA =====
    st.subheader("🚀 Siap Mencoba?")
    st.success("Unggah gambar burung Anda di menu **Prediksi** dan mulai mengenali spesies burung secara otomatis!")

if __name__ == "__main__":
    show()
