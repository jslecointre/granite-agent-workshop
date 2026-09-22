---
title: Building Efficient AI Agents with IBM Granite
description: Building Efficient AI Agents with IBM Granite 4.1 -- IBM TechXchange Lab 1538
logo: images/ibm-blue-background.png
---

## Introduction

IBM Granite 4.1 8B is a workhorse model for strong, cost-effective performance on enterprise workflows matching previous Granite 4.0 32B model, delivering frontier-level results at a fraction of the cost. In this session, you will work through recipes from the Granite Agent Cookbook on Google Colab. Using Granite 4.1, you will progress from a simple Function Calling agent through Plan-and-Solve, Route-and-Solve, ToolRAG, and ReAct. Each recipe builds on the last, teaching when to use each pattern, its latency and token cost, and context management best practices across Granite 4.1's 512K context window. You will write trajectory-based tests, evaluate with LLM-as-a-Judge, and instrument with LangFuse. Leave with the skills and recipes to build enterprise-ready agentic workflows.

New to Granite? See [About Granite](about-granite.md) for a primer on the model family and the Granite 4.2 models this workshop runs on.

By the end of this workshop, you will learn about:

### 01. Building Agents

Building from scratch to drop-in-and-run agent harnesses. You start by writing a function-calling loop by hand, so you can see exactly what the model returns and what your own code has to do with it. From there, the labs cover the patterns that matter in practice -- **Plan-and-Solve**, **Route-and-Solve**, **ToolRAG** and **ReAct** -- building on that same model, tools and agent rather than starting over each time.

### 02. Testing Agents

How to evaluate your agents, and how to build an effective eval harness. Agents fail differently from ordinary software: the output can be fluent, confident and wrong, and the same input can take a different path on a different day. This part covers testing the trajectory as well as the final answer, scoring answers with LLM-as-a-Judge, and assembling it all into a harness you can run on every change.

### 03. Productionizing Agents

How to observe, maintain and package your agents. Once an agent leaves your notebook, print statements stop being an option. This part covers instrumenting an agent so every model call and tool call is recorded as a trace you can search and cost, and packaging an agent so other applications can call it.

### 04. Advancing Agents

Context management, securing and sandboxing your agents. The difference between a demo and something you'd put in front of colleagues is mostly what happens to context over long runs, and what happens when someone is deliberately unhelpful. This part covers managing a large context window, the OWASP risks that change most when a model is given tools, and sandboxing what your agent is allowed to do.

## About this workshop

The introductory page of the workshop is broken down into the following sections:

* [Agenda](#agenda)
* [Technology Used](#technology-used)
* [Credits](#credits)

### Agenda

The workshop is organized into four parts, each covered by one or more Jupyter notebooks. Some labs are still being built -- those are marked below and are not yet linked from this site.

| Part | Lab | Description | Status |
| :--- | :--- | :--- | :--- |
| Pre-work | [Pre-work](pre-work/README.md) | Set up your environment | ✅ |
| Getting started | [00. Access the Model](part-00-getting-started/README.md) | Connect to Granite and run a first prompt | ✅ |
| 01. Building Agents | [01. Function Calling](part-01-building-agents/function-calling.md) | Write a tool-calling loop by hand, then with LangGraph and `create_agent` | ✅ |
| 01. Building Agents | [02. Agent Patterns](part-01-building-agents/agent-patterns.md) | Plan-and-Solve, Route-and-Solve, ToolRAG, ReAct | ✅ |
| 02. Testing Agents | 03. Evaluation | Trajectory tests, LLM-as-a-Judge, multi-turn tests, eval harness | 🚧 Coming soon |
| 03. Productionizing Agents | [04. Observability](part-03-productionizing-agents/observability.md) | Instrument an agent and read a trace with Langfuse | ✅ |
| 03. Productionizing Agents | 05. MCP Packaging | Package an agent as an MCP server | 🚧 Coming soon |
| 04. Advancing Agents | 06. Iterate | Context management, OWASP risks, sandboxing | 🚧 Coming soon |

### Technology Used

The following technology is used in the workshop:

* [Google Colab](https://colab.research.google.com)
* [IBM Granite AI foundation models](https://www.ibm.com/granite) -- see [About Granite](about-granite.md)
* [Jupyter notebooks](https://jupyter.org/)
* [LangGraph](https://www.langchain.com/langgraph)
* [Langfuse](https://langfuse.com)
* [Ollama](https://ollama.com)
* [Replicate](https://replicate.com/)

### Credits

* [BJ Hargrave](https://github.com/bjhargrave)
* [Prattyush Mangal](https://github.com/prattyushmangal)
* [Jacques-Sylvain Lecointre](https://github.com/jslecointre)
* [Aditya Gidh](https://github.com/adigidh)
* [Shonda Witherspoon](https://github.com/swith004)
