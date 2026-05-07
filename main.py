import streamlit as st
import pandas as pd
import time
import google.generativeai as genai

# --- [1. GEMINI AI INTEGRATION] ---
try:
    # Sening rasmdagi API kaliting
    API_KEY = "AIzaSyDk7EUBPyH6ywpd48zulMai37ltnslJnVo" 
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("Tizim ulanishida xatolik yuz berdi!")

# --- [2. CUSTOM CSS STYLING] ---
st.set_page_config(page_title="KGO Online School", layout="wide", page_icon="🎓")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&family=Poppins:wght@300;600&display=swap');
    
    .stApp {
        background: radial-gradient(circle at center, #001d3d 0%, #000814 100%);
        color: #ffffff;
        font-family: 'Poppins', sans-serif;
    }
    
    .header-box {
        text-align: center;
        padding: 30px;
        background: rgba(255, 255, 255, 0.02);
        border-bottom: 3px solid #ffc300;
        border-radius: 0 0 40px 40px;
        margin-bottom: 25px;
    }

    .stButton>button {
        background: linear-gradient(135deg, #ffc300 0%, #ffb703 100%) !important;
        color: #000814 !important;
        font-family: 'Orbitron', sans-serif !important;
        font-weight: 900 !important;
        font-size: 17px !important;
        border-radius: 15px !important;
        height: 120px !important;
        width: 100% !important;
        transition: 0.3s all;
        border: none !important;
        box-shadow: 0 5px 15px rgba(255, 195, 0, 0.2);
    }

    .stButton>button:hover {
        transform: translateY(-8px);
        box-shadow: 0 15px 35px rgba(255, 195, 0, 0.5);
        background: #ffffff !important;
    }

    .ai-box {
        background: rgba(0, 0, 0, 0.7);
        padding: 20px;
        border-radius: 15px;
        border-left: 4px solid #00f5ff;
        font-family: 'Courier New', monospace;
        color: #00f5ff;
        font-size: 17px;
        margin-top: 15px;
    }
</style>
""", unsafe_allow_html=True)

# --- [3. SESSION STATE] ---
if 'is_pro' not in st.session_state: st.session_state.is_pro = False
if 'page' not in st.session_state: st.session_state.page = 'main'

# --- [4. HELPER FUNCTIONS] ---
def typewriter(text):
    placeholder = st.empty()
    full_text = ""
    for char in text:
        full_text += char
        placeholder.markdown(f'<div class="ai-box">{full_text}▌</div>', unsafe_allow_html=True)
        time.sleep(0.01)

# --- [5. HEADER SECTION] ---
st.markdown('<div class="header-box"><h1 style="font-family:Orbitron; color:#ffc300; margin:0;">KGO ACADEMY</h1><p style="opacity:0.7; letter-spacing:2px;">FUTURE OF EDUCATION</p></div>', unsafe_allow_html=True)

# --- [6. TOP NAVIGATION & PROMO] ---
if not st.session_state.is_pro:
    _, col_promo = st.columns([5, 1.2])
    with col_promo:
        with st.popover("🟢 PRO / PROMO"):
            st.subheader("Aktivatsiya")
            p_code = st.text_input("Maxfiy kod:", type="password", placeholder="******")
            if st.button("TASDIQLASH", use_container_width=True):
                if p_code == "KAMA":
                    st.session_state.is_pro = True
                    st.success("Admin mode on!")
                    st.rerun()
                elif p_code == "UZKGO":
                    st.session_state.is_pro = True
                    st.success("Pro activated!")
                    st.rerun()
                else:
                    st.error("Kod noto'g'ri!")
            st.divider()
            st.info("💳 Karta: 8600 0000 0000 0000\n\nTo'lovdan so'ng chekni @KGO_Admin ga yuboring.")

# --- [7. MAIN DASHBOARD] ---
if st.session_state.page == 'main':
    st.write("<br>", unsafe_allow_html=True)
    num_btns = 5 if st.session_state.is_pro else 3
    cols = st.columns(num_btns)
    
    with cols[0]:
        if st.button("🌍 LANGUAGE\nLAB"): st.session_state.page = 'lang'; st.rerun()
    with cols[1]:
        if st.button("📐 MATH\nCENTER"): st.session_state.page = 'math'; st.rerun()
    with cols[2]:
        if st.button("👨‍🏫 GeminGPT\nTEACHER"): st.session_state.page = 'gemin'; st.rerun()
            
    if st.session_state.is_pro:
        with cols[3]:
            if st.button("🤖 CREATE AI\n(HuggingFace)"): st.session_state.page = 'create_ai'; st.rerun()
        with cols[4]:
            if st.button("📚 SCIENCES\n(Full Course)"): st.session_state.page = 'sciences'; st.rerun()

# --- [8. PAGE LOGIC] ---

elif st.session_state.page == 'lang':
    st.title("🌍 Language Intelligence")
    lang = st.selectbox("Til:", ["English", "Russian"])
    lvl = st.select_slider("Level:", ["Starter", "A1", "A2", "B1", "B2"])
    if st.button("DARSNI BOSHLASH"):
        prompt = f"Menga {lang} tilidan {lvl} darajasi uchun 50 ta vocabulary (Eng-Uzb-Rus) va 10 ta speaking savolini yozib ber."
        response = model.generate_content(prompt)
        typewriter(response.text)
    if st.button("⬅️ ORQAGA"): st.session_state.page = 'main'; st.rerun()

elif st.session_state.page == 'gemin':
    st.title("👨‍🏫 GeminGPT Assistant")
    q = st.text_input("Savolingizni yozing:")
    if st.button("SAVOL YUBORISH"):
        response = model.generate_content(q)
        typewriter(response.text)
    if st.button("⬅️ ORQAGA"): st.session_state.page = 'main'; st.rerun()

elif st.session_state.page == 'sciences':
    st.title("📚 Full Science Library (PRO)")
    sci = st.selectbox("Fanni tanlang:", ["Ona tili", "Fizika", "Tarix", "Adabiyot", "Kimyo"])
    if st.button("DARSNI TUSHUNTIR"):
        prompt = f"Menga {sci} fanidan eng muhim mavzuni noldan tushuntirib ber."
        response = model.generate_content(prompt)
        typewriter(response.text)
    if st.button("⬅️ ORQAGA"): st.session_state.page = 'main'; st.rerun()

elif st.session_state.page == 'create_ai':
    st.title("🤖 AI Creation Workshop (PRO)")
    st.write("O'z AI-ingizni yaratish bo'yicha ko'rsatma:")
    if st.button("YO'RIQNOMA"):
        guide = "1. HuggingFace.co-ga kirish.\n2. Space yaratish.\n3. SDK: Streamlit tanlash.\n4. KGO API-ni Secrets-ga qo'yish."
        typewriter(guide)
    if st.button("⬅️ ORQAGA"): st.session_state.page = 'main'; st.rerun()

# --- [FOOTER] ---
st.markdown("<br><br><hr><center>© 2026 KGO Online School | Kamron Xudaynazarov</center>", unsafe_allow_html=True)
