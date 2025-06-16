"""MCP client."""

import asyncio

from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()


SERVER_CONFIGS = {
    "playwright": {
        "url": "http://localhost:8931/mcp",
        "transport": "streamable_http",
    },
}

client = MultiServerMCPClient(SERVER_CONFIGS)

async def make_graph():
    """make_graph."""
    async with client.session("playwright") as session:
        tools = await load_mcp_tools(session)
        agent = create_react_agent(
            "openai:gpt-4.1",
            tools,
        )
        print(await agent.ainvoke({"messages": "naver에 접속해줘"}))
        print(await agent.ainvoke({"messages": "검색창에 가나다 라고 입력해줘"}))


if __name__ == '__main__':
    asyncio.run(make_graph())
