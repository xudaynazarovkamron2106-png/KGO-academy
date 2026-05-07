import streamlit as st
import time

# --- [1. MA'LUMOTLAR BAZASI (DATABASE)] ---
# Har bir daraja va til uchun alohida ma'lumotlar
DATABASE = {
    "English": {
        "Starter": {"vocab": "1. Hello - Salom\n2. Apple - Olma\n3. School - Maktab", "speaking": "What is your name?"},
        "A1": {"vocab": "1. Journey - Sayohat\n2. Experience - Tajriba\n3. Skill - Mahorat", "speaking": "Tell me about your daily routine."},
        "B2": {"vocab": "1. Hypothesis - Faraz\n2. Consequently - Natijada\n3. Sustainable - Barqaror", "speaking": "Discuss the impact of AI on humanity."}
    },
    "Russian": {
        "Starter": {"vocab": "1. Привет - Salom\n2. Книга - Kitob\n3. Вода - Suv", "speaking": "Как тебя зовут?"},
        "A1": {"vocab": "1. Путешествие - Sayohat\n2. Работа - Ish\n3. Семья - Oila", "speaking": "Расскажи о своей семье."},
        "B2": {"vocab": "1. Влияние - Ta'sir\n2. Следовательно - Shuning uchun\n3. Развитие - Rivojlanish", "speaking": "Как технологии меняют мир?"}
    },
    "Math": {
        "Algebra": "Formulalar: (a+b)² = a² + 2ab + b²\nKvadrat tenglama: x = (-b ± √D) / 2a",
        "Geometriya": "Pifagor teoremasi: a² + b² = c²\nDoira yuzi: S = πr²",
        "Logika": "Agar A=B va B=C bo'lsa, unda A=C bo'ladi."
    }
}

# --- [2. PAGE CONFIG] ---
st.set_page_config(page_title="KGO BOSS ACADEMY", layout="wide")

