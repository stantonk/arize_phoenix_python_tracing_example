import os
from phoenix.otel import register

PROJECT = "my-llm-app"

# # You can either use OTEL GRPC
# os.environ["PHOENIX_COLLECTOR_ENDPOINT"] = "http://localhost:4317"
#
# tracer_provider = register(
#     project_name=PROJECT,
#     auto_instrument=True,
#     protocol="grpc",
# )

# OR, use http/protobuf
os.environ["PHOENIX_COLLECTOR_ENDPOINT"] = "http://localhost:6006/v1/traces"

tracer_provider = register(
    project_name=PROJECT,
    auto_instrument=True,
    protocol="http/protobuf",
)
tracer = tracer_provider.get_tracer(__name__)
