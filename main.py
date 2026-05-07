import streamlit as st
import time
import random

# --- [1. DATABASE & LOGIC] ---
KGO_DATA = {
    "fizika": ["Nyuton qonunlari - Dinamika asosi.", "Olamning kengayishi - Katta portlash nazariyasi.", "Kvant fizikasi - Zarralar dunyosi."],
    "ona tili": ["O'zbek tili - Davlat tili maqomida.", "Morfologiya - So'z turkumlari.", "Sintaksis - Gap qurilishi."],
    "math": ["Algebra: Logarifmlar va Hosilalar.", "Geometriya: Fazoviy shakllar.", "Trigonometriya: Sinus va Kosinus."],
}

# --- [2. PAGE CONFIG] ---
st.set_page_config(page_title="KGO ELITE ACADEMY", layout="wide")

# --- [3. SUPER GRAPHIC DIZAYN (CSS)] ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Rajdhani:wght@500;700&display=swap');

    /* Asosiy fon - Kosmik qora-ko'k */
    .stApp {
        background: radial-gradient(circle at center, #001529 0%, #000000 100%);
        color: #e0e0e0;
        font-family: 'Rajdhani', sans-serif;
    }

    /* Neon Sarlavha */
    .neon-header {
        text-align: center;
        padding: 50px;
        background: rgba(0, 255, 255, 0.03);
        border-bottom: 2px solid #00f2ff;
        box-shadow: 0 0 20px #00f2ff33;
        border-radius: 0 0 100px 100px;
        margin-bottom: 50px;
    }
    
    .neon-text {
        font-family: 'Orbitron', sans-serif;
        font-size: 70px;
        color: #ffc300;
        text-shadow: 0 0 15px #ffc300, 0 0 30px #ffc300;
        letter-spacing: 10px;
    }

    /* Tugmalar - Cyberpunk Style */
    .stButton>button {
        background: linear-gradient(45deg, #00f2ff 0%, #0066ff 100%) !important;
        color: white !important;
        font-family: 'Orbitron', sans-serif !important;
        font-weight: 900 !important;
        border-radius: 0px 20px 0px 20px !important;
        height: 120px !important;
        border: 2px solid #00f2ff !important;
        transition: 0.5s all ease;
        text-transform: uppercase;
        box-shadow: 5px 5px 0px #ffc300;
    }

    .stButton>button:hover {
        transform: scale(1.05) rotate(-1deg);
        background: #ffc300 !important;
        color: black !important;
        box-shadow: 0 0 30px #ffc300;
        border: 2px solid black !important;
    }

    /* AI Javob qutisi - Shishasimon (Glassmorphism) */
    .glass-box {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 30px;
        border-radius: 30px;
        color: #00f2ff;
        font-size: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }

    /* Footer Bo'limlari */
    .footer-section {
        background: rgba(0,0,0,0.8);
        padding: 40px;
        border-top: 2px solid #ffc300;
        margin-top: 100px;
        border-radius: 50px 50px 0 0;
    }
</style>
""", unsafe_allow_html=True)

# --- [4. SESSION STATE] ---
if 'is_pro' not in st.session_state: st.session_state.is_pro = False
if 'is_boss' not in st.session_state: st.session_state.is_boss = False
if 'page' not in st.session_state: st.session_state.page = 'main'

# --- [5. ANIMATION AI TALK] ---
def ai_voice(text):
    placeholder = st.empty()
    full = ""
    for char in text:
        full += char
        placeholder.markdown(f'<div class="glass-box">{full}▌</div>', unsafe_allow_html=True)
        time.sleep(0.01)

# --- [6. TOP NAVIGATION (BOSS & PROMO)] ---
st.markdown('<div class="neon-header"><h1 class="neon-text">KGO ACADEMY</h1></div>', unsafe_allow_html=True)

if not st.session_state.is_pro:
    _, col_top = st.columns([5, 1.2])
    with col_top:
        with st.popover("🟢 ACCESS PANEL"):
            code = st.text_input("PASSWORD:", type="password")
            if st.button("UNLOCK"):
                if code == "KAMA":
                    st.session_state.is_pro = True
                    st.session_state.is_boss = True
                    st.rerun()
                elif code == "UZKGO":
                    st.session_state.is_pro = True
                    st.rerun()
            st.write("---")
            st.info("Admin: @PrimeK21")

# --- [7. BOSS INTERFACE] ---
if st.session_state.is_boss:
    st.success("🤖 ASSALOMU ALEYKUM BOSS! TIZIM SIZNING NAZORATINGIZDA. HAMMA MODULLAR AKTIV.")

# --- [8. MAIN DASHBOARD] ---
if st.session_state.page == 'main':
    st.write("<br><br>", unsafe_allow_html=True)
    num_btns = 5 if st.session_state.is_pro else 3
    cols = st.columns(num_btns)
    
    with cols[0]:
        if st.button("🌍 LANGUAGES"): st.session_state.page = 'lang'; st.rerun()
    with cols[1]:
        if st.button("📐 MATH HUB"): st.session_state.page = 'math'; st.rerun()
    with cols[2]:
        if st.button("👨‍🏫 GeminGPT"): st.session_state.page = 'gemin'; st.rerun()
        
    if st.session_state.is_pro:
        with cols[3]:
            if st.button("🤖 CREATE AI"): st.session_state.page = 'create_ai'; st.rerun()
        with cols[4]:
            if st.button("📚 SCIENCES"): st.session_state.page = 'sciences'; st.rerun()

# --- [9. PAGE LOGIC (NAMUNA)] ---
elif st.session_state.page == 'gemin':
    st.title("👨‍🏫 KGO Intelligent Assistant")
    user_q = st.text_input("Savolingizni kiriting:")
    if st.button("ANALIZ QILISH"):
        if not st.session_state.is_pro:
            ai_voice("Free versiyada javoblar cheklangan. @PrimeK21 ga bog'laning.")
        else:
            ai_voice(f"Tizim '{user_q}' bo'yicha ma'lumotlarni qidirmoqda... Topildi: Bu mavzu KGO bazasida mavjud.")
    if st.button("⬅️ DASHBOARD"): st.session_state.page = 'main'; st.rerun()

# ... (Boshqa sahifalar ham shunday davom etadi)

# --- [10. FOOTER: ABOUT, HELP, COMPLAINT] ---
st.markdown('<div class="footer-section">', unsafe_allow_html=True)
f_col1, f_col2, f_col3 = st.columns(3)

with f_col1:
    st.write("### ℹ️ About Academy")
    st.write("KGO Academy — bu 2026-yilning eng ilg'or ta'lim platformasi. Kamron Xudaynazarov tomonidan asos solingan.")

with f_col2:
    st.write("### 🛠 Help Center")
    st.write("Savollaringiz bo'lsa: \n1. @PrimeK21 ga yozing \n2. Video darslarni ko'ring")
    if st.button("HELP"): st.toast("Tez orada operator bog'lanadi!")

with f_col3:
    st.write("### ⚠️ Complaints")
    complaint = st.text_area("Shikoyat yoki taklifingizni yozing:")
    if st.button("SEND"):
        st.success("Rahmat! Xabaringiz Kamronning shaxsiy bazasiga yuborildi.")

st.markdown('</div>', unsafe_allow_html=True)
