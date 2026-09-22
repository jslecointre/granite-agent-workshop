from __future__ import annotations

from typing import Annotated, TypedDict

from langchain.agents import create_agent
from langchain_core.messages import AIMessage, AnyMessage, HumanMessage
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.graph.state import CompiledStateGraph
from langgraph.prebuilt import ToolNode

from granite_agent.model import get_llm
from granite_agent.tools import get_current_weather, get_stock_price

DEFAULT_TOOLS = [get_stock_price, get_current_weather]


class State(TypedDict, total=False):
    # Messages have the type "list". The `add_messages` function
    # in the annotation defines how this state key should be updated
    # (in this case, it appends messages to the list, rather than overwriting them)
    messages: Annotated[list[AnyMessage], add_messages]


def route_tools(state: State) -> str:
    """
    This is conditional_edge function to route to the ToolNode if the last message
    in the state has tool calls. Otherwise, route to the END node to complete the
    workflow.
    """
    messages = state.get("messages")
    if not messages:
        raise ValueError(f"No messages found in input state to tool_edge: {state}")

    last_message = messages[-1]
    # If the last message is from the model and it contains a tool call request
    if isinstance(last_message, AIMessage) and len(last_message.tool_calls) > 0:
        return "tools"
    return END


def build_graph(llm=None, tools=None) -> CompiledStateGraph[State]:
    """Build the from-scratch LangGraph function-calling agent from 01_function_calling."""
    llm = llm or get_llm()
    tools = tools or DEFAULT_TOOLS
    llm_with_tools = llm.bind_tools(tools)

    def llm_node(state: State) -> State:
        messages = state.get("messages", [])
        response_message = llm_with_tools.invoke(messages)
        state_update = State(messages=[response_message])
        return state_update

    graph_builder = StateGraph(State)
    graph_builder.add_node("llm", llm_node)
    graph_builder.add_node("tools", ToolNode(tools=tools))
    graph_builder.add_edge(START, "llm")
    graph_builder.add_conditional_edges(
        "llm",
        route_tools,
        {
            "tools": "tools",
            END: END,
        },
    )
    graph_builder.add_edge("tools", "llm")
    return graph_builder.compile()


def run_agent(graph, user_input: str) -> None:
    """Stream a single-turn request through a graph or create_agent-built agent,
    printing each step so the tool-call/response flow is visible."""
    user_message = HumanMessage(user_input)
    print(user_message.pretty_repr())
    input = State(messages=[user_message])
    for event in graph.stream(input):
        for value in event.values():
            print(value["messages"][-1].pretty_repr())


def build_agent(llm=None, tools=None):
    """The same agent as `build_graph()`, built with LangChain's `create_agent`.

    Not specifying the `prompt` argument means the agent behaves like the
    from-scratch graph above. For Granite, providing a system prompt would
    replace the model's default tool-calling system prompt, which can break
    tool calling -- so `prompt` is intentionally left unset here.
    """
    return create_agent(model=llm or get_llm(), tools=tools or DEFAULT_TOOLS)
