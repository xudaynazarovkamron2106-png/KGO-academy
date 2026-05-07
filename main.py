import streamlit as st
import time

# --- [1. ENGINE CONFIGURATION] ---
st.set_page_config(page_title="KGO Academy | Central Intelligence", page_icon="👑", layout="wide")

# --- [2. SUPREME INTERFACE DESIGN - CSS] ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@900&family=Inter:wght@400;700&display=swap');
    
    .stApp { background: #020617; color: white; font-family: 'Inter', sans-serif; }
    
    .mega-title { 
        font-family: 'Orbitron', sans-serif; 
        font-size: 80px; 
        text-align: center; 
        background: linear-gradient(90deg, #ffd700, #ffffff, #ffd700);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 50px;
    }

    /* Markaziy tugmalar stili */
    .stButton>button {
        background: linear-gradient(135deg, #ffd700 0%, #b8860b 100%) !important;
        color: black !important;
        font-family: 'Orbitron', sans-serif !important;
        font-weight: 900 !important;
        font-size: 20px !important;
        border-radius: 25px !important;
        height: 100px !important;
        border: none !important;
        box-shadow: 0 10px 30px rgba(255, 215, 0, 0.2);
        transition: 0.4s all;
    }

    .stButton>button:hover {
        transform: scale(1.05) translateY(-10px);
        box-shadow: 0 20px 50px rgba(255, 215, 0, 0.5);
    }

    .lesson-box {
        background: rgba(15, 23, 42, 0.8);
        border: 2px solid #ffd700;
        border-radius: 30px;
        padding: 40px;
        margin-top: 20px;
    }

    .step-card {
        background: #1e293b;
        border-left: 8px solid #ffd700;
        padding: 20px;
        margin: 15px 0;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# --- [3. SESSION STATE] ---
if 'view' not in st.session_state: st.session_state.view = 'main'

# --- [4. MAIN SCREEN - ALL BUTTONS HERE] ---
if st.session_state.view == 'main':
    st.markdown('<h1 class="mega-title">KGO ACADEMY</h1>', unsafe_allow_html=True)
    st.write("<h3 style='text-align:center;'>Barcha tizimlar tayyor. Yo'nalishni tanlang:</h3>", unsafe_allow_html=True)
    st.write("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🤖 AI CREATION (HUGGING FACE)"):
            st.session_state.view = 'ai_lesson'
            st.rerun()

    with col2:
        if st.button("💻 WEB FACTORY (GITHUB GUIDE)"):
            st.session_state.view = 'web_lesson'
            st.rerun()

    with col3:
        if st.button("🌍 LANGUAGE MASTER (ENG/RUS)"):
            st.session_state.view = 'lang_lesson'
            st.rerun()

    st.write("---")
    st.write(f"<p style='text-align:center;'>Founder: Kamron Xudaynazarov | 📍 Samarqand | 📞 +998 93 729 28 66</p>", unsafe_allow_html=True)

# --- [5. LESSON PAGES - AUTOMATIC CONTENT] ---

# >>> AI LESSON (HUGGING FACE) <<<
elif st.session_state.view == 'ai_lesson':
    st.markdown("## 🤖 Hugging Face orqali AI yaratish")
    st.markdown('<div class="lesson-box">', unsafe_allow_html=True)
    st.write("### AI Ustoz: 'Hugging Face - bu AI modellari dunyosi. Diqqat bilan bajaring:'")
    
    st.markdown("""
    <div class="step-card">
        <b>1. Ro'yxatdan o'tish:</b> <a href="https://huggingface.co" style="color:#ffd700;">huggingface.co</a> saytiga kiring. 
        <b>O'ng tarafdagi eng tepada 'Sign Up'</b> tugmasini bosing.
    </div>
    <div class="step-card">
        <b>2. Space yaratish:</b> Sahifaning <b>tepa menyusidan 'Spaces'</b> bo'limini toping (ikkinchi yoki uchinchi bo'lim). 
        Keyin <b>o'ng tarafda ko'k rangli 'Create new Space'</b> tugmasini bosing.
    </div>
    <div class="step-card">
        <b>3. Sozlamalar:</b> Space nomini yozing. Pastroqda <b>'Streamlit'</b> variantini tanlang (u o'rtada turadi). 
        Eng pastga tushib <b>'Create Space'</b> tugmasini bosing.
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("⬅️ ASOSIY EKRANGA QAYTISH"):
        st.session_state.view = 'main'
        st.rerun()

# >>> WEB LESSON (GITHUB) <<<
elif st.session_state.view == 'web_lesson':
    st.markdown("## 💻 Web Factory: GitHub & Deployment")
    st.markdown('<div class="lesson-box">', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="step-card">
        <b>1. GitHub Account:</b> <a href="https://github.com" style="color:#ffd700;">github.com</a> ga kiring. 
        <b>O'ng tepada 'Sign Up'</b> bor. Emailingizni tasdiqlang.
    </div>
    <div class="step-card">
        <b>2. Yangi Loyiha:</b> Dashboardingizning <b>chap tarafida yashil 'New'</b> tugmasi turadi. 
        Shuni bosing va 'kgo-site' deb nom bering.
    </div>
    <div class="step-card">
        <b>3. Kodni Joylash:</b> Repository yaratilgach, <b>'creating a new file'</b> havolasini bosing. 
        Fayl nomini <b>main.py</b> qiling va kodingizni ichiga tashlab, pastdagi <b>'Commit changes'</b> tugmasini bosing.
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("⬅️ ASOSIY EKRANGA QAYTISH"):
        st.session_state.view = 'main'
        st.rerun()

# >>> LANGUAGE LESSON (AUTOMATIC ENG/RUS) <<<
elif st.session_state.view == 'lang_lesson':
    st.title("🌍 Language Lab: Automatic Learning")
    
    option = st.radio("Qaysi tilni boshlaymiz?", ["English 🇺🇸", "Russian 🇷🇺"], horizontal=True)
    
    st.markdown('<div class="lesson-box">', unsafe_allow_html=True)
    if option == "English 🇺🇸":
        st.write("### 🇺🇸 Ingliz tili: Zero to IELTS")
        st.write("AI Teacher: 'Darhol Present Simple zamonidan boshlaymiz.'")
        st.markdown("""
        - **Harflar:** Ingliz alifbosida 26 harf bor. Unlilar: A, E, I, O, U.
        - **Zamonlar:** - *Present Simple:* Kundalik ishlar (I go to school). 
            - *Present Continuous:* Hozir qilayotgan ishingiz (I am learning English).
        - **IELTS Strategy:** Reading bo'limida 'Skimming' va 'Scanning' texnikasidan foydalaning.
        """)
    else:
        st.write("### 🇷🇺 Rus tili: Noldan o'rganish")
        st.markdown("""
        - **Alifbo:** 33 ta harf. Eng muhimi 'Ь' va 'Ъ' belgilarini o'rganish.
        - **Gap qurish:** Rus tilida gaplar 'Padej' (kelishik) orqali o'zgaradi.
        - **Maslahat:** Har kuni kamida 10 ta fe'l yodlang.
        """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("⬅️ ASOSIY EKRANGA QAYTISH"):
        st.session_state.view = 'main'
        st.rerun()
