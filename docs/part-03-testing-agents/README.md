---
title: 3. Testing Agents
description: Trajectory tests, LLM-as-a-Judge and an eval harness
logo: images/ibm-blue-background.png
notebook: notebooks/02_evaluation.ipynb
---

# Testing Agents

/// warning | Coming soon
This lab is still being written. The notebook exists as a placeholder and has no content yet.
///

Agents fail differently from ordinary software: an answer can be fluent, confident and wrong, and the same input can take a different path on a different day. This lab will cover:

1. Testing the **trajectory**, meaning the tools the agent called and in what order, as well as the final answer.
2. Scoring answers with **LLM-as-a-Judge**.
3. Multi-turn tests.
4. Putting these together into an **eval harness** you can run on every change.

Until the lab is ready, see [Testing agents](https://github.com/ibm-granite-community/granite-agent-cookbook/blob/main/testing_agents.md) in the Granite Agent Cookbook.
