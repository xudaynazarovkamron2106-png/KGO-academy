import streamlit as st
import pandas as pd
import time
import numpy as np

# --- [1. ENGINE CONFIGURATION] ---
st.set_page_config(page_title="KGO Online Academy | Pro", page_icon="🎓", layout="wide")

# --- [2. ELITE ACADEMY DESIGN - CSS] ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@800&family=Poppins:wght@300;600&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #001d3d 0%, #003566 50%, #000814 100%);
        color: #edf2f4;
        font-family: 'Poppins', sans-serif;
    }
    
    /* Header Section */
    .academy-header {
        text-align: center;
        padding: 60px;
        background: rgba(255, 255, 255, 0.03);
        border-bottom: 5px solid #ffc300;
        border-radius: 0 0 100px 100px;
        margin-bottom: 50px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.5);
    }

    /* Big Service Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #ffc300 0%, #ffb703 100%) !important;
        color: #000814 !important;
        font-weight: 900 !important;
        font-family: 'Montserrat', sans-serif !important;
        font-size: 20px !important;
        border-radius: 25px !important;
        height: 140px !important;
        width: 100% !important;
        border: none !important;
        transition: 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }

    .stButton>button:hover {
        transform: translateY(-15px) scale(1.03);
        box-shadow: 0 25px 50px rgba(255, 195, 0, 0.4);
        background: #ffffff !important;
    }

    /* Footer Buttons Style */
    .footer-btn>div>button {
        height: 50px !important;
        font-size: 14px !important;
        background: rgba(255,255,255,0.1) !important;
        color: white !important;
        border: 1px solid #ffc300 !important;
    }

    .lesson-card {
        background: rgba(15, 23, 42, 0.7);
        backdrop-filter: blur(20px);
        padding: 40px;
        border-radius: 40px;
        border: 1px solid rgba(255, 195, 0, 0.3);
        margin-top: 20px;
    }

    .stat-box {
        text-align: center;
        padding: 20px;
        background: rgba(255, 195, 0, 0.1);
        border-radius: 20px;
        border: 1px solid #ffc300;
    }
</style>
""", unsafe_allow_html=True)

# --- [3. SESSION STATE] ---
if 'page' not in st.session_state: st.session_state.page = 'main'
if 'lang' not in st.session_state: st.session_state.lang = 'ENG'

# --- [4. CONSTANT HEADER] ---
st.markdown("""
<div class="academy-header">
    <h1 style='font-family: Montserrat; font-size: 70px; margin:0; color: #ffc300;'>KGO ACADEMY</h1>
    <p style='letter-spacing: 5px; font-size: 20px; opacity: 0.8;'>THE ELITE ONLINE SCHOOL SYSTEM</p>
