import streamlit as st
import pandas as pd
import time
import google.generativeai as genai

# --- [1. GEMINI AI CONFIGURATION] ---
# Sening rasmdagi API kaliting
try:
    API_KEY = "AIzaSyDk7EUBPyH6ywpd48zulMai37ltnslJnVo" 
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("API tizimida xatolik bor! Kalitni tekshiring.")

# --- [2. PROFESSIONAL ACADEMY STYLING] ---
st.set_page_config(page_title="KGO Online School", layout="wide", page_icon="🎓")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&family=Poppins:wght@300;600&display=swap');
    
    .stApp {
        background: radial-gradient(circle at center, #001d3d 0%, #000814 100%);
        color: #ffffff;
        font-family: 'Poppins', sans-serif;
    }
    
    /* Neon Header */
    .academy-header {
        text-align: center;
        padding: 50px;
        background: rgba(255, 255, 255, 0.02);
        border-bottom: 4px solid #ffc300;
        border-radius: 0 0 60px 60px;
        margin-bottom: 40px;
    }

    /* Main Service Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #ffc300 0%, #ffb703 100%) !important;
        color: #000814 !important;
        font-family: 'Orbitron', sans-serif !important;
        font-weight: 900 !important;
        font-size: 18px !important;
        border-radius: 20px !important;
        height: 130px !important;
        width: 100% !important;
        transition: 0.4s all;
        box-shadow: 0 8px 20px rgba(255, 195, 0, 0.2);
    }

    .stButton>button:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 40px rgba(255, 195, 0, 0.5);
        background: #ffffff !important;
    }

    /* Typewriter Box */
    .ai-writer {
        background: rgba(0, 0, 0, 0.5);
        padding: 25px;
        border-radius: 20px;
        border-left: 5px solid #00f5ff;
        font-family: 'Courier New', monospace;
        color: #00f5ff;
        font-size: 18px;
        line-height: 1.5;
    }

    /* Promo Section */
    .promo-card {
        background: rgba(255, 195, 0, 0.1);
        padding: 20px;
        border-radius: 20px;
        border: 2px dashed #ffc300;
        margin-bottom: 30px;
    }
</style>
""", unsafe_allow_html=True)

# --- [3. SESSION STATE] ---
if 'is_pro' not in st.session_state: st.session_state.is_pro = False
if 'is_admin' not in st.session_state: st.session_state.is_admin = False
if 'page' not in st.session_state: st.session_state.page = 'main'

# --- [4. TYPEWRITER EFFECT FUNCTION] ---
def typewriter_ai(text):
    placeholder = st.empty()
    full_text = ""
    for char in text:
        full_text += char
        placeholder.markdown(f'<div class="ai-writer">{full_text}▌</div>', unsafe_allow_html=True)
        time.sleep(0.01)

# --- [5. MAIN INTERFACE] ---
st.markdown("""
<div class="academy-header">
    <h1 style='font-family: Orbitron; font-size: 50px; margin:0; color:#ffc300;'>KGO ACADEMY</h1>
    <p style='letter-spacing: 4px; opacity:0.7;'>ELITE ONLINE SCHOOL BY KAMRON X.</p>
</div>
""", unsafe_allow_html=True)

if st.session_state.page == 'main':
    
    # PROMOKOD JOYI (FAQAT FREE BO'LGANDA CHIQADI)
    if not st.session_state.is_pro:
        st.markdown('<div class="promo-card">', unsafe_allow_html=True)
        pc1, pc2 = st.columns([3, 1])
        p_code = pc1.text_input("Promokod kiriting (KAMA yoki UZKGO):", placeholder="Promokodni bering...")
        if pc2.button("PRO-NI YOQISH"):
            if p_code == "KAMA":
                st.session_state.is_pro = True
                st.session_state.is_admin = True
                st.success("Salom Admin Kamron! Barcha tizimlar ochildi.")
                st.rerun()
            elif p_code == "UZKGO":
                st.session_state.is_pro = True
                st.success("UZKGO faollashdi! 24 soatlik Pro Access.")
                st.rerun()
            else:
                st.error("Xato kod!")
        st.markdown('</div>', unsafe_allow_html=True)

    # TUGMALAR GENERATSIYASI
    n_cols = 5 if st.session_state.is_pro else 3
    cols = st.columns(n_cols)
    
    with cols[0]:
        if st.button("🌍 LANGUAGE\nLAB"): st.session_state.page = 'lang'; st.rerun()
    with cols[1]:
        if st.button("📐 MATH\nCENTER"): st.session_state.page = 'math'; st.rerun()
    with cols[2]:
        if st.button("👨‍🏫 GeminGPT\nTEACHER"): st.session_state.page = 'gemin'; st.rerun()
        
    if st.session_state.is_pro:
        with cols[3]:
            if st.button("🤖 CREATE AI\nPRO"): st.session_state.page = 'create_ai'; st.rerun()
        with cols[4]:
            if st.button("📚 SCIENCES\nPRO"): st.session_state.page = 'sciences'; st.rerun()

# --- [6. PAGE LOGIC: LANGUAGE] ---
elif st.session_state.page == 'lang':
    st.title("🌍 Language Intelligence")
    lang = st.radio("Tilni tanlang:", ["English", "Russian"], horizontal=True)
    lvl = st.select_slider("Daraja:", ["Starter", "A1", "A2", "B1", "B2"])
    
    if st.button("DARSNI BOSHLASH"):
        with st.spinner("AI darsni tayyorlamoqda..."):
            prompt = f"{lang} tilidan {lvl} darajasi uchun 50 ta eng muhim vocabulary (Word-Uzbek-Russian jadvalli) va 10 ta speaking savolini yozib ber."
            response = model.generate_content(prompt)
            typewriter_ai(response.text)
    
    if st.button("⬅️ DASHBOARD"): st.session_state.page = 'main'; st.rerun()

# --- [7. PAGE LOGIC: GeminGPT] ---
elif st.session_state.page == 'gemin':
    st.title("👨‍🏫 GeminGPT Universal Assistant")
    st.write("Fizika, matematika yoki xohlagan faningizdan savol bering.")
    q = st.text_input("Savolingiz:")
    if st.button("SO'RASH"):
        response = model.generate_content(q)
        typewriter_ai(response.text)
    if st.button("⬅️ DASHBOARD"): st.session_state.page = 'main'; st.rerun()

# --- [8. PAGE LOGIC: SCIENCES (PRO)] ---
elif st.session_state.page == 'sciences':
    st.title("📚 Full Science Library (PRO)")
    subj = st.selectbox("Fanni tanlang:", ["Ona tili", "Fizika", "Tarix", "Adabiyot", "Kimyo"])
    if st.button("DARSNI BOSHLASH"):
        prompt = f"{subj} fanidan 1-mavzuni juda batafsil, noldan boshlab o'qituvchi kabi tushuntirib ber."
        response = model.generate_content(prompt)
        typewriter_ai(response.text)
    if st.button("⬅️ DASHBOARD"): st.session_state.page = 'main'; st.rerun()

# --- [9. PAGE LOGIC: CREATE AI (PRO)] ---
elif st.session_state.page == 'create_ai':
    st.title("🤖 AI Development (PRO)")
    if st.button("HUGGINGFACE YO'RIQNOMASINI OLISH"):
        guide = "GeminGPT Guide:\n1. HuggingFace-ga kiring.\n2. Streamlit SDK tanlang.\n3. Secrets-ga API key qo'ying.\n4. Kodingizni yuklang."
        typewriter_ai(guide)
    if st.button("⬅️ DASHBOARD"): st.session_state.page = 'main'; st.rerun()

# --- [FOOTER] ---
st.write("<br><hr>", unsafe_allow_html=True)
st.write("© 2026 KGO Online School | Founder: Kamron Xudaynazarov")
