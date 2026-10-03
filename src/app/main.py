"""Telemetry ingestion service."""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Telemetry Service")


class MetricPayload(BaseModel):
    metric_name: str
    value: float


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/ingest")
def ingest(payload: MetricPayload):
    return {"status": "ingested", "metric": payload.metric_name, "value": payload.value}
