# GitHub README Generator Agent

A Python‑based agent that automatically generates a comprehensive `README.md` for a public GitHub repository.  
It pulls repository metadata and a curated set of source files, feeds them to a Groq‑powered LLM via LangChain, and produces a README, insights, and analysis.

---

## Features

- **URL Parsing** – Extracts owner and repository name from any GitHub URL.
- **Repository Metadata Retrieval** – Calls the GitHub REST API to fetch description, stars, languages, topics, and default branch.
- **File Tree & Content Extraction** – Recursively lists files, prioritizes key files (`README.md`, `app.py`, etc.), and downloads up to ~45 k characters of source code.
- **LLM Interaction** – Uses a Groq LLM (default `openai/gpt-oss-20b`) to generate a README, insights, and analysis from the gathered data.
- **State Machine Workflow** – Implements a LangGraph `StateGraph` to manage the agent’s workflow (state machine definition is in `app.py`).

---

## Technologies Used

| Library | Purpose |
|---------|---------|
| **Python 3.8+** | Core language |
| **LangChain** | LLM orchestration |
| **LangGraph** | State‑machine graph for the agent |
| **Groq** (`langchain_groq`) | LLM provider |
| **Streamlit** | Web UI (`streamlit_app.py`) |
| **Requests** | HTTP client for GitHub API |
| **python‑dotenv** | Environment‑variable loading |

---

## Project Structure

```
├── .env.example          # Example environment variables
├── .gitignore
├── README.md
├── app.py                # Core logic & LangGraph definition
├── render.yaml           # Deployment configuration (e.g., Render.com)
├── requirements.txt      # Runtime dependencies
└── streamlit_app.py      # Streamlit UI entry point
```

---

## Prerequisites

- Python 3.8 or newer
- `pip` (Python package installer)
- A GitHub personal access token (optional, required for private‑repo support)
- A Groq API key (required)

---

## Installation & Setup

```bash
# 1. Clone the repository
git clone https://github.com/naveen7793970572/GitHub_README_Generator_Agent.git
cd GitHub_README_Generator_Agent

# 2. Create and activate a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the project root (copy from `.env.example`) and set the following:

| Variable | Description | Example |
|----------|-------------|---------|
| `GITHUB_TOKEN` | Personal access token for GitHub API (optional). | `ghp_XXXXXXXXXXXXXXXXXXXX` |
| `GROQ_API_KEY` | API key for Groq LLM. | `sk-XXXXXXXXXXXXXXXXXXXX` |
| `GROQ_MODEL` | Optional; defaults to `openai/gpt-oss-20b`. | `openai/gpt-4o-mini` |

> **Note:** The application will also look for `GROQ_API_KEY` in `streamlit.secrets` if running via Streamlit.

---

## How to Run

The primary entry point is the Streamlit UI:

```bash
streamlit run streamlit_app.py
```

The UI will prompt you to enter a GitHub repository URL.  
After submission, the agent will:

1. Parse the URL.
2. Retrieve repository metadata and a curated set of source files.
3. Generate a README, insights, and analysis using the Groq LLM.
4. Display the results in the browser.

> **Fallback:** If you prefer a non‑UI approach, you can invoke the core logic directly from `app.py`, but it is not a standalone CLI.

---

## Usage

1. Open the Streamlit app in your browser (default: `http://localhost:8501`).
2. Paste a public GitHub repository URL (e.g., `https://github.com/owner/repo`).
3. Click **Generate README**.
4. View the generated README, insights, and analysis in the app.
5. Copy the generated README to your repository or save it locally.

---

## Contributing

Contributions are welcome!  
If you find a bug or have a feature request, please open an issue.  
Pull requests should:

1. Follow the existing code style.
2. Include tests if applicable (no tests are currently provided).
3. Update documentation where necessary.

---

## License

The license for this project is not specified in the repository.  
Please refer to the repository’s `LICENSE` file (if added) or contact the maintainer for licensing details.
