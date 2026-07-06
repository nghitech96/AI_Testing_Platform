from pydantic import BaseModel
from typing import List


class EvaluationRequest(BaseModel):
    dataset: str
    model: str
    metrics: List[str]


class EvaluationResponse(BaseModel):
    run_id: int
    status: str
    pass_rate: float
    average_score: float
    report_name: str