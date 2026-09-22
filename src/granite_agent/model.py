from __future__ import annotations

import requests
from ibm_granite_community.notebook_utils import get_env_var


def ollama_has_model(host: str, model: str) -> bool:
    """True only if `host` answers AND `model` is already pulled there.

    Checking reachability alone is not enough: a running Ollama without the
    requested tag would otherwise trigger an on-demand pull, which needs
    network access we don't have on the day.
    """
    try:
        tags = requests.get(f"{host}/api/tags", timeout=2).json()
        return model in {m["name"] for m in tags.get("models", [])}
    except requests.RequestException:
        return False


def get_llm(model: str | None = None, *, backend: str | None = None, **kwargs):
    """Return a LangChain chat model for Granite.

    Args:
        model: Model tag/path to use. Defaults to the `GRANITE_MODEL` env
            var (or "granite4.2:3b") for Ollama, and to `REPLICATE_MODEL`
            (or "ibm-granite/granite-4.2-8b") for Replicate.
        backend: Force "ollama" or "replicate"; omit to auto-resolve
            (Ollama if the tag is pulled locally, Replicate otherwise).
        **kwargs: Extra keyword arguments passed through to the chat model.
    """
    host = get_env_var("OLLAMA_HOST", "http://127.0.0.1:11434")
    model = model or get_env_var("GRANITE_MODEL", "granite4.2:3b")

    if backend != "replicate" and (backend == "ollama" or ollama_has_model(host, model)):
        from langchain_ollama import ChatOllama

        return ChatOllama(
            model=model,
            base_url=host,
            num_predict=8192,  # Set the maximum number of tokens to generate as output.
            **kwargs,
        )

    from langchain_replicate import ChatReplicate

    return ChatReplicate(
        model=get_env_var("REPLICATE_MODEL", "ibm-granite/granite-4.2-8b"),
        replicate_api_token=get_env_var("REPLICATE_API_TOKEN"),
        model_kwargs={
            "max_completion_tokens": 8192,  # Set the maximum number of tokens to generate as output.
            "chat_template_kwargs": {"enable_thinking": False},
        },
        **kwargs,
    )
