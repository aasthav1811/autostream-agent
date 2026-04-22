def classify_intent(user_input: str):
    text = user_input.lower()

    # HIGH INTENT 
    if any(phrase in text for phrase in [
        "i want", "i would like", "sign up", "subscribe",
        "buy", "start", "try", "get started"
    ]):
        return "high_intent"
    
    # Inquiry
    if any(word in text for word in [
        "price", "pricing", "plan", "cost", "features"
    ]):
        return "inquiry"
    
    # Greeting
    if any(word in text.split() for word in [
        "hi", "hello", "hey"
    ]):
        return "greeting"
    
    return "unknown"