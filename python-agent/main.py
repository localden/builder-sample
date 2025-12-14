import asyncio
import os
from agent_framework import ChatAgent
from agent_framework.azure import AzureOpenAIChatClient
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

# Get configuration for agent
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4.1-mini")

if not endpoint:
    raise ValueError("AZURE_OPENAI_ENDPOINT is not set. Please set this environment variable.")

instructions = """
    1. A robot may not injure a human being...
    2. A robot must obey orders given it by human beings...
    3. A robot must protect its own existence...
    
    Objective: Give me the TLDR in exactly 5 words.
    """

# Get Azure token for authentication
# DefaultAzureCredential will check: Environment Vars -> Azure CLI -> Managed Identity
credential = DefaultAzureCredential()
token_provider = get_bearer_token_provider(
    credential, 
    "https://cognitiveservices.azure.com/.default"
)

# Create Azure OpenAI client
chat_client = AzureOpenAIChatClient(
    endpoint=endpoint,
    deployment_name=deployment_name,
    api_version="2024-08-01-preview",
    ad_token_provider=token_provider
)

# Create the agent
agent = ChatAgent(
    chat_client=chat_client,
    instructions=instructions
)

# Optional: Add MCP tool from remote URL
# agent.add_mcp_server("https://example.com/mcp-server")

# Optional: Add MCP tool with authentication
# import httpx
# headers = {"Authorization": "Bearer YOUR_TOKEN_HERE"}
# agent.add_mcp_server("https://example.com/mcp-server", headers=headers)

# Stay in a loop for continuous conversation
async def main():
    """Run interactive conversation loop with the agent."""
    while True:
        user_message = input("Enter your message: ")
        
        # Check for exit commands
        if not user_message or user_message.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        
        try:
            # Invoke the agent and output the text result
            result = await agent.run(user_message)
            print(f"\n{result.text}\n")
        except Exception as ex:
            print(f"Error: {ex}\n")

if __name__ == "__main__":
    asyncio.run(main())