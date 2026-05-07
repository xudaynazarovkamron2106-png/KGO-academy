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
    st.error("API tizimida ulanishda xatolik!")

# --- [2. ELITE ACADEMY STYLING] ---
st.set_page_config(page_title="KGO Online School", layout="wide", page_icon="🎓")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&family=Poppins:wght@300;600&display=swap');
    
    .stApp {
        background: radial-gradient(circle at center, #001d3d 0%, #000814 100%);
        color: #ffffff;
        font-family: 'Poppins', sans-serif;
    }
    
    /* Header */
    .academy-header {
        text-align: center;
        padding: 40px;
        background: rgba(255, 255, 255, 0.02);
        border-bottom: 4px solid #ffc300;
        border-radius: 0 0 50px 50px;
        margin-bottom: 30px;
    }

    /* Main Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #ffc300 0%, #ffb703 100%) !important;
        color: #000814 !important;
        font-family: 'Orbitron', sans-serif !important;
        font-weight: 900 !important;
        font-size: 18px !important;
        border-radius: 20px !important;
        height: 140px !important;
        width: 100% !important;
        transition: 0.4s all;
        box-shadow: 0 8px 25px rgba(255, 195, 0, 0.3);
        border: none !important;
    }

    .stButton>button:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 45px rgba(255, 195, 0, 0.6);
        background: #ffffff !important;
    }

    /* AI Writer Style */
    .ai-response-box {
        background: rgba(0, 0, 0, 0.6);
        padding: 25px;
        border-radius: 20px;
        border-left: 5px solid #00f5ff;
        font-family: 'Courier New', monospace;
        color: #00f5ff;
        font-size: 18px;
        line-height: 1.6;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# --- [3. SESSION STATE] ---
if 'is_pro' not in st.session_state: st.session_state.is_pro = False
if 'page' not in st.session_state: st.session_state.page = 'main'

# --- [4. TYPEWRITER FUNCTION] ---
def typewriter_effect(text):
    placeholder = st.empty()
    full_text = ""
    for char in text:
        full_text += char
        placeholder.markdown(f'<div class="ai-response-box">{full_text}▌</div>', unsafe_allow_html=True)
        time.sleep(0.01)

# --- [5. HEADER & TOP NAVIGATION] ---
st.markdown("""
<div class="academy-header">
    <h1 style='font-family: Orbitron; font-size: 55px; margin:0; color:#ffc300;'>KGO ACADEMY</h1>
    <p style='letter-spacing: 3px; opacity:0.8;'>PREMIUM ED-TECH SYSTEM</p>
</div>
""", unsafe_allow_html=True)

# --- [TOP GREEN BUTTON - PROMO/PRO] ---
if not st.session_state.is_pro:
    col_t1, col_t2 = st.columns([6, 1.2])
    with col_t2:
        with st.popover("🟢 PRO / PROMO"):
            st.write("### KGO PRO Activation")
            p_code = st.text_input("Promokod yoki To'lov kodi:", placeholder="KAMA / UZKGO ...")
            if st.button("ACTIVATE", use_container_width=True):
                if p_code == "KAMA":
                    st.session_state.is_pro = True
                    st.success("Admin Panel Enabled!")
                    st.rerun()
                elif p_code == "UZKGO":
                    st.session_state.is_pro = True
                    st.success("Trial Activated!")
                    st.rerun()
                else:
                    st.error("Xato kod!")
            st.write("---")
            st.write("💳 Karta: 8600 0000 0000 0000")
            st.write("💡 Pro Trail: $1.99 / 1 kun")

# --- [6. MAIN DASHBOARD] ---
if st.session_state.page == 'main':
    st.write("<br>", unsafe_allow_html=True)
    
    n_btns = 5 if st.session_state.is_pro else 3
    cols = st.columns(n_btns)
    
    with cols[0]:
        if st.button("🌍 LANGUAGE\nMASTER"): 
            st.session_state.page = 'lang'
            st.rerun()
    with cols[1]:
        if st.button("📐 MATH\nCENTER"): 
            st.session_state.page = 'math'
            st.rerun()
    with cols[2]:
        if st.button("👨‍🏫 GeminGPT\nTEACHER"): 
            st.session_state.page = 'gemin'
            st.rerun()
            
    if st.session_state.is_pro:
        with cols[3]:
            if st.button("🤖 CREATE AI\nPRO"): 
                st.session_state.page = 'create_ai'
                st.rerun()
        with cols[4]:
            if st.button("📚 SCIENCES\nPRO"): 
                st.session_state.page = 'sciences'
                st.rerun()

# --- [7. PAGE LOGIC: LANGUAGE] ---
elif st.session_state.page == 'lang':
    st.title("🌍 Language Intelligence")
    l_col, r_col = st.columns([1, 2])
    target_lang = l_col.selectbox("Til:", ["English", "Russian"])
    target_lvl = l_col.select_slider("Daraja:", ["Starter", "A1", "A2", "B1", "B2"])
    
    if st.button("DARSNI GENERATSIYA QILISH"):
        prompt = f"Menga {target_lang} tilidan {target_lvl} darajasi uchun 50 ta muhim vocabulary (jadvalda: Word, Uzbek, Russian) va 10 ta speaking savolini yozib ber."
        response = model.generate_content(prompt)
        typewriter_effect(response.text)
    
    if st.button("⬅️ BACK"): st.session_state.page = 'main'; st.rerun()

# --- [8. PAGE LOGIC: GeminGPT] ---
elif st.session_state.page == 'gemin':
    st.title("👨‍🏫 GeminGPT Assistant")
    q = st.text_input("Savolingizni yozing (Matematika, Fizika va h.k.):")
    if st.button("AI JAVOBI"):
        response = model.generate_content(q)
        typewriter_effect(response.text)
    if st.button("⬅️ BACK"): st.session_state.page = 'main'; st.rerun()

# --- [9. PAGE LOGIC: SCIENCES (PRO)] ---
elif st.session_state.page == 'sciences':
    st.title("📚 Full Science Education (PRO)")
    subj = st.selectbox("Fanni tanlang:", ["Ona tili", "Fizika", "Tarix", "Adabiyot", "Kimyo"])
    if st.button("DARSNI BOSHLASH"):
        prompt = f"Menga {subj} fanidan 1-mavzuni juda batafsil, noldan tushuntirib ber."
        response = model.generate_content(prompt)
        typewriter_effect(response.text)
    if st.button("⬅️ BACK"): st.session_state.page = 'main'; st.rerun()

# --- [10. PAGE LOGIC: CREATE AI (PRO)] ---
elif st.session_state.page == 'create_ai':
    st.title("🤖 AI Creation Workshop (PRO)")
    if st.button("GUIDE-NI KO'RISH"):
        guide = "KGO Step-by-Step:\n1. HuggingFace Spaces oching.\n2. Streamlit tanlang.\n3. Secrets-ga Gemini API-ni qo'ying.\n4. KGO master kodini yuklang."
        typewriter_effect(guide)
    if st.button("⬅️ BACK"): st.session_state.page = 'main'; st.rerun()

# --- [FOOTER] ---
st.write("<br><br><hr>", unsafe_allow_html=True)
st.write("© 2026 KGO Online School | Founder: Kamron Xudaynazarov")
