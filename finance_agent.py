from agno.models.groq import Groq
from agno.agent import Agent
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

def get_company_symbol(company: str) -> str:
    """Use this function to get the symbol for a company.

    Args:
        company (str): The name of the company.

    Returns:
        str: The symbol for the company.
    """
    symbols = {
        "Phidata": "MSFT",
        "Infosys": "INFY",
        "Tesla": "TSLA",
        "Apple": "AAPL",
        "Microsoft": "MSFT",
        "Amazon": "AMZN",
        "Google": "GOOGL",
    }
    return symbols.get(company, "Unknown")


agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True,analyst_recommendations=True, stock_fundamentals=True),get_company_symbol],
    instructions= [
        "Use tables to display data."
        "Use bullet points to display lists.",],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True
)
agent.print_response(
    "Summarize and compare analyst recommendations and fundamentals for vedanta and ltimindtree. show in tables.What do this company do? and what is forecast for their stocks", stream=True
)
