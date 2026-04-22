from agent.graph import build_graph

graph = build_graph()

state = {
    "user_input": "",
    "intent": "",
    "response": "",
    "name": None,
    "email": None,
    "platform": None
}

print("AutoStream AI Agent 🎬 (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        break

    state["user_input"] = user_input

    if state["intent"] == "high_intent":
        if not state["name"]:
            state["name"] = user_input
        elif not state["email"]:
            state["email"] = user_input
        elif not state["platform"]:
            state["platform"] = user_input

    state = graph.invoke(state)

    print("Agent:", state["response"])