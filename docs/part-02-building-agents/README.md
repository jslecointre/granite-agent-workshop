---
title: 2. Building Agents
description: Five agent architectures with Granite and LangGraph
logo: images/ibm-blue-background.png
---

# Building Agents

This part covers development. Each lab is a self-contained notebook that builds one agent architecture with IBM Granite and [LangGraph](https://www.langchain.com/langgraph). Start with the Function Calling Agent: every other pattern builds on it.

| Lab | Pattern | Core idea | Good fit when |
| :--- | :--- | :--- | :--- |
| [2.1](function-calling.md) | **Function Calling** | The model picks tools, your program runs them, loop until a final answer | Always start here: check whether the simplest agent already meets your use case |
| [2.2](plan-and-solve.md) | **Plan-and-Solve** | Plan all the steps up front, execute them, replan from what actually happened | The task has several dependent steps and you want to inspect the plan |
| [2.3](route-and-solve.md) | **Route-and-Solve** | A router sends each query to one specialized subagent with a smaller toolset | Your tools group naturally into domains |
| [2.4](toolrag.md) | **ToolRAG** | Retrieve a small relevant subset of tools before binding them to the model | You have too many tools to fit in the model's context at once |
| [2.5](react.md) | **ReAct** | Interleave visible reasoning ("Thought") with tool calls in one loop | You want to inspect the model's reasoning step by step |

Each notebook installs its own dependencies and defines its own `get_llm()` helper, so you can run the labs in any order.

/// tip | Short on time?
This part is planned for about 30 minutes, which isn't enough to finish all five labs. Do [2.1 Function Calling](function-calling.md) first, then pick the one or two patterns closest to your own use case. Every notebook stays published here, so you can finish the rest after the session.
///
