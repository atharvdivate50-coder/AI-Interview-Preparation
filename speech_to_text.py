import speech_recognition as sr

def capture_speech():
    """
    Listens to the microphone and converts speech into text.
    Includes a longer pause threshold to prevent the mic from turning off early.
    """
    recognizer = sr.Recognizer()
    
    # --- CONFIGURATION TO PREVENT EARLY CUT-OFF ---
    # Increase the time the system waits after you stop talking (default is 0.8)
    recognizer.pause_threshold = 2.0 
    # The minimum seconds of speaking to count as a phrase
    recognizer.phrase_threshold = 0.3
    # -----------------------------------------------

    with sr.Microphone() as source:
        print("\n[Listening...] Speak your answer now. (Take your time)")
        # This helps the AI ignore background noise like a fan
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        try:
            # Added a timeout of 10 seconds to wait for you to start
            # Added a phrase_time_limit of 30 seconds for your full answer
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=30)
        except sr.WaitTimeoutError:
            print("[Error] No speech detected. Please try typing.")
            return input("Type your answer: ")

    try:
        print("[System] Converting speech to text...")
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("[Error] Could not understand audio. Please type your answer.")
        return input("Type your answer: ")
    except sr.RequestError:
        print("[Error] Speech service is unavailable. Please type your answer.")
        return input("Type your answer: ")