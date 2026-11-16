from google.adk.agents import LlmAgent

root_agent = LlmAgent(
    name="root_agent",
    model="gemini-3.5-flash",
    description="My first AI assistant.",
    instruction="You are a helpful assistant that can answer questions and assist with tasks.",
)
