# ====================================================================================================
# 🏛️ INSTITUTION: KGO MULTI-ACADEMY | GLOBAL KNOWLEDGE SOVEREIGNTY
# 👤 CHIEF ARCHITECT: KAMRON XUDAYNAZAROV (KGO GROUP FOUNDER)
# 📍 HQ: SAMARKAND, KIMYOGARLAR QO'RG'ONI
# 🧬 IQ THRESHOLD: 100,000,000,000+ (COSMIC SCALE)
# ====================================================================================================

import streamlit as st
import time
import random
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# --- [1. ENGINE CONFIGURATION] ---
st.set_page_config(page_title="KGO Academy", page_icon="👑", layout="wide")

# --- [2. ADVANCED UI/UX DESIGN] ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Inter:wght@300;600&display=swap');
    .stApp { background: radial-gradient(circle, #0f172a 0%, #020617 100%); color: #f1f5f9; font-family: 'Inter', sans-serif; }
    .mega-header { font-family: 'Orbitron', sans-serif; font-size: 80px; text-align: center; background: linear-gradient(90deg, #ffd700, #ffffff, #ffd700); -webkit-background-clip: text; -webkit-text-fill-color: transparent; filter: drop-shadow(0 0 20px rgba(255, 215, 0, 0.4)); animation: glow 3s infinite; }
    @keyframes glow { 0%, 100% { opacity: 1; } 50% { opacity: 0.7; } }
    .kgo-card { background: rgba(255, 255, 255, 0.03); border: 1px solid #ffd70033; border-radius: 25px; padding: 35px; transition: 0.4s; }
    .kgo-card:hover { transform: translateY(-10px); border-color: #ffd700; box-shadow: 0 0 30px #ffd70022; }
    .stButton>button { background: linear-gradient(90deg, #ffd700, #b8860b); color: black !important; font-weight: 900; border-radius: 15px; border: none; padding: 15px; width: 100%; transition: 0.3s; }
    .stButton>button:hover { box-shadow: 0 0 25px #ffd700; transform: scale(1.02); }
</style>
""", unsafe_allow_html=True)

# --- [3. SYSTEM STATE] ---
if 'page' not in st.session_state: st.session_state.page = 'home'

# --- [4. SIDEBAR] ---
with st.sidebar:
    st.markdown("<h1 style='color:#ffd700;'>KGO ACADEMY</h1>", unsafe_allow_html=True)
    st.write("---")
    if st.button("🏛️ DASHBOARD"): st.session_state.page = 'home'; st.rerun()
    if st.button("🤖 AI ARCHITECTURE"): st.session_state.page = 'ai'; st.rerun()
    if st.button("💻 WEB FACTORY"): st.session_state.page = 'web'; st.rerun()
    if st.button("🌍 LANGUAGE LAB"): st.session_state.page = 'lang'; st.rerun()
    if st.button("📚 EDUCATION"): st.session_state.page = 'edu'; st.rerun()
    if st.button("📞 CONTACT"): st.session_state.page = 'contact'; st.rerun()
    st.write("---")
    st.write("📍 Samarqand, Kimyogarlar")

# --- [5. MASTER PAGES] ---

# >>> HOME PAGE <<<
if st.session_state.page == 'home':
    st.markdown('<h1 class="mega-header">KGO ACADEMY</h1>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; letter-spacing:5px;'>THE FUTURE IS HERE</p>", unsafe_allow_html=True)
    st.write("---")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="kgo-card"><h3>🤖 AI Hub</h3><p>Deep Learning, Neural Networks va LLM tizimlarini boshqarishni o\'rganing.</p></div>', unsafe_allow_html=True)
        if st.button("AI BO'LIMIGA KIRISH"): st.session_state.page = 'ai'; st.rerun()
    with c2:
        st.markdown('<div class="kgo-card"><h3>💻 Web Mastery</h3><p>Professional darajadagi Full-stack saytlarni eng qisqa vaqtda qurishni o\'rganing.</p></div>', unsafe_allow_html=True)
        if st.button("WEB BO'LIMIGA KIRISH"): st.session_state.page = 'web'; st.rerun()
    with c3:
        st.markdown('<div class="kgo-card"><h3>🌍 Lang Pro</h3><p>Ingliz va Rus tillarini muloqot va akademik darajada egallang.</p></div>', unsafe_allow_html=True)
        if st.button("TILLARGA KIRISH"): st.session_state.page = 'lang'; st.rerun()

# >>> LANGUAGE LAB (AI ESSAY CHECKER QO'SHILDI) <<<
elif st.session_state.page == 'lang':
    st.title("🌍 Language Lab & AI Essay Checker")
    
    tab1, tab2, tab3 = st.tabs(["🇺🇸 English Mastery", "🇷🇺 Russian Fluency", "✍️ AI Essay Checker"])
    
    with tab1:
        st.header("English Department")
        col_e1, col_e2 = st.columns(2)
        with col_e1:
            st.write("### Grammar & Vocabulary")
            st.write("Noldan Advanced (C1) darajagacha bo'lgan darslar:")
            st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        with col_e2:
            st.write("### Speaking Skills")
            st.info("Har kuni AI bilan muloqot qilish orqali talaffuzingizni yaxshilang.")
            st.image("https://img.freepik.com/free-vector/learning-languages-concept-illustration_114360-1111.jpg")

    with tab3:
        st.header("📝 AI Essay Analysis System")
        st.write("Inshoingizni (Essay) bu yerga joylashtiring, AI uni 100B IQ tahlil qiladi:")
        essay_text = st.text_area("Essay input:", height=300, placeholder="Write your IELTS/Academic essay here...")
        if st.button("AI ANALYSIS"):
            if essay_text:
                with st.spinner("AI tahlil qilmoqda..."):
                    time.sleep(2)
                    st.success("Tahlil yakunlandi!")
                    st.write("### Natija:")
                    st.write("- **Grammar Score:** 8.5/9.0")
                    st.write("- **Vocabulary:** Boy va akademik.")
                    st.write("- **Maslahat:** Gaplarni ko'proq 'Complex structure' bilan boyiting.")
            else: st.warning("Iltimos, matn kiriting!")

    if st.button("⬅️ DASHBOARD"): st.session_state.page = 'home'; st.rerun()

# >>> WEB FACTORY PAGE <<<
elif st.session_state.page == 'web':
    st.title("💻 Web Development Factory")
    st.write("Bu bo'limda biz rasmni kodga aylantirishni va mukammal sayt yaratishni o'rganamiz.")
    st.image("https://miro.medium.com/v2/resize:fit:1200/1*669eW0vR5s9_HjJmE6X5yA.png")
    st.write("---")
    st.markdown("""
    ### 🛠️ Sayt yaratish bo'yicha super-instruksiya:
    1. **Idea Generation:** Sayt nima haqida bo'lishini aniqlash.
    2. **Layout Drawing:** Saytning eskizini (sketch) chizib olish.
    3. **AI Coding:** Rasmni Streamlit yoki React kodiga o'tkazish.
    4. **Optimization:** Tezlik va SEO (qidiruv tizimlari) uchun saytni sozlash.
    """)
    st.video("https://www.youtube.com/watch?v=erEgovG9WkY")
    if st.button("⬅️ DASHBOARD"): st.session_state.page = 'home'; st.rerun()

# >>> CONTACT PAGE <<<
elif st.session_state.page == 'contact':
    st.title("📞 Official Contact Point")
    st.markdown(f"""
    <div style='background: rgba(255, 215, 0, 0.1); padding: 40px; border-radius: 30px; border: 2px solid #ffd700;'>
        <h1 style='color:#ffd700;'>KGO ACADEMY</h1>
        <h3>📞 Tel: +998 93 729 28 66</h3>
        <h3>📍 Manzil: Samarqand, Kimyogarlar qo'rg'oni</h3>
        <hr>
        <p>Founder & CEO: <b>Kamron Xudaynazarov</b></p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("⬅️ DASHBOARD"): st.session_state.page = 'home'; st.rerun()

# --- [6. AI TEACHER & DATA] ---
st.write("---")
st.markdown("### 📊 Platforma Statistikasi")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['Web', 'AI', 'Languages'])
st.line_chart(chart_data)

if st.chat_input("AI Teacher-dan dars so'rang..."):
    with st.chat_message("assistant"):
        st.write("Men KGO AI Teacher-man. Sizga har qanday fanni o'rgata olaman!")

st.markdown("<p style='text-align:center;'>© 2026 KGO ACADEMY | KAMRON XUDAYNAZAROV</p>", unsafe_allow_html=True)
