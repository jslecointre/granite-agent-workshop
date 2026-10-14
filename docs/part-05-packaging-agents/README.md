---
title: 5. Packaging Agents
description: Package an agent's tools and the agent itself so other applications can call them
logo: images/ibm-blue-background.png
---

# Packaging Agents

An agent that only runs inside a notebook is hard for anything else to use. This part packages the travel-planning agent behind two open protocols, one for each boundary it crosses:

| Lab | Protocol | What crosses the boundary | Use it when |
| :--- | :--- | :--- | :--- |
| [5.1](mcp.md) | **Model Context Protocol (MCP)** | Tools: the agent calls a server's functions | Several agents share a tool, or the tool is owned by another team |
| [5.2](a2a.md) | **Agent2Agent (A2A)** | Tasks: an agent delegates work to another agent | Agents are built, deployed or owned separately and must collaborate |

Both labs use the same scenario, a trip to Atlanta on 2026-10-25, so you can compare calling a tool with delegating to an agent.

For more background on deploying AI agents to production , see [CI/CD for agentic development](https://github.com/ibm-granite-community/granite-agent-cookbook/blob/main/cicd_agent-dev-blog.md) in the Granite Agent Cookbook.
