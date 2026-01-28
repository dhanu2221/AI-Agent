from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_anthropic import ChatAnthropic
from langchain_core.tools import tool
from langchain.agents import create_agent
# from langchain_core.messages import AIMessage

load_dotenv()

class ResearchResponse(BaseModel): 
    summary: str
    topic: str

llm = ChatAnthropic(model="claude-sonnet-4-5-20250929", temperature=0)

agent = create_agent(
    model=llm,
    tools=[],
    system_prompt="You are a research assistant.",
    response_format=ResearchResponse,
    debug=False,
)

state = agent.invoke({"messages": [("user", "what is java programming language?")]})

resp: ResearchResponse = state["structured_response"]
print(resp.summary)
