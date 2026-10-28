# AI-Powered Support Ticket Classifier

An end-to-end, production-grade customer support ticket classification pipeline built with **LangGraph**, **LangChain**, **Groq** (with OpenAI fallback), and **FastAPI**.

---

## Features

- **Multi-Step LangGraph Orchestration**: Pipeline routing: `PII Redaction` → `Prompt Injection Guard` → `Classification` → `Validation` → `Fallback Retry` → `Cost Tracking`.
- **High-Speed Inference via Groq**: Fast structured output using `openai/gpt-oss-20b` (or `llama-3.3-70b-versatile`) with seamless fallback to OpenAI (`gpt-4o-mini`).
- **PII Redaction**: Regex-based masking for emails, phone numbers, and credit cards before text reaches the LLM.
- **Prompt Injection Defense**: LLM-as-a-judge security guard that intercepts prompt injection and jailbreak attempts.
- **Strict Output Validation**: Pydantic schema enforcement with automated business-rule checks.
- **Retry & Graceful Degradation**: Exponential backoff with tenacity and safe fallback if API limits or errors occur.
- **Token & Cost Calculation**: Accurate token accounting supporting `o200k_base` / `cl100k_base` with Groq pricing models.
- **Interactive Web Dashboard**: Built-in browser UI served directly at `http://localhost:8000/`.

---

## Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/somasriman07/support-ticket-classifier.git
cd support-ticket-classifier
```

### 2. Set up virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configure environment variables
Copy the template and add your API key:
```bash
cp .env.example .env
```
Edit `.env`:
```env
GROQ_API_KEY=gsk_...your_groq_api_key...
DEFAULT_MODEL=openai/gpt-oss-20b
PROMPT_VERSION=v2
LOG_COSTS=true
```

### 4. Run the Application
```bash
python main.py
```
- Web UI: [http://localhost:8000](http://localhost:8000)
- Swagger Docs: [http://localhost:8000/docs](http://localhost:8000/docs)
- Health check: [http://localhost:8000/health](http://localhost:8000/health)

---

## Running Tests

```bash
pytest tests/test_classifier.py -v
```

---

## Full Documentation

For detailed architecture diagrams, module breakdown, prompt versioning specs, and schema details, see [documentation.md](documentation.md).
