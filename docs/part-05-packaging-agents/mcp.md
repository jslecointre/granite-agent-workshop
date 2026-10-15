---
title: 5.1 Packaging Tools with MCP
description: Serve an agent's tools over the Model Context Protocol and use them from a Granite agent
logo: images/ibm-blue-background.png
notebook: notebooks/05_packaging_mcp.ipynb
---

# Packaging Tools with MCP

The tools in [Building Agents](../part-02-building-agents/README.md) are Python functions inside the agent's process: no other agent, framework or team can use them. The [Model Context Protocol (MCP)](https://modelcontextprotocol.io) moves tools into a separate server with a standard interface, so any MCP client can discover and call them.

In this lab you package three travel tools (`find_flight`, `book_hotel`, `get_forecast`) as an MCP server, test them by hand, then give them to a Granite agent that plans a trip to Atlanta.

## What you will learn

| Step | You do | Takeaway |
| :--- | :--- | :--- |
| 1 | Read how MCP works | A client and a server exchange JSON-RPC: `initialize` → `tools/list` → `tools/call`. When something breaks, find which of the three failed. |
| 2 | Build the server with [FastMCP](https://github.com/modelcontextprotocol/python-sdk) | One decorator turns a typed Python function into a tool. The docstring becomes the description the model reads, so write it for the model. |
| 2.1 | Call the tools in [MCP Inspector](https://github.com/modelcontextprotocol/inspector) | Test the server with no model involved. If a tool misbehaves here, the bug is in the server, not in the prompt. |
| 3 | Connect a LangGraph agent with [`langchain-mcp-adapters`](https://reference.langchain.com/python/langchain-mcp-adapters) | `MultiServerMCPClient` turns MCP tools into LangChain tools: the agent code contains no protocol code. |
| 4 | Decide when MCP is worth it | Use it when a tool is shared, owned by another team, or must run in another process. For one agent in one process, a plain tool is simpler. |

## Prerequisites

This lab is a [Jupyter notebook](https://jupyter.org/). At the workshop, your workstation is already set up: there is nothing to install. To run it on your own machine or in Colab, complete [Getting Started](../getting-started/README.md) first.

Step 2.1 also needs [Node](https://nodejs.org/) 22 or later, to run MCP Inspector with `npx`. It is optional: the rest of the notebook runs without it.

## Lab

[![Packaging Tools with MCP](https://badgen.net/badge/icon/github?icon=github&label=View%20on "View on GitHub")]({{ config.repo_url }}/blob/{{ extra.repo_branch }}/{{ notebook }}){:target="_blank"}
[![Packaging Tools with MCP](https://colab.research.google.com/assets/colab-badge.svg "Open In Colab")]({{ extra.colab_url }}/blob/{{ extra.repo_branch }}/{{ notebook }}){:target="_blank"}

Open the notebook in the way that matches where you are working:

/// tab | Lab workstation

In the JupyterLab file browser, open `granite-agent-workshop/{{ notebook }}`. If JupyterLab isn't running yet, see [Getting Started](../getting-started/README.md#open-jupyterlab).

///

/// tab | Colab

Click **Open in Colab** above. The first code cell installs everything the notebook needs. Colab needs a Replicate API token: see [Setting up Replicate](../part-01-access-the-model/README.md#setting-up-replicate).

MCP Inspector (step 2.1) needs a local browser and terminal, so skip it in Colab.

///

/// tab | Your own machine

From the `granite-agent-workshop` folder you cloned in [Getting Started](../getting-started/README.md), with its virtual environment active, run:

```shell
jupyter notebook {{ notebook }}
```

///

## MCP Inspector

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) is a browser MCP client: it calls your server's tools directly, with no model involved.

### Start the Inspector

1. Run the notebook up to step 2: it writes `notebooks/travel_mcp_server.py`.
1. Open [http://localhost:6274](http://localhost:6274){:target="_blank"}. If the Inspector loads, go to the next step.
1. Otherwise, from the `granite-agent-workshop` folder, run the command below and open the URL it prints. Keep the terminal open; `Ctrl+C` stops it.

    ```shell
    npx -y @modelcontextprotocol/inspector
    ```

### Configure the travel server

On **Servers**, select **Add Servers** and paste these values:

1. **Server ID**:

    ```text
    travel
    ```

1. **Transport**: `stdio (local process)`.

1. **Command** and **Arguments**:

    /// tab | Lab workstation

    **Command**:

    ```text
    /root/granite-agent-workshop-tx2026/.venv/bin/python
    ```

    **Arguments**:

    ```text
    /root/granite-agent-workshop-tx2026/granite-agent-workshop/notebooks/travel_mcp_server.py
    ```

    ///

    /// tab | Your own machine

    With the virtual environment active, print the two values (first line → **Command**, second → **Arguments**):

    ```shell
    python -c "import sys; print(sys.executable)"
    realpath notebooks/travel_mcp_server.py
    ```

    ///

1. **Environment**: leave empty.

![MCP Inspector server form configured for the travel server](../images/mcp_inspector_configure.png)

The Inspector starts the server itself over `stdio`: don't run `travel_mcp_server.py` separately.

### Connect

Save, then turn on the toggle on the `travel` card. It shows **Connected**, and the **Protocol** panel logs the `initialize` and `tools/list` messages. If it fails, check the **Console** tab.

![The travel server connected in MCP Inspector](../images/mcp_inspector_travel_connect.png)

### Call a tool

Open **Tools**, select `find_flight`, paste these values, then select **Execute Tool**:

1. **Destination**:

    ```text
    ATLANTA
    ```

1. **Date**:

    ```text
    2026-10-25
    ```

![Calling find_flight from MCP Inspector](../images/mcp_inspector_execute_tool.png)
