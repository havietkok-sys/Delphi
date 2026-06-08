# Delphi

FastAPI-applikation som laddar upp CSV-filer, analyserar data med Pandas och låter användaren ställa frågor till en SmolLLM-modell genom en typad Runnable-kedja.

---

## Installation

```bash
uv sync

# Starta appen
uv run uvicorn app.main:app --reload

# Köra tester
uv run pytest
```

---

## Endpoints

### GET /health

Kontrollerar att API:t är igång.

Svar:

```json
{
  "status": "ok"
}
```

---

### POST /data/upload

Laddar upp en CSV-fil och sparar datasetet i minnet.

Svar:

```json
{
  "rows": 150,
  "columns": ["city", "temp_c"],
  "dtypes": {
    "city": "object",
    "temp_c": "float64"
  }
}
```

---

### GET /data/stats

Returnerar statistik från Pandas `describe()`.

---

### POST /ai/ask

Tar emot en fråga om datasetet och skickar den genom Runnable-kedjan:

```text
PromptBuilder
↓
LLMRunner
↓
ResponseParser
```

Exempel:

```json
{
  "question": "Vilken stad har högst temperatur?"
}
```

---


## Techstack

- Python
- FastAPI
- Pandas
- Pydantic
- Transformers
- SmolLM2-135M-Instruct
- Pytest
- Uvicorn
- Git
- uv

---

## Tools

- Black (kodformatering)

---

## Antaganden

- Dataset lagras endast i minnet.
- Endast en CSV åt gången stöds.
- SmolLM körs lokalt via HuggingFace Transformers.