# --- [3. DIZAYN (STYLES)] ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&family=Share+Tech+Mono&display=swap');
    
    .stApp { background: #000428; background: linear-gradient(to bottom, #004e92, #000428); color: white; }
    
    .boss-msg { 
        background: rgba(0, 255, 0, 0.1); 
        border: 2px solid #00ff00; 
        padding: 20px; 
        border-radius: 15px; 
        font-family: 'Share Tech Mono', monospace;
        color: #00ff00;
        text-shadow: 0 0 10px #00ff00;
    }

    .stButton>button { 
        background: linear-gradient(135deg, #ffc300 0%, #ffb703 100%) !important;
        color: #000!important; font-weight: bold!important; border-radius: 12px!important;
        height: 100px!important; font-family: 'Orbitron'; border: none!important;
    }
    
    .ai-card {
        background: rgba(0,0,0,0.6); padding: 25px; border-radius: 20px;
        border-left: 5px solid #ffc300; font-family: 'Consolas'; font-size: 18px;
    }
</style>
""", unsafe_allow_html=True)

# --- [4. SESSION STATE] ---
if 'is_pro' not in st.session_state: st.session_state.is_pro = False
if 'is_boss' not in st.session_state: st.session_state.is_boss = False
if 'page' not in st.session_state: st.session_state.page = 'main'

# --- [5. TYPEWRITER EFFECT] ---
def write_ai(text):
    placeholder = st.empty()
    full = ""
    for char in text:
        full += char
        placeholder.markdown(f'<div class="ai-card">{full}▌</div>', unsafe_allow_html=True)
        time.sleep(0.01)

# --- [6. HEADER & PROMO] ---
st.markdown('<h1 style="text-align:center; font-family:Orbitron; color:#ffc300;">KGO ACADEMY SYSTEM</h1>', unsafe_allow_html=True)

if not st.session_state.is_pro:
    _, c_promo = st.columns([5, 1.5])
    with c_promo:
        with st.popover("🟢 PRO / LOGIN"):
            code = st.text_input("Maxfiy kod:", type="password")
            if st.button("KIRISH"):
                if code == "KAMA":
                    st.session_state.is_pro = True
                    st.session_state.is_boss = True
                    st.rerun()
                elif code == "UZKGO":
                    st.session_state.is_pro = True
                    st.rerun()
            st.write("---")
            st.info("To'lov va yangiliklar: [@PrimeK21](https://t.me/PrimeK21)")

# --- [7. BOSS WELCOME] ---
if st.session_state.is_boss:
    st.markdown(f"""
    <div class="boss-msg">
        [SYSTEM ONLINE] <br>
        STATUS: Kamron Xudaynazarov (BOSS) nazorati ostida. <br>
        MESSAGE: Assalomu aleykum Boss, sayt yaxshi ishlab turibdi. Hamma tizimlar barqaror!
    </div>
    """, unsafe_allow_html=True)

# --- [8. MAIN PAGE] ---
if st.session_state.page == 'main':
    st.write("<br>", unsafe_allow_html=True)
    n_cols = 5 if st.session_state.is_pro else 3
    cols = st.columns(n_cols)
    
    with cols[0]:
        if st.button("🌍 LANGUAGE\n(ENG/RUS)"): st.session_state.page = 'lang'; st.rerun()
    with cols[1]:
        if st.button("📐 MATH\n(FORMULAS)"): st.session_state.page = 'math'; st.rerun()
    with cols[2]:
        if st.button("👨‍🏫 GeminGPT\n(TUTOR)"): st.session_state.page = 'gemin'; st.rerun()
        
    if st.session_state.is_pro:
        with cols[3]:
            if st.button("🤖 CREATE AI\n(BOSS MODE)"): st.session_state.page = 'create_ai'; st.rerun()
        with cols[4]:
            if st.button("📚 SCIENCES\n(ALL SUBJECTS)"): st.session_state.page = 'sciences'; st.rerun()

# --- [9. PAGE LOGICS] ---
elif st.session_state.page == 'lang':
    st.header("🌍 Multi-Language Center")
    l, r = st.columns(2)
    sel_lang = l.selectbox("Tilni tanlang:", ["English", "Russian"])
    sel_lvl = r.selectbox("Darajani tanlang:", ["Starter", "A1", "B2"])
    
    if st.button("DARSNI KO'RISH"):
        data = DATABASE[sel_lang].get(sel_lvl, DATABASE[sel_lang]["Starter"])
        txt = f"--- {sel_lang} {sel_lvl} ---\n\nVOCABULARY:\n{data['vocab']}\n\nSPEAKING:\n{data['speaking']}"
        write_ai(txt)
    if st.button("⬅️ DASHBOARD"): st.session_state.page = 'main'; st.rerun()

elif st.session_state.page == 'math':
    st.header("📐 Mathematics Hub")
    m_type = st.radio("Bo'limni tanlang:", ["Algebra", "Geometriya", "Logika"], horizontal=True)
    if st.button("FORMULALARNI CHIQAR"):
        write_ai(DATABASE["Math"][m_type])
    if st.button("⬅️ DASHBOARD"): st.session_state.page = 'main'; st.rerun()

elif st.session_state.page == 'gemin':
    st.header("👨‍🏫 GeminGPT Tutor")
    user_q = st.text_input("Savolingizni bering:")
    if st.button("JAVOB"):
        if not st.session_state.is_pro:
            write_ai("Free Trail-da javoblar cheklangan. To'liq darslar uchun @PrimeK21 ga bog'laning.")
        else:
            if "salom" in user_q.lower():
                write_ai("Assalomu aleykum! Men KGO AI repetitoriman. Sizga qanday yordam bera olaman?")
            else:
                write_ai(f"Tizim '{user_q}' bo'yicha ma'lumotlarni tahlil qilmoqda... Javob: Bu soha bo'yicha darslarimiz Sciences bo'limida batafsil yoritilgan.")
    if st.button("⬅️ DASHBOARD"): st.session_state.page = 'main'; st.rerun()

elif st.session_state.page == 'sciences':
    st.header("📚 Full Sciences (PRO ONLY)")
    sc = st.selectbox("Fan:", ["Fizika", "Tarix", "Ona tili", "Adabiyot"])
    if st.button("O'QISH"):
        write_ai(f"{sc} fani bo'yicha KGO Professional kursi boshlandi. 1-Mavzu: Kirish...")
    if st.button("⬅️ DASHBOARD"): st.session_state.page = 'main'; st.rerun()

elif st.session_state.page == 'create_ai':
    st.header("🤖 AI Creation (BOSS MODE)")
    write_ai("Tizim nazoratda. Kamron, siz yangi model yaratishingiz uchun HuggingFace bazasi ulandi.")
    if st.button("⬅️ DASHBOARD"): st.session_state.page = 'main'; st.rerun()

# --- [10. FOOTER] ---
st.markdown(f"<br><hr><p style='text-align:center;'>To'lov va yangiliklar uchun: <a href='https://t.me/PrimeK21' style='color:#ffc300;'>@PrimeK21</a></p>", unsafe_allow_html=True)
