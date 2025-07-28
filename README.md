# agent-phi-alpha
Phidata is a framework for building multi-modal agents and workflows.
Build agents with memory, knowledge, tools and reasoning.
Build teams of agents that can work together to solve problems.
Interact with your agents and workflows using a beautiful Agent UI.
​
## Key Features
  - Simple & Elegant
  - Powerful & Flexible
  - Multi-Modal by default
  - Multi-Agent orchestration
  - A beautiful Agent UI to chat with your agents
  - Agentic RAG built-in
  - Structured outputs
  - Reasoning built-in
  - Monitoring & Debugging built-in
​
## Installation
Phidata is available on PyPI. You can install it using pip:
```bash
pip install -U phidata
```
​
## Simple & Elegant
Phidata Agents are simple and elegant, resulting in minimal, beautiful code.
For example, you can create a web search agent in 10 lines of code.
web_search.py
```python
# web_search.py
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo

web_agent = Agent(
    name="Web Agent",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)
web_agent.print_response("Tell me about OpenAI Sora?", stream=True)
```

Setup
1. Setup your virtual environment
   Mac
   ```bash
   python3 -m venv ~/.venvs/aienv
   source ~/.venvs/aienv/bin/activate
   ```
   Windows
   ```bash
   python -m venv %USERPROFILE%\.venvs\aienv
   %USERPROFILE%\.venvs\aienv\Scripts\activate
   ```

```bash
# Install libraries
python3 -m venv ~/.venvs/aienv
source ~/.venvs/aienv/bin/activate

# Windows
python -m venv %USERPROFILE%\.venvs\aienv
%USERPROFILE%\.venvs\aienv\Scripts\activate
```
2. Install libraries in Mac
```bash
pip install -U phidata openai duckduckgo-search
```

In Windows
```bash
pip install -U phidata openai duckduckgo-search
```
3. Export your OpenAI key

Phidata works with most model providers but for these examples let’s use OpenAI.

Mac:

```bash
export OPENAI_API_KEY=sk-***
```
Windows

```bash
set OPENAI_API_KEY=sk-***
```
4. Create a file named `.env` in the root directory and add your OpenAI key
```bash
OPENAI_API_KEY=sk-***
```
Run the agent

```bash
python web_search.py
```
You should see the agent respond with information about OpenAI Sora, including sources from DuckDuckGo.

## Documentation
For more detailed documentation, including advanced features, multi-agent orchestration, and more examples, please visit the [Phidata Documentation](https://phidata.readthedocs.io/).
