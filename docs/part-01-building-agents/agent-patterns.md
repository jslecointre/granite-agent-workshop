---
title: 02. Agent Patterns
description: Plan-and-Solve, Route-and-Solve, ToolRAG and ReAct
logo: images/ibm-blue-background.png
notebook: notebooks/02_agent_patterns.ipynb
---

# Agent Patterns

The [Function Calling Agent](function-calling.md) lab built a single agent that calls tools directly. Real systems often need more structure than that -- a visible plan, tools grouped by domain, a toolset too large to hand the model all at once, or a visible reasoning trace. This lab covers four patterns that address those needs, building incrementally on the model, tools and agent from [01. Function Calling](function-calling.md) rather than starting over each time.

## Which pattern for which problem?

| Pattern | Core idea | Good fit when |
| :--- | :--- | :--- |
| **Plan-and-Solve** | Plan all the steps up front, execute them, replan from what actually happened | The task is multi-step with real dependencies between steps, and you want the plan itself to be inspectable |
| **Route-and-Solve** | A router picks one specialized subagent (with its own, smaller toolset) per query | Your tools naturally group into domains and a single agent seeing all of them would be error-prone |
| **ToolRAG** | Semantically retrieve a small relevant subset of tools before binding them to the model | You have hundreds or thousands of tools -- too many to fit in the model's context at once |
| **ReAct** | Interleave visible reasoning ("Thought") with tool calls, in one loop | You want the model's reasoning trace to be inspectable step by step, not just its tool calls |

### Plan-and-Solve

Plan-and-Solve Agents consist of a planner node and a Function Calling (FC) node. The planner node considers the query, reasons about it, and generates a complete plan for execution, selecting the tools to use and their ordering. The output of the planner node is passed to the FC node, which loads up the tool calls, assisted by the LLM to set the tool call parameters. Once the FC node has executed the plan, the agent may or may not invoke the planner node again to determine if some additional steps are required based on the tool results.

**Pros:**

- Plan can be extracted and observed.
- Planning evokes thinking/reasoning behaviors, often leading to higher accuracy.
- The FC node does not have to do the complex task of decision-making, it only has to load up the prescribed tool-call objects.
- Supporting hints/examples of tools used for queries can aide in agent accuracy.

**Cons:**

- Additional model invocations required for planning.

**When to use:** this approach is useful when you have tools or an agent setup that requires custom reasoning instructions, such as hints, or when you want to define interdependencies between tools. It also suits use cases with longer reasoning traces or more steps than simpler agents need. In production settings, this approach can offer a simplified human-in-the-loop pattern by allowing the user to validate generated plans before execution.

### Route-and-Solve

Route-and-Solve Agents consist of a router and multiple function calling subagents. Each subagent has, in its toolkit, a subset of the complete list of tools -- a semantic grouping of tools into categories that the router selects from based on the end user query. This can be thought of as a router which routes to multiple function-calling subagents, each represented to the router as a callable tool.

**Pros:**

- Subagent architectures enable conceptual segmentation and reduce the likelihood of incorrect tool selection.
- Easily extendable in a modular way with new subagents as required -- add tools, wrap the subagent as one more tool, no graph changes needed.

**Cons:**

- Subagent routing and rerouting to a supervisor can impose complicated logic with unique edge cases.

**When to use:** this approach is effective when there is a natural clustering of tools which can be applied to the complete toolkit.

/// example
If your agent has tools that interact with the Internet, a Database and Email, you may define a sub-agent for each of these.
///

This approach also improves performance when there may be a large set of tools available: since each subagent only chooses from a subset of the tools, it is less likely to select an incorrect tool if the router has effectively done its job.

### ToolRAG

ToolRAG Agents operate by first doing retrieval-augmented generation (RAG) on the set of available tools based on the query, and only show a subset of the toolset to the model to select from for a given query. This pre-filtering approach reduces the likelihood of the model choosing the wrong tools, since it is already being shown a smaller set of relevant tools to pick from.

**Pros:**

- Reduced likelihood of wrong tool selection.
- Reduces the number of input tokens used for model invocation.
- Easy way to extend with new tools without incurring concerns of context windows or agent accuracy regression.

**Cons:**

- Tool pre-filtering may not surface the relevant tool for the model to select from.

**When to use:** this approach is effective when you have a large set of tools and not all are relevant for any single query. This dynamic filtering differs from Route-and-Solve's static grouping (defined by the agent developer at build time): ToolRAG instead dynamically filters at runtime based on the incoming query.

### ReAct

ReAct and Reasoning Agents are similar to function calling agents but with additional, *visible* reasoning: the model alternates between a "Thought" (what to do next) and an "Action" (a tool call), until it reaches a final answer. Each tool selection is followed by another iteration to see if the agent reasons to select another tool or is ready to answer.

**Pros:**

- Reasoning augmented tool calling can improve accuracy over non-reasoning approaches.
- Iterative tool loading can improve agent accuracy for longer trajectory-based problems.
- The visible reasoning trace makes it easier to debug *why* the agent did something, not just *what* it did.

**Cons:**

- Reasoning requires additional token output, which contributes to inference time and cost.
- ReAct and reasoning patterns may require custom response parsing, which can require model-specific code.

**When to use:** this approach extends the simple function-calling approach from [01. Function Calling](function-calling.md), and is suitable for scenarios with a small to medium list of tools where the use case is targeted to a domain. Accompanying this approach with ToolRAG can extend it to work with more tools and more generic queries.

## Prerequisites

This lab is a [Jupyter notebook](https://jupyter.org/). Please follow the instructions in [pre-work](../pre-work/README.md) to run the lab, and complete [01. Function Calling](function-calling.md) first -- this lab reuses its model and tools rather than redefining them.

/// note | Two sections need more setup
The Plan-and-Solve section uses the larger `granite4.2:8b` model, and ToolRAG needs an embedding model and a local vector store. Both are marked **⭐ Stretch** in the notebook -- Route-and-Solve and ReAct are the quicker sections to start with.
///

## Lab

[![Agent Patterns](https://badgen.net/badge/icon/github?icon=github&label=View%20on "View on GitHub")]({{ config.repo_url }}/blob/{{ git.commit }}/{{ notebook }}){:target="_blank"}
[![Agent Patterns](https://colab.research.google.com/assets/colab-badge.svg "Open In Colab")]({{ extra.colab_url }}/blob/{{ git.commit }}/{{ notebook }}){:target="_blank"}

To run the notebook from your command line in Jupyter using the active virtual environment from the [pre-work](../pre-work/README.md#install-jupyter), run:

```shell
jupyter notebook {{ notebook }}
```

The path of the notebook file above is relative to the `granite-agent-workshop` folder from the git clone in the [pre-work](../pre-work/README.md#clone-the-workshop-repository).