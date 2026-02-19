def analyze_answer_with_ai(question, user_answer, reference_keywords):
    """
    Scans the user answer for key industry terms to provide a score.
    Uses 'Partial Matching' to allow for word variations (e.g., 'styling' for 'style').
    """
    # 1. Preparation: Lowercase everything for fair matching
    answer_lower = user_answer.lower()
    # Split the answer into individual words to check for partial matches
    user_words = answer_lower.split()
    
    matched_keywords = []

    # 2. Matching Logic: Check for keywords in the user's answer
    for word in reference_keywords:
        target = word.lower()
        
        # Check A: Does the exact keyword exist in the full text?
        if target in answer_lower:
            matched_keywords.append(word)
            continue
            
        # Check B: Partial match - Is the keyword contained within any word the user said?
        # This catches 'inheritance' if the user said 'inheriting' or 'inheritance'
        for u_word in user_words:
            if target in u_word or u_word in target:
                if len(u_word) > 3: # Ignore very short words like 'a', 'the', 'is'
                    matched_keywords.append(word)
                    break

    # 3. Score Calculation
    # Base score of 2.0 to reward effort/participation
    if len(reference_keywords) > 0:
        match_percentage = len(matched_keywords) / len(reference_keywords)
        # Scale the 8.0 remaining points based on accuracy
        score = 2.0 + (match_percentage * 8.0)
    else:
        score = 5.0 # Fallback for questions without keywords

    # Ensure score stays within 0-10 range and round to 1 decimal
    score = round(min(score, 10.0), 1)

    # 4. Feedback Generation
    if score >= 8:
        feedback = f"Excellent! You used critical terms: {', '.join(matched_keywords)}."
    elif score >= 5:
        feedback = f"Good answer. You mentioned {len(matched_keywords)} key terms. Try to be more technical."
    else:
        # Provide constructive advice by showing them what they missed
        missed = [w for w in reference_keywords if w not in matched_keywords]
        feedback = f"The answer is too brief. Try to include: {', '.join(missed[:3])}."

    return score, feedback