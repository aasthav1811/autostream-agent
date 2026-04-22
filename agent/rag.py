import json

def load_knowledge():
    with open("data/knowledge.json", "r") as f:
        return json.load(f)

knowledge_base = load_knowledge()

def retrieve_answer(query: str):
    query = query.lower()

    if any(word in query for word in ["price", "pricing", "plan", "plans"]):
        return """
Basic Plan: $29/month, 10 videos/month, 720p
Pro Plan: $79/month, Unlimited videos, 4K, AI captions
"""
    
    elif "refund" in query:
        return "No refunds after 7 days"
    
    elif "support" in query:
        return "24/7 support available only on Pro plan"
    
    return "Can you clarify your question?"