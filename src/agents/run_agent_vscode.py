import os
from typing import Optional
from azure.core.credentials import AccessToken
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.agents.models import ListSortOrder

from dotenv import load_dotenv
load_dotenv()

class VSCodeCredential(object):
    def get_token(
        self, *scopes: str, claims: Optional[str] = None, tenant_id: Optional[str] = None, **kwargs
    ) -> AccessToken:
        with open("/tmp/ai_token", "r") as file:
            token = file.read().strip()
            return AccessToken(token, expires_on=0)

project = AIProjectClient(
    credential=VSCodeCredential(),
    endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"])

agent = project.agents.get_agent("asst_l8fWFQJrIlOBRY9qRHtTYT09")

thread = project.agents.threads.get("thread_yr6pTi19CN9GaKE5BJv0Op1D")

message = project.agents.messages.create(
    thread_id=thread.id,
    role="user",
    content="Hello Agent"
)

run = project.agents.runs.create_and_process(
    thread_id=thread.id,
    agent_id=agent.id)

messages = project.agents.messages.list(thread_id=thread.id)


messages = project.agents.messages.list(thread_id=thread.id, order=ListSortOrder.ASCENDING)
for message in messages:
    if message.run_id == run.id and message.text_messages:
        print(f"{message.role}: {message.text_messages[-1].text.value}")

