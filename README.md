# Resume and Job Matcher

Skill/requirement comparison that avoids inventing credentials.

## Status
Portfolio MVP / learning project. It is not represented as production-deployed. Before real-world use, review security, privacy, evaluation, reliability, and deployment requirements.

## Setup (Windows PowerShell)
```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run
See the command in the project section below. This starter is designed to run locally with demo/sample data and no API key.

## Engineering checklist
- [ ] Run the app locally and capture a screenshot
- [ ] Run tests: `python -m pytest`
- [ ] Add real evaluation examples and report results
- [ ] Review input validation, error handling, logging, and secrets
- [ ] Add a deployment guide only after testing deployment
- [ ] Update this README with verified behavior and limitations

## Run
```powershell
streamlit run app.py
```

This uses keyword overlap, not a validated ATS score or an automated hiring decision.


## Recommended real AI integration
- **Framework choice:** Pydantic + optional embeddings
- **Integration pattern:** structured skills extraction and evidence-linked matching
- **Validation:** fairness and hallucination tests

Use a provider adapter and typed outputs. Do not install every framework into every app: choose the smallest appropriate set to reduce dependency conflicts and demonstrate intentional engineering decisions.
