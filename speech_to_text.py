import speech_recognition as sr
import streamlit as st

def capture_speech():
    """
    Records audio from the microphone and converts it into text using Google's API.
    """
    recognizer = sr.Recognizer()
    
    # Increase pause threshold to give the user time to think (2 seconds)
    recognizer.pause_threshold = 2.0 
    
    try:
        # Use the system microphone as the audio source
        with sr.Microphone() as source:
            st.toast("🎤 Listening... Speak your answer now.")
            # Reduce background noise interference
            recognizer.adjust_for_ambient_noise(source, duration=1)
            # Listen for a maximum of 30 seconds
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=30)
            
            # Convert the captured audio into text
            text = recognizer.recognize_google(audio)
            return text
    except Exception as e:
        # Handle cases where the microphone is blocked or silent
        st.error("Microphone error: Please check your browser permissions or use Keyboard mode.")
        return ""