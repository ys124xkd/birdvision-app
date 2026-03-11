import streamlit as st
from PIL import Image
import os
import requests
from io import BytesIO

def load_image(img_path):
    """
    Load image dari path lokal atau URL. 
    Return None jika gagal load.
    """
    try:
        if img_path.startswith("http"):
            response = requests.get(img_path)
            img = Image.open(BytesIO(response.content))
        else:
            img = Image.open(img_path)
        return img
    except Exception as e:
        st.warning(f"⚠️ Tidak bisa memuat gambar: {img_path}")
        return None

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
    # 🔹 List burung
    # ============================================================
    birds = [
        {"img": "assets/american_goldfinch.jpeg", "emoji": "💛", "name": "American Goldfinch (*Spinus tristis*)", "desc": """American Goldfinch merupakan burung penyanyi kecil dari keluarga *Fringillidae* yang tersebar luas di Amerika Utara. Burung jantan dikenal karena warna kuning cerahnya yang mencolok dengan kontras hitam pada sayap dan kepala. Warna ini akan memudar menjadi kusam saat musim dingin, sementara betina memiliki warna zaitun kekuningan sepanjang tahun. Mereka beradaptasi dengan baik di area terbuka seperti padang rumput dan kebun bunga matahari. Populasi mereka stabil, meskipun hilangnya habitat tetap menjadi ancaman."""},
        {"img": "assets/barn_owl.jpeg", "emoji": "🦉", "name": "Barn Owl (*Tyto alba*)", "desc": """Barn Owl adalah burung nokturnal dengan wajah berbentuk hati berwarna putih pucat, sayap panjang, dan mata hitam besar yang beradaptasi sempurna untuk penglihatan malam. Mereka memiliki pendengaran sangat sensitif dan terbang senyap saat berburu. Sarangnya ditemukan di bangunan tua, menara gereja, gua, atau lubang pohon besar. Populasi terancam akibat hilangnya habitat dan penggunaan pestisida."""},
        {"img": "assets/carmine_bee_eater.jpeg", "emoji": "❤️", "name": "Carmine Bee-eater (*Merops nubicus*)", "desc": """Carmine Bee-eater memiliki bulu merah muda cerah dan kepala biru muda. Hidup di savana dan tepi sungai Afrika sub-Sahara. Burung ini menangkap lebah dan serangga di udara, menepuk lebah di permukaan keras untuk menghilangkan sengat. Hidup berkoloni besar dan membuat sarang berupa terowongan di tebing pasir."""},
        {"img": "assets/downy_woodpecker.jpeg", "emoji": "🪶", "name": "Downy Woodpecker (*Dryobates pubescens*)", "desc": """Downy Woodpecker adalah pelatuk terkecil di Amerika Utara. Bulu hitam-putihnya khas, jantan memiliki titik merah di belakang kepala. Paruh digunakan untuk mematuk batang pohon mencari serangga. Mereka membantu mengontrol hama dan membuat lubang pohon yang digunakan burung lain."""},
        {"img": "assets/emperor_penguin.jpeg", "emoji": "🐧", "name": "Emperor Penguin (*Aptenodytes forsteri*)", "desc": """Emperor Penguin adalah pinguin terbesar di dunia dan berkembang biak di musim dingin Antartika. Betina bertelur satu butir dan jantan menjaga telur di atas kakinya selama dua bulan. Dapat menyelam hingga 500 meter dan menahan napas 20 menit. Populasi hampir terancam akibat pencairan es dan perubahan iklim."""},
        {"img": "assets/flamingo.jpeg", "emoji": "🦩", "name": "Flamingo (*Phoenicopterus roseus*)", "desc": """Flamingo berwarna merah muda dengan leher panjang dan kaki ramping. Hidup di danau garam dan rawa dangkal. Warna berasal dari pigmen karotenoid pada udang kecil dan alga yang mereka makan. Paruhnya sebagai saringan alami. Hidup berkoloni besar dan berperan menjaga kualitas air dan keseimbangan ekosistem."""}
    ]

    # ============================================================
    # 🔹 Tampilkan 2 baris x 3 kolom
    # ============================================================
    for i in range(0, len(birds), 3):
        cols = st.columns(3, gap="large")
        for col, bird in zip(cols, birds[i:i+3]):
            with col:
                img = load_image(bird["img"])
                if img:
                    st.image(img, width=250)
                st.markdown(
                    f"### {bird['emoji']} {bird['name']}\n{bird['desc']}",
                    unsafe_allow_html=True
                )

    # ============================================================
    # 🎨 CSS Styling
    # ============================================================
    st.markdown("""
    <style>
    /* Heading h3 */
    .stMarkdown h3 {
        color: #e85d04 !important;
        margin-top: 10px;
    }
    /* Paragraf */
    .stMarkdown p {
        text-align: justify !important;
        font-size: 15px !important;
        line-height: 1.6 !important;
    }
    /* Responsif untuk mobile */
    @media (max-width: 768px) {
        div[data-testid="column"] {
            width: 100% !important;
            display: block !important;
            margin-bottom: 1rem !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)


