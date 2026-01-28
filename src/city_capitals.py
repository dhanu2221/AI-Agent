# ----- Agent -----for more structured response
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_anthropic import ChatAnthropic
from langchain_core.tools import tool
from langchain.agents import create_agent

load_dotenv()

class CityGuide(BaseModel):
    country: str
    capital: str
    summary: str              # 1–2 lines
    famous_places: list[str]  # 4–6
    things_to_do: list[str]   # 3–5

llm = ChatAnthropic(model="claude-sonnet-4-5-20250929", temperature=0)

@tool
def get_capital(country: str) -> str:
    """Return the capital of a country."""
    return {"France":"Paris","India":"New Delhi","USA":"Washington, D.C."}.get(country, "Unknown")

agent = create_agent(
    model=llm,
    tools=[get_capital],
    system_prompt=(
        "You are a concise city guide.\n"
        "Use tools to get the capital if needed.\n"
        "Return: 1–2 line summary + 4–6 famous places + 3–5 things to do."
    ),
    response_format=CityGuide,
    debug=False,
)

country = "UK"
state = agent.invoke({"messages": [("user", f"City guide for the capital of {country}.")]})
g: CityGuide = state["structured_response"]

print(f"{g.capital} ({g.country}) — {g.summary}")
print("Famous places:", "; ".join(g.famous_places))
print("Things to do:", "; ".join(g.things_to_do))