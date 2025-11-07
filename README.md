# a2a-tutorial
This source is a slightly modified version based on the one presented by "Mehmet Hilmi Emel" at OSSummitKorea 2025.

## Environment
```shell
# Create a virtual environment
$ python3 -m venv .venv

# Activate the environment
$ source .venv/bin/activate

# Install necessary libraries
$ pip install google-adk fastmcp "google-adk[a2a]" requests numpy pandas openmeteo-requests dotenv litellm
```

## Script
- I'm planning to go to South Korea. Could you first give me some information about the country? I have 1,000 dollars to spend there - how much would that be in Korean won?

## Running
```shell
# server agent
$ adk web

# mcpserver
$ python my_mcp_server.py

# agentgateway
$ agentgateway -f agent_gateway_config.yaml

# a2a server
$ uvicorn server_agent.agent:country_agent_server --host localhost --port 8002

# client agent
$ adk web
```

## References
- https://google.github.io/adk-docs/a2a/quickstart-exposing/
- https://github.com/google/adk-python/blob/main/contributing/samples/hello_world_litellm/agent.py