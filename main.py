from chatgptdeepresearchagent import ChatGPTDeepResearchAgent
from tracing import tracer_provider

#  mkvirtualenv arize_test
#  pip install arize-phoenix-otel
#  pip install openinference-instrumentation-openai
#  pip install openai
tracer = tracer_provider.get_tracer(__name__)


@tracer.chain
def my_func(input: str) -> str:
    return "output"

if __name__ == '__main__':
    print("running...")
    f = ChatGPTDeepResearchAgent()
    f.run_agent(["hi", "yo", "bye felicia"])