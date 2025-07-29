import os
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.model.ollama import Ollama
import openai
import os
import phi
from phi.playground import Playground

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

phi.api_key = os.getenv("PHIDATA_API_KEY")
phi.groq_api_key = os.getenv("GROQ_API_KEY")


from phi.playground import serve_playground_app, playground


## Financial AI Agent
financial_agent = Agent(
    name="Financial AI Agent",
    description="An agent that can answer financial questions and provide stock information.",
    # role="Answer financial questions and provide stock information.",
    model=Groq(id="gemma2-9b-it"),
    # tools=[YFinanceTools(stock_price=True, stock_fundamentals=True, company_news=True, analyst_recommendations=True)],
    # instructions="Use the table format for stock information and provide a summary of the stock's performance.",
    show_tool_calls=True,
    markdown=True,
)

financial_agent.print_response("What is the current stock price of Apple Inc. and its recent performance?", stream=True)


# Initialize the Playground with the financial agent
app=Playground(
    agents=[
        financial_agent,
    ]).get_app()


if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)