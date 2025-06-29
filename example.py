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
@tool
def get_weather(city_name: str) -> str:
    """
    This function takes a city name as input and returns a string describing the weather in that city.
    """
    weather_data = {
        "London": "Sunny, 20°C",
        "Paris": "Cloudy, 18°C",
        "Tokyo": "Rainy, 15°C",
    }
    if city_name in weather_data:
        return weather_data[city_name]
    else:
        return "ไม่พบข้อมูลสภาพอากาศสำหรับเมืองนี้"

def add_numbers(a: float, b: float) -> float:
    """
    This function takes two numbers as input and returns their sum.
    """
    return a + b

def parsing_add_numbers(input_str: str) -> float:
    """
    This function parses a string input to extract two numbers and returns their sum.
    """
    try:
        # Split the input string by spaces and convert to float
        numbers = list(map(float, input_str.split(",")))
        if len(numbers) != 2:
            raise ValueError("Input must contain exactly two numbers.")
        return add_numbers(float(numbers[0]), float(numbers[1]))
    except ValueError as e:
        return f"Error parsing input: {e}"


def subtract_numbers(a: float, b: float) -> float:
    """
    This function takes two numbers as input and returns their difference.
    """
    return a - b

# 2. Wrap Function as a LangChain Tool:
tools = [
    get_weather,
    Tool(
        name="add_numbers",
        func=parsing_add_numbers,
        description="useful for when you need to add two numbers together. The input to this tool should be a comma separated list of numbers of length two.",
    ),
    StructuredTool(
        name="subtract_numbers",
        func=subtract_numbers,
        description="useful for when you need to subtract two numbers.",
        args_schema={
            "type": "object",
            "properties": {
                "a": {
                    "type": "float",
                    "description": "The first number to subtract from.",
                },
                "b": {
                    "type": "float",
                    "description": "The second number to subtract.",
                },
            },
            "required": ["a", "b"],
        },
    ),
]

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
prompt1 = "What is the weather in London?"
response1 = agent.run(prompt1)
print(f"Prompt: {prompt1}\nResponse: {response1}\n")

prompt2 = "What is the sum of 5 and 3?"
response2 = agent.run(prompt2)
print(f"Prompt: {prompt2}\nResponse: {response2}")

prompt3 = "What is the difference between 10 and 4?"
response3 = agent.run(prompt3)
print(f"Prompt: {prompt3}\nResponse: {response3}")