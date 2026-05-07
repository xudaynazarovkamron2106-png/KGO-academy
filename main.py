import streamlit as st
import time
import random
import requests
from streamlit_lottie import st_lottie

# --- [1. MEGA DATABASE] ---
KGO_DB = {
    "English": {
        "Starter": {
            "content": "### 🇬🇧 Dars 1: Basics\n1. Hello - Salom\n2. Name - Ism\n3. Friend - Do'st",
            "test": {"q": " 'Kitob' ingliz tilida nima?", "a": "Book", "options": ["Apple", "Book", "Car"]}
        },
        "B2": {
            "content": "### 🇬🇧 Dars 20: Advanced\nEconomic stability is crucial for growth...",
            "test": {"q": "Synonym of 'Crucial'?", "a": "Essential", "options": ["Essential", "Small", "Weak"]}
        }
    },
    "Russian": {
        "Starter": {
            "content": "### 🇷🇺 Урок 1: Приветствие\n1. Привет - Salom\n2. Спасибо - Rahmat\n3. Пока - Xayr",
            "test": {"q": " 'Rahmat' rus tilida nima?", "a": "Спасибо", "options": ["Привет", "Спасибо", "Пожалуйста"]}
        }
    },
    "Math": {
        "Algebra": {
            "content": "### 📐 Algebra: Formulalar\n(a+b)² = a² + 2ab + b²\nx = (-b ± √D) / 2a",
            "test": {"q": "Diskriminant formulasi?", "a": "D = b² - 4ac", "options": ["D = b² - 4ac", "D = a+b", "D = 2ab"]}
        }
    }
}

# --- [2. SAFE ANIMATION LOADER] ---
def load_lottie(url):
    try:
        r = requests.get(url, timeout=5)
        return r.json() if r.status_code == 200 else None
    except:
        return None

# Futuristik Robot linki
robot_anim = load_lottie("https://lottie.host/7db26941-8608-466d-9653-5d519b5d2e0b/9U3T5YpI1L.json")

