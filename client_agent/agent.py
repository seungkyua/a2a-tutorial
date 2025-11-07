import os
from dotenv import load_dotenv
from google.adk.agents import LlmAgent
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent
from google.adk.models.lite_llm import LiteLlm

load_dotenv()
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

remote_country_agent = RemoteA2aAgent(
    name = "country_agent",
    description = "An agent that gives information about the country",
    agent_card = (
        f"http://localhost:3002" ## => AgentGateway URL for A2A server
    ),
)

travel_agent = LlmAgent(
    name = "travel_agent",
    model = LiteLlm(model="openai/gpt-5-nano"),
    description = (
        "A smart travel assistant that connects users with specialized sub-agents..."
    ),
    instruction = ("""
        You are a travel assistant. When a user’s request relates to flights, bookings, visas, or country-specific information, delegate the conversation to the appropriate sub-agent:
        ...
        country_agent for local information, culture, and travel tips
    """),
    sub_agents=[remote_country_agent],
)

root_agent = travel_agent