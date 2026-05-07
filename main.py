import streamlit as st
import pandas as pd
import time

# --- [1. KGO AI KNOWLEDGE DATABASE] ---
# Bu yerda barcha fanlar uchun ma'lumotlar bazasini quramiz
KGO_DATA = {
    "English": {
        "Starter": {"vocab": "1. Apple - Olma\n2. Book - Kitob\n3. Cat - Mushuk...", "speaking": "1. What is your name?\n2. How are you?"},
        "A1": {"vocab": "1. Journey - Sayohat\n2. Goal - Maqsad...", "speaking": "1. Tell me about your city.\n2. What is your hobby?"}
    },
    "Fizika": "1-Mavzu: Nyuton qonunlari.\nFizika tabiat hodisalarini o'rganadi. Birinchi qonun: Inersiya...",
    "Ona tili": "1-Mavzu: Gap bo'laklari.\nGapning asosi ega va kesimdir. Masalan: Kamron o'qiyapti.",
    "Tarix": "1-Mavzu: Qadimgi dunyo.\nO'zbekiston hududida ilk davlatlar: Xorazm va Baqtriya...",
    "Math": "Matematika - fanlar podshosi. 2x2=4. Kvadrat ildiz: sqrt(x)..."
}

# --- [2. PAGE CONFIG] ---
st.set_page_config(page_title="KGO Academy Pro", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&family=Poppins:wght@300;600&display=swap');
    .stApp { background: radial-gradient(circle, #001d3d 0%, #000814 100%); color: white; font-family: 'Poppins', sans-serif; }
    .header-box { text-align: center; padding: 30px; border-bottom: 3px solid #ffc300; border-radius: 0 0 50px 50px; background: rgba(255,255,255,0.02); }
    .stButton>button { background: linear-gradient(135deg, #ffc300 0%, #ffb703 100%) !important; color: #000814 !important; font-family: 'Orbitron', sans-serif !important; font-weight: bold; height: 120px; border-radius: 20px; border: none; transition: 0.3s; }
    .stButton>button:hover { transform: translateY(-10px); box-shadow: 0 15px 30px #ffc30088; background: white !important; }
    .ai-output { background: rgba(0,0,0,0.7); padding: 25px; border-radius: 20px; border-left: 5px solid #00f5ff; font-family: 'Courier New', monospace; color: #00f5ff; font-size: 18px; line-height: 1.6; }
</style>
""", unsafe_allow_html=True)

# --- [3. SESSION STATE] ---
if 'is_pro' not in st.session_state: st.session_state.is_pro = False
if 'page' not in st.session_state: st.session_state.page = 'main'

# --- [4. TYPEWRITER EFFECT] ---
def kgo_typewriter(text):
    placeholder = st.empty()
    full_text = ""
    for char in text:
        full_text += char
        placeholder.markdown(f'<div class="ai-output">{full_text}▌</div>', unsafe_allow_html=True)
        time.sleep(0.01)

# --- [5. TOP NAVIGATION] ---
st.markdown('<div class="header-box"><h1 style="color:#ffc300; font-family:Orbitron; font-size:50px;">KGO ACADEMY</h1></div>', unsafe_allow_html=True)

if not st.session_state.is_pro:
    _, col_top = st.columns([5, 1.2])
    with col_top:
        with st.popover("🟢 PRO / PROMO"):
            p_code = st.text_input("Maxfiy kod:", type="password")
            if st.button("ACTIVATE"):
                if p_code == "KAMA": st.session_state.is_pro = True; st.rerun()
                elif p_code == "UZKGO": st.session_state.is_pro = True; st.rerun()
                else: st.error("Xato!")

# --- [6. MAIN DASHBOARD] ---
if st.session_state.page == 'main':
    st.write("<br>", unsafe_allow_html=True)
    num = 5 if st.session_state.is_pro else 3
    cols = st.columns(num)
    
    with cols[0]:
        if st.button("🌍 LANGUAGE"): st.session_state.page = 'lang'; st.rerun()
    with cols[1]:
        if st.button("📐 MATH"): st.session_state.page = 'math'; st.rerun()
    with cols[2]:
        if st.button("👨‍🏫 GeminGPT"): st.session_state.page = 'gemin'; st.rerun()
    
    if st.session_state.is_pro:
        with cols[3]:
            if st.button("🤖 CREATE AI"): st.session_state.page = 'create_ai'; st.rerun()
        with cols[4]:
            if st.button("📚 SCIENCES"): st.session_state.page = 'sciences'; st.rerun()

# --- [7. PAGES LOGIC] ---
elif st.session_state.page == 'lang':
    st.title("🌍 Language Intelligence")
    lang = st.selectbox("Til:", ["English", "Russian"])
    lvl = st.select_slider("Level:", ["Starter", "A1", "A2", "B1", "B2"])
    if st.button("DARSNI KO'RISH"):
        # API-siz, bazadan ma'lumot olamiz
        text = f"--- {lang} {lvl} DARSI ---\n\n"
        text += "1. VOCABULARY (50 ta so'z):\n" + KGO_DATA["English"]["Starter"]["vocab"]
        text += "\n\n2. SPEAKING QUESTIONS (10 ta):\n" + KGO_DATA["English"]["Starter"]["speaking"]
        kgo_typewriter(text)
    if st.button("⬅️ BACK"): st.session_state.page = 'main'; st.rerun()

elif st.session_state.page == 'gemin':
    st.title("👨‍🏫 GeminGPT (Internal AI)")
    q = st.text_input("Savolingizni yozing:")
    if st.button("JAVOB"):
        if "salom" in q.lower(): kgo_typewriter("Salom! Men KGO Academy-ning ichki intellektiman. Savolingizga javob berishga tayyorman.")
        elif "matematika" in q.lower(): kgo_typewriter(KGO_DATA["Math"])
        else: kgo_typewriter("Kechirasiz, hozircha bazamda bu savolga javob yo'q. Tez orada qo'shiladi!")
    if st.button("⬅️ BACK"): st.session_state.page = 'main'; st.rerun()

elif st.session_state.page == 'sciences':
    st.title("📚 Full Science (PRO)")
    sci = st.selectbox("Fan:", ["Fizika", "Ona tili", "Tarix"])
    if st.button("DARSNI BOSHLASH"):
        kgo_typewriter(KGO_DATA[sci])
    if st.button("⬅️ BACK"): st.session_state.page = 'main'; st.rerun()

elif st.session_state.page == 'create_ai':
    st.title("🤖 AI Creation (PRO)")
    kgo_typewriter("KGO AI Builder ishga tushdi...\n1. Model tanlang: KGO-Lite\n2. Platforma: Streamlit\n3. Tayyor! O'z AI-ingiz ishlamoqda.")
    if st.button("⬅️ BACK"): st.session_state.page = 'main'; st.rerun()

st.markdown("<br><hr><center>© 2026 KGO ACADEMY | KAMRON X.</center>", unsafe_allow_html=True)
