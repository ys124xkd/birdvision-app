import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

def show():
    # ============================================================
    # 🏷️ Judul & Deskripsi
    # ============================================================
    st.subheader("📚 Edukasi Spesies Burung")
    st.write("""
    Burung adalah makhluk menakjubkan yang memainkan peran penting dalam ekosistem bumi. 
    Dari hutan tropis hingga padang salju Antartika, mereka menunjukkan keberagaman luar biasa 
    dalam bentuk, warna, dan perilaku.  

    Burung tidak hanya memberikan keindahan visual dan suara yang menenangkan, tetapi juga 
    berfungsi sebagai penyerbuk, pengendali hama alami, dan indikator kesehatan lingkungan.  
    Memahami perilaku, habitat, dan adaptasi spesies burung sangat penting untuk menjaga 
    keseimbangan ekosistem dan melestarikan keanekaragaman hayati.

    Halaman ini menyajikan beberapa spesies burung dari *Bird Species Dataset* 
    yang dikumpulkan dari berbagai wilayah dunia, lengkap dengan deskripsi rinci, habitat, 
    karakter unik, dan fakta menarik yang bisa menjadi referensi edukatif bagi pelajar, 
    peneliti, atau pecinta burung.  
    Dengan informasi ini, diharapkan pengguna dapat mengenal lebih dekat, menghargai, 
    dan berkontribusi pada pelestarian spesies burung di alam liar.
    """)

    # ============================================================
    # 🔹 Layout kolom 1 - 3 burung pertama
    # ============================================================
    col1, col2, col3 = st.columns(3)

    # ============================================================
    # 🟡 American Goldfinch
    # ============================================================
    with col1:
        st.image("assets/american_goldfinch.jpeg", width=250)
        st.markdown("""
        ### 💛 American Goldfinch (*Spinus tristis*)
        American Goldfinch merupakan burung penyanyi kecil dari keluarga *Fringillidae* 
        yang tersebar luas di Amerika Utara, mulai dari Kanada hingga Meksiko.  
        Burung jantan dikenal karena warna kuning cerahnya yang mencolok dengan kontras hitam 
        pada sayap dan kepala. Warna ini akan memudar menjadi kusam saat musim dingin, 
        sementara betina memiliki warna zaitun kekuningan sepanjang tahun.

        Mereka beradaptasi dengan baik di area terbuka seperti padang rumput, 
        kebun bunga matahari, dan lahan pertanian. Burung ini sepenuhnya *granivora* (pemakan biji),
        dengan makanan utama berupa biji tanaman thistle, aster, dan bunga matahari.  
        Paruhnya yang kecil dan runcing memungkinkan mereka mengupas biji dengan efisien.

        Uniknya, American Goldfinch adalah salah satu dari sedikit burung 
        yang bersarang di akhir musim panas, menunggu hingga biji-bijian melimpah.  
        Dalam ekosistem, mereka membantu penyebaran benih tanaman liar dan menjadi indikator kesehatan lingkungan.  
        Meskipun populasinya stabil, hilangnya habitat alami tetap menjadi ancaman di beberapa daerah.
        """)

    # ============================================================
    # 🦉 Barn Owl
    # ============================================================
    with col2:
        st.image("assets/barn_owl.jpeg", width=250)
        st.markdown("""
        ### 🦉 Barn Owl (*Tyto alba*)
        Barn Owl adalah burung nokturnal dari keluarga *Tytonidae* yang tersebar di hampir seluruh dunia, 
        menjadikannya salah satu burung hantu dengan persebaran terluas.  
        Ciri khasnya adalah wajah berbentuk hati berwarna putih pucat, sayap panjang, 
        dan mata hitam besar yang beradaptasi sempurna untuk penglihatan malam.

        Mereka memiliki pendengaran sangat sensitif, mampu mendeteksi gerakan tikus hanya dari suara gesekan di rerumputan.  
        Saat berburu, Barn Owl terbang dengan senyap berkat struktur bulu yang halus dan aerodinamis.  
        Makanan utamanya meliputi tikus, burung kecil, dan serangga besar — satu ekor bisa memangsa hingga 1.000 tikus per tahun!  

        Sarangnya sering ditemukan di bangunan tua, menara gereja, gua, atau lubang pohon besar.  
        Dalam ekosistem, Barn Owl berfungsi sebagai pengendali alami populasi tikus.  
        Namun, penggunaan pestisida dan hilangnya habitat menjadi ancaman utama bagi mereka.
        """)

    # ============================================================
    # ❤️ Carmine Bee-eater
    # ============================================================
    with col3:
        st.image("assets/Carmine_Bee_eater.jpeg", width=250)
        st.markdown("""
        ### ❤️ Carmine Bee-eater (*Merops nubicus*)
        Carmine Bee-eater adalah burung paling berwarna dari keluarga *Meropidae*, 
        dengan bulu merah muda cerah dan kepala biru muda.  
        Mereka hidup di savana dan daerah berpasir di Afrika sub-Sahara, 
        sering ditemukan di tepi sungai besar.

        Burung ini pemburu udara yang hebat — mereka menangkap lebah, tawon, dan capung di udara.  
        Sebelum memakan lebah, mereka menepuknya di permukaan keras untuk menghilangkan sengatnya terlebih dahulu.  
        Mereka hidup berkoloni besar dan membuat sarang berupa terowongan di tebing pasir.  

        Carmine Bee-eater memiliki peran penting dalam menjaga keseimbangan populasi serangga di alam liar.
        """)

    # ============================================================
    # 🔹 Layout kolom 2 - 3 burung berikutnya
    # ============================================================
    col4, col5, col6 = st.columns(3)

    # ============================================================
    # 🪶 Downy Woodpecker
    # ============================================================
    with col4:
        st.image("assets/downy_woodpecker.jpeg", width=250)
        st.markdown("""
        ### 🪶 Downy Woodpecker (*Dryobates pubescens*)
        Downy Woodpecker merupakan spesies pelatuk terkecil di Amerika Utara (14–17 cm).  
        Bulu hitam-putihnya khas, dengan jantan memiliki titik merah di bagian belakang kepala.  
        Paruhnya digunakan untuk mematuk batang pohon mencari serangga di bawah kulit kayu.

        Mereka menghuni hutan gugur, taman kota, dan area dengan banyak pohon tua.  
        Downy Woodpecker membantu mengontrol hama dan menciptakan lubang pohon 
        yang digunakan burung lain untuk bersarang.  
        Populasi mereka relatif stabil dan beradaptasi baik terhadap lingkungan manusia.
        """)

    # ============================================================
    # 🐧 Emperor Penguin
    # ============================================================
    with col5:
        st.image("assets/emperor_penguin.jpeg", width=250)
        st.markdown("""
        ### 🐧 Emperor Penguin (*Aptenodytes forsteri*)
        Emperor Penguin adalah spesies pinguin terbesar di dunia dan satu-satunya 
        yang berkembang biak di tengah musim dingin Antartika.  
        Mereka bisa mencapai tinggi 120 cm dan berat hingga 40 kg.  

        Saat musim kawin, betina bertelur satu butir lalu meninggalkannya kepada jantan, 
        yang menjaga telur di atas kakinya selama dua bulan tanpa makan.  
        Emperor Penguin mampu menyelam hingga kedalaman 500 meter dan menahan napas selama 20 menit.  
        Populasinya termasuk kategori “Hampir Terancam” akibat pencairan es dan perubahan iklim.
        """)

    # ============================================================
    # 🦩 Flamingo
    # ============================================================
    with col6:
        st.image("assets/flamingo.jpeg", width=250)
        st.markdown("""
        ### 🦩 Flamingo (*Phoenicopterus roseus*)
        Flamingo adalah burung berwarna merah muda dengan leher panjang dan kaki ramping.  
        Mereka hidup di danau garam dan rawa dangkal di Afrika, Asia Selatan, dan Eropa.  
        Warna khas mereka berasal dari pigmen *karotenoid* pada udang kecil dan alga yang mereka makan.

        Paruhnya berfungsi sebagai saringan alami untuk menyaring air berlumpur dan mengambil plankton.  
        Flamingo hidup berkoloni besar hingga puluhan ribu individu dan memiliki perilaku sosial tinggi.  
        Mereka berperan menjaga kualitas air dan keseimbangan ekosistem perairan dangkal.
        """)

    # ============================================================
    # 🎨 CSS Styling
    # ============================================================
    st.markdown("""
    <style>
    .stMarkdown h3 {
        color: #e85d04;
        margin-top: 15px;
    }
    .stMarkdown p {
        text-align: justify;
        font-size: 15px;
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)
