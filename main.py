import streamlit as st

# --- [1. SAHIFA SOZLAMALARI] ---
st.set_page_config(page_title="KGO Academy", page_icon="🎓", layout="wide")

if 'page' not in st.session_state:
    st.session_state.page = 'home'

# --- [2. DAXSHATLI DIZAYN] ---
st.markdown("""
<style>
    .stApp { background: #020617; color: white; }
    .title { font-size: 50px; font-weight: 900; text-align: center; color: #ffd700; }
    .btn-desc { font-size: 14px; color: #94a3b8; text-align: center; margin-bottom: 10px; }
    .card { background: #0f172a; padding: 20px; border-radius: 15px; border: 1px solid #334155; }
</style>
""", unsafe_allow_html=True)

# --- [3. SAHIFALAR] ---

# --- ASOSIY SAHIFA ---
if st.session_state.page == 'home':
    st.markdown('<h1 class="title">KGO ACADEMY</h1>', unsafe_allow_html=True)
    st.write("---")
    
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write("### 🤖 1. AI Architecture")
        st.write('<p class="btn-desc">GeminGPT kabi aqlli botlarni noldan qurishni o\'rgatadi.</p>', unsafe_allow_html=True)
        if st.button("AI Bo'limiga o'tish", use_container_width=True):
            st.session_state.page = 'ai'
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write("### 💻 2. Website Creation")
        st.write('<p class="btn-desc">Rasmlardan qanday qilib tayyor sayt yaratish sirlari.</p>', unsafe_allow_html=True)
        if st.button("Web Bo'limiga o'tish", use_container_width=True):
            st.session_state.page = 'web'
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write("### 🌍 3. Foreign Languages")
        st.write('<p class="btn-desc">Ingliz va Rus tillarini Grammar, Speaking va Essay bilan o\'rganing.</p>', unsafe_allow_html=True)
        if st.button("Tillar Bo'limiga o'tish", use_container_width=True):
            st.session_state.page = 'lang'
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    with col4:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write("### 📚 4. Umumiy Ta'lim")
        st.write('<p class="btn-desc">Matematika, Ona tili va boshqa fanlar darsliklari.</p>', unsafe_allow_html=True)
        if st.button("Fanlar Bo'limiga o'tish", use_container_width=True):
            st.session_state.page = 'edu'
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# --- 2-BUTTON: WEB SITE ---
elif st.session_state.page == 'web':
    st.title("💻 Website Creation")
    st.write("### Sayt yaratish bosqichlari:")
    # Rasm bilan tushuntirish
    st.image("https://miro.medium.com/v2/resize:fit:1200/1*669eW0vR5s9_HjJmE6X5yA.png", caption="Web Development Roadmap")
    st.markdown("""
    1. **Design:** Avval saytning rasmini chizasiz.
    2. **Coding:** Rasmdagi elementlarni Python yoki HTML kodiga aylantirasiz.
    3. **Launch:** Tayyor kodni internetga chiqarasiz.
    """)
    if st.button("⬅️ Bosh sahifa"): st.session_state.page = 'home'; st.rerun()

# --- 3-BUTTON: TILLAR ---
elif st.session_state.page == 'lang':
    st.title("🌍 Foreign Languages")
    til = st.selectbox("Tilni tanlang:", ["Ingliz tili 🇺🇸", "Rus tili 🇷🇺"])
    
    st.subheader(f"{til} bo'yicha darslar:")
    t1, t2, t3 = st.tabs(["📖 Grammar", "🗣️ Speaking", "📝 Essay"])
    
    with t1:
        st.write("Grammatika qoidalari: Tenses, Articles va boshqalar.")
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # Namuna video
    with t2:
        st.write("Talaffuz va kundalik muloqot mashqlari.")
        st.image("https://img.freepik.com/free-vector/english-language-concept-illustration_114360-1111.jpg", width=400)
    with t3:
        st.write("Insho yozish strukturasi va namunalari.")

    if st.button("⬅️ Bosh sahifa"): st.session_state.page = 'home'; st.rerun()

# --- 4-BUTTON: TA'LIM ---
elif st.session_state.page == 'edu':
    st.title("📚 Umumiy Ta'lim Fanlari")
    fan = st.radio("Fanni tanlang:", ["Matematika", "Ona tili", "Fizika"])
    
    st.subheader(f"{fan} dars xonasi")
    st.image("https://img.freepik.com/free-vector/back-to-school-background_23-2148604516.jpg", width=600)
    st.write(f"Siz hozir {fan} fani bo'yicha video darslar va rasmli qo'llanmalarni ko'rishingiz mumkin.")
    
    if st.button("⬅️ Bosh sahifa"): st.session_state.page = 'home'; st.rerun()

# --- [4. AI TEACHER & BUSINESS] ---
st.write("---")
st.sidebar.markdown("### 👨‍🏫 KGO AI Teacher")
st.sidebar.info("Salom! Men sizga saytlar yaratish, tillar va biznesni qanday boshlashni o'rgataman.")
if st.sidebar.button("Biznes darsi"):
    st.sidebar.success("Biznes darsi: 1. G'oya -> 2. Sayt -> 3. Mijoz!")

st.markdown('<div style="text-align:center; color:gray;">© 2026 KGO Group | Kamron Xudaynazarov</div>', unsafe_allow_html=True)
