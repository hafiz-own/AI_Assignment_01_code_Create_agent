from dotenv import load_dotenv

load_dotenv()

from langchain.chat_models import init_chat_model

llm = init_chat_model("groq:openai/gpt-oss-20b", reasoning_effort="low")

llm = init_chat_model(
    model="auto",  # Or force a specific model like "groq/llama3-70b-8192"
    model_provider="openai",  # Tells LangChain to use the OpenAI API format
    base_url="http://localhost:20128/v1",  # Points the traffic to OmniRoute
    api_key="sk-dummy",  # LangChain requires a key to be set, but OmniRoute ignores it
    temperature=0.7,
)


# llm = init_chat_model("ollama:qwen3:8b", reasoning = False)
# llm = init_chat_model("ollama:qwen2.5:3b")
# llm = init_chat_model("openai:aion-labs/aion-3.5", base_url="https://api.aionlabs.ai/v1")
