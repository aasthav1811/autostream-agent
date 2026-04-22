from agent.intent_classifier import classify_intent
from agent.rag import retrieve_answer
from agent.tools import mock_lead_capture

def intent_node(state):
    state["intent"] = classify_intent(state["user_input"])
    return state

def response_node(state):
    intent = state["intent"]

    if state.get("stage"):
        if state["stage"] == "ask_name":
            state["name"] = state["user_input"]
            state["stage"] = "ask_email"
            state["response"] = "Great! What's your email?"
            return state

        elif state["stage"] == "ask_email":
            state["email"] = state["user_input"]
            state["stage"] = "ask_platform"
            state["response"] = "Which platform do you create content on?"
            return state

        elif state["stage"] == "ask_platform":
            state["platform"] = state["user_input"]

            from agent.tools import mock_lead_capture
            mock_lead_capture(state["name"], state["email"], state["platform"])

            state["stage"] = None
            state["response"] = "🎉 You're all set! Our team will reach out shortly."
            return state
  
    if intent == "high_intent":
        state["stage"] = "ask_name"
        state["response"] = "Awesome! Let's get you started. What's your name?"
        return state

    if intent == "greeting":
        state["response"] = "Hey there! 👋 How can I help you with AutoStream today?"

    elif intent == "inquiry":
        from agent.rag import retrieve_answer
        state["response"] = retrieve_answer(state["user_input"])

    else:
        state["response"] = "Can you clarify your question?"

    return state