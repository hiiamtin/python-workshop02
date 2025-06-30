import os
from langchain.agents import AgentType, initialize_agent
from langchain.tools import Tool,tool,StructuredTool


import getpass
import os

from langchain.agents import AgentType, initialize_agent
from langchain.tools import Tool

# Import LLM wrappers
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_anthropic import ChatAnthropic	

# PROVIDER = "openai"  # เปลี่ยนเป็น "google" หรือ "anthropic" ตามที่คุณต้องการ
PROVIDER = "google"
if PROVIDER == "openai":
    API_KEY_NAME = "OPENAI_API_KEY"
elif PROVIDER == "codesmart":
    API_KEY_NAME = "OPENAI_API_KEY"
elif PROVIDER == "google":
    API_KEY_NAME = "GOOGLE_API_KEY"
elif PROVIDER == "anthropic":
    API_KEY_NAME = "ANTHROPIC_API_KEY"
else:
    raise ValueError(f"Unknown provider: {PROVIDER}")


# กำหนด API Key แบบ manual (ใส่ API key ของคุณที่นี่)
# os.environ['OPENAI_API_KEY'] = "xxxx"
# os.environ['GOOGLE_API_KEY'] = "xxxxx"
# os.environ['ANTHROPIC_API_KEY'] = "xxxxx"


if not os.environ.get(API_KEY_NAME):
    os.environ[API_KEY_NAME] = getpass.getpass("Enter your API key: ")

################################################################ WORKSHOP CREATE TOOLS ################################################################

# 1. Define a Simple Python Function:

# 2. Wrap Function as a LangChain Tool:
tools = []

################################################################## END WORKSHOP CREATE TOOLS ################################################################



# 3. Create a Simple Agent:
if PROVIDER == "openai": # สำหรับ OpenAI
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0) 
elif PROVIDER == "codesmart": # สำหรับ CodeSmart
    llm = ChatOpenAI(
        model="codesmart",
        base_url='https://api.codesmart.app/v1',
        api_key=os.environ[API_KEY_NAME]) 
elif PROVIDER == "google": # สำหรับ Google Gemini
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash") 
elif PROVIDER == "anthropic": # สำหรับ Anthropic Claude
    llm = ChatAnthropic(model="claude-2", temperature=0) 
else:
    raise ValueError(f"Unknown provider: {PROVIDER}")

agent = initialize_agent(
    tools,
    llm,
    # agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, # not support multiple inputs tool
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION, 
    verbose=False,  # Set to True if you want to see the agent's reasoning steps
)

# 4. Run the Agent and Observe:
prompt1 = "promt1"
response1 = agent.run(prompt1)
print(f"Prompt: {prompt1}\nResponse: {response1}\n")

prompt2 = "promt3"
response2 = agent.run(prompt2)
print(f"Prompt: {prompt2}\nResponse: {response2}")

prompt3 = "promt3"
response3 = agent.run(prompt3)
print(f"Prompt: {prompt3}\nResponse: {response3}")

# or you can use the agent with a loop to continuously get user input
# while True:
#     user_input = input("You: ")
#     if user_input.lower() in ["exit", "quit"]:
#         break
#     response = agent.run(user_input)