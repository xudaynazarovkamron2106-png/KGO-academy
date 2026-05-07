import streamlit as st
import time
import random
import requests
from streamlit_lottie import st_lottie

# --- [1. MEGA DATABASE - HAR BIR DARSA TEST QO'SHILDI] ---
DATABASE = {
    "English": {
        "Starter": {
            "content": "Dars 1: Greeting (Salomlashish)\n1. Hello - Salom\n2. Goodbye - Xayr\n3. Teacher - O'qituvchi",
            "test": {"q": " 'Olma' ingliz tilida nima?", "a": "Apple", "options": ["Apple", "Book", "Car"]}
        },
        "A1": {
            "content": "Dars 5: Present Simple\nI work, You work, He works...",
            "test": {"q": "He ____ (work) in a bank.", "a": "works", "options": ["work", "works", "working"]}
        }
    },
    "Math": {
        "Algebra": {
            "content": "Mavzu: Kvadrat tenglamalar\nax² + bx + c = 0",
            "test": {"q": "D = b² - 4ac nima deyiladi?", "a": "Diskriminant", "options": ["Diskriminant", "Ildiz", "Daraja"]}
        }
    }
}

# --- [2. ANIMATSIYA YUKLASH] ---
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200: return None
    return r.json()

robot_anim = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_q5pk6hyu.json")

# --- [3. PAGE CONFIG & CSS] ---
st.set_page_config(page_title="KGO SUPREME", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@900&family=Rajdhani:wght@600&display=swap');
    .stApp { background: #000428; color: #00f2ff; font-family: 'Rajdhani'; }
    .boss-panel { border: 3px solid #00ff00; padding: 20px; border-radius: 20px; background: rgba(0,255,0,0.05); color: #00ff00; font-family: 'Orbitron'; box-shadow: 0 0 20px #00ff00; }
    .stButton>button { background: linear-gradient(45deg, #ffc300, #ff8800) !important; color: black !important; font-weight: bold !important; border-radius: 10px !important; border: none !important; transition: 0.3s; }
    .stButton>button:hover { transform: translateY(-5px); box-shadow: 0 10px 20px #ffc30088; }
    .footer { background: rgba(255,255,255,0.05); padding: 30px; border-radius: 30px 30px 0 0; margin-top: 50px; border-top: 1px solid #00f2ff; }
</style>
""", unsafe_allow_html=True)

# --- [4. SESSION STATE] ---
if 'is_pro' not in st.session_state: st.session_state.is_pro = False
if 'is_boss' not in st.session_state: st.session_state.is_boss = False
if 'score' not in st.session_state: st.session_state.score = 0
if 'page' not in st.session_state: st.session_state.page = 'main'

# --- [5. HEADER & LOGIN] ---
col1, col2 = st.columns([4, 1])
with col1:
    st.markdown('<h1 style="font-family:Orbitron; font-size:60px; color:#ffc300;">KGO ACADEMY PRO</h1>', unsafe_allow_html=True)
with col2:
    if not st.session_state.is_pro:
        with st.popover("🔑 LOGIN"):
            code = st.text_input("PASSWORD:", type="password")
            if st.button("UNLOCK"):
                if code == "KAMA": st.session_state.is_pro = True; st.session_state.is_boss = True; st.rerun()
                elif code == "UZKGO": st.session_state.is_pro = True; st.rerun()

# --- [6. BOSS STATUS] ---
if st.session_state.is_boss:
    st.markdown('<div class="boss-panel">🛡️ BOSS STATUS: Kamron X. Online <br> [Tizim nazoratda, ballar cheksiz]</div>', unsafe_allow_html=True)

# --- [7. MAIN DASHBOARD] ---
if st.session_state.page == 'main':
    st_lottie(robot_anim, height=200)
    st.write(f"### 🏆 Sening ballaring: {st.session_state.score}")
    
    cols = st.columns(5 if st.session_state.is_pro else 3)
    titles = ["🌍 LANGUAGES", "📐 MATH HUB", "👨‍🏫 AI TUTOR", "🤖 CREATE AI", "📚 SCIENCES"]
    pages = ["lang", "math", "gemin", "create_ai", "sciences"]
    
    for i in range(len(cols)):
        with cols[i]:
            if st.button(titles[i]): st.session_state.page = pages[i]; st.rerun()

# --- [8. SMART LESSON & TEST SYSTEM] ---
elif st.session_state.page == 'lang':
    st.header("🌍 Til o'rganish va Test topshirish")
    lang_sel = st.selectbox("Til:", ["English", "Russian"])
    lvl_sel = st.selectbox("Daraja:", ["Starter", "A1"])
    
    if st.button("DARSNI O'QISH"):
        st.info(DATABASE["English"][lvl_sel]["content"])
        
    st.write("---")
    st.write("### 📝 Bilimingni tekshir:")
    test_data = DATABASE["English"][lvl_sel]["test"]
    ans = st.radio(test_data["q"], test_data["options"])
    
    if st.button("JAVOBNI TEKSHIRISH"):
        if ans == test_data["a"]:
            st.success("To'g'ri! +10 Ball")
            st.session_state.score += 10
            st.balloons()
        else:
            st.error("Xato! Qaytadan o'qing.")
            
    if st.button("🏠 DASHBOARD"): st.session_state.page = 'main'; st.rerun()

# --- [9. FOOTER SECTION] ---
st.markdown('<div class="footer">', unsafe_allow_html=True)
f1, f2, f3 = st.columns(3)
with f1:
    st.write("### ℹ️ ABOUT")
    st.write("KGO Academy - Kelajak ta'limi hozirda!")
with f2:
    st.write("### 🛠 HELP")
    st.write("To'lov: @PrimeK21 \nYangiliklar: @KGO_News")
with f3:
    st.write("### ⚠️ SHIKOYAT")
    shikoyat = st.text_area("Xabar yo'llang:")
    if st.button("YUBORISH"): st.success("Xabar BOSSga ketdi!")
st.markdown('</div>', unsafe_allow_html=True)
