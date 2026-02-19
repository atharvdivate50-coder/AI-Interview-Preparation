import streamlit as st
import random
import time
from modules.question_engine import get_all_questions
from nlp_evaluator import analyze_answer_with_ai
from vision_analyzer import analyze_interview_presence
from speech_to_text import capture_speech

# ---------------------------------------------------------
# 1. PAGE CONFIGURATION & UI STYLING
# ---------------------------------------------------------
# Set the browser tab title, robot icon, and wide layout to keep the title on one line
st.set_page_config(page_title="AI Interview Prep 2.0", page_icon="🤖", layout="wide")

# Inject Custom CSS for professional branding and visibility
st.markdown("""
    <style>
    .title-text { 
        font-size: 48px !important; 
        font-weight: 800 !important; 
        color: #1E90FF !important; 
        white-space: nowrap !important; 
        margin-bottom: 0px !important;
        line-height: 1.2 !important;
    }
    .stButton>button { 
        width: 100%; 
        border-radius: 5px; 
        height: 3em; 
        background-color: #007bff; 
        color: white; 
        font-weight: bold; 
    }
    .stInfo { font-size: 1.1em; border-left: 5px solid #007bff; }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. HEADER SECTION
# ---------------------------------------------------------
# Create a two-column layout for the logo and the giant blue title
col_logo, col_title = st.columns([1, 10])
with col_logo:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=80)
with col_title:
    st.markdown('<h1 class="title-text">AI-Powered Interview Preparation</h1>', unsafe_allow_html=True)

st.markdown("""
Welcome to your personal AI career coach. This platform uses **Computer Vision** and **NLP** to simulate a real interview environment, providing feedback on your technical accuracy and 
professional presence.
""")
st.markdown("---")

# ---------------------------------------------------------
# 3. SESSION STATE INITIALIZATION
# ---------------------------------------------------------
# Streamlit re-runs the script on every interaction; we use session_state 
# to "remember" data across these re-runs
if "questions" not in st.session_state:
    st.session_state.questions = [] # Stores selected questions
if "current_q" not in st.session_state:
    st.session_state.current_q = 0   # Tracks which question index we are on
if "current_answer" not in st.session_state:
    st.session_state.current_answer = "" # Temporarily stores spoken text
if "interview_active" not in st.session_state:
    st.session_state.interview_active = False # Tracks if the interview has started
if "vision_scanned" not in st.session_state:
    st.session_state.vision_scanned = False # Ensures webcam runs once per question
if "scores" not in st.session_state:
    st.session_state.scores = [] # List to store AI scores for final average

# ---------------------------------------------------------
# 4. SIDEBAR SETTINGS (USER INPUT)
# ---------------------------------------------------------
with st.sidebar:
    st.header("Preparation Settings")
    job_role = st.text_input("Target Job Role", "").strip()
    company = st.text_input("Target Company", "").strip()
    num_q = st.slider("Number of Questions", 1, 10, 2)
    input_mode = st.radio("Input Method", ["Voice", "Keyboard"])
    
    # Trigger to fetch questions and start the session
    if st.button("🚀 Start New Interview"):
        questions_list = get_all_questions(job_role, company)
        if questions_list:
            random.shuffle(questions_list)
            st.session_state.questions = questions_list[:num_q]
            st.session_state.current_q = 0
            st.session_state.current_answer = ""
            st.session_state.scores = []
            st.session_state.vision_scanned = False
            st.session_state.interview_active = True
            st.rerun() # Refresh page to show the first question
        else:
            st.error("No questions found for this role.")

# ---------------------------------------------------------
# 5. MAIN INTERVIEW INTERFACE
# ---------------------------------------------------------
if st.session_state.interview_active:
    curr_idx = st.session_state.current_q
    
    # Check if current question index is within the list size
    if curr_idx < len(st.session_state.questions):
        q_text, keywords = st.session_state.questions[curr_idx]
        
        st.subheader(f"Question {curr_idx + 1} of {len(st.session_state.questions)}")
        st.info(f"**{q_text}**")

        # Step 5a: Automatic Vision Scan 
        # Runs automatically at the start of every question
        if not st.session_state.vision_scanned:
            with st.spinner("AI is analyzing your professional presence..."):
                v_score, v_msg = analyze_interview_presence()
                st.session_state.vision_scanned = True
                st.session_state.last_vision = (v_score, v_msg)
            st.rerun() # Refresh to show the scan results and answer box
        
        v_score, v_msg = st.session_state.last_vision
        st.write(f"📷 **Presence Check:** {v_msg} ({v_score}/10)")
        
        # Step 5b: Answer Capture (Voice or Typing)
        if input_mode == "Voice":
            if st.button("🎤 Start Speaking"):
                st.session_state.current_answer = capture_speech()
            # The text area is linked to the session state so voice data persists
            user_ans = st.text_area("Your Spoken Answer:", value=st.session_state.current_answer, height=150)
        else:
            user_ans = st.text_area("Type your answer here:", height=150)

        st.markdown("---")
        
        # Step 5c: AI Evaluation Logic
        if st.button("✅ Submit Final Answer"):
            if user_ans and len(user_ans) > 5:
                # Call the Keyword-NLP module to grade the answer
                ai_score, ai_feedback = analyze_answer_with_ai(q_text, user_ans, keywords)
                st.session_state.scores.append(ai_score)
                
                st.success(f"**Score Recorded!** (AI Content: {ai_score}/10)")
                st.write(f"**Interviewer Feedback:** {ai_feedback}")
                
                # Update counters and reset temporary storage for next question
                st.session_state.current_q += 1
                st.session_state.vision_scanned = False
                st.session_state.current_answer = ""
                
                # If more questions remain, show 'Proceed', otherwise show 'Complete'
                if st.session_state.current_q < len(st.session_state.questions):
                    if st.button("Proceed to Next Question"):
                        st.rerun()
                else:
                    if st.button("Complete Session & Final Score"):
                        st.rerun()
            else:
                st.warning("Please provide a more detailed answer first.")
                
    else:
        # ---------------------------------------------------------
        # 6. FINAL SUMMARY REPORT
        # ---------------------------------------------------------
        # This section triggers when current_q >= total questions
        st.success("✔ All Interview Questions Completed Successfully.")
        avg_score = sum(st.session_state.scores) / len(st.session_state.scores)
        
        st.markdown("### Final Interview Report")
        col1, col2 = st.columns(2)
        col1.metric("Average Accuracy", f"{round(avg_score, 2)}/10")
        col2.metric("Completion Status", "100%")
        
        st.write(f"### Performance Summary")
        st.write(f"In your simulation for the **{job_role}** role at **{company}**, you demonstrated solid technical grounding. Your keyword alignment was **{round(avg_score * 10, 1)}%**.")
        
        # Reset button to go back to the setup screen
        if st.button("Start New Preparation"):
            st.session_state.interview_active = False
            st.rerun()
else:
    # Landing page state before "Start" is clicked
    st.write("Please configure your settings in the sidebar and click **Start New Interview**.")