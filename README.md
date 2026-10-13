# EduGenie — Gemini-Powered Learning Assistant

EduGenie is a student-friendly web app that can answer questions, explain concepts, create a 3-question multiple-choice quiz, summarize notes, and recommend a learning path. It uses FastAPI for the backend, HTML/CSS/JavaScript for the interface, and Google's Gemini API for AI responses.

## Requirements
- Python 3.10 or newer
- Internet connection
- A Gemini API key

## Run on Windows using VS Code

1. Extract this ZIP and open the `EduGenie-Complete-Project` folder in VS Code.
2. Open **Terminal → New Terminal**.
3. Create a virtual environment:

   ```powershell
   python -m venv .venv
   ```

   If `python` is not recognized, install Python from https://www.python.org/downloads/ and select **Add Python to PATH** during setup. Then restart VS Code.
4. Activate the environment in PowerShell:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

   If PowerShell blocks activation, use Command Prompt in VS Code and run `.venv\Scripts\activate.bat` instead.
5. Install packages:

   ```powershell
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```
6. Copy `.env.example` to a new file named `.env` in the project root. Get a Gemini API key from https://aistudio.google.com/app/apikey and replace `your_gemini_api_key_here` with your own key. Keep `.env` private; never upload it to GitHub.
7. Start the app:

   ```powershell
   python -m uvicorn main:app --reload
   ```
8. Open http://127.0.0.1:8000 in your browser. API documentation is at http://127.0.0.1:8000/docs.

## Features
- **Ask a question** — answers a student's question in accessible language.
- **Explain a topic** — provides a definition, steps, example, and recap.
- **Create a quiz** — generates three MCQs with four options and answer explanations.
- **Summarize notes** — extracts the main idea and key points from supplied text.
- **Learning path** — suggests ordered learning stages and practice activities.

## Test
With the environment activated and dependencies installed, run:

```powershell
python -m pytest
```

## API endpoints
- `GET /` — web interface
- `GET /health` — health check
- `POST /api/task` — unified task endpoint; JSON body example: `{"task":"explain","text":"Photosynthesis"}`
- `POST /qa`, `/explain`, `/quiz`, `/summarize`, `/learn/recommendations` — task-specific endpoints; each accepts a JSON body with `task` and `text`.

## Troubleshooting
- **Missing API key:** confirm the file is named `.env` (not `.env.txt`) and contains `GEMINI_API_KEY=your_actual_key`.
- **Module not found:** activate `.venv` and run `pip install -r requirements.txt` again.
- **Port already in use:** run `python -m uvicorn main:app --reload --port 8001` and visit http://127.0.0.1:8001.
- **Gemini request fails:** check internet access, API key validity, quota, and the model name in `.env`.
