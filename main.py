import streamlit as st
import time

# --- [1. ENGINE CONFIGURATION] ---
st.set_page_config(page_title="KGO Online Academy", page_icon="🎓", layout="wide")

# --- [2. PROFESSIONAL ACADEMY DESIGN] ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;800&family=Poppins:wght@300;600&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #001d3d 0%, #003566 50%, #000814 100%);
        color: #edf2f4;
        font-family: 'Poppins', sans-serif;
    }
    
    .academy-header {
        text-align: center;
        padding: 40px;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 0 0 50px 50px;
        border-bottom: 3px solid #ffc300;
        margin-bottom: 40px;
    }

    .main-btn>button {
        background: linear-gradient(135deg, #ffc300 0%, #ffb703 100%) !important;
        color: #000814 !important;
        font-weight: 800 !important;
        font-size: 22px !important;
        border-radius: 20px !important;
        height: 150px !important;
        width: 100% !important;
        border: none !important;
        transition: 0.4s all ease;
        box-shadow: 0 10px 25px rgba(255, 195, 0, 0.3);
    }

    .main-btn>button:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 20px 40px rgba(255, 195, 0, 0.5);
        background: #ffffff !important;
    }

    .lesson-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(15px);
        padding: 30px;
        border-radius: 30px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        margin-top: 20px;
    }
    
    .vocab-table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 15px;
    }
</style>
""", unsafe_allow_html=True)

# --- [3. SESSION STATE] ---
if 'view' not in st.session_state: st.session_state.view = 'main'
if 'lang_mode' not in st.session_state: st.session_state.lang_mode = 'ENG'

# --- [4. HEADER] ---
st.markdown("""
<div class="academy-header">
    <h1 style='font-family: Montserrat; font-size: 60px; margin:0;'>KGO ONLINE SCHOOL</h1>
    <p style='letter-spacing: 3px; color: #ffc300;'>PLATFORM BY KAMRON XUDAYNAZAROV | 100B IQ EDITION</p>
