"""
Unified LLM client factory supporting Groq and OpenAI providers.
Automatically detects GROQ_API_KEY or OPENAI_API_KEY from environment.
"""

import os
from typing import Optional, Any
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

GROQ_BASE_URL = os.getenv("GROQ_BASE_URL", "https://api.groq.com/openai/v1")


def get_default_model() -> str:
    if os.getenv("DEFAULT_MODEL"):
        return os.getenv("DEFAULT_MODEL")
    if os.getenv("GROQ_API_KEY"):
        return "openai/gpt-oss-20b"
    return "gpt-4o-mini"


def get_llm(
    model: Optional[str] = None,
    temperature: float = 0.0,
    seed: Optional[int] = 42,
    model_kwargs: Optional[dict[str, Any]] = None,
    **kwargs,
) -> ChatOpenAI:
    """
    Build a ChatOpenAI instance configured for Groq or OpenAI.
    Prioritizes GROQ_API_KEY if present, otherwise falls back to OPENAI_API_KEY.
    """
    chosen_model = model or get_default_model()
    groq_api_key = os.getenv("GROQ_API_KEY")
    openai_api_key = os.getenv("OPENAI_API_KEY")

    params: dict[str, Any] = {
        "model": chosen_model,
        "temperature": temperature,
        **kwargs,
    }

    if seed is not None:
        params["seed"] = seed

    if model_kwargs:
        params["model_kwargs"] = model_kwargs

    if groq_api_key:
        params["api_key"] = groq_api_key
        params["base_url"] = GROQ_BASE_URL
    elif openai_api_key:
        params["api_key"] = openai_api_key

    return ChatOpenAI(**params)
