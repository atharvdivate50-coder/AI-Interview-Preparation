import random
import time
import os
# Ensure your custom modules are imported correctly
from modules.question_engine import get_all_questions
from nlp_evaluator import analyze_answer_with_ai
from vision_analyzer import analyze_interview_presence
from speech_to_text import capture_speech

def clear_screen():
    """Clears the terminal for a cleaner user interface."""
    os.system('cls' if os.name == 'nt' else 'clear')

def run_interview():
    clear_screen()
    print("=================================================")
    print("   WELCOME TO AI-POWERED INTERVIEW PREP 2.0")
    print("=================================================")

    # Step 1: User Inputs
    # We use .strip() to handle accidental leading/trailing spaces
    job_role = input("Enter Target Job Role: ").strip()
    company = input("Enter Target Company: ").strip()
    
    try:
        num_questions = int(input("How many questions do you want to practice? : "))
    except ValueError:
        print("[Error] Please enter a valid number for questions.")
        return

    # Step 2: Fetch questions from the expanded database
    questions_list = get_all_questions(job_role, company)

    if not questions_list:
        print(f"\n[Error] No questions found for '{job_role}' at '{company}'.")
        print("Tip: Try roles like 'Software Engineer' or 'Data Scientist'.")
        return

    # Shuffle to ensure variety in every session
    random.shuffle(questions_list)
    
    # Step 3: Input Mode Selection
    print("\nHow would you like to answer?")
    print("1. Speak (Voice Recognition)")
    print("2. Type (Keyboard)")
    choice = input("Select 1 or 2: ").strip()

    total_ai_score = 0
    total_vision_score = 0
    actual_num_questions = min(num_questions, len(questions_list))

    # Step 4: Interview Loop
    for i in range(actual_num_questions):
        question, keywords = questions_list[i]
        
        print(f"\n-------------------------------------------------")
        print(f"QUESTION {i+1}: {question}")
        print("-------------------------------------------------")
        
        # Give the user a moment to prepare
        print("[System] Preparing camera and audio...")
        time.sleep(1)

        # Vision Analysis (runs once per question to check posture/presence)
        vision_score, vision_msg = analyze_interview_presence()
        
        # Capture Answer based on user choice
        if choice == "1":
            user_answer = capture_speech()
        else:
            user_answer = input("\n[System] Type your answer: ")
        
        # Fallback if speech recognition fails or returns empty
        if not user_answer or len(user_answer.strip()) < 2:
            print("[Warning] No answer detected. Moving to next question.")
            continue

        print("\n[System] AI is analyzing your response... please wait.")
        
        # Evaluation using the Keyword-Based NLP Module
        ai_score, ai_feedback = analyze_answer_with_ai(question, user_answer, keywords)
        
        # Results Display for this specific question
        print(f"\n>>> INTERVIEWER EVALUATION <<<")
        print(f"Confidence (Vision) Score: {vision_score}/10")
        print(f"Content (AI) Score: {ai_score}/10")
        print(f"Vision Feedback: {vision_msg}")
        print(f"AI Feedback: {ai_feedback}")
        
        total_ai_score += ai_score
        total_vision_score += vision_score

    # Final Summary Calculation
    if actual_num_questions > 0:
        avg_ai = round(total_ai_score / actual_num_questions, 2)
        avg_vision = round(total_vision_score / actual_num_questions, 2)
        final_avg = round((avg_ai + avg_vision) / 2, 2)
        
        print("\n=================================================")
        print(f"INTERVIEW COMPLETE!")
        print(f"Average AI Content Score: {avg_ai}/10")
        print(f"Average Vision Confidence Score: {avg_vision}/10")
        print(f"OVERALL PERFORMANCE SCORE: {final_avg}/10")
        
        # Performance-based encouragement
        if final_avg >= 8:
            print("Result: Outstanding! You are ready for the real interview. 🚀")
        elif final_avg >= 5:
            print("Result: Good effort. Keep refining your key concepts. 💡")
        else:
            print("Result: Needs more preparation. Focus on the basics. 💪")
        print("=================================================")
    else:
        print("\n[System] Session ended without answering any questions.")

if __name__ == "__main__":
    run_interview()