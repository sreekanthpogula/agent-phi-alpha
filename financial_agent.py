import os
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.model.ollama import Ollama
import openai
import os

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Web Search Agent
web_search_agent = Agent(
    # name="Web Search Agent",
    # description="An agent that can search the web for information.",
    # role="Search the web for information and answer questions.",
    model=Ollama(id="llama2"),
    # tools=[DuckDuckGo()],
    # instructions="Always provide a concise and accurate answer with the source included.",
    # show_tool_calls=True,
    markdown=True,
)

# web_search_agent.print_response("What is the latest news about Apple Inc.?", stream=True)

## Financial AI Agent
financial_agent = Agent(
    # name="Financial AI Agent",
    # description="An agent that can answer financial questions and provide stock information.",
    # role="Answer financial questions and provide stock information.",
    model=Ollama(id="llama2"),
    # tools=[YFinanceTools(stock_price=True, stock_fundamentals=True, company_news=True, analyst_recommendations=True)],
    # instructions="Use the table format for stock information and provide a summary of the stock's performance.",
    # show_tool_calls=True,
    markdown=True,
)

# financial_agent.print_response("What is the current stock price of Apple Inc. and its recent performance?", stream=True)

# multi_ai_agent = Agent(
#     team=[
#         web_search_agent,
#         financial_agent,
#     ],
#     # name="Multi AI Agent",
#     # description="An agent that can answer general and financial questions.",
#     # instructions=["Always include sources for web search results.", "Use the table format for stock information."],
#     # show_tool_calls=True,
#     model=Ollama(id="llama2"),
#     markdown=True,
# )

# Example usage
# multi_ai_agent.print_response("What is the current stock price of Apple Inc. and its recent performance? Also, search for the latest news about Apple Inc.", stream=True)

multi_agents = [web_search_agent, financial_agent]  # , multi_ai_agent]

# Example usage for multiple agents
for agent in multi_agents:
    print(f"Response from {agent}:")
    if agent == web_search_agent:
        agent.print_response("What is the latest news about Apple Inc.?", stream=True)
    elif agent == financial_agent:
        agent.print_response("What is the current stock price of Apple Inc. and its recent performance? Always include sources for web search results. Use the table format for stock information.", stream=True)
    print("\n" + "="*50 + "\n")