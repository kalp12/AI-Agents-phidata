from agno.models.groq import Groq
from agno.agent import Agent
from agno.tools.yfinance import YFinanceTools
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv

load_dotenv()

web_agent = Agent(
    name="Web Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    # model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    instructions=[
        "Always include sources when using web search.",
        "Give concise summaries with bullet points."
        ],
    show_tool_calls=True,
    markdown=True
)
finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data for Indian companies",
    # role="Get financial data",
    model=Groq(id="llama-3.3-70b-versatile"),
    # model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
    instructions=[
        "Use the following tickers: 'LTIM.NS' for LTIMindtree, and 'TCS.NS' for TCS.",
        "If analyst recommendations are not available, still return price and company info.",
        "Display data using markdown tables."
    ],
    show_tool_calls=True,
    markdown=True,
)

agent_team = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    team=[web_agent, finance_agent],
    instructions=[
        "Use the following tickers: 'LTIM.NS' for LTIMindtree, and 'VEDL.NS' for Vedanta.",
        "If analyst recommendations are not available, still return price and company info.",
        "Display data using markdown tables."
    ],
    show_tool_calls=True,
    markdown=True,
)

agent_team.print_response(
    "Summarize and compare analyst recommendations and fundamentals for vedanta and ltimindtree. show in tables.What do this company do? and what is forecast for their stocks", stream=True
)

# agent_team.print_response("Get analyst recommendations for LTIMindtree", stream=True)


# agent_team.print_response("What do Vedanta and LTIMindtree do?")
# agent_team.print_response("Compare analyst recommendations and fundamentals for Vedanta and LTIMindtree in a table.")
# agent_team.print_response("What is the stock forecast for Vedanta and LTIMindtree?")
