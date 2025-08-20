import os
from typing import List

import openai
from openai import completions
from openai import OpenAI

from openinference.instrumentation.openai import OpenAIInstrumentor

from tracing import tracer_provider
tracer = tracer_provider.get_tracer(__name__)

OpenAIInstrumentor().instrument(tracer_provider=tracer_provider)

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

class ChatGPTDeepResearchAgent:
    def __init__(self):
        pass

    @tracer.tool
    def _call_tool(self, command):
        print(f"sub-agent: {command}")

    @tracer.agent
    def run_agent(self, commands: List[str]):
        print(f"running commands... {commands}")
        self._call_tool(commands[0])

        response = client.responses.create(
            model="gpt-4.1-mini",  # You can change the model if needed
            input="Tell me a short fantasy story about a dragon and a young adventurer."
        )

        # Print the story
        print(response.output[0].content[0].text)
