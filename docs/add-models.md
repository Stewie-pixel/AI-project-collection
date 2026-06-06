# New Model Onboarding Guide

This document is the blueprint for adding a new ML model to the collection.
Follow every step in order. The entire pipeline is automated after setup.


## Checklist

- [ ] 1. Create child repo on GitHub
- [ ] 2. Create Hugging Face Space
- [ ] 3. Wrap model in FastAPI
- [ ] 4. Add GitHub secrets
- [ ] 5. Add workflow file
- [ ] 6. Push to main


## Step 1 — Create Child Repo

Create a new public repo on GitHub under `Stewie-pixel`:
```
Name:        <model-name>  (e.g. house-price-prediction)
Visibility:  Public
```

Naming convention: `kebab-case`, descriptive, no abbreviations.


## Step 2 — Create Hugging Face Space

Go to huggingface.co/new-space:
```
Owner:       Stewie-pixel
Space name:  <model-name>  (must match GitHub repo name exactly)
SDK:         Docker
Visibility:  Public
```


## Step 3 — Wrap Model in FastAPI

Every model must expose an HTTP API. Required structure:

```
<model-name>/
├── main.py              ← FastAPI app (entry point)
├── model.py             ← prediction logic (renamed from original script)
├── requirements.txt     ← must include fastapi and uvicorn
├── Dockerfile
├── README.md            ← must have HF Space YAML frontmatter
└── models/
    └── *.pkl            ← trained model artifacts
```

### `Dockerfile` template
```dockerfile
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    MODEL_DIR=/app/models

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && pip cache purge

COPY . .

VOLUME ${MODEL_DIR}
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### `main.py` template
```python
from fastapi import FastAPI
from pydantic import BaseModel
from model import predict  # import your prediction function

app = FastAPI(title="<Model Title>")

class InputSchema(BaseModel):
    # define your input fields here
    pass

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict_endpoint(data: InputSchema):
    result = predict(data.model_dump())
    return {"input": data.model_dump(), "prediction": result}
```

### `README.md` frontmatter (required by HF)
```markdown
---
title: <Model Title>
emoji: <pick one>
colorFrom: blue
colorTo: green
sdk: docker
app_port: 8000
pinned: false
---
```


## Step 4 — Add GitHub Secrets

Go to the child repo → **Settings → Secrets and variables → Actions**

| Secret | Value |
|---|---|
| `HF_TOKEN` | Hugging Face write token (same for all repos) |
| `CENTRAL_REPO_TOKEN` | GitHub PAT with `repo` scope (same for all repos) |


## Step 5 — Add Workflow File

Create `.github/workflows/deploy.yml` with the content below.
Update every value marked with `← CHANGE THIS`.

```yaml
name: Deploy to Hugging Face Space

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          fetch-depth: 0
          lfs: true

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install huggingface_hub with Xet support
        run: pip install "huggingface_hub[hf_xet]"

      - name: Push to Hugging Face Space
        if: github.ref == 'refs/heads/main' && github.event_name == 'push'
        run: |
          mkdir hf-deploy
          cp main.py hf-deploy/
          cp model.py hf-deploy/
          cp requirements.txt hf-deploy/
          cp Dockerfile hf-deploy/
          mkdir hf-deploy/models
          cp models/*.pkl hf-deploy/models/

          python - <<'EOF'
          from huggingface_hub import HfApi
          api = HfApi()
          api.upload_folder(
              folder_path="hf-deploy",
              repo_id="Stewie-pixel/<model-name>",     # ← CHANGE THIS
              repo_type="space",
              token="${{ secrets.HF_TOKEN }}",
              commit_message="deploy: ${{ github.sha }}",
              ignore_patterns=["README.md"]
          )
          print("Upload complete")
          EOF

      - name: Trigger central deployment
        if: github.ref == 'refs/heads/main' && github.event_name == 'push'
        run: |
          curl -X POST \
            -H "Authorization: token ${{ secrets.CENTRAL_REPO_TOKEN }}" \
            -H "Accept: application/vnd.github.v3+json" \
            https://api.github.com/repos/Stewie-pixel/AI-project-collection/dispatches \
            -d '{
              "event_type": "deploy-model",
              "client_payload": {
                "model_name": "<model-name>",
                "title": "<Display Name>",
                "models": "<Algorithm(s)>",
                "domain": "<Domain>",
                "accuracy": "<~XX%>",
                "tags": "<Tag1,Tag2,Tag3>",
                "github": "https://github.com/Stewie-pixel/<model-name>",
                "hf_space": "https://huggingface.co/spaces/Stewie-pixel/<model-name>",
                "status": "live"
              }
            }'
```


## Step 6 — Push to Main

```bash
git add .
git commit -m "feat: initial model deployment"
git push origin main
```

The pipeline will automatically:
1. Upload model files to HF Space via Xet
2. HF builds the Docker container
3. API goes live at `huggingface.co/spaces/Stewie-pixel/<model-name>`
4. `models.json` in AI-project-collection updates
5. Dashboard at `stewie-pixel.github.io/AI-project-collection` reflects the new model


## Domain Reference

| Domain | Examples |
|---|---|
| Regression | Salary, house price, stock prediction |
| Classification | Spam, fraud, disease detection |
| Clustering | Customer segmentation |
| NLP | Sentiment analysis, text classification |
| Computer Vision | Image classification, object detection |
| Time Series | Sales forecasting, anomaly detection |
| Deep Learning | Neural network based models |
| Reinforcement Learning | Agent-based models |


## Reference Implementation

Model #01 — Employee Salary Prediction is the reference implementation.

- GitHub: https://github.com/Stewie-pixel/employee-salary-prediction
- HF Space: https://huggingface.co/spaces/Stewie-pixel/employee-salary-prediction