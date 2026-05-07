# ====================================================================================================
# 🏛️ PLATFORMA: KGO ACADEMY - FUTURE LEARNING SYSTEMS
# 🎓 MAQSAD: AI VA TEXNOLOGIYALARNI 100,000 IQ DARAJASIDA O'RGATISH
# 👤 ASOSCHI: KAMRON XUDAYNAZAROV
# ====================================================================================================

import streamlit as st
import time

# --- [SECTION 1] SAHIFA SOZLAMALARI ---
st.set_page_config(
    page_title="KGO Academy | Knowledge is Power",
    page_icon="🎓",
    layout="wide"
)

# --- [SECTION 2] ACADEMY PREMIUM DESIGN (CSS) ---
st.markdown("""
<style>
    /* KGO Academy uchun maxsus qora va tilla rangli dizayn */
    .stApp {
        background: radial-gradient(circle at top, #0f172a, #020617);
        color: #e2e8f0;
    }
    
    .academy-header {
        text-align: center;
        padding: 50px;
        background: rgba(255, 255, 255, 0.03);
        border-radius: 30px;
        border: 1px solid rgba(255, 215, 0, 0.2);
        margin-bottom: 40px;
    }
    
    .kgo-title {
        font-size: 70px;
        font-weight: 900;
        letter-spacing: 5px;
        background: linear-gradient(90deg, #ffd700, #ffffff, #ffd700);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: shine 3s linear infinite;
    }
    
    @keyframes shine {
        to { background-position: 200% center; }
    }

    .course-box {
        background: #0f172a;
        padding: 30px;
        border-radius: 20px;
        border-bottom: 4px solid #ffd700;
        transition: 0.4s;
        height: 100%;
    }
    
    .course-box:hover {
        transform: scale(1.05);
        box-shadow: 0 20px 40px rgba(255, 215, 0, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# --- [SECTION 3] ASOSIY QISM ---
st.markdown('<div class="academy-header">', unsafe_allow_html=True)
st.markdown('<h1 class="kgo-title">KGO ACADEMY</h1>', unsafe_allow_html=True)
st.markdown('<h3>Build the Future with AI</h3>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- [SECTION 4] DARSLAR ---
st.subheader("🚀 Bizning Kurslar")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="course-box">
        <h2 style="color:#ffd700;">🧠 AI Architecture</h2>
        <p>GeminGPT kabi murakkab AI tizimlarini yaratishni o'rganing.</p>
        <hr>
        <li>Python Foundation</li>
        <li>API Integration</li>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="course-box">
        <h2 style="color:#ffd700;">🎨 Prompt Mastery</h2>
        <p>FLUX va Ideogram yordamida san'at darajasidagi rasmlar yaratish.</p>
        <hr>
        <li>Advanced Prompts</li>
        <li>Style Engineering</li>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="course-box">
        <h2 style="color:#ffd700;">💻 Web Development</h2>
        <p>Professional saytlar va Streamlit interfeyslarini qurish.</p>
        <hr>
        <li>Modern UI/UX</li>
        <li>Deployment</li>
    </div>
    """, unsafe_allow_html=True)

# --- [SECTION 5] YANGI AI - KGO TUTOR ---
st.write("---")
st.header("👨‍🏫 KGO Tutor bilan bog'lanish")

if "academy_chat" not in st.session_state:
    st.session_state.academy_chat = []

chat_input = st.chat_input("Akademiyaga oid savolingizni bering...")

if chat_input:
    # Bu yerda yangi AI logic bo'ladi
    st.session_state.academy_chat.append({"role": "user", "content": chat_input})
    
    with st.chat_message("assistant"):
        st.write("Salom! Men KGO Academy yordamchisiman. Kamron Xudaynazarovning bilimlar bazasi asosida sizga yordam beraman.")

st.markdown("<br><br><p style='text-align:center;'>© 2026 KGO GROUP GLOBAL SYSTEMS | KAMRON XUDAYNAZAROV</p>", unsafe_allow_html=True)
