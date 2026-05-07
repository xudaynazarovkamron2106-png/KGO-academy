import streamlit as st
import time

# --- [1. ENGINE CONFIGURATION] ---
st.set_page_config(page_title="KGO Academy | GeminGPT", page_icon="👑", layout="wide")

# --- [2. FUTURISTIC NEON DESIGN - CSS] ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Rajdhani:wght@300;600&display=swap');
    
    .stApp {
        background: radial-gradient(circle at center, #001219 0%, #000000 100%);
        color: #00f5ff;
        font-family: 'Rajdhani', sans-serif;
    }
    
    .mega-header {
        font-family: 'Orbitron', sans-serif;
        font-size: clamp(40px, 8vw, 90px);
        text-align: center;
        background: linear-gradient(180deg, #00f5ff, #005f73);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 0 15px #00f5ff);
        margin-bottom: 30px;
    }

    /* Katta neon tugmalar */
    .stButton>button {
        background: rgba(0, 245, 255, 0.05) !important;
        color: #00f5ff !important;
        font-family: 'Orbitron', sans-serif !important;
        font-weight: 900 !important;
        font-size: 18px !important;
        border: 2px solid #00f5ff !important;
        border-radius: 15px !important;
        height: 120px !important;
        width: 100% !important;
        transition: 0.5s all ease;
        box-shadow: 0 0 10px #00f5ff22;
    }

    .stButton>button:hover {
        background: #00f5ff !important;
        color: #000000 !important;
        box-shadow: 0 0 40px #00f5ff;
        transform: translateY(-10px);
    }

    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(0, 245, 255, 0.2);
        border-radius: 25px;
        padding: 30px;
        margin: 10px 0;
    }

    .level-btn>button {
        height: 50px !important;
        font-size: 14px !important;
    }
</style>
""", unsafe_allow_html=True)

# --- [3. SESSION STATE] ---
if 'view' not in st.session_state: st.session_state.view = 'main'
if 'lang_level' not in st.session_state: st.session_state.lang_level = None

# --- [4. MAIN INTERFACE] ---
if st.session_state.view == 'main':
    st.markdown('<h1 class="mega-header">KGO ACADEMY</h1>', unsafe_allow_html=True)
    st.write("<h4 style='text-align:center; color:#00f5ff;'>SYSTEM STATUS: ONLINE | IQ: 100,000,000,000</h4>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    
    with col1:
        if st.button("🤖 AI ARCHITECTURE\n(Hugging Face)"):
            st.session_state.view = 'ai_logic'
            st.rerun()
    with col2:
        if st.button("💻 WEB FACTORY\n(GitHub Master)"):
            st.session_state.view = 'web_logic'
            st.rerun()
    with col3:
        if st.button("🌍 LANGUAGE MASTER\n(Levels A1-B2)"):
            st.session_state.view = 'lang_logic'
            st.rerun()
    with col4:
        if st.button("👨‍🏫 GeminGPT TEACHER\n(All Sciences)"):
            st.session_state.view = 'gemin_gpt'
            st.rerun()

    st.markdown("<br><p style='text-align:center; opacity:0.6;'>Founder: Kamron Xudaynazarov | 📍 Samarkand | 📞 +998 93 729 28 66</p>", unsafe_allow_html=True)

# --- [5. PAGES LOGIC] ---

# >>> LANGUAGE MASTER (WITH LEVELS) <<<
elif st.session_state.view == 'lang_logic':
    st.title("🌍 Language Intelligence System")
    lang = st.radio("Tilni tanlang:", ["English 🇺🇸", "Russian 🇷🇺"], horizontal=True)
    
    st.write("### Darajani tanlang:")
    l_col1, l_col2, l_col3, l_col4, l_col5, l_col6 = st.columns(6)
    levels = ["Starter1", "Starter2", "A1", "A2", "B1", "B2"]
    cols = [l_col1, l_col2, l_col3, l_col4, l_col5, l_col6]
    
    for i, lvl in enumerate(levels):
        with cols[i]:
            if st.button(lvl, key=f"lvl_{lvl}"):
                st.session_state.lang_level = lvl

    if st.session_state.lang_level:
        st.markdown(f'<div class="glass-card">', unsafe_allow_html=True)
        st.subheader(f"Level: {st.session_state.lang_level} ({lang})")
        
        if st.session_state.lang_level in ["Starter1", "Starter2"]:
            st.write("**Vocabulary:** Hello, Apple, Book, Pen, School.")
            st.write("**Speaking:** 'My name is Kamron. I am from Samarkand.'")
            st.write("**Grammar:** Verb TO BE (Am/Is/Are).")
        elif "A" in st.session_state.lang_level:
            st.write("**Vocabulary:** Environment, Technology, Education, Travel.")
            st.write("**Speaking:** 'I like creating websites because it is my passion.'")
            st.write("**Grammar:** Present Simple vs Continuous.")
        else:
            st.write("**Vocabulary:** Artificial Intelligence, Global Economy, Sustainability.")
            st.write("**Speaking:** 'The integration of AI into education is inevitable.'")
            st.write("**Grammar:** Passive Voice, Conditionals (If sentences).")
        st.markdown('</div>', unsafe_allow_html=True)

    if st.button("⬅️ BACK TO HUB"):
        st.session_state.view = 'main'
        st.rerun()

# >>> GeminGPT TEACHER (ALL SCIENCES) <<<
elif st.session_state.view == 'gemin_gpt':
    st.title("👨‍🏫 GeminGPT Universal Teacher")
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    topic = st.text_input("GeminGPT-dan xohlagan narsangizni so'rang (Masalan: Kvant fizikasi, Matematika, Biznes):")
    
    if topic:
        with st.spinner("GeminGPT 100B IQ tahlil qilmoqda..."):
            time.sleep(1)
            st.success(f"Dars: {topic}")
            st.write(f"**GeminGPT:** '{topic}' haqida ma'lumot shuki, bu soha kelajakda Kamron Xudaynazarov kabi innovatorlar uchun juda muhim. Mana asosiy qoidalar...")
            st.info("💡 GeminGPT maslahati: Doimo amaliyotga e'tibor bering!")
    
    st.write("---")
    st.write("### Fanlar bo'limi:")
    f_col1, f_col2, f_col3 = st.columns(3)
    f_col1.metric("Matematika", "Advanced", "+100% IQ")
    f_col2.metric("Fizika", "Quantum", "Active")
    f_col3.metric("Web", "Full-Stack", "Professional")
    st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("⬅️ BACK TO HUB"):
        st.session_state.view = 'main'
        st.rerun()

# >>> WEB FACTORY (RE-BUILT) <<<
elif st.session_state.view == 'web_logic':
    st.title("💻 Web Factory: Deployment Master")
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("""
    ### 1. GitHub Account (Account ochish)
    - **Qayerda:** `github.com` - O'ng tepa burchak **'Sign Up'** tugmasi.
    - **Nima:** Email kiriting, parolni eslab qoling.
    
    ### 2. Repository yaratish
    - **Qayerda:** Chap tarafdagi yashil **'New'** tugmasi.
    - **Nima:** Nomini `kgo-academy` qiling.
    
    ### 3. Streamlit Cloud ulanishi
    - **Qayerda:** `share.streamlit.io` saytida GitHub orqali Login bosing.
    - **Nima:** **'New app'** tugmasini bosing va yaratgan repository-ni tanlang.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    if st.button("⬅️ BACK TO HUB"):
        st.session_state.view = 'main'
        st.rerun()

# >>> AI LOGIC (HUGGING FACE RE-BUILT) <<<
elif st.session_state.view == 'ai_logic':
    st.title("🤖 AI Architecture: Hugging Face Specialist")
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("""
    ### 1. Hugging Face Spaces
    - **Tugma:** Tepa menyudagi **'Spaces'** bo'limi.
    - **Harakat:** O'ng tarafdagi ko'k **'Create new Space'** tugmasi.
    
    ### 2. SDK Tanlash
    - **Tugma:** Pastroqda **'Streamlit'** belgisini tanlang (aynan o'rtada).
    
    ### 3. Modelni yuklash
    - **Harakat:** Space yaratilgach, **'Files'** bo'limiga kiring va 'Add file' tugmasi orqali `app.py` yaratib kodni joylang.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    if st.button("⬅️ BACK TO HUB"):
        st.session_state.view = 'main'
        st.rerun()
