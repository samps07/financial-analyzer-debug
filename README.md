# financial-analyzer-debug

# AI Financial Document Analyzer (Debug Challenge)

A multi-modal RAG-based QA system built with **FastAPI**, **CrewAI**, and **Google Gemini**.

## 🛠 Bugs Found & Fixed
- **Environment Bug:** Resolved Python 3.12 compatibility issues with `js2py/pipwin` by standardizing the build on **Python 3.11**.
- **Import Conflicts:** Fixed deprecated imports for `crewai.Agent` and `crewai.tools`.
- **Logic Refactoring:** Replaced inefficient prompts with a 4-agent pipeline (Verifier, Analyst, Risk Assessor, Investment Advisor).
- **Dependency Missing:** Integrated `python-multipart` to enable FastAPI file uploads.
- **Bonus Feature:** Implemented **MongoDB Integration** via `motor` for persistent analysis history.

## 🚀 Setup Instructions
1. Clone the repo: `git clone https://github.com/samps07/financial-analyzer-debug`
2. Create Venv: `python -m venv venv`
3. Install: `pip install -r requirements.txt`
4. Set `.env` with `GEMINI_API_KEY` and `MONGODB_URL`.
5. Run: `uvicorn main:app --reload`

## 📡 API Documentation
- **Endpoint:** `POST /analyze`
- **Payload:** Multipart Form (File: PDF, Query: String)
- **Response:** JSON including analysis results and `database_record_id`.

> **Note on Local Environment:** On some Windows systems with existing Google Cloud SDKs, LiteLLM may default to Vertex AI routing. The code is optimized for **Google AI Studio**; if 404s occur, ensure no `GOOGLE_APPLICATION_CREDENTIALS` are set in the environment.
