from agno.agent import Agent
# from agno.models.openai import OpenAIChat
from agno.models.groq import Groq
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile")
)
agent.print_response("Share a 2 sentence love story between dosa and samosa")




# agent = Agent(
#     model=OpenAIChat(id="gpt-4o"),
#     description="You are an enthusiastic news reporter with a flair for storytelling!",
#     markdown=True
# )
# agent.print_response("Tell me about a breaking news story from New York.", stream=True)