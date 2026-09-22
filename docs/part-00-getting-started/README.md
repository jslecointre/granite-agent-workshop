---
title: 00. Access the Model
description: Warm-up notebook -- connect to Granite and run a first prompt
logo: images/ibm-blue-background.png
notebook: notebooks/00_access_the_model.ipynb
---

# Access the Model

This is the warm-up notebook for the workshop. It doesn't build an agent -- it confirms your environment can reach a Granite model, and shows the exact model-connection code every other notebook in this workshop reuses.

The model-selection logic (local Ollama first, [Replicate](https://replicate.com) as the hosted fallback) is defined once, as `get_llm()` in `src/granite_agent/model.py`. Starting with the [Function Calling](../part-01-building-agents/function-calling.md) lab, every notebook in this workshop imports this exact function instead of redefining it -- so if a model connection ever misbehaves, this is the one place to look.

By the end of this notebook, you will have:

1. Confirmed which backend you're using (a local Ollama server, or Replicate).
2. Sent a single prompt to Granite and read back a response, with nothing else in the way -- no tools, no agent loop.

## Prerequisites

This lab is a [Jupyter notebook](https://jupyter.org/). Please follow the instructions in [pre-work](../pre-work/README.md) to run the lab.

## Lab

[![Access the Model](https://badgen.net/badge/icon/github?icon=github&label=View%20on "View on GitHub")]({{ config.repo_url }}/blob/{{ git.commit }}/{{ notebook }}){:target="_blank"}
[![Access the Model](https://colab.research.google.com/assets/colab-badge.svg "Open In Colab")]({{ extra.colab_url }}/blob/{{ git.commit }}/{{ notebook }}){:target="_blank"}

To run the notebook from your command line in Jupyter using the active virtual environment from the [pre-work](../pre-work/README.md#install-jupyter), run:

```shell
jupyter notebook {{ notebook }}
```

The path of the notebook file above is relative to the `granite-agent-workshop` folder from the git clone in the [pre-work](../pre-work/README.md#clone-the-workshop-repository).