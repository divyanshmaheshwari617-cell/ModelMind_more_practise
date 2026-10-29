# ModelMind — More Practice

Next.js frontend and FastAPI backend containing **417 practice questions**. Coding exercises currently have **14 automated evaluation definitions**; the remaining coding questions are practice-only until tests are authored. Objective questions are checked by the server when an answer key exists. The UI does not claim unevaluated answers are correct.

## Requirements
Node.js 20.9+; Python 3.10+; npm. The backend Python environment needs FastAPI, Uvicorn, NumPy, Pandas, scikit-learn.

## Start backend (PowerShell)
```powershell
cd backend
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload --port 8015
```

## Start frontend (a second PowerShell window)
```powershell
npm install
npm run dev
```
Browse http://localhost:3000 . API health: http://127.0.0.1:8015/api/health .

Set `NEXT_PUBLIC_EVALUATOR_API_URL` if the API runs at another address. Never put secrets in `NEXT_PUBLIC_` variables.

## Important safety note
The Python code evaluator uses AST checks and a subprocess timeout, **not a robust OS sandbox**. It must only run on a trusted, local development machine. Do **not** expose `/api/run` to untrusted internet traffic. For production, move execution to a separately isolated container/VM with no network, unprivileged user, resource limits, and an enforced filesystem policy.

## Limitations
- 417 distinct questions; not every problem has a configured answer or automated test.
- Some question types offer self-directed practice until authoring and grading are completed.
- No authentication, multi-user progress sync, or production-grade execution isolation is included.
