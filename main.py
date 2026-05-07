import streamlit as st
import time

# --- [CONFIG] ---
st.set_page_config(page_title="KGO Academy", page_icon="👑", layout="wide")

# --- [DESIGN] ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@900&family=Inter:wght@400;700&display=swap');
    .stApp { background: #020617; color: white; font-family: 'Inter', sans-serif; }
    .mega-header { font-family: 'Orbitron', sans-serif; font-size: 60px; text-align: center; color: #ffd700; text-shadow: 0 0 20px #ffd700; }
    .step-box { background: #0f172a; border-left: 5px solid #ffd700; padding: 20px; border-radius: 10px; margin: 15px 0; }
    .ai-speech { background: #1e293b; padding: 15px; border-radius: 15px; font-style: italic; border: 1px dashed #ffd700; }
    .highlight { color: #ffd700; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

if 'page' not in st.session_state: st.session_state.page = 'home'

# --- [SIDEBAR] ---
with st.sidebar:
    st.markdown("<h1 style='color:#ffd700;'>KGO MENU</h1>", unsafe_allow_html=True)
    if st.button("🏛️ Dashboard"): st.session_state.page = 'home'; st.rerun()
    if st.button("🤖 AI Architecture"): st.session_state.page = 'ai'; st.rerun()
    if st.button("💻 Web Factory"): st.session_state.page = 'web'; st.rerun()
    if st.button("🌍 Language Lab"): st.session_state.page = 'lang'; st.rerun()
    st.write("---")
    st.write("📍 Samarqand, Kimyogarlar")
    st.write("📞 +998 93 729 28 66")

# --- [PAGES] ---

if st.session_state.page == 'home':
    st.markdown('<h1 class="mega-header">KGO ACADEMY</h1>', unsafe_allow_html=True)
    st.write("### 🧬 100,000,000,000 IQ Tizimiga xush kelibsiz!")
    st.write("Bu yerda bilim kutib turmaydi, u darhol beriladi.")

# >>> LANGUAGE LAB (AVTOMATIK DARSLIK) <<<
elif st.session_state.page == 'lang':
    st.title("🌍 Language Lab: Zero to IELTS")
    lang_choice = st.radio("Tilni tanlang:", ["English 🇺🇸", "Russian 🇷🇺"], horizontal=True)
    
    st.markdown('<div class="ai-speech"><b>KGO AI Teacher:</b> "Siz tanlov qildingiz, endi diqqat bilan eshiting. Men darsni boshladim!"</div>', unsafe_allow_html=True)
    
    if lang_choice == "English 🇺🇸":
        st.subheader("📚 Ingliz tili: Alifbodan IELTS gacha")
        
        with st.expander("1️⃣ STEP: Basics (Alifbo va Talaffuz)", expanded=True):
            st.write("Ingliz tili 26 harfdan iborat. Eng muhimi unli harflar: **A, E, I, O, U**.")
            st.info("💡 Qoida: 'A' harfi so'z boshida 'Ey' (Apple - noto'g'ri, Epl) yoki 'A' deb o'qiladi.")
        
        with st.expander("2️⃣ STEP: Tenses (Zamonlar - Fundamental)", expanded=True):
            st.markdown("""
            - **Present Simple (Hozirgi oddiy zamon):** Doimiy takrorlanadigan ishlar. 
                - *Formula:* `Subject + Verb (s/es)`
                - *Misol:* I speak English. (Men inglizcha gapiraman).
            - **Past Simple (O'tgan zamon):** Tugagan ishlar.
                - *Formula:* `Subject + Verb (ed/2-shakl)`
                - *Misol:* I learned English. (Men inglizcha o'rgandim).
            """)
        
        with st.expander("3️⃣ STEP: IELTS Road to 9.0", expanded=True):
            st.warning("IELTS uchun sizga 4 ta ko'nikma kerak: Reading, Writing, Listening, Speaking.")
            st.write("**Writing Task 2:** Sizdan kamida 250 ta so'zdan iborat akademik insho so'raladi.")

# >>> WEB FACTORY (INSTRUKSIYA BILAN) <<<
elif st.session_state.page == 'web':
    st.title("💻 Web Factory: Professional Guide")
    st.write("### Sayt yaratish va GitHub-ga joylash (Qadamma-qadam)")
    
    st.markdown("""
    <div class="step-box">
        <b class="highlight">1-QADAM: GitHub Account ochish</b><br>
        1. <a href="https://github.com" style="color:cyan;">github.com</a> saytiga kiring.<br>
        2. O'ng tepa burchakda <b>'Sign Up'</b> tugmasini bosing.<br>
        3. Emailingizni yozing va 'Continue' bosing.<br>
        4. Parol o'ylab toping (kamida 8 ta belgi).
    </div>
    <div class="step-box">
        <b class="highlight">2-QADAM: Yangi Repository (Loyiha) yaratish</b><br>
        1. Profilingizga kirgach, chap tarafdagi <b>'New'</b> (yashil tugma) bosing.<br>
        2. 'Repository name' qismiga <b>'kgo-academy'</b> deb yozing.<br>
        3. Pastroqqa tushib, <b>'Public'</b> tanlang va <b>'Create repository'</b> bosing.
    </div>
    <div class="step-box">
        <b class="highlight">3-QADAM: Kodni yuklash</b><br>
        1. 'Add file' tugmasini bosing (o'ng tepada).<br>
        2. 'Create new file' bosing, nomini <b>main.py</b> qiling va kodingizni joylang.
    </div>
    """, unsafe_allow_html=True)

# >>> AI ARCHITECTURE (HUGGING FACE BILAN) <<<
elif st.session_state.page == 'ai':
    st.title("🤖 AI Architecture: Hugging Face Guide")
    st.write("### O'z AI-ingni yaratish (Hugging Face orqali)")
    
    st.markdown("""
    <div class="step-box">
        <b class="highlight">1. Hugging Face-da ro'yxatdan o'tish</b><br>
        1. <a href="https://huggingface.co" style="color:cyan;">huggingface.co</a> ga kiring.<br>
        2. O'ng tepada <b>'Sign Up'</b> tugmasi bor, shuni bosing.<br>
        3. Email va Username kiriting.
    </div>
    <div class="step-box">
        <b class="highlight">2. Modelni tanlash yoki Space yaratish</b><br>
        1. Sahifaning tepa qismidagi menyudan <b>'Spaces'</b> bo'limiga o'ting.<br>
        2. O'ng tarafda <b>'Create new Space'</b> (ko'k tugma) bosing.<br>
        3. Space nomini yozing (masalan: 'my-ai-bot').<br>
        4. 'SDK' qismidan <b>'Streamlit'</b>ni tanlang (pastki qatorda o'rtada).
    </div>
    <div class="step-box">
        <b class="highlight">3. Modelni ishga tushirish</b><br>
        1. Sahifaning pastida <b>'Create Space'</b> tugmasini bosing.<br>
        2. Endi 'Files' bo'limiga o'tib, 'app.py' fayliga AI kodingizni yozing.
    </div>
    """, unsafe_allow_html=True)

# --- [FOOTER] ---
st.write("---")
st.markdown("<p style='text-align:center;'>© 2026 KGO ACADEMY | FOUNDER: KAMRON XUDAYNAZAROV</p>", unsafe_allow_html=True)
