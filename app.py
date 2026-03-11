import streamlit as st
import home
import education
import prediction

st.set_page_config(page_title="Bird-Vision", layout="wide")

# ===== CSS RESPONSIVE GLOBAL =====
st.markdown("""
    <style>
        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
            max-width: 100% !important;
        }

        /* Judul responsif */
        .main-title {
            font-size: 3rem;
            font-weight: 700;
            text-align: left;
            margin-bottom: 1rem;
        }

        /* Tablet */
        @media (max-width: 900px) {
            .main-title {
                font-size: 2.4rem;
            }
            .block-container {
                padding-left: 0.8rem;
                padding-right: 0.8rem;
            }
        }

        /* HP */
        @media (max-width: 600px) {
            .main-title {
                font-size: 1.8rem;
            }
            .block-container {
                padding-left: 0.5rem;
                padding-right: 0.5rem;
            }
        }
    </style>
""", unsafe_allow_html=True)

# ===== JUDUL =====
st.markdown('<div class="main-title">🦜BirdVision</div>', unsafe_allow_html=True)

# ===== TABS =====
tab1, tab3, tab4 = st.tabs(["Home", "Education", "Prediction"])

with tab1:
    home.show()


with tab3:
    education.show()

with tab4:
    prediction.show()



