import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))
    
import nest_asyncio

nest_asyncio.apply()

from pydantic_ai import Agent

from app.config import settings

agent = Agent(
    model=settings.classifier_model,
    instructions="You are my friend",
)

response = agent.run_sync("How are you ?")
