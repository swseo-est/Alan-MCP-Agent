import sys
import asyncio
from contextlib import asynccontextmanager

from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent

from dotenv import load_dotenv


if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

load_dotenv()

async def make_graph():
    client = MultiServerMCPClient(
        {
            "playwright-mcp": {
                "command": "npx",
                "args": [
                    "-y",
                    "@smithery/cli@latest",
                    "run",
                    "@microsoft/playwright-mcp",
                    "--key",
                    "a457b5a4-cd03-4a13-b2ac-cf99c04f6fc4"
                ],
                "transport": "stdio",
            }
        }
    )

    tools = await client.get_tools()
    agent = create_react_agent("openai:gpt-4.1", tools)
    return agent

# print(f"Event loop policy: {asyncio.get_event_loop_policy()}")
#
# agent = asyncio.run(make_graph())
#
# msg = agent.ainvoke({"messages": "https://www.msit.go.kr/bbs/list.do?sCode=user&mId=311&mPid=121 페이지에서 스위스 박사 과정생 관련 사업을 찾아주고, 있다면 페이지를 열어서 내용을 확인해줘"})
# print(asyncio.run(msg))