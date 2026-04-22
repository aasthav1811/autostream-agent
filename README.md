A) How to Run the Project Locally:

1. Clone the repository and navigate to the project folder:
git clone <your-repo-link>
cd autostream-agent

2. Install all required dependencies:
pip install -r requirements.txt

3. Run the application:
python main.py

Once the agent starts, test it with a sample flow:
“Hi” → Greeting
“What is your pricing?” → RAG-based response
“I want to try the Pro plan” → High-intent detection
Provide name, email, and platform → Lead capture triggered

Ensure you run commands from the root folder (autostream-agent) and that agent/__init__.py exists.

B) Architecture Explanation:
I chose LangGraph because it enables structured, stateful workflows rather than linear chains, which is essential for multi-turn conversational agents. The agent is modeled as a graph with nodes for intent detection and response generation, allowing clear separation of reasoning and action steps.

State is managed using a shared AgentState object that persists across conversation turns, enabling the agent to track user intent and progressively collect lead information (name, email, platform). This ensures that tool execution only occurs when all required fields are available.

The RAG pipeline is implemented using a local JSON knowledge base, ensuring deterministic and fast responses for pricing and policy queries without relying solely on the LLM.

C) Workflow
User → Intent Detection → RAG → High Intent → Lead Capture → Tool Execution

D) Tech Stack
- Python
- LangGraph
- LangChain
- JSON (Knowledge Base)

E) WhatsApp Integration:
To integrate with WhatsApp, I would use the WhatsApp Business API (via Meta or Twilio). Incoming messages would be received through a webhook endpoint (Flask/FastAPI). The webhook would pass the user message to the LangGraph agent, maintain session state using a database (Redis or PostgreSQL), and return the agent’s response back to WhatsApp via the API. This enables persistent conversations across multiple user sessions.

F) Future Scope
Future improvements include vector embeddings for semantic retrieval and LLM-based intent classification.
