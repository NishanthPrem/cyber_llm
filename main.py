import logfire
import os
import openai
from pydantic_ai import Agent
from dotenv import load_dotenv


load_dotenv()

logfire.configure()
logfire.instrument_openai()

openai.api_key = os.getenv("OPENAI_API_KEY")

agent = Agent('openai:gpt-4o')

result = agent.run_sync(
    'How does pyodide let you run Python in the browser? (short answer please)'
)

print(f'Output: {result.data}')