</div>
""", unsafe_allow_html=True)

# --- [5. PAGE ROUTING] ---

# >>> MAIN DASHBOARD <<<
if st.session_state.page == 'main':
    # Stats Row
    s1, s2, s3, s4 = st.columns(4)
    s1.markdown('<div class="stat-box">⭐ 4.9/5 Rating</div>', unsafe_allow_html=True)
    s2.markdown('<div class="stat-box">👨‍🎓 10K+ Students</div>', unsafe_allow_html=True)
    s3.markdown('<div class="stat-box">🌍 24/7 Access</div>', unsafe_allow_html=True)
    s4.markdown('<div class="stat-box">🏆 IQ 100B Base</div>', unsafe_allow_html=True)
    
    st.write("<br><br>", unsafe_allow_html=True)
    
    # 4 Main Service Buttons
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    
    with col1:
        if st.button("🌍 LANGUAGE MASTER\n(Starter to B2)"):
            st.session_state.page = 'lang'
            st.rerun()
    with col2:
        if st.button("👨‍🏫 GeminGPT TEACHER\n(Ask Anything)"):
            st.session_state.page = 'gemin'
            st.rerun()
    with col3:
        if st.button("💻 WEB FACTORY\n(Code to Cloud)"):
            st.session_state.page = 'web'
            st.rerun()
    with col4:
        if st.button("🤖 AI ARCHITECTURE\n(Build Neural Nets)"):
            st.session_state.page = 'ai'
            st.rerun()

# >>> LANGUAGE PAGE <<<
elif st.session_state.page == 'lang':
    st.title("🌍 Language Department")
    mode = st.radio("Language:", ["English 🇺🇸", "Russian 🇷🇺"], horizontal=True)
    lvl = st.select_slider("Select Level:", ["Starter 1", "Starter 2", "A1", "A2", "B1", "B2"])
    
    st.markdown('<div class="lesson-card">', unsafe_allow_html=True)
    if mode == "English 🇺🇸":
        st.subheader(f"Level {lvl} English Program")
        tab1, tab2, tab3 = st.tabs(["📚 Grammar", "📖 50 Vocabulary", "🗣️ 10 Speaking"])
        with tab1:
            st.write("### Grammar Focus: Tenses")
            st.markdown("- **Present Simple:** Daily habits. \n- **Present Continuous:** Now. \n- **Past Simple:** Yesterday. \n- **Future Simple:** Tomorrow.")
        with tab2:
            data = [{"English": f"Word {i}", "Uzbek": f"Tarjima {i}", "Russian": f"Перевод {i}"} for i in range(1, 51)]
            st.table(pd.DataFrame(data))
        with tab3:
            for i in range(1, 11): st.write(f"{i}. Speaking topic question {i} for {lvl}")
    else:
        st.subheader(f"Уровень {lvl} - Программа русского языка")
        # Ruscha darslik qismi...
        st.write("Darsliklar yuklanmoqda...")
    st.markdown('</div>', unsafe_allow_html=True)
    if st.button("⬅️ BACK TO HOME"): st.session_state.page = 'main'; st.rerun()

# >>> GeminGPT PAGE <<<
elif st.session_state.page == 'gemin':
    st.title("👨‍🏫 GeminGPT Universal Tutor")
    st.markdown('<div class="lesson-card">', unsafe_allow_html=True)
    st.write("### Har qanday fanni tanlang va savol bering:")
    subj = st.selectbox("Fan:", ["Matematika", "Fizika", "IT", "Iqtisod", "Biologiya"])
    quest = st.text_input(f"{subj} bo'yicha savolingiz:")
    if st.button("GET 100B IQ ANSWER"):
        st.info(f"GeminGPT: {subj} bo'yicha tahlil yakunlandi. Kamron Xudaynazarov algoritmi bo'yicha javob...")
    st.markdown('</div>', unsafe_allow_html=True)
    if st.button("⬅️ BACK TO HOME"): st.session_state.page = 'main'; st.rerun()

# >>> WEB PAGE <<<
elif st.session_state.page == 'web':
    st.title("💻 Web Factory: Deployment")
    st.markdown('<div class="lesson-card">', unsafe_allow_html=True)
    st.write("### GitHub & Streamlit Masterclass")
    st.markdown("""
    1. **GitHub:** 'Sign Up' bosing (O'ng tepa).
    2. **Repo:** 'New' bosing (Yashil tugma, chapda).
    3. **Cloud:** 'share.streamlit.io' saytiga ulaning.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    if st.button("⬅️ BACK TO HOME"): st.session_state.page = 'main'; st.rerun()

# >>> AI PAGE <<<
elif st.session_state.page == 'ai':
    st.title("🤖 AI Architecture")
    st.markdown('<div class="lesson-card">', unsafe_allow_html=True)
    st.write("### Hugging Face Integration")
    st.markdown("1. **Spaces:** Tepa menyuda. \n2. **Create:** Ko'k tugma o'ngda. \n3. **SDK:** Streamlit.")
    st.markdown('</div>', unsafe_allow_html=True)
    if st.button("⬅️ BACK TO HOME"): st.session_state.page = 'main'; st.rerun()

# >>> FOOTER PAGES <<<
elif st.session_state.page == 'complaint':
    st.title("⚠️ Complaint Center")
    st.markdown('<div class="lesson-card">', unsafe_allow_html=True)
    st.text_area("Shikoyat mazmuni:")
    st.button("SUBMIT COMPLAINT")
    st.markdown('</div>', unsafe_allow_html=True)
    if st.button("⬅️ BACK"): st.session_state.page = 'main'; st.rerun()

elif st.session_state.page == 'help':
    st.title("🆘 Help & Support")
    st.markdown('<div class="lesson-card">', unsafe_allow_html=True)
    st.write("Tezkor yordam: +998 93 729 28 66")
    st.write("Telegram: @KGO_Admin")
    st.markdown('</div>', unsafe_allow_html=True)
    if st.button("⬅️ BACK"): st.session_state.page = 'main'; st.rerun()

elif st.session_state.page == 'about':
    st.title("ℹ️ About KGO Academy")
    st.markdown('<div class="lesson-card">', unsafe_allow_html=True)
    st.write("KGO Academy — Kamron Xudaynazarov tomonidan asos solingan zamonaviy ta'lim platformasi.")
    st.write("Bizning maqsadimiz — 100,000,000,000 IQ darajasidagi ta'limni hamma uchun ochiq qilish.")
    st.markdown('</div>', unsafe_allow_html=True)
    if st.button("⬅️ BACK"): st.session_state.page = 'main'; st.rerun()

# --- [6. DYNAMIC FOOTER - ALWAYS VISIBLE] ---
st.write("<br><br><br><hr>", unsafe_allow_html=True)
f1, f2, f3, f4 = st.columns([2, 1, 1, 1])

with f1:
    st.write("© 2026 KGO ONLINE SCHOOL | SAMARKAND")
with f2:
    st.markdown('<div class="footer-btn">', unsafe_allow_html=True)
    if st.button("ℹ️ About", key="f_about"): 
        st.session_state.page = 'about'
        st.rerun()
with f3:
    if st.button("🆘 Help", key="f_help"): 
        st.session_state.page = 'help'
        st.rerun()
with f4:
    if st.button("⚠️ Complaint", key="f_comp"): 
        st.session_state.page = 'complaint'
        st.rerun()
st.markdown('</div>', unsafe_allow_html=True)