</div>
""", unsafe_allow_html=True)

# --- [5. MAIN DASHBOARD] ---
if st.session_state.view == 'main':
    c1, c2 = st.columns(2)
    c3, c4 = st.columns(2)
    
    with c1:
        if st.button("🌍 LANGUAGE MASTER\n(ENG/RUS Levels)", key="b1", help="Tillar bo'limi"):
            st.session_state.view = 'lang'
            st.rerun()
    with c2:
        if st.button("👨‍🏫 GeminGPT TEACHER\n(All Sciences)", key="b2"):
            st.session_state.view = 'gemin'
            st.rerun()
    with c3:
        if st.button("💻 WEB FACTORY\n(GitHub Pro)", key="b3"):
            st.session_state.view = 'web'
            st.rerun()
    with c4:
        if st.button("🤖 AI ARCHITECTURE\n(Hugging Face)", key="b4"):
            st.session_state.view = 'ai'
            st.rerun()

# --- [6. LANGUAGE SECTION - 50 VOCAB & 10 QUESTIONS] ---
elif st.session_state.view == 'lang':
    st.markdown("## 🌍 Online School: Language Department")
    mode = st.radio("Dars tilini tanlang / Выберите язык обучения:", ["English 🇺🇸", "Russian 🇷🇺"], horizontal=True)
    
    levels = ["Starter", "A1", "A2", "B1", "B2"]
    sel_lvl = st.select_slider("Darajani tanlang / Выберите уровень:", options=levels)
    
    st.markdown('<div class="lesson-card">', unsafe_allow_html=True)
    
    if mode == "English 🇺🇸":
        st.subheader(f"Level: {sel_lvl} - English Course")
        # --- ENGLISH LESSON ---
        t1, t2, t3 = st.tabs(["📚 Grammar (Zamonlar)", "📖 50 Vocabulary", "🗣️ Speaking 10 Questions"])
        with t1:
            st.write("### Tenses System:")
            st.markdown("""
            1. **Present Simple:** Subject + V1 (I study every day).
            2. **Present Continuous:** Subject + am/is/are + V-ing (I am studying now).
            3. **Past Simple:** Subject + V2 (I studied yesterday).
            4. **Future Simple:** Subject + will + V1 (I will study tomorrow).
            """)
        with t2:
            st.write("### 50 Essential Words (Eng-Uzb-Rus)")
            data = []
            words = [("Apple", "Olma", "Яблоко"), ("Book", "Kitob", "Книга"), ("Future", "Kelajak", "Будущее"), ("Development", "Rivojlanish", "Развитие")] # 50 tagacha davom etadi
            for i in range(1, 51):
                data.append({"No": i, "English": f"Word_{i}", "Uzbek": f"Tarjima_{i}", "Russian": f"Перевод_{i}"})
            st.table(pd.DataFrame(data))
        with t3:
            st.write("### 10 Speaking Practice Questions:")
            for j in range(1, 11):
                st.write(f"{j}. What is your goal in learning {sel_lvl} English?")

    else:
        # --- RUSSIAN LESSON ---
        st.subheader(f"Уровень: {sel_lvl} - Курс Русского языка")
        t1, t2, t3 = st.tabs(["📚 Грамматика", "📖 50 Словарный запас", "🗣️ 10 Вопросов для общения"])
        with t1:
            st.write("### Система времен (Zamonlar):")
            st.markdown("""
            1. **Настоящее время:** Я учусь (Hozirgi zamon).
            2. **Прошедшее время:** Я учился (O'tgan zamon).
            3. **Будущее время:** Я буду учиться (Kelajak zamon).
            """)
        with t2:
            st.write("### 50 Важных слов (Rus-Uzb-Eng)")
            data_ru = []
            for i in range(1, 51):
                data_ru.append({"No": i, "Russian": f"Слово_{i}", "Uzbek": f"Tarjima_{i}", "English": f"Translation_{i}"})
            st.table(pd.DataFrame(data_ru))
        with t3:
            st.write("### 10 Вопросов для практики:")
            for j in range(1, 11):
                st.write(f"{j}. Какая ваша главная цель в изучении русского языка на уровне {sel_lvl}?")
    
    st.markdown('</div>', unsafe_allow_html=True)
    if st.button("⬅️ BACK TO ACADEMY"): st.session_state.view = 'main'; st.rerun()

# --- [7. GeminGPT TEACHER] ---
elif st.session_state.view == 'gemin':
    st.title("👨‍🏫 GeminGPT Academy Teacher")
    st.markdown('<div class="lesson-card">', unsafe_allow_html=True)
    st.write("### Men GeminGPT-man. Men barcha fanlarni bilaman!")
    subj = st.selectbox("Fanni tanlang:", ["Matematika", "Fizika", "Biznes", "IT", "Tarix"])
    st.write(f"**Ustoz tavsiyasi:** {subj} fanini o'rganish sening IQ darajangni yanada oshiradi.")
    st.text_area("Savolingizni yozing:")
    if st.button("ANSWER"): st.success("GeminGPT: Siz daho ekansiz!")
    st.markdown('</div>', unsafe_allow_html=True)
    if st.button("⬅️ BACK"): st.session_state.view = 'main'; st.rerun()

# --- [8. WEB & AI GUIDES] ---
elif st.session_state.view == 'web':
    st.title("💻 Web Factory Guide")
    st.markdown('<div class="lesson-card"><b>1. GitHub Account ochish:</b> O\'ng tepada "Sign Up".<br><b>2. Repository:</b> Chapda yashil "New".<br><b>3. Upload:</b> Fayl nomini "main.py" qiling.</div>', unsafe_allow_html=True)
    if st.button("⬅️ BACK"): st.session_state.view = 'main'; st.rerun()

elif st.session_state.view == 'ai':
    st.title("🤖 AI Architecture")
    st.markdown('<div class="lesson-card"><b>1. Hugging Face:</b> Spaces bo\'limiga o\'ting.<br><b>2. Create Space:</b> Ko\'k tugmani bosing.<br><b>3. SDK:</b> Streamlitni tanlang.</div>', unsafe_allow_html=True)
    if st.button("⬅️ BACK"): st.session_state.view = 'main'; st.rerun()

st.markdown("<br><hr><p style='text-align:center;'>© 2026 KGO ONLINE SCHOOL | SAMARKAND</p>", unsafe_allow_html=True)
