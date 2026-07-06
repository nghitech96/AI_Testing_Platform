from fastapi import APIRouter, HTTPException
from backend.schemas.evaluation import (
    EvaluationRequest,
    EvaluationResponse
)
from backend.services.evaluator import evaluate_dataset

router = APIRouter(
    prefix="/evaluation",
    tags=["Evaluation"]
)

@router.post(
    "/run",
    response_model=EvaluationResponse
)
async def run_evaluation(request: EvaluationRequest):

    try:
        result = evaluate_dataset(
            dataset=request.dataset,
            model=request.model,
            metrics=request.metrics
        )

        return result

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )