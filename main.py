from strands import Agent
from strands.models import BedrockModel

model = BedrockModel(
    model_id="us.anthropic.claude-sonnet-4-5-20250929-v1:0",
    region_name="us-east-1",
)

agent = Agent(model=model)
response = agent("What is 12 * 7?")
print(response)