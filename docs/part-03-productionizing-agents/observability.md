---
title: 04. Observability
description: Instrument an agent and read a trace with Langfuse
logo: images/ibm-blue-background.png
notebook: notebooks/04_observability.ipynb
---

# Agent Observability with Langfuse

Once an agent leaves your notebook, print statements stop being an option. Unlike traditional deterministic software, agentic AI systems produce non-deterministic, multi-step behaviors that shift the operational question from "is it up?" to "is it right?" Observability -- capturing rich telemetry and traceability -- is what lets you answer that question in production.

This lab reuses the exact agent from [01. Function Calling](../part-01-building-agents/function-calling.md) (`get_llm()`, `get_stock_price`, `get_current_weather`, `build_agent()`) and instruments it with [Langfuse](https://langfuse.com) tracing. You will:

1. Instrument the agent with Langfuse's callback handler and capture a trace, with no code changes to the agent itself.
2. Review the trace in the Langfuse UI: LLM generations, tool calls, token counts, latency and cost.
3. Collect and read a trace as JSON, to understand its structure well enough to write your own analysis over it.
4. **⭐ Stretch:** run a Langfuse experiment to score agent output automatically, and see two ways to build a trace manually when automatic instrumentation isn't enough.

/// tip | Works even without Langfuse running yet
This lab ships with a real, pre-captured sample trace (`trace.json`) alongside the notebook. Step 3 (reading a trace as JSON) works from that sample even before you've set up Langfuse, or if a live extraction fails for any reason -- so you can explore the trace structure immediately and come back to live tracing once your Langfuse instance is ready.
///

## Setting up Langfuse

This lab uses a **self-hosted Langfuse at `http://localhost:3000`** during the live workshop (see the lab guide's familiarization walkthrough). If you're working through this on your own machine, or in Colab where nothing runs on `localhost`, use [Langfuse Cloud](https://us.cloud.langfuse.com/) instead -- the notebook works the same way either way, only `LANGFUSE_HOST` changes.

Once you have access to a Langfuse project:

1. Go to **Settings → API Keys** and generate a new key pair.
2. Copy your **Public Key**, **Secret Key**, and **Host URL** into your `.env` file:

    ```dotenv
    LANGFUSE_SECRET_KEY=sk-lf-xxxxx
    LANGFUSE_PUBLIC_KEY=pk-lf-xxxxx
    LANGFUSE_HOST=http://localhost:3000
    ```

## Prerequisites

This lab is a [Jupyter notebook](https://jupyter.org/). Please follow the instructions in [pre-work](../pre-work/README.md) to run the lab, and complete [01. Function Calling](../part-01-building-agents/function-calling.md) first -- this lab reuses its model, tools and agent rather than redefining them.

## Lab

[![Agent Observability](https://badgen.net/badge/icon/github?icon=github&label=View%20on "View on GitHub")]({{ config.repo_url }}/blob/{{ git.commit }}/{{ notebook }}){:target="_blank"}
[![Agent Observability](https://colab.research.google.com/assets/colab-badge.svg "Open In Colab")]({{ extra.colab_url }}/blob/{{ git.commit }}/{{ notebook }}){:target="_blank"}

To run the notebook from your command line in Jupyter using the active virtual environment from the [pre-work](../pre-work/README.md#install-jupyter), run:

```shell
jupyter notebook {{ notebook }}
```

The path of the notebook file above is relative to the `granite-agent-workshop` folder from the git clone in the [pre-work](../pre-work/README.md#clone-the-workshop-repository).