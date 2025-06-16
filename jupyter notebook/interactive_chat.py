from dotenv import load_dotenv
import os

from langchain_core.messages import HumanMessage


async def run_interactive_chat(compiled_graph, pretty_print_result):
    load_dotenv()

    print("=== 챗봇 테스트 (종료하려면 '종료' 또는 'exit' 입력) ===")
    while True:
        input_text = input("\n[USER] ")
        if input_text.strip().lower() in ["종료", "exit"]:
            print("대화를 종료합니다.")
            break

        result = await compiled_graph.ainvoke({"messages": HumanMessage(content=input_text)})
        pretty_print_result(result) 