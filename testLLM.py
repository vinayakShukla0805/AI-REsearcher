from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

load_dotenv()

llm = ChatMistralAI(
    model="codestral-2508",
    temperature=0
)

response = llm.invoke("Explain AI agents in two sentences.")
print(response.content)