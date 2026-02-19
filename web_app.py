import streamlit as st
import random
import time
import requests
from streamlit_lottie import st_lottie
# Importing custom modules
from modules.question_engine import get_all_questions
from nlp_evaluator import analyze_answer_with_ai
from speech_to_text import capture_speech

# --- STEP 1: ANIMATION LOADER ---
# Fetches professional success animation data
def load_lottieurl(url: str):
    try:
        r = requests.get(url)
        return r.json() if r.status_code == 200 else None
    except:
        return None

lottie_success = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_pqnfmone.json")

# --- STEP 2: PAGE CONFIG & STYLING ---
st.set_page_config(page_title="AI Interview Prep 2.0", layout="wide")

# CSS to match the exact look of your screenshot (Large Blue Title)
st.markdown("""
    <style>
    .main-title {
        font-size: 55px !important;
        font-weight: 800 !important;
        color: #3498db !important;
        margin-left: 20px !important;
        display: inline-block;
        vertical-align: middle;
    }
    .header-container {
        display: flex;
        align-items: center;
        margin-bottom: 20px;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #007bff;
        color: white;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- STEP 3: PROFESSIONAL HEADER (Matches image_6ef71f.png) ---
# This container aligns the avatar and text horizontally
st.markdown(f"""
    <div class="header-container">
        <img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" width="80">
        <span class="main-title">AI-Powered Interview Preparation</span>
    </div>
    """, unsafe_allow_html=True)

st.write("Welcome to your personal AI career coach. This platform uses **Computer Vision** and **NLP** to simulate a real interview environment, providing feedback on your technical accuracy and professional presence.")
st.markdown("---")

# --- STEP 4: SESSION STATE ---
if "interview_active" not in st.session_state:
    st.session_state.interview_active = False
if "scores" not in st.session_state:
    st.session_state.scores = []
if "current_q" not in st.session_state:
    st.session_state.current_q = 0

# --- STEP 5: SIDEBAR ---
with st.sidebar:
    st.header("Preparation Settings")
    job_role = st.text_input("Target Job Role", "").strip()
    company = st.text_input("Target Company", "").strip()
    num_q = st.slider("Number of Questions", 1, 5, 2)
    input_mode = st.radio("Input Method", ["Voice", "Keyboard"])
    
    if st.button("🚀 Start New Interview"):
        # Fetching questions from the engine
        questions_list = get_all_questions(job_role, company)
        if questions_list:
            random.shuffle(questions_list)
            st.session_state.questions = questions_list[:num_q]
            st.session_state.current_q = 0
            st.session_state.scores = []
            st.session_state.interview_active = True
            st.rerun()
        else:
            st.error("No questions found for this role.")

# --- STEP 6: INTERVIEW FLOW ---
if st.session_state.interview_active:
    idx = st.session_state.current_q
    if idx < len(st.session_state.questions):
        q_text, keywords = st.session_state.questions[idx]
        st.subheader(f"Question {idx + 1}:")
        st.info(f"**{q_text}**")

        if input_mode == "Voice":
            if st.button("🎤 Start Speaking"):
                st.session_state.ans_text = capture_speech()
            user_ans = st.text_area("Answer:", value=st.session_state.get('ans_text', ''), height=150)
        else:
            user_ans = st.text_area("Type Answer:", height=150)

        if st.button("✅ Submit"):
            score, feedback = analyze_answer_with_ai(q_text, user_ans, keywords)
            st.session_state.scores.append(score)
            st.write(f"**Feedback:** {feedback}")
            st.session_state.current_q += 1
            st.button("Next Question")
    else:
        # --- PROFESSIONAL ANIMATION & COMPLETION ---
        if lottie_success:
            st_lottie(lottie_success, height=300)
        
        st.success("✔ Interview Completed Successfully.")
        avg = sum(st.session_state.scores) / len(st.session_state.scores)
        st.metric("Final Performance Score", f"{round(avg, 2)}/10")
        st.balloons()
        
        if st.button("Restart"):
            st.session_state.interview_active = False
            st.rerun()
else:
    # Initial landing message matching image_6ef71f.png
    st.write("Please configure your settings in the sidebar and click **Start New Interview**.")