# --- [3. DESIGN & STYLES] ---
st.set_page_config(page_title="KGO ACADEMY BOSS", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@900&family=Rajdhani:wght@500&display=swap');
    
    .stApp { background: #000428; color: #00f2ff; font-family: 'Rajdhani'; }
    
    .boss-ui { border: 2px solid #00ff00; padding: 15px; border-radius: 15px; background: rgba(0,255,0,0.05); color: #00ff00; font-family: 'Orbitron'; margin-bottom: 20px; text-shadow: 0 0 5px #00ff00; }
    
    .stButton>button { 
        background: linear-gradient(45deg, #00f2ff, #0066ff) !important; 
        color: white !important; font-weight: bold !important; border-radius: 10px !important; 
        height: 100px !important; width: 100% !important; border: none !important; transition: 0.3s;
    }
    .stButton>button:hover { transform: scale(1.05); box-shadow: 0 0 20px #00f2ff; color: #ffc300 !important; }

    .glass-card { background: rgba(255,255,255,0.05); backdrop-filter: blur(10px); padding: 25px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.1); margin-top: 20px; }

    .footer { background: rgba(0,0,0,0.5); padding: 40px; border-radius: 40px 40px 0 0; border-top: 2px solid #ffc300; margin-top: 60px; }
</style>
""", unsafe_allow_html=True)

# --- [4. SESSION STATE] ---
if 'is_pro' not in st.session_state: st.session_state.is_pro = False
if 'is_boss' not in st.session_state: st.session_state.is_boss = False
if 'page' not in st.session_state: st.session_state.page = 'main'
if 'score' not in st.session_state: st.session_state.score = 0

# --- [5. TYPEWRITER EFFECT] ---
def kgo_talk(text):
    placeholder = st.empty()
    full = ""
    for char in text:
        full += char
        placeholder.markdown(f'<div class="glass-card">{full}▌</div>', unsafe_allow_html=True)
        time.sleep(0.01)

# --- [6. HEADER & ACCESS] ---
st.markdown('<h1 style="text-align:center; font-family:Orbitron; color:#ffc300; font-size:50px;">KGO ACADEMY</h1>', unsafe_allow_html=True)

if not st.session_state.is_pro:
    _, c_log = st.columns([5, 1.2])
    with c_log:
        with st.popover("🟢 PRO ACCESS"):
            code = st.text_input("PASSWORD:", type="password")
            if st.button("UNLOCK"):
                if code == "KAMA": st.session_state.is_pro = True; st.session_state.is_boss = True; st.rerun()
                elif code == "UZKGO": st.session_state.is_pro = True; st.rerun()
            st.info("Pay: @PrimeK21")

if st.session_state.is_boss:
    st.markdown('<div class="boss-ui">🛡️ BOSS MODE: Kamron X. Online <br> Sayt yaxshi ishlab turibdi, tizim nazorat ostida!</div>', unsafe_allow_html=True)

# --- [7. MAIN DASHBOARD] ---
if st.session_state.page == 'main':
    # Animatsiyani xavfsiz chiqarish
    if robot_anim:
        st_lottie(robot_anim, height=220, key="main_robot")
    else:
        st.markdown("<center>🚀 <b>KGO ACADEMY ONLINE</b></center>", unsafe_allow_html=True)

    st.write(f"### 🏆 Sizning ballaringiz: {st.session_state.score}")
    
    num = 5 if st.session_state.is_pro else 3
    cols = st.columns(num)
    btns = ["🌍 LANGUAGES", "📐 MATH HUB", "👨‍🏫 AI CHAT", "🤖 CREATE AI", "📚 SCIENCES"]
    p_names = ["lang", "math", "gemin", "create_ai", "sciences"]

    for i in range(num):
        with cols[i]:
            if st.button(btns[i]): st.session_state.page = p_names[i]; st.rerun()

# --- [8. PAGE LOGICS] ---
elif st.session_state.page == 'lang':
    st.header("🌍 Multi-Language Center")
    l_sel = st.selectbox("Til:", ["English", "Russian"])
    lvl = st.selectbox("Daraja:", ["Starter", "B2" if l_sel=="English" else "Starter"])
    
    if st.button("DARSNI O'QISH"):
        kgo_talk(KGO_DB[l_sel][lvl]["content"])
    
    st.write("---")
    test = KGO_DB[l_sel][lvl]["test"]
    user_ans = st.radio(test["q"], test["options"])
    if st.button("TEKSHIRISH"):
        if user_ans == test["a"]:
            st.success("To'g'ri! +10 Ball"); st.session_state.score += 10; st.balloons()
        else: st.error("Xato! Qayta o'qing.")
    if st.button("⬅️ DASHBOARD"): st.session_state.page = 'main'; st.rerun()

elif st.session_state.page == 'math':
    st.header("📐 Mathematics Hub")
    if st.button("ALGEBRA DARSI"): kgo_talk(KGO_DB["Math"]["Algebra"]["content"])
    st.write("---")
    m_test = KGO_DB["Math"]["Algebra"]["test"]
    m_ans = st.radio(m_test["q"], m_test["options"])
    if st.button("TESTNI TEKSHIR"):
        if m_ans == m_test["a"]: st.success("Bravo!"); st.session_state.score += 10
        else: st.error("Xato!")
    if st.button("⬅️ DASHBOARD"): st.session_state.page = 'main'; st.rerun()

elif st.session_state.page == 'gemin':
    st.header("👨‍🏫 AI Tutor")
    q = st.text_input("Savol bering:")
    if st.button("SO'RASH"):
        if st.session_state.is_pro: kgo_talk(f"'{q}' bo'yicha tahlil: Bu mavzu darsliklarimizning 3-qismida mavjud.")
        else: kgo_talk("Free versiyada chat cheklangan. @PrimeK21 ga bog'laning.")
    if st.button("⬅️ DASHBOARD"): st.session_state.page = 'main'; st.rerun()

# --- [9. FOOTER: ABOUT, HELP, SHIKOYAT] ---
st.markdown('<div class="footer">', unsafe_allow_html=True)
f1, f2, f3 = st.columns(3)

with f1:
    st.write("### ℹ️ ABOUT")
    st.write("KGO Academy — Kamron Xudaynazarov tomonidan yaratilgan 2026-yilning eng zamonaviy platformasi.")

with f2:
    st.write("### 🛠 HELP & PAY")
    st.write("To'lov va savollar uchun: [@PrimeK21](https://t.me/PrimeK21)")
    st.write("Telegram Kanal: @KGO_News")

with f3:
    st.write("### ⚠️ SHIKOYAT")
    msg = st.text_area("Xabar yoki shikoyatingiz:")
    if st.button("YUBORISH"):
        st.success("Xabar BOSSga yuborildi! Tez orada ko'rib chiqiladi.")

st.markdown('</div>', unsafe_allow_html=True)
