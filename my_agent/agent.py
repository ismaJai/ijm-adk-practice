# ./adk_agent_samples/mcp_agent/agent.py
import os
from google.adk.agents import LlmAgent
from google.adk.agents import Agent
from google.adk.tools.mcp_tool import MCPToolset
from google.adk.tools.mcp_tool import StdioConnectionParams
from google.adk.tools.mcp_tool import StreamableHTTPConnectionParams
from mcp import StdioServerParameters

MCP_URL = "http://localhost:3000/mcp"


root_agent = LlmAgent(
    model='gemini-2.0-flash',
    name='maps_assistant_agent',
    instruction='Help the user with Mongo DB MCP tools to get information about Mongo Databases',
    tools = [
        MCPToolset (
            connection_params = StreamableHTTPConnectionParams(
                url=MCP_URL)
        )
    ]
)
