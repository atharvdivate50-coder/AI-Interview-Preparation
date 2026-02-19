def analyze_answer_with_ai(question, user_answer, reference_keywords):
    """
    Scans the user answer for industry keywords and calculates a 0-10 score.
    """
    # 1. Preparation: Normalize text to lowercase for fair matching
    answer_lower = user_answer.lower()
    user_words = answer_lower.split()
    matched_keywords = []

    # 2. Matching Logic: Identify keywords present in the user's answer
    for word in reference_keywords:
        target = word.lower()
        
        # Exact matching check
        if target in answer_lower:
            matched_keywords.append(word)
            continue
            
        # Partial matching check (e.g., 'styling' matches 'style')
        for u_word in user_words:
            if target in u_word or u_word in target:
                # Ignore very short words to prevent false matches
                if len(u_word) > 3: 
                    matched_keywords.append(word)
                    break

    # 3. Score Calculation
    # We provide a base score of 2.0 to reward effort
    if len(reference_keywords) > 0:
        match_percentage = len(matched_keywords) / len(reference_keywords)
        # Final score scales from 2.0 to 10.0
        score = 2.0 + (match_percentage * 8.0)
    else:
        # Fallback score if a question has no keywords defined
        score = 5.0 

    score = round(min(score, 10.0), 1)

    # 4. Feedback Generation based on the calculated score
    if score >= 8:
        feedback = f"Excellent! You used critical terms: {', '.join(matched_keywords)}."
    elif score >= 5:
        feedback = f"Good answer. You mentioned {len(matched_keywords)} key terms. Try to be more technical."
    else:
        # Identify and suggest missing keywords for improvement
        missed = [w for w in reference_keywords if w not in matched_keywords]
        feedback = f"The answer is too brief. Try to include: {', '.join(missed[:3])}."

    return score, feedback