import os
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.agents import AgentsClient

from dotenv import load_dotenv
load_dotenv()

endpoint = os.environ["AZURE_AI_PROJECT_ENDPOINT"]

project = AIProjectClient(
    endpoint=endpoint, 
    credential=DefaultAzureCredential(exclude_interactive_browser_credential=False))

agent = project.agents.create_agent(
    name="my-agent",
    model="gpt-4o",
    instructions="You are helpful agent")


print(f"Created agent, agent ID: {agent.id}")

project.agents.delete_agent(agent.id)
print("Deleted